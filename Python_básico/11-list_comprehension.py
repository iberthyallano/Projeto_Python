#-*- coding: utf-8 -*-
#SEM_LIST_COMPREHENSION
x = [1,2,3,4,5];
y = [];

for i in x:
	y.append(i**2);

print(x);
print(y);

print("\n");

#COM_LIST_COMPREHENSION

z = [1,2,3,4,5];
t = [i**2 for i in z];
w = [i for i in z if i%2==1]

print(z);
print(t);
print(w);
