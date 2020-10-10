#-*- coding: utf-8 -*-

X = "Meu eu sou:"
Y = "IBERTHY"
#CONCATENANDO_STRINGS
concatenar = X + " " + Y;
print(concatenar);
#TAMANHO_DA_STRING
tamanho = len(concatenar);
print(tamanho);
#PEGANDO_UMA_PARTE_ESPECÍFICA_DA_STRING
letra = Y[0];
print(letra);
#PEGANDO_UM_PEDAÇO_DA_STRING
pedaco = Y[0:4];
print(pedaco);
#TRANSFORMANDO_TODA_A_STRING_EM_MENUSCULA
menusculo = Y.lower();
print(menusculo);
#TRANSFORMANDO_TODA_A_STRING_EM_MAIUSCULA
maiusculo = X.upper();
print(maiusculo);
#TRANSFORMANDO_A_STRING_EM_MATRIZ
transformaLista = X.split(" ");
print(transformaLista[0]);
print(transformaLista[1]);
print(transformaLista[2]);


minhaString = "O RATO ROEU A ROUPA DO REI DE ROMA";
#FAZENDO_UMA_BUSCA_DENTRO_DE_UMA_STRING
busca = minhaString.find("REI");
print(busca);

#EXIBINDO_A_STRING_DE_BUSCA_ATÉ_O_FINAL
print(minhaString[busca:]);

#FAZENDO_UMA_SUBSTITUIÇÃO_EM_UMA_PARTE_DA_STRING
substituir = minhaString.replace("DO REI", "DA RAINHA");
print(substituir);















