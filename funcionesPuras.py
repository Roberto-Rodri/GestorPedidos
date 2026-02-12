def total_pedidos(df):
    return len(df)


def pedidos_pagados(x):
    df_pagados = x[x["estado"] == "pagado"]
    return len(df_pagados)
