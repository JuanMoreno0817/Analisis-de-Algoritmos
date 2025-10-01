import time
from dna_hmm import (
    hmm_evaluate_logp, hmm_recognize_states,
    DoubleVector, DoubleVector2D
)

# PARÁMETROS
pi = DoubleVector([0.5, 0.5])  # [H, L]
A  = DoubleVector2D([
    [0.5, 0.5],  # H -> [H, L]
    [0.4, 0.6]   # L -> [H, L]
])
B  = DoubleVector2D([
    [0.2, 0.3, 0.3, 0.2],  # H: [A, C, G, T]
    [0.3, 0.2, 0.2, 0.3]   # L: [A, C, G, T]
])

# Secuencia de prueba
seq = "GGCACTGAA"

def states_to_labels(path, state0_label='H', state1_label='L'):
    """Convierte estados numéricos a etiquetas biológicas"""
    return [state0_label if s == 0 else state1_label for s in path]

print("=== EVALUACIÓN Y RECONOCIMIENTO CON PARÁMETROS DEL TALLER ===")
print(f"Secuencia: {seq}")
print("Parámetros: pi=[0.5, 0.5], A=[[0.5,0.5],[0.4,0.6]], B=[[0.2,0.3,0.3,0.2],[0.3,0.2,0.2,0.3]]")

# EVALUACIÓN (Probabilidad)
t0 = time.perf_counter()
logp = hmm_evaluate_logp(seq, pi, A, B)
t1 = time.perf_counter()
print(f"\n[SWIG/C++] Evaluación - logP(seq) = {logp:.6f}  (time: {(t1-t0)*1e3:.3f} ms)")

# RECONOCIMIENTO (Viterbi)
t0 = time.perf_counter()
path_numeric = hmm_recognize_states(seq, pi, A, B)
t1 = time.perf_counter()

# Convertir y etiquetar
path_list = list(path_numeric)
path_labels = states_to_labels(path_list, 'H', 'L')

print(f"[SWIG/C++] Reconocimiento - Tiempo: {(t1-t0)*1e3:.3f} ms")
print(f"Secuencia ADN:    {seq}")
print(f"Estados predichos: {''.join(path_labels)}")
print(f"Estados numéricos: {path_list}")

# ANÁLISIS DE REGIONES
print("\n--- ANÁLISIS DE REGIONES GC ---")
current_state = path_labels[0]
start = 0
regions = []

for i in range(1, len(path_labels)):
    if path_labels[i] != current_state:
        length = i - start
        regions.append((current_state, start, i-1, length))
        current_state = path_labels[i]
        start = i

# Última región
length = len(path_labels) - start
regions.append((current_state, start, len(path_labels)-1, length))

for state, start_idx, end_idx, length in regions:
    gc_content = "Alto" if state == 'H' else "Bajo"
    print(f"Región {state} (GC {gc_content}): posiciones {start_idx}-{end_idx} (longitud: {length})")