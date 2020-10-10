#-*- coding: utf-8 -*-

arquivo1 = open("arquivo.txt");

lendo = arquivo1.read();
print(lendo);

arquivo2 = open("arquivo.txt");

linhas = arquivo2.readlines();
for linha in linhas:
	print(linha);

criaArquivo = open("arquivo2.txt", "w");
criaArquivo.write("TÔ ESCREVENDO NO ARQUIVO");
criaArquivo.close();

adicionaNoArquivo = open("arquivo2.txt", "a");
adicionaNoArquivo.write("\nTÔ ADICIONANDO NO ARQUIVO");
adicionaNoArquivo.close();




