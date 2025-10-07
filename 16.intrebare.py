
friends = [  ("andrew",10),("george",20),("andrew",5),("ann",10) ]

for i in friends:
    print(i, type(i))

## Iterez printr-o lista pentru a adauga in dictionar
names = { }
print("names:", names, type(names))
for name, amount in friends:
    print(name, amount, type(name), type(amount))
    names[name] = amount
print("names:", names, type(names))


### ITEREARE PRINT-O COLECTIE PENTRU A ADAUGA IN ALTA COLECTIE  (COMPREHENTION)
## DICTIONARY COMPREHENTION
names = { name : amount for name, amount in friends }
print("names:", names, type(names))


## SET COMPREHENTION
names = { name for name, amount in friends }
print(names)