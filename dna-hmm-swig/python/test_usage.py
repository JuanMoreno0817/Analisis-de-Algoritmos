import time
from dna_hmm import (
    hmm_evaluate_logp, hmm_recognize_states,
    DoubleVector, DoubleVector2D
)

# === Parámetros del modelo ===
pi = DoubleVector([0.5, 0.5])
A  = DoubleVector2D([
    [0.5, 0.5],
    [0.4, 0.6]
])

B  = DoubleVector2D([
    [0.2, 0.3, 0.3, 0.2],  # H: A,C,G,T
    [0.3, 0.2, 0.2, 0.3],  # L: A,C,G,T
])

# Secuencia de prueba
seq = str("ATCGGATCGCG")

# --- Evaluación ---
t0 = time.perf_counter()
logp = hmm_evaluate_logp(seq, pi, A, B)
t1 = time.perf_counter()
print(f"[SWIG/C++] logP(seq) = {logp:.6f}  (time: {(t1-t0)*1e3:.3f} ms)")

# --- Reconocimiento ---
t0 = time.perf_counter()
path = hmm_recognize_states(seq, pi, A, B)
t1 = time.perf_counter()
print(f"[SWIG/C++] Viterbi path (len={len(path)}):")
print(path)
print(f"Time: {(t1-t0)*1e3:.3f} ms")