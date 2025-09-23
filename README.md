# Analisis-de-Algoritmos: Modelo Oculto de Markov para ADN

Este proyecto implementa un **Modelo Oculto de Markov (HMM)** optimizado para el an�lisis de secuencias de ADN. La l�gica principal est� escrita en **C++** y se expone a Python a trav�s de un *wrapper* generado con **SWIG**. El modelo est� dise�ado para identificar regiones codificantes (estado 'C') y no codificantes (estado 'N') en una secuencia de nucle�tidos.

---

### Estructura del Proyecto

El proyecto se organiza en dos directorios principales para separar el c�digo fuente C++ de los scripts de Python:

-   `cpp/`: Contiene el c�digo en C++ y los archivos de interfaz de SWIG.
    -   `dna_hmm.h`: Define las estructuras de datos (`HMM`, `ViterbiResult`) y declara las funciones principales como `forward_log_prob` y `viterbi_decode`. Tambi�n incluye funciones planas para exponer a SWIG.
    -   `dna_hmm.cpp`: Contiene la implementaci�n de los algoritmos `forward_log_prob` y `viterbi_decode`.
    -   `dna_hmm.i`: Es el archivo de interfaz de SWIG que define el m�dulo de Python y expone las funciones de C++.

-   `python/`: Contiene los scripts y el archivo de configuraci�n de Python.
    -   `setup.py`: Script de `setuptools` utilizado para automatizar la compilaci�n del c�digo C++ y la creaci�n del m�dulo de Python `_dna_hmm.pyd`.
    -   `test_usage.py`: Un script de ejemplo que demuestra c�mo cargar el modelo HMM y utilizar las funciones de evaluaci�n y reconocimiento para una secuencia de prueba.
    -   `baseline_pure_py.py`: Implementaci�n de referencia de los algoritmos en Python puro para comparar el rendimiento con la versi�n de C++.

---

### Dependencias

Para compilar y ejecutar este proyecto, se usaron las siguientes herramientas:

-   **Compilador de C++**: Un compilador compatible con C++17, como GCC o Visual C++.
-   **SWIG**: Se utiliza para generar el c�digo de acoplamiento (*wrapper*) entre C++ y Python.
-   **Python 3**: El entorno de ejecuci�n de Python.
-   **setuptools**: Una biblioteca de Python para el empaquetado de proyectos.

---

### Compilaci�n e Instalaci�n

Sigue estos pasos para compilar e instalar el m�dulo de Python desde el c�digo fuente:

1.  Aseg�rate de que SWIG est� instalado y disponible en tu `PATH`.
2.  Navega al directorio `python/` donde se encuentra el archivo `setup.py`.
3.  Ejecuta el siguiente comando en la terminal para compilar la extensi�n de C++ y crear el m�dulo de Python:

    ```bash
    python setup.py build_ext --inplace
    ```

Este comando generar� el archivo `_dna_hmm.pyd` y lo colocar� en el mismo directorio `python/`, haci�ndolo inmediatamente importable.

---

### Uso y Funcionalidades

Las funcionalidades del HMM est�n expuestas en dos funciones principales que puedes llamar desde Python:

-   `hmm_evaluate_logp(seq, pi, A, B)`: Calcula la probabilidad logar�tmica de la secuencia de observaci�n utilizando el algoritmo *Forward*. Es �til para evaluar qu� tan bien un modelo HMM espec�fico se ajusta a una secuencia de datos.
-   `hmm_recognize_states(seq, pi, A, B)`: Utiliza el algoritmo de *Viterbi* para decodificar la secuencia de observaci�n y encontrar la ruta de estados m�s probable. Retorna una lista de enteros que representan la secuencia de estados subyacentes.

Para ver un ejemplo pr�ctico de c�mo se usan estas funciones, puedes ejecutar el script `test_usage.py`:

```bash
python test_usage.py
```
