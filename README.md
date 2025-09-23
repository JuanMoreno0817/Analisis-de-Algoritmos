# Analisis-de-Algoritmos: Modelo Oculto de Markov para ADN

Este proyecto implementa un **Modelo Oculto de Markov (HMM)** optimizado para el análisis de secuencias de ADN. La lógica principal está escrita en **C++** y se expone a Python a través de un *wrapper* generado con **SWIG**. El modelo está diseñado para identificar regiones codificantes (estado 'C') y no codificantes (estado 'N') en una secuencia de nucleótidos.

---

### Estructura del Proyecto

El proyecto se organiza en dos directorios principales para separar el código fuente C++ de los scripts de Python:

-   `cpp/`: Contiene el código en C++ y los archivos de interfaz de SWIG.
    -   `dna_hmm.h`: Define las estructuras de datos (`HMM`, `ViterbiResult`) y declara las funciones principales como `forward_log_prob` y `viterbi_decode`. También incluye funciones planas para exponer a SWIG.
    -   `dna_hmm.cpp`: Contiene la implementación de los algoritmos `forward_log_prob` y `viterbi_decode`.
    -   `dna_hmm.i`: Es el archivo de interfaz de SWIG que define el módulo de Python y expone las funciones de C++.

-   `python/`: Contiene los scripts y el archivo de configuración de Python.
    -   `setup.py`: Script de `setuptools` utilizado para automatizar la compilación del código C++ y la creación del módulo de Python `_dna_hmm.pyd`.
    -   `test_usage.py`: Un script de ejemplo que demuestra cómo cargar el modelo HMM y utilizar las funciones de evaluación y reconocimiento para una secuencia de prueba.
    -   `baseline_pure_py.py`: Implementación de referencia de los algoritmos en Python puro para comparar el rendimiento con la versión de C++.

---

### Dependencias

Para compilar y ejecutar este proyecto, se usaron las siguientes herramientas:

-   **Compilador de C++**: Un compilador compatible con C++17, como GCC o Visual C++.
-   **SWIG**: Se utiliza para generar el código de acoplamiento (*wrapper*) entre C++ y Python.
-   **Python 3**: El entorno de ejecución de Python.
-   **setuptools**: Una biblioteca de Python para el empaquetado de proyectos.

---

### Compilación e Instalación

Sigue estos pasos para compilar e instalar el módulo de Python desde el código fuente:

1.  Asegúrate de que SWIG esté instalado y disponible en tu `PATH`.
2.  Navega al directorio `python/` donde se encuentra el archivo `setup.py`.
3.  Ejecuta el siguiente comando en la terminal para compilar la extensión de C++ y crear el módulo de Python:

    ```bash
    python setup.py build_ext --inplace
    ```

Este comando generará el archivo `_dna_hmm.pyd` y lo colocará en el mismo directorio `python/`, haciéndolo inmediatamente importable.

---

### Uso y Funcionalidades

Las funcionalidades del HMM están expuestas en dos funciones principales que puedes llamar desde Python:

-   `hmm_evaluate_logp(seq, pi, A, B)`: Calcula la probabilidad logarítmica de la secuencia de observación utilizando el algoritmo *Forward*. Es útil para evaluar qué tan bien un modelo HMM específico se ajusta a una secuencia de datos.
-   `hmm_recognize_states(seq, pi, A, B)`: Utiliza el algoritmo de *Viterbi* para decodificar la secuencia de observación y encontrar la ruta de estados más probable. Retorna una lista de enteros que representan la secuencia de estados subyacentes.

Para ver un ejemplo práctico de cómo se usan estas funciones, puedes ejecutar el script `test_usage.py`:

```bash
python test_usage.py
```
