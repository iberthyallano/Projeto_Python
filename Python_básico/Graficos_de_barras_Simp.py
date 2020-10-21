#Visualisação de dados em Python

import matplotlib.pyplot as plt;

x = [1, 2, 3, 4, 5];
y = [2, 3, 7, 1, 4];


#legendas
plt.title("Gráfico de barras");
plt.xlabel("Eixo X");
plt.ylabel("Eixo y");

plt.bar(x, y);
plt.show();