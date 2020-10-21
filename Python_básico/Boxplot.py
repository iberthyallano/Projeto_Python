import matplotlib.pyplot as plt;
import random

vetor = [];

for i in range(10):
    aux = random.randint(0, 500);
    vetor.append(aux);

plt.boxplot(vetor);
plt.title("Boxplot");
plt.show();