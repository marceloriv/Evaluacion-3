pasajeros = []
ganancia_total = 0
asiento_comun = 0
acumulador_comun = 0
asiento_piernas = 0
acumulador_piernas = 0
asiento_no_reclina = 0
acumulador_no_reclina = 0
precios_asientos = ({
    "común":60000,
    "espacio adicional piernas":80000,
    "No reclina":50000
    })


def comprar_pasaje():
    try:
        cantidad_pasajes = int(input("¿Cuando pasajes desea comprar?\n"))
    except ValueError:
        print("Solo números")
        return
    while cantidad_pasajes > 198:
        print("No puede superar la cantidad de asientos")
        cantidad_pasajes = int(input("¿Cuando pasajes desea comprar?\n"))
    if cantidad_pasajes < 0 or not cantidad_pasajes:
        print("La cantidad de pasajes no puede ser negativo\nNo puede estar vació")
    for pasajes in range(cantidad_pasajes):
        print("\tPrecios Asientos")
        print(f"1.Común:{precios_asientos["común"]}$")
        print(f"2.Espacio adiciona para piernas:{precios_asientos["espacio adicional piernas"]}$")
        print(f"3.No reclina:{precios_asientos["No reclina"]}$")
        try:
            rut = input("ingrese su rut:\n-Sin guion ni puntos\n-Formato numérico\n-Sin dígito verificador\n ")
        except ValueError:
            print("Solo números")
            return
        while not rut or len(rut)>=9 or rut.isalpha()==True:
            print("El rut esta mal ingresado")
            rut = input("ingrese su rut:\n-Sin guion ni puntos\n-Formato numérico\n-Sin dígito verificador\n ")
            
        try:
            asiento = int(input("Elija su tipo de asiento:"))
        except ValueError:
            print("Valor incorrecto")
            return
        if asiento == 1:
            tipo_asiento=precios_asientos["común"]
            asiento_comun += 1
            acumulador_comun+=precios_asientos["común"]
        elif asiento == 2:
            tipo_asiento=precios_asientos["espacio adicional piernas"]
            asiento_piernas+=1
            acumulador_piernas += precios_asientos["espacio adicional piernas"]
        elif asiento == 3:
            tipo_asiento=precios_asientos["No reclina"]
            asiento_no_reclina+=1
            acumulador_no_reclina += precios_asientos["No reclina"]
        pasajero = {
            "rut":rut,
            "Tipo de asiento":tipo_asiento
            }
        pasajeros.append(pasajero)


def mostrar_ubicaciones_disponibles():
        if not pasajeros:
            print("No hay pasajeros para buscar")


def listado_de_pasajeros():
    if not pasajeros:
        for i in pasajeros:
            print(f"rut:"[i["rut"]])
            print(f"Tipo de asiento:"[i["tipo_asiento"]])

def buscar_pasajero():
    if not pasajeros:
        print("No hay pasajeros para buscar")
    rut_a_buscar = input("Ingrese a rut a buscar")
    for pasajero in pasajeros:
        if rut_a_buscar == pasajeros[pasajero["rut"]]:
            print(pasajero)


def reasignar_asiento():
    if not pasajeros:
        print("No hay pasajeros para reasignar")



def mostrar_ganancias_totales():
    print("Tipo de Asiento\t\tCantidad\tTotal")
    print(f"Asiento Común:${precios_asientos['común']}\t\t{asiento_comun}\t{acumulador_comun}")
    print(f"Asiento Común:${precios_asientos['espacio adicional piernas']}\t\t{asiento_piernas}\t{acumulador_piernas}")
    print(f"Asiento Común:${precios_asientos['No reclina']}\t\t{asiento_no_reclina}\t{acumulador_no_reclina}")


def menu():
    while True:
        print("1.Comprar Pasajes")
        print("2.Mostrar ubicaciones disponibles")
        print("3.Listado de pasajeros")
        print("4.Buscar Pasajeros")
        print("5.Reasignar Asiento")
        print("6.Mostrar Ganancias totales")
        print("7.Salir")
        try:
            opcion = int(input("Ingrese una opción: "))
        except ValueError as ex:
            print(f"Solo numero\n{ex}")
            return
        if opcion == 1:
            comprar_pasaje()
        elif opcion == 2:
            mostrar_ubicaciones_disponibles()
        elif opcion == 3:
            listado_de_pasajeros()
        elif opcion == 4:
            buscar_pasajero()
        elif opcion == 5:
            reasignar_asiento()
        elif opcion == 6:
            mostrar_ganancias_totales()
        elif opcion == 7:
            print("Adios...")
        else:
            print("Opcion incorrecta")
            return

# _main_
while True:
    try:
        menu()
    except Exception as error:
        print(f"Ocurrió un error inesperado\n{error}")
        continue

