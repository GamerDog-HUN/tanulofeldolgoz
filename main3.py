#0
print("Tanulok feldolgozása.")

#1
tanulok = []
while True:
    print("Kérem a tanuló adatait:")
    tanulo={}
    tanulo["nev"] = input("Tanulo neve: ")
    tanulo["szId"] = input("Tanuló születési ideje: ")
    tanulo["magassag"] = int(input("Magasság: "))

    tanulok.append(tanulo)

    valasz = input("További tanuló? (igen/nem): ")
    if valasz.lower() != 'igen':
        break

#2


#3 Hozzáférés listaelem segítségével.
print("\nTanulók listája\n")
for item in tanulok:
    #!!!!!Figylni kell arra hogy az f-string és a kulcsoknka a határolói külnbőzöek legyenek
    print(f'Név: {item["nev"]}, születési ideje: {item["szId"]}, magasság: {item["magassag"]}')