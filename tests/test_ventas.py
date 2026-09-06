from src.ventas import actualizar_stock


def test_actualizar_stock_despues_de_venta():
    stock_inicial = 10
    cantidad_vendida = 3

    stock_final = actualizar_stock(stock_inicial, cantidad_vendida)

    assert stock_final == 7