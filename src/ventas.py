def actualizar_stock(stock_actual, cantidad_vendida):
    if cantidad_vendida <= 0:
        raise ValueError("La cantidad vendida debe ser mayor que cero")

    if cantidad_vendida > stock_actual:
        raise ValueError("Stock insuficiente")

    return stock_actual - cantidad_vendida