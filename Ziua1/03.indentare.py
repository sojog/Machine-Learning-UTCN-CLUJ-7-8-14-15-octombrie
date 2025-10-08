

varsta = 20

# Varianta 1 - imbricare clasica
if varsta < 14:
    print("Copil")
else:
    if varsta < 18:
        print("Adolescent")
    else:
        if varsta < 65:
            print("Adult")
        else:  
            print("Pensionar")


# Varianta 2 - IF ELIF
if varsta < 14:
    print("Copil")
elif varsta < 18:
    print("Adolescent")
elif varsta < 65:
    print("Adult")
else:  
    print("Pensionar")