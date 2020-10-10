notas = [];
total = 0;
for i in range(0,3):
	notas.append(input("Digite as notas: "));
	total += notas[i];
media = total / len(notas);
if(media < 6):
	print("Reprovado");
elif(media >= 6):
	print("Aprovado");

