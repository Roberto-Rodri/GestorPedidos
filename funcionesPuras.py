def total_pedidos(x):
    return len(x)

#def pedidos_pagados(x):
    #df_pagados=x[x['estado']== 'pagado']
   # return len(df_pagados)  

def total_pagados(lista):
    if not lista: 
        return 0
    
    cabeza = lista[0]
    cola = lista[1:]
    
    # Si el estado es pagado, sumamos. Si no, sumamos 0.
    valor = (cabeza['cantidad'] * cabeza['precio']) if cabeza['estado'] == 'pagado' else 0
    
    return valor + total_pagados(cola)
