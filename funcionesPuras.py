def total_pedidos(df):
    return len(df)


"""
def pedidos_pagados(x):
    df_pagados=x[x['estado']== 'pagado']
    return len(df_pagados)
"""


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
