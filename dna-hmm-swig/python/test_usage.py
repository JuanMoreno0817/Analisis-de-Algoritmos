import time
from dna_hmm import (
    hmm_evaluate_logp, hmm_recognize_states,
    DoubleVector, DoubleVector2D
)

# === Parámetros del modelo (ajusta a tu "Figura 2") ===
pi = DoubleVector([0.5, 0.5])
A  = DoubleVector2D([[0.95, 0.05],
      [0.05, 0.95]])

B  = DoubleVector2D([
    [0.30, 0.20, 0.20, 0.30],  # N: A,C,G,T
    [0.20, 0.30, 0.30, 0.20],  # C
])

# Secuencia de prueba (ejemplo)
seq = str("ATGCGTACGTTACGCGCGTTTACGCGCGCGTATATATAGCGC")
print(type(seq), type(pi), type(A), type(B))
print(pi)
print(A)
print(B)
# --- Evaluación (Forward en log) ---
t0 = time.perf_counter()
logp = hmm_evaluate_logp(seq, pi, A, B)
t1 = time.perf_counter()
print(f"[SWIG/C++] logP(seq) = {logp:.6f}  (time: {(t1-t0)*1e3:.3f} ms)")

# --- Reconocimiento (Viterbi) ---
t0 = time.perf_counter()
path = hmm_recognize_states(seq, pi, A, B)
t1 = time.perf_counter()
print(f"[SWIG/C++] Viterbi path (len={len(path)}):")
print(path)
print(f"Time: {(t1-t0)*1e3:.3f} ms")

# Opcional: imprime segmentos codificantes (estado 1)
def segments(states):
    res = []
    s = None
    for i, st in enumerate(states):
        if st == 1 and s is None:
            s = i
        if st == 0 and s is not None:
            res.append((s, i-1))
            s = None
    if s is not None:
        res.append((s, len(states)-1))
    return res

print("Regiones codificantes (índices 0-based):", segments(path))
