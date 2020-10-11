#-*- coding: utf-8 -*-

class Potencia:
    def __init__(self,a,b):
        self.base = a;
        self.expoente = b;

    def resultPotencia(self):
        return self.base ** self.expoente; 
    
    def multiplicaPotencia(self, potenciacao):
        if(self.base == potenciacao.base):
            return Potencia(self.base, (potenciacao.expoente + self.expoente));
        elif(self.expoente == potenciacao.expoente and self.base != potenciacao.base):
            return Potencia((self.base * potenciacao.base), self.expoente);
        else:
            return Potencia((self.resultPotencia() * potenciacao.resultPotencia()), 1);

    def dividePotencia(self, potenciacao):
        if(self.base == potenciacao.base):
            return Potencia(self.base, (self.expoente - potenciacao.expoente));
        elif(self.expoente == potenciacao.expoente and self.base != potenciacao.base):
            return Potencia((self.base / potenciacao.base), self.expoente);
        else:
            return Potencia((self.resultPotencia() / potenciacao.resultPotencia()), 1);

    def potenciaDePotencia(self, expoente2):
        return Potencia(self.base, (self.expoente * expoente2));
        
