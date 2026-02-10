import baseDatos as bd
import funcionesYerik as y

bd.df_pedidos.to_csv("pedidos.csv", index=False)

print("=" * 50)
print("OPCIONES")
print("=" * 50)
print("""
1. Calcular totales de pedidos
2. Identificar pedidos pagados
3. Consultar información por cliente
4. Inferir información a partir de reglas lógicas
0. Salir
""")

opcion = str(input("Elige la opción: "))
match opcion:
    case "3":
        nombre = str(input("Ingrese el nombre del cliente: "))
        print(y.consultar_info(nombre))
    case _:
        print("Opcion invalida")
