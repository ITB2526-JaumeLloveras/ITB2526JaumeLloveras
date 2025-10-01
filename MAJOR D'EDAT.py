print("Bon dia")
nom=input("Diga'm el teu nom")
from datetime import date
avui = date.today ()
print(f"Avui estem a {avui}")
naixement=int(input(f"Perfecte {nom} ara diga'm l'any que vas neixer"))
any=(avui.year)
mes=(avui.month)
dia=(avui.day)
if any-naixement>18:
    print("Molt Bé ets major d'edat")
    edat= any-naixement
    MJ=edat-18
    print(f"Portes {MJ} any sent major d'edat")
elif any-naixement==18:
    naixementmes=int(input(f"De quin mes ets"))
    if mes-naixement>0:
        MJM=mes-naixementmes
        print(f"et falten {MJM} per tenir els 18")
    elif mes-naixementmes<0:
        print("Encara no ets major d'edat")
    elif mes-naixementmes==0:
        naixementdia=int(input("Quin dia has nascut"))
        if naixementdia-dia==0:
            print("Moltes felicitats, es el teu aniversari")
        elif naixementdia-dia>0:
            MJF=naixementdia-dia
            print(f"Mala sort, et quedan encara {MJF} dias per a tenir els 18")
        elif naixementdia-dia<0:
            print("Enorabona, ja tens 18")
elif any-naixement<18:
    print("Mala sort, encara no ets major d'edat")





