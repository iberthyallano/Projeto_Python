from Genomas import Genomas;

entradaHumano = 'src/Database/DadosGenoma/humano.fasta';
saidaHumano = 'src/Database/DadosGenoma/humano.html';

entradaBacteria = 'src/Database/DadosGenoma/bacteria.fasta';
saidaBacteria = 'src/Database/DadosGenoma/bacteria.html';

h = Genomas(entradaHumano, saidaHumano);
b = Genomas(entradaBacteria, saidaBacteria);

h.resultGenomas();
print(h.genoma);
h.criaHtml();

print("\n");

b.resultGenomas();
print(b.genoma);
b.criaHtml();