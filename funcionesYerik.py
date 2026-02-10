import baseDatos as bd


def consultar_info(nombre):
    bd.df_pedidos.loc[lambda i: i["cliente"].str.contains(nombre, case=False, na=False)]
