try:
    preuoriginal=float(input("Diga'm el preu original de l'article"))
    descompte=float(input("Diga'm el descompte que t'ofereixen en percentatge"))
except ValueError:
    print("Intrudueixme un número vàlid, no lletres")
    try:
        preuoriginal=float(input("Diga'm el preu original de l'article"))
        descompte=float(input("Diga'm el descompte que t'ofereixen en percentatge"))
    except ValueError:
        print("Intrudueixme un número vàlid")
    else:
        descomptefinal=(preuoriginal*descompte)/100
        preufinal=preuoriginal-descomptefinal
        print(f"El preu final de l'article es de {preufinal} euros")
else:
    descomptefinal=(preuoriginal*descompte)/100
    preufinal=preuoriginal-descomptefinal
    print(f"El preu final de l'article es de {preufinal} euros")






