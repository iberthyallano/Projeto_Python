#-*- coding: utf-8 -*-

#SEM_FUNCAO_MAP

def dobro(x):
	return x*2;

valor = [1,2,3,4,5];

for i in valor:
	print(dobro(i));


#COM_FUNCAO_MAP
valor2 = [1,2,3,4,5];
print(map(dobro, valor));

