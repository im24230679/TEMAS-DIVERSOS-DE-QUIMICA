import matplotlib.pyplot as plt
import numpy as np

# Relación entre elementos y electronegatividad
elementos = ["H", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na"]
electronegatividad = [2.2, 0.98, 1.57, 2.04, 2.55, 3.04, 3.44, 3.98, 0.0, 0.93]

plt.figure(figsize=(15, 5))

# Gráfico 1: Elementos y Electronegatividad
plt.subplot(1, 3, 1)
plt.bar(elementos, electronegatividad, color="skyblue")
plt.title("Relación entre elementos y electronegatividad")
plt.xlabel("Elementos")
plt.ylabel("Electronegatividad (Pauling)")

# Relación entre elementos y masa molar
masa_molar = [1.008, 6.94, 9.012, 10.81, 12.01, 14.01, 16.00, 19.00, 20.18, 22.99]

plt.subplot(1, 3, 2)
plt.plot(elementos, masa_molar, marker="o", linestyle="--", color="green")
plt.title("Relación entre elementos y masa molar")
plt.xlabel("Elementos")
plt.ylabel("Masa molar (g/mol)")

# Relación entre viscosidad y temperatura de un aceite de motor
temperatura = np.linspace(20, 100, 10)  # Temperaturas de 20°C a 100°C
viscosidad = 1000 / (temperatura + 50)  # Viscosidad simulada (cP)

plt.subplot(1, 3, 3)
plt.plot(temperatura, viscosidad, marker="s", color="red")
plt.title("Relación de viscosidad y temperatura del aceite")
plt.xlabel("Temperatura (°C)")
plt.ylabel("Viscosidad (cP)")

# Ajustar diseño
plt.tight_layout()
plt.show()
