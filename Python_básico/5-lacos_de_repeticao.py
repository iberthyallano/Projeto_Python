#-*- coding: utf-8 -*-

#WHILE
X = 1;
while(X <= 10):
	print(X);
	X += 1;

print("\n");
array = [1,2,3,4,5];
array2 = ["A","B","C","D","E"];
matriz = [[1,2,3], [4,5,6],[7,8,9]];
#PRINTANDO_UMA_ARRAY
for i in array:
	print (i);

print("\n");

#PRINTANDO_UMA_ARRAY2
for j in array2:
	print(j);

print("\n");

#PRINTANDO_UMA_MATRIZ
for i in matriz:
	for j in i:
		print(j);

print("\n");

#CRIANDO_UM_FOR_RANGE_QUE_VAI_DE_0_A_10
for g in range(10):
	print(g);

#CRIANDO_UM_FOR_RANGE_ENTRE_0_E_20
for l in range(0, 20):
	print(l);

#CRIANDO_UM_FOR_RANGE_ENTRE_0_E_20_DE_2_EM_2
for k in range(0, 20, 2):
	print(k);


