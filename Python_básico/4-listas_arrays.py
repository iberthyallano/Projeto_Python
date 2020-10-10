#-*- coding: utf-8 -*-

minhaLista1 = ["abacaxi", "melancia", "abacate"];
minhaLista2 = [1,2,3,4,5];
minhaLista3 = [1,"abacaxi",9.84, True];

print(minhaLista1);
print("\n");
print(minhaLista2);
print("\n");
for elemento in minhaLista3:
	print(elemento);


tamanho = len(minhaLista1);
print("\n");
print(tamanho);

minhaLista4 = ["banana", "uva", "limao"];
print("\n");
print(minhaLista4);
print("\n");
minhaLista4.append("laranja")
print(minhaLista4);

print("\n");
if 7 in minhaLista2 or 3 in minhaLista2:
	print("Tem um 3 na lista 2");
else:
	print("Não tem um 7 na lista 2");
print("\n");

del minhaLista4[2:];
print(minhaLista4);
print("\n");

minhaLista5 = [11,24,3,104,50,1,55,9,0];
print(minhaLista5);
print("\n");

minhaLista5.reverse();
print(minhaLista5);
print("\n");


minhaLista5.sort();
print(minhaLista5);
print("\n");

retorno = sorted(minhaLista5);
print(retorno);
print("\n");

minhaLista5.sort(reverse = True);
print(minhaLista5);
print("\n");




