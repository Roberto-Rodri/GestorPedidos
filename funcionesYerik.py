import unicodedata as u


def consultar_info(d, nombre):
    acentos = lambda s: (
        u.normalize("NFKD", s).encode("ascii", errors="ignore").decode("utf-8")
    )
    nombre_limpio = acentos(nombre)

    info = d.loc[
        lambda df: (
            df["cliente"]
            .apply(lambda x: acentos(str(x)))
            .str.contains(nombre_limpio, case=False, na=False)
        )
    ]
    return info


def inferir_info(d):
    envio_listo = d[d["estado"].apply(lambda x: x == "pagado")]
    return envio_listo


def total_pagados(df):
    if df.empty:
        return 0

    cabeza = df.iloc[0]
    cola = df.iloc[1:]

    if cabeza["estado"] == "pagado":
        valor_actual = cabeza["cantidad"] * cabeza["precio"]
    else:
        valor_actual = 0

    return valor_actual + total_pagados(cola)
