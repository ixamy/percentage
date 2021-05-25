#by ixamy
def percentage(paid,total):
    paid=float(paid)
    total=float(total)
    percentage="{:.2f}".format(paid*100/total)
    return percentage

print("Ingresar monto adelanto, total e imprimir en pantalla el porcentaje correspondiente.")
print('\nPorcentaje: ' + str(percentage(input('Adelanto: '),input('Total: '))))
input('\nPresionar Enter para salir...')