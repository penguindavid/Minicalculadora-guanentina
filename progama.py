input 

import math 
print("------------------------")
print("1)suma")
print("2)resta")
print("3)multiplicacion")
print("4)divizion")
print("5)potencia")
print("6)logaritmo ")
print("------------------------")

opc =int(input("digite la operacion a realizar: "))

x = int(input("digite el primer numero de la operacion: "))
y = int(input("digite el segundo numero de la operacion: "))

if opc == 1:
    print(f"el resultado de la suma es {(x)+(y)}")

if opc == 2:
    print(f"el resultado de la resta es {(x)-(y)}")

if opc == 3:
    print(f"el resultado de la multiplicacion es {(x)*(y)}")

if opc == 4:
    print(f"el resultado de la division es {(x)/(y)}")

if opc == 5:
    print(f"el resulado de la potencia es {(x)**(y)}")

if opc == 6:
    print("El valor es: ", math.log(x, y))

else:
    print("error")


