#-*- coding: utf-8 -*-

def pares(i):
	if (i%2 == 0):
		return i 

#SEM_FUNCAO_FILTER
lista = [11,12,13,14,15,16,17,18,19,20];
listaPar = [];

for i in lista:
	listaPar.append(pares(i));

print(listaPar);

#COM_FUNCAO_FILTER

lista2 = [1,2,3,4,5,6,7,8,9,10];

listaPares = filter(pares, lista2);

print(listaPares);

