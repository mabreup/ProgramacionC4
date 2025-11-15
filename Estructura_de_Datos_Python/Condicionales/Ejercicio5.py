#Ingresa el monto de una compra. Si es mayor a 500 aplica un 10% de descuento, sino paga precio normal.
monto = float(input("Por favor, ingresa el monto de la compra: "))
if monto > 500:
    desc = monto * 0.10
    total = monto - desc
    print("Se aplicó un descuento del 10%. El total a pagar es:", total)
else:
    print("El total a pagar es:", monto)
    