edat=int(input("Hola, diga'm la teva edat"))
if edat>=18:
    print("Molt bé, ets major d'edat")
    print("programa acabat")
else:
    edatfaltant=18-(edat)
    print(f"Encara ets menor, et falten {edatfaltant} ")