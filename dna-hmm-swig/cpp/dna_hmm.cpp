#include "dna_hmm.h"
#include <cmath>
#include <limits>
#include <stdexcept>

static inline int nuc2idx(char c) {
    switch(c) {
        case 'A': case 'a': return 0;
        case 'C': case 'c': return 1;
        case 'G': case 'g': return 2;
        case 'T': case 't': return 3;
        default: return -1;
    }
}

static inline double log_safe(double x) {
    if (x <= 0.0) return -std::numeric_limits<double>::infinity();
    return std::log(x);
}

static inline double logsumexp(const std::vector<double>& v) {
    double m = -std::numeric_limits<double>::infinity();
    for (double x : v) if (x > m) m = x;
    if (!std::isfinite(m)) return m;
    double s = 0.0;
    for (double x : v) s += std::exp(x - m);
    return m + std::log(s);
}

double forward_log_prob(
    const std::string& seq,
    const std::vector<double>& pi,
    const std::vector<std::vector<double>>& A,
    const std::vector<std::vector<double>>& B
) {
    const int N = (int)pi.size();
    if ((int)A.size() != N) throw std::runtime_error("A size mismatch");
    if ((int)B.size() != N) throw std::runtime_error("B size mismatch");

    const int T = (int)seq.size();
    if (T == 0) return -std::numeric_limits<double>::infinity();

    // alpha[t][i] en log
    std::vector<std::vector<double>> alpha(T, std::vector<double>(N, -INFINITY));

    int o0 = nuc2idx(seq[0]);
    if (o0 < 0) throw std::runtime_error("Invalid nucleotide in seq");
    for (int i = 0; i < N; ++i) {
        alpha[0][i] = log_safe(pi[i]) + log_safe(B[i][o0]);
    }

    for (int t = 1; t < T; ++t) {
        int ot = nuc2idx(seq[t]);
        if (ot < 0) throw std::runtime_error("Invalid nucleotide in seq");
        for (int j = 0; j < N; ++j) {
            std::vector<double> terms; terms.reserve(N);
            for (int i = 0; i < N; ++i) {
                terms.push_back(alpha[t-1][i] + log_safe(A[i][j]));
            }
            alpha[t][j] = logsumexp(terms) + log_safe(B[j][ot]);
        }
    }

    return logsumexp(alpha[T-1]);
}

ViterbiResult viterbi_decode(
    const std::string& seq,
    const std::vector<double>& pi,
    const std::vector<std::vector<double>>& A,
    const std::vector<std::vector<double>>& B
) {
    const int N = (int)pi.size();
    const int T = (int)seq.size();
    ViterbiResult res;
    if (T == 0) {
        res.logp = -std::numeric_limits<double>::infinity();
        return res;
    }

    std::vector<std::vector<double>> dp(T, std::vector<double>(N, -INFINITY));
    std::vector<std::vector<int>> back(T, std::vector<int>(N, -1));

    int o0 = nuc2idx(seq[0]);
    if (o0 < 0) throw std::runtime_error("Invalid nucleotide in seq");

    for (int i = 0; i < N; ++i)
        dp[0][i] = log_safe(pi[i]) + log_safe(B[i][o0]);

    for (int t = 1; t < T; ++t) {
        int ot = nuc2idx(seq[t]);
        if (ot < 0) throw std::runtime_error("Invalid nucleotide in seq");
        for (int j = 0; j < N; ++j) {
            double best = -INFINITY;
            int arg = -1;
            for (int i = 0; i < N; ++i) {
                double val = dp[t-1][i] + log_safe(A[i][j]);
                if (val > best) { best = val; arg = i; }
            }
            dp[t][j] = best + log_safe(B[j][ot]);
            back[t][j] = arg;
        }
    }

    // backtrack
    double best = -INFINITY; int arg = -1;
    for (int i = 0; i < N; ++i) {
        if (dp[T-1][i] > best) { best = dp[T-1][i]; arg = i; }
    }
    res.logp = best;
    res.path.assign(T, 0);
    res.path[T-1] = arg;
    for (int t = T-1; t > 0; --t) {
        res.path[t-1] = back[t][res.path[t]];
    }
    return res;
}

double hmm_evaluate_logp(const std::string& seq,
                         const std::vector<double>& pi,
                         const std::vector<std::vector<double>>& A,
                         const std::vector<std::vector<double>>& B) {
    return forward_log_prob(seq, pi, A, B);
}

std::vector<int> hmm_recognize_states(const std::string& seq,
                         const std::vector<double>& pi,
                         const std::vector<std::vector<double>>& A,
                         const std::vector<std::vector<double>>& B) {
    auto r = viterbi_decode(seq, pi, A, B);
    return r.path;
}
