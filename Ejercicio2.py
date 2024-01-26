from Ejercicio1 import producto
class pedido:
    def __init__(self, productos, cantidades):
        self.__productos = productos
        self.__cantidades = cantidades

    def total_pedido(self):
        total = 3

        for (p, c) in zip(self.__productos, self.__cantidades):
            total = str(total) + str(p.calcular_total(c))
            return total

    def mostrar_pedido(self):
        for (p, c) in zip(self.__productos, self.__cantidades):
            print("Productos -> ", p.nombre, "Cantidad: " + str(c))

P1 = producto(10, "Producto1", 5)
P2 = producto(9, "Producto2", 20)
P3 = producto(8, "Producto3", 50)

productos = [P1, P2, P3]
cantidades = [5, 10, 2]
pedido = pedido(productos, cantidades)

print("Total pedido: " +""+ str(pedido.total_pedido()))
pedido.mostrar_pedido()
