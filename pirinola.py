import random
pirinola=0
puntos_acumulados=0
for i in range(1,3): 
    toma=('toma:1','toma:2','toma todo',"pon 2","pon 1","pierde todo")
    decidetirar=(int(input("desea seguir jugando pirinola?, marque el numero que desea 1.si 2.no (recuerde que tiene 3 intentos) ")))
    if decidetirar==1:
        pirinola=pirinola+1
        tomas=random.choice(toma)
        print("la cara de la pirinola es: ",tomas)
        if tomas=="toma 1":
            puntos_acumulados=puntos_acumulados+2
            print("usted gano 2 puntos")
        if tomas=="toma 2":
            print("usted gano 1 puntos")
            puntos_acumulados=puntos_acumulados+1
        if tomas=="toma todo":
                print("usted multiplico los puntos")
                puntos_acumulados=puntos_acumulados*2
        if tomas=="pon 2":
        
                print("usted perdio 2 puntos")
                puntos_acumulados=puntos_acumulados-2

                print("usted tiene 0 puntos")
        if tomas=="pon 1":
                puntos_acumulados=puntos_acumulados-1
                print("usted tiene 0 puntos")
        if tomas=="pierde todo":
            tirapirinola=tirapirinola+3
            print("usted perdio todo")
            puntos_acumulados=puntos_acumulados-puntos_acumulados
    print("puntos que lleva: ",puntos_acumulados)
    if decidetirar==2:
        pirinola=pirinola+3
        print("usted salio del juego por lo tanto termino")
print("gracias por jugar"," obtuvo un total de: ",puntos_acumulados)

    