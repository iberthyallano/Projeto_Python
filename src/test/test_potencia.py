from .Potencia import Potencia

p = Potencia(2, 2);
print(p.resultPotencia());#2² = 4


print("\n");
#POTENCIA DE MESMA BASE 
pot1 = Potencia(2,3);
a = p.multiplicaPotencia(pot1);#2⁵ = 32
print(a.resultPotencia());

pot2 = Potencia(2,6);
b = pot2.dividePotencia(p);
print(b.resultPotencia());#2⁴ = 16


print("\n");
#POTENCIA DE BASES DISTINTAS E MESMO EXPOENTE
pot1 = Potencia(3,2);
c = p.multiplicaPotencia(pot1);# (3*2)² = 36
print(c.resultPotencia());

pot2 = Potencia(6,2);
d = pot2.dividePotencia(p);
print(d.resultPotencia());# (6/2)² = 9


print("\n");
#POTENCIA DE BASES DISTINTAS E EXPOENTE DISTINTOS
pot1 = Potencia(3,3);
c = p.multiplicaPotencia(pot1);# 2² * 3³ = 108
print(c.resultPotencia());

pot2 = Potencia(3,3);
d = pot2.dividePotencia(p);
print(d.resultPotencia());# 3³ * 2² = 6.75


print("\n");
#POTENCIA DE POTENCIA
expo = 5;
e = p.potenciaDePotencia(expo);
print(e.resultPotencia());#2¹⁰ = 1024