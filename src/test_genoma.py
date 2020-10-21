from Genomas import Genomas;

entradaHumano = 'src/dadosGenoma/humano.fasta';
saidaHumano = 'src/dadosGenoma/humano.html';

entradaBacteria = 'src/dadosGenoma/bacteria.fasta';
saidaBacteria = 'src/dadosGenoma/bacteria.html';



h = Genomas(entradaHumano, saidaHumano);
b = Genomas(entradaBacteria, saidaBacteria);

h.resultGenomas();
print(h.genoma);
h.criaHtml();

print("\n");

b.resultGenomas();
print(b.genoma);
b.criaHtml();