import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.signal import square
from scipy.signal import sawtooth
from matplotlib.widgets import Slider
from matplotlib.ticker import MultipleLocator
from matplotlib.widgets import Button
from scipy.optimize import minimize_scalar

f = lambda t: square(t) -7 #definimos la función que representaremos como suma de los armónicos de la serie de Fourier
T = 2*np.pi #definimos el periodo de la función
num_armónicos = 26 #definimos el número de armónicos

w = 2*np.pi/T
# === Termino de continua de la serie de fourier ===
int0, _ = quad(f, 0, T)
a0 = int0/T
# === Calculamos los coeficientes an y bn ===
an, bn, An=[0], [0], []
for n in range(1, num_armónicos+1):
    #Coeficiente de las frecuencias de los cosenos
    int_an, _ = quad(lambda t: f(t)*np.cos(n*w*t), 0, T)
    an.append(int_an * 2/T)
    #Coeficiente de las frecuencias de los senos
    int_bn, _ = quad(lambda t: f(t)*np.sin(n*w*t), 0, T)
    bn.append(int_bn * 2/T)
    #Calculamos la magnitud de los armónicos
    An.append(np.sqrt(an[n]**2+bn[n]**2))

# === Calculamos la expresión de f(t) como suma de los armónicos de la serie de fourier ===
fig, ax = plt.subplots(1, 2)
plt.subplots_adjust(bottom=0.2)
t =np.arange(-3*T, 3*T, 0.05)
line1, = ax[0].plot(t, np.full_like(t, a0), lw=1, color="blue")
line2, = ax[0].plot(t, f(t), lw=1, color="green")
res_max = minimize_scalar(lambda t: -f(t), bounds=(0, T), method='bounded')
res_min = minimize_scalar(lambda t: f(t), bounds=(0, T), method='bounded')
ax[0].set_ylim(-abs(f(res_min.x))*1.2, abs(f(res_max.x))*1.2)
ax[0].set_xlim(-3*T, 3*T)
ax[0].axhline(0, color="k", lw=0.4)
ax[0].axvline(0, color="k", lw=0.4)
ax[0].grid()

# === Representamos el diagrama de barras con los armónicos ===
x=range(1, len(An)+1)
ax[1].bar(x, An, color="r")
ax[1].set_xlim(1, len(An)+1.5)
ax[1].autoscale(enable=True, axis='x', tight=True)
plt.gca().xaxis.set_major_locator(MultipleLocator(1))

# === Definimos los valores del slider ===
eje_slider = plt.axes([0.2, 0.1, 0.2, 0.03])
slider_armónicos = Slider(eje_slider, "Número de armónicos", 0, num_armónicos, valinit=0, valstep=1)

# === Creamos un boton para centrar y descentrar la gráfica ===
centrado = [0]
ax_button2 = plt.axes([0.5, 0.05, 0.15, 0.075])  # [left, bottom, width, height]
button2 = Button(ax_button2, 'Centrar')
def toggle2(event):
    centrado[0] = not centrado[0]
    if centrado[0] and f(res_min.x)>0:
        # Modo centrado
        ax[0].set_ylim(f(res_min.x)*0.9, f(res_max.x)*1.1)
        button2.label.set_text("Descentrar")  # cambia texto del botón
    elif centrado[0] and f(res_min.x)<0:
        # Modo centrado
        ax[0].set_ylim(f(res_min.x)*1.1, f(res_max.x)*0.9)
        button2.label.set_text("Descentrar")  # cambia texto del botón
    else:
        # Restaurar límites originales
        ax[0].set_ylim(-abs(f(res_min.x))*1.2, abs(f(res_max.x))*1.2)
        button2.label.set_text("Centrar")
    fig.canvas.draw_idle()
button2.on_clicked(toggle2)

# === Creamos un boton para esconder y mostrar f(t) ===
ax_button = plt.axes([0.7, 0.05, 0.15, 0.075])  # [left, bottom, width, height]
button = Button(ax_button, 'Esconder / Mostrar f(t)')
visible = [True]  # usamos lista para poder modificar dentro de la función

def toggle(event):
    visible[0] = not visible[0]  # alterna True/False
    line2.set_visible(visible[0])
    fig.canvas.draw_idle()       # actualizar el gráfico
button.on_clicked(toggle)

# === Función para cambiar la gráfica a medida que cambia el slider ===
def update(val):
    num_armónicos = slider_armónicos.val
    fourier_suma=0
    for n in range(0, num_armónicos+1):
        fourier_suma +=  an[n]*np.cos(n*w*t) + bn[n]*np.sin(n*w*t)
    fourier = fourier_suma + a0
    line1.set_ydata(fourier)
    #ax[0].relim()
    #ax[0].autoscale_view()
    fig.canvas.draw_idle()

slider_armónicos.on_changed(update)

plt.show()































