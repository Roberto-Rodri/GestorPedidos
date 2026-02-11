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
            print(f"El numero total de pedidos es: {total_pedidos}")
        case "2":
            total_pagados = n.total_pagados(df)
            print(total_pagados)
        case "3":
            nombre = str(input("Ingrese el nombre del cliente: "))
            print(y.consultar_info(df, nombre))
        case "0":
            print("Saliendo...")
            break
        case _:
            print("Opcion invalida")
