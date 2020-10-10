#-*- coding: utf-8 -*-

meuDicionario = {"A":"AMEIXA", "B":"BOLA", "C":"CACHORRO"};

print(meuDicionario);
print("\n");

print(meuDicionario["A"]);
print(meuDicionario["B"]);
print(meuDicionario["C"]);
print("\n");

for chave in meuDicionario:
	print(chave);
print("\n");


for chave in meuDicionario:
	print(meuDicionario[chave]);
print("\n");

for chave in meuDicionario:
	print(chave+":"+meuDicionario[chave]);
print("\n");

for i in meuDicionario.items():
	print(i);
print("\n");

for j in meuDicionario.values():
	print(j);
print("\n");

for g in meuDicionario.keys():
	print(g);
print("\n");



