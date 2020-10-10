#-*- coding: utf-8 -*-
inteiro = 10;
print(inteiro);
print(inteiro + inteiro);
#O_PY_É_TIPO_PARECIDO_COM_JS
print("\n\nNO PY O '||' e 'OR' O '&&' e 'AND'\n\n");

X = 4;
Y = 4;
Z = 4;
W = 3;
#VAI_DAR_TRUE
print(X == Y and Y == Z);
#VAI_DAR_TRUE
print(X == Y or Y == W);
#VAI_DAR_TRUE
print(X != Y or Y == Z and Z != W);

if(X == Y or Y == W):
	print("Tô no IF");
if(W < Z):
	print("Entrei no IF, pois W é menor que Z");
if(W == Z):
	print("Entrei no IF, pois W é igual a Z");
elif(W != Z):
	print("Entrei no ELIF, pois W é diferente a Z");
else:
	print("Não entrei no IF, pois W é menor que Z");

