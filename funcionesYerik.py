def consultar_info(df, nombre):
    info = df.loc[lambda i: i["cliente"].str.contains(nombre, case=False, na=False)]
    return info
