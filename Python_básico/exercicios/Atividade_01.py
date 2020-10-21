#Crescimento da população brasileira 1980-2016
#Dados do DATASUS

#-*- coding: utf-8 -*-

import matplotlib.pyplot as plt;

data = open("pop_brasileira.csv").readlines();

#anos
x = [];
#população
y = [];

for i in range(len(data)):
    if i != 0:
        linha = data[i].split(";");
        x.append(int(linha[0]));
        y.append(int(linha[1]));


plt.plot(x, y, color='k', linestyle='--');
plt.bar(x, y, color='#e4e4e4');

plt.title("Crescimento da população brasileira 1980-2016");
plt.xlabel("Ano");
plt.ylabel("População x100.000");
plt.show();
