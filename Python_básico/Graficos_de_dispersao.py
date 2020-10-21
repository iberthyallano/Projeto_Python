#Visualisação de dados em Python

import matplotlib.pyplot as plt;

x = [1, 3, 5, 7, 9];
y = [2, 3, 7, 1, 4];
z = [200, 300, 400, 500, 600];


#legendas
plt.title("Gráfico de dispersão");
plt.xlabel("Eixo X");
plt.ylabel("Eixo y");

#https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html
#link para estilização dos gráficos
plt.scatter(x, y, label="Meus pontos", color='#990000', marker='.', s=z);
plt.plot(x, y, color="k", linestyle=":");


plt.legend()
# plt.show();
# plt.savefig("fiura_de_teste.png", dpi=1200);#Quanto mais alto o DPI, maior sua resolução
plt.savefig("fiura_de_teste.pdf");#melhor qualidade final

