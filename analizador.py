productos = [
    {"nombre": "Producto A", "precio": 150},
    {"nombre": "Producto B", "precio": 200},
    {"nombre": "Producto C", "precio": 50},
    {"nombre": "Producto D", "precio": 400},
    {"nombre": "Producto E", "precio": 350},
]

def categorizar_precio(producto):
    producto_nombre = producto["nombre"]
    producto_precio = producto["precio"]
    if producto_precio < 200:
        return f"{producto_nombre} es un producto económico."
    elif producto_precio < 300:
        return f"{producto_nombre} es un producto de precio medio."
    else:
        return f"{producto_nombre} es un producto caro."

def analizar_precio(productos):
    resultados = []
    for producto in productos:
        resultado = categorizar_precio(producto)
        resultados.append(resultado)
    return resultados

print(analizar_precio(productos))

def precio_promedio(productos):
    total_precio = 0
    for producto in productos:
        total_precio += producto["precio"]
    promedio = total_precio / len(productos)
    return promedio

print(precio_promedio(productos))

def producto_mas_caro(productos):
    producto_caro = productos[0]
    for producto in productos:
        if producto["precio"] > producto_caro["precio"]:
            producto_caro = producto
    return producto_caro

print(f"Producto más caro: {producto_mas_caro(productos)['nombre']}")

def producto_mas_barato(productos):
    producto_barato = productos[0]
    for producto in productos:
        if producto["precio"] < producto_barato["precio"]:
            producto_barato = producto
    return producto_barato

print(f"Producto más barato: {producto_mas_barato(productos)['nombre']}")


def generar_reporte(productos):
    print("===== REPORTE DE PRECIOS =====")
    for categoria in analizar_precio(productos):
        print(categoria)
    print(f"Precio promedio: {precio_promedio(productos)}") # 2. calcular el precio promedio (usar precio_promedio)
    print(f"Producto más caro: {producto_mas_caro(productos)['nombre']}") # 3. producto más caro (usar producto_mas_caro)
    print(f"Producto más barato: {producto_mas_barato(productos)['nombre']}") # 4.
    print("==============================")
            
    
generar_reporte(productos)