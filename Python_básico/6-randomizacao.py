#-*- coding: utf-8 -*-

import random


for i  in range(0,10):
	random.seed(3);
	numero = random.randint(0, 10)
	print(numero);

print("\n");

for i  in range(0,10):
	numero = random.randint(0, 10)
	print(numero);

print("\n");

lista = [5,10,15,20];
for i  in range(0,10):
	numero = random.choice(lista)
	print(numero);
