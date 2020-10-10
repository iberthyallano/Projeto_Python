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
	print("1- SOMA");
	print("2- MULTIPLICAÇÃO");
	print("3- SUBTRAÇÃO");
	print("4- DIVIÇÃO");
	print("5- POTENCIAÇÃO");
	print("6- SAIR");

def main():
	i = 0;
	while(i < 10):
		menu();
		op = input("Digite a operação que deseja fazer: ");
		if(op < 1 or op > 6):
			print("NÃO EXISTE ESSA OPÇÃO");
		
		if(op == 6):	
			print("Saindo...");
			i = 11;
		
		else:	
			A = input("Digite o valor de A: ");
			B = input("Digite o valor de B: ");
			if(op == 1):
				print(soma(A,B));
			elif(op == 2):
				print(multiplicacao(A,B));
			elif(op == 3):
				print(multiplicacao(A,B));
			elif(op == 4):
				print(multiplicacao(A,B));
			elif(op == 5):
				print(multiplicacao(A,B));


main()

