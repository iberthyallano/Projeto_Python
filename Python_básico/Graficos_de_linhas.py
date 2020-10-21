#Visualisação de dados em Python

import matplotlib.pyplot as plt;

x = [1, 2, 5];
y = [2, 3, 7];

#título
plt.title("Testando gráficos com python");

#títulos de X e Y
plt.xlabel("Eixo X");
plt.ylabel("Eixo y");

plt.plot(x, y);

plt.show();
