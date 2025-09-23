#pragma once
#include <vector>
#include <string>
#include <unordered_map>

struct HMM {
    int N = 2;  // estados: 0=N, 1=C
    int M = 4;  // A,C,G,T
    std::vector<double> pi;                 // size N
    std::vector<std::vector<double>> A;     // NxN
    std::vector<std::vector<double>> B;     // NxM
};

struct ViterbiResult {
    std::vector<int> path;   // estados 0/1 por posición
    double logp;             // log-probabilidad del mejor camino
};

double forward_log_prob(
    const std::string& seq,
    const std::vector<double>& pi,
    const std::vector<std::vector<double>>& A,
    const std::vector<std::vector<double>>& B
);

// Viterbi: camino más probable y su log-prob
ViterbiResult viterbi_decode(
    const std::string& seq,
    const std::vector<double>& pi,
    const std::vector<std::vector<double>>& A,
    const std::vector<std::vector<double>>& B
);

// Funciones "planas" para exponer por SWIG:
double hmm_evaluate_logp(const std::string& seq,
                         const std::vector<double>& pi,
                         const std::vector<std::vector<double>>& A,
                         const std::vector<std::vector<double>>& B);

std::vector<int> hmm_recognize_states(const std::string& seq,
                         const std::vector<double>& pi,
                         const std::vector<std::vector<double>>& A,
                         const std::vector<std::vector<double>>& B);
