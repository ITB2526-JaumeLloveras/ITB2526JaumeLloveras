#Algoritme que permeti a l'usuari calcular el consum d'aigua en un domicili.
#Calcula la factura d'aigua, donats en litres d'aigua gastats per l'usuari sabent el seguent
#Hi ha cuota fixe de 6 euros mensuals
#Consum menor de 50 litres, no es paga la quota variable nomes fixe
#Consum entre 50 i 200 litres, es paga 0.10 euros per litre
#Consum superior a 200 litres, es paga 0.3 euros per litre
# En catala tot siusplau
try:
    litres_gastats=float(input("Introdueix els litres d'aigua gastats aquest mes: "))
except ValueError:
    print("Si us plau, introdueix un número vàlid per als litres gastats.")
    try:
        litres_gastats=float(input("Introdueix els litres d'aigua gastats aquest mes: "))
    except ValueError:
        print("Entrada invàlida. Si us plau, reinicia el programa i introdueix un número vàlid.")
    else:
        quota_fixa=6.0
        if litres_gastats < 50:
            quota_variable=0.0
        elif 50 <= litres_gastats <= 200:
            quota_variable=litres_gastats * 0.10
        else:
            quota_variable=litres_gastats * 0.30
        factura_total=quota_fixa + quota_variable
        print(f"La teva factura d'aigua aquest mes és de {factura_total:.2f} euros.")
else:
    quota_fixa=6.0
    if litres_gastats < 50:
        quota_variable=0.0
    elif 50 <= litres_gastats <= 200:
        quota_variable=litres_gastats * 0.10
    else:
        quota_variable=litres_gastats * 0.30
    factura_total=quota_fixa + quota_variable
    print(f"La teva factura d'aigua aquest mes és de {factura_total:.2f} euros.")


