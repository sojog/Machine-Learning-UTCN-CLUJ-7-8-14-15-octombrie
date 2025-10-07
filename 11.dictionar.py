## LISTA este o COLECTIE ORDONATA
#     0        1         2 
l = ["Ana", "Maria", "Andreea"]

print("Lungimea listei", len(l))

## DICTIONARUL este o COLECTIE bazata de cheie 
d = {
    # cheie : valoare
    "verde" : "Ana",
    "rosu": "Maria",
    "albastru":"Andreea"
}

print("Lungimea dictionarului", len(d))

print(l[0])
print(d["verde"])

### ADAUGARE IN LISTA
l.append("Florina")

### ADAUGARE IN DICTIONAR
d["blue"] = "Florina"

print(l)
print(d)