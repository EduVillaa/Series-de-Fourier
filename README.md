# Rectificador de Media Onda a partir de Series de Fourier

Este proyecto es un trabajo de clase que implementa un **rectificador de media onda** utilizando **series de Fourier** en Python. Permite visualizar la señal original, su aproximación mediante armónicos y analizar cómo se forma la señal rectificada a partir de la suma de senos y cosenos.

---

## Descripción del Proyecto

El código realiza las siguientes funciones:

1. Define un **rectificador de media onda** de una señal senoidal con amplitud `Vm` y frecuencia `freq`.
2. Calcula los **coeficientes de la serie de Fourier**:
   - Término de continua `a0`.
   - Coeficientes `an` y `bn` para los cosenos y senos de cada armónico.
   - Magnitud de cada armónico `An`.
3. Representa gráficamente:
   - La señal rectificada original.
   - La aproximación mediante un número variable de armónicos.
   - Diagrama de barras mostrando la magnitud de cada armónico.
4. Permite **interactividad** mediante:
   - Slider para cambiar el número de armónicos sumados en tiempo real.
   - Botón para centrar/descentrar la gráfica.
   - Botón para mostrar/esconder la señal original `f(t)`.

---

## Requisitos

- Python 3.x
- Librerías:
  - `numpy`
  - `matplotlib`
  - `scipy`
