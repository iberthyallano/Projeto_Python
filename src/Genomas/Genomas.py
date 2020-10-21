class Genomas:
    def __init__(self, entrada, saida):
        self.entrada = open(entrada).read();
        self.saida = open(saida, "w");
        self.genoma = {}
        for i in ['A','T','C','G']:
            for j in ['A','T','C','G']:
                self.genoma[i+j] = 0;

    def resultGenomas(self):
        self.entrada = self.entrada.replace("\n", "");
        for k in range(len(self.entrada)-1):
            self.genoma[self.entrada[k] + self.entrada[k+1]] += 1;
        return self.genoma;
    
    def criaHtml(self):
        i = 1;
        for t in self.genoma:
            transparencia = self.genoma[t] / max(self.genoma.values());
            self.saida.write("<div style='width:100px; border:1px solid #111; height:100px; float:left; background-color:rgba(0, 0, 0, "+str(transparencia)+"); color:white'>"+t+"</div>\n");
            if(i%4 == 0):
                self.saida.write("<div style='clear:both'></div>\n");
            i += 1
        self.saida.close();