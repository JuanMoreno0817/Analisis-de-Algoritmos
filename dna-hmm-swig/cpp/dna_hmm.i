%module dna_hmm

%{
#include "dna_hmm.h"
%}


%include <std_string.i>
%include <std_vector.i>
%include "dna_hmm.h"

/* Soporte de std::vector para listas de Python */
namespace std {
    %template(DoubleVector) vector<double>;
    %template(IntVector) vector<int>;
    %template(DoubleVector2D) vector< vector<double> >;
}

double hmm_evaluate_logp(const std::string& seq,
                         const std::vector<double>& pi,
                         const std::vector<std::vector<double>>& A,
                         const std::vector<std::vector<double>>& B);

std::vector<int> hmm_recognize_states(const std::string& seq,
                         const std::vector<double>& pi,
                         const std::vector<std::vector<double>>& A,
                         const std::vector<std::vector<double>>& B);
