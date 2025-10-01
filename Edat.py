edat=int(input("Hola, diga'm la teva edat"))
if edat>=18:
    print("Molt bé, ets major d'edat")
    edatMJ=(edat)-18
    if edatMJ==0:
        print("Has complert aquest any, enorabona")
    else:
        print(f"Portes sent major d'edat {edatMJ}")
    print("programa acabat")
else:
    edatfaltant=18-(edat)
    print(f"Encara ets menor, et falten {edatfaltant} ")
    print("Programa finalitzat")