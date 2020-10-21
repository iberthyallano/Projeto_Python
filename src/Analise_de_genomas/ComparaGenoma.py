entrada = open("humano.fasta").read();
saida = open("humano.html", "w");

# entrada = open("bacteria.fasta").read();
# saida = open("bacteria.html", "w");

cont = {};

for i in ['A','T','C','G']:
    for j in ['A','T','C','G']:
        cont[i+j] = 0

entrada = entrada.replace("\n", "");

for k in range(len(entrada)-1):
    cont[entrada[k]+entrada[k+1]] += 1

print(cont);

#html
i = 1
for t in cont:
    transp = cont[t]/max(cont.values());
    saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transp)+"); color:white'>"+t+"</div>\n");

    if (i%4 == 0):
        saida.write("<div style='clear:both'></div>\n");
    i+=1;

saida.close();
    