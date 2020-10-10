#-*- coding: utf-8 -*-

def soma(a,b):
	return a + b;

def multiplicacao(a,b):
	return a * b; 

def subtracao(a,b):
	return a - b;

def divisao(a,b):
	return a / b;

def potencia(a,b):
	return a ** b;

def menu():
	print("CALCULADORA:");
	print("1- SOMA (+)");
	print("2- MULTIPLICAÇÃO (*)");
	print("3- SUBTRAÇÃO (-)");
	print("4- DIVIÇÃO (/)");
	print("5- POTENCIAÇÃO (^)");
	print("6- SAIR (x)");

def main():
	i = 0;
	valores = []
	while(i < 10):
		menu();
		print("Digite a equação");
		for i in range(0,3):
			valores.append(input());

		if(valores[1] == "+"):
			print(soma(valores[0],valores[2]));
		elif(valores[1] == "*"):
			print(multiplicacao(valores[0],valores[2]));
		elif(valores[1] == "-"):
			print(subtracao(valores[0],valores[2]));
		elif(valores[1] == "/"):
			print(divisao(valores[0],valores[2]));
		elif(valores[1] == "^"):
			print(potencia(valores[0],valores[2]));
		elif(valores[1] == "x"):
			print("Saindo...");
			i = 11;
		else:
			print("Operação inválida");

main();

