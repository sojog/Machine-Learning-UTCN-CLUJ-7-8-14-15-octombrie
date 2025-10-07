# IN alte limbaje:
# for (i=0; i<10; i++) :

# IN python:
lista_mea = [32, 31, 0, "Salut", "bine"]
for item in lista_mea:
    print(item)


for i in range(5): # ECHIVALENT CU for (i=0; i<5; i++) 
    print(i)

print()
for i in range(2, 7): # ECHIVALENT CU for (i=0; i<5; i++) 
    print(i)


r = range(2, 7)
print(r) # Afiseaza obiectul 

list_r = list(r)
print(list_r)