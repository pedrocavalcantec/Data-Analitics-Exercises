import matplotlib.pyplot as plt

names = ['group_a', 'group_b', 'group_c']
values = [1, 10, 100]

plt.figure(figsize=(9, 3))

plt.subplot(131)
plt.bar(names, values)
plt.title('Gráfico de Barras')

plt.subplot(132)
plt.scatter(names, values)
plt.title('Gráfico de Dispersão')

plt.subplot(133)
plt.plot(names, values)
plt.title('Gráfico de Linha')

plt.suptitle('Categorical Plotting')
plt.tight_layout()  

plt.show()