import math, time

def nuc2idx(c):
    return {'A':0,'C':1,'G':2,'T':3,
            'a':0,'c':1,'g':2,'t':3}.get(c, -1)

def log_safe(x): return -math.inf if x <= 0.0 else math.log(x)
def logsumexp(v):
    m = max(v)
    if not math.isfinite(m): return m
    return m + math.log(sum(math.exp(x-m) for x in v))

def forward_log_prob(seq, pi, A, B):
    N = len(pi); T = len(seq)
    if T == 0: return -math.inf
    alpha = [[-math.inf]*N for _ in range(T)]
    o0 = nuc2idx(seq[0]); assert o0 >= 0
    for i in range(N):
        alpha[0][i] = log_safe(pi[i]) + log_safe(B[i][o0])
    for t in range(1, T):
        ot = nuc2idx(seq[t]); assert ot >= 0
        for j in range(N):
            terms = [alpha[t-1][i] + log_safe(A[i][j]) for i in range(N)]
            alpha[t][j] = logsumexp(terms) + log_safe(B[j][ot])
    return logsumexp(alpha[-1])

def viterbi(seq, pi, A, B):
    N = len(pi); T = len(seq)
    dp = [[-math.inf]*N for _ in range(T)]
    back = [[-1]*N for _ in range(T)]
    o0 = nuc2idx(seq[0]); assert o0 >= 0
    for i in range(N):
        dp[0][i] = log_safe(pi[i]) + log_safe(B[i][o0])
    for t in range(1, T):
        ot = nuc2idx(seq[t]); assert ot >= 0
        for j in range(N):
            best, arg = -math.inf, -1
            for i in range(N):
                val = dp[t-1][i] + log_safe(A[i][j])
                if val > best: best, arg = val, i
            dp[t][j] = best + log_safe(B[j][ot])
            back[t][j] = arg
    best, arg = max((dp[-1][i], i) for i in range(N))
    path = [0]*T
    path[-1] = arg
    for t in range(T-1, 0, -1):
        path[t-1] = back[t][path[t]]
    return path, best

if __name__ == "__main__":
    pi = [0.5, 0.5]
    A  = [[0.95,0.05],[0.05,0.95]]
    B  = [[0.30,0.20,0.20,0.30],[0.20,0.30,0.30,0.20]]
    seq = "ATGCGTACGTTACGCGCGTTTACGCGCGCGTATATATAGCGC"

    t0 = time.perf_counter()
    lp = forward_log_prob(seq, pi, A, B)
    t1 = time.perf_counter()
    print(f"[PurePy] logP = {lp:.6f} (time: {(t1-t0)*1e3:.3f} ms)")

    t0 = time.perf_counter()
    path, vlp = viterbi(seq, pi, A, B)
    t1 = time.perf_counter()
    print(f"[PurePy] Viterbi len={len(path)} time: {(t1-t0)*1e3:.3f} ms")
