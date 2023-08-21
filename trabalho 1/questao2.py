import matplotlib.pyplot as plt
import numpy as np

# Dados para os gráficos
x = np.linspace(0, 10, 100)
y1, y2, y3, y4, y5, y6 = np.sin(x), np.cos(x), x, x ** 2, np.exp(x), np.log(x[1:])

# Criar uma grade de 2x3 para os subplots
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

axs[0, 0].plot(x, y1)
axs[0, 0].set_title('Seno')

axs[0, 1].plot(x, y2)
axs[0, 1].set_title('Cosseno')

axs[0, 2].plot(x, y3)
axs[0, 2].set_title('Linear')

axs[1, 0].plot(x, y4)
axs[1, 0].set_title('Quadrático')

axs[1, 1].plot(x, y5)
axs[1, 1].set_title('Exponencial')

axs[1, 2].plot(x[1:], y6)
axs[1, 2].set_title('Logarítmico')

# Ajustar layout para evitar sobreposição de rótulos
plt.tight_layout()

# Exibir os subplots
plt.show()