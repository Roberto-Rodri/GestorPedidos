import baseDatos as bd
import funcionesPuras as n
import funcionesYerik as y

bd.df_pedidos.to_csv("pedidos.csv", index=False)
df = bd.df_pedidos
while True:
    print("=" * 50)
    print("OPCIONES")
    print("=" * 50)
    print("""
    1. Calcular totales de pedidos
    2. Identificar pedidos pagados
    3. Consultar información por cliente
    4. Inferir información a partir de reglas lógicas
    5. Salir
    """)

    opcion = str(input("Elige la opción: "))
    match opcion:
        case "1":
            total_pedidos = n.total_pedidos(df)
            print("=" * 50)
            print(f"El numero total de pedidos es: {total_pedidos}")
            print("=" * 50, "\n")
        case "2":
            total_pagados = n.total_pagados(df)
            print("=" * 50)
            print(f"El ingreso total de los pedidos pagados es: {total_pagados}")
            print("=" * 50, "\n")
        case "3":
            nombre = str(input("\nIngrese el nombre del cliente: "))
            print("Informacion del cliente")
            print("=" * 50)
            print(y.consultar_info(df, nombre))
            print("=" * 50, "\n")
        case "4":
            print("\nPedidos listos para envio\n")
            print("=" * 50)
            print(y.inferir_info(df))
            print("=" * 50, "\n")
        case "0":
            print("\nSaliendo...\n")
            break
        case _:
            print("\nOpcion invalida\n")
