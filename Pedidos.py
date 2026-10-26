
class Order:
    def __init__(self, quantity, customer):
        self.quantity = quantity
        self.customer = customer

    def print(self):
        print(f"   Cliente: {self.customer}")
        print(f"   Cantidad: {self.quantity}")
        print("   ----------------")


class Node:
    def __init__(self, info):
        self.info = info
        self.next = None


class Queue:
    def __init__(self):
        self.top = None
        self.tail = None
        self.count = 0

    def size(self):
        return self.count

    def isEmpty(self):
        return self.count == 0

    def front(self):
        if self.isEmpty():
            return None
        return self.top.info

    def enqueue(self, info):
        nuevo = Node(info)

        if self.isEmpty():
            self.top = nuevo
        else:
            self.tail.next = nuevo

        self.tail = nuevo
        self.count += 1

    def dequeue(self):
        if self.isEmpty():
            return None

        pedido = self.top.info
        self.top = self.top.next
        self.count -= 1

        if self.isEmpty():
            self.tail = None

        return pedido

    def printInfo(self):
        print("\n******** QUEUE DUMP ********")
        print(f"Cantidad de pedidos: {self.size()}")

        actual = self.top
        posicion = 1

        while actual is not None:
            print(f"\n** Elemento {posicion}")
            actual.info.print()

            actual = actual.next
            posicion += 1

        if self.isEmpty():
            print("La cola esta vacia.")

        print("****************************\n")

    def getNth(self, pos):
        if pos < 1 or pos > self.size():
            return None

        actual = self.top

        for i in range(1, pos):
            actual = actual.next

        return actual.info


class TestQueue:
    @staticmethod
    def main():
        cola = Queue()

        pedido1 = Order(20, "Cliente 1")
        pedido2 = Order(30, "Cliente 2")
        pedido3 = Order(40, "Cliente 3")
        pedido4 = Order(50, "Cliente 4")

        print("=== INSERTANDO PEDIDOS ===")

        cola.enqueue(pedido1)
        cola.printInfo()

        cola.enqueue(pedido2)
        cola.printInfo()

        cola.enqueue(pedido3)
        cola.printInfo()

        cola.enqueue(pedido4)
        cola.printInfo()

        print("=== PRIMER PEDIDO ===")
        primero = cola.front()

        if primero is not None:
            primero.print()

        cola.printInfo()

        print("\n=== OBTENER ELEMENTO 3 ===")
        tercero = cola.getNth(3)

        if tercero is not None:
            tercero.print()
        else:
            print("Posicion no valida.")

        cola.printInfo()

        print("\n=== ATENDIENDO PEDIDO ===")
        atendido = cola.dequeue()

        if atendido is not None:
            print("Pedido atendido:")
            atendido.print()

        cola.printInfo()

        print("\n=== ATENDIENDO OTRO PEDIDO ===")
        atendido = cola.dequeue()

        if atendido is not None:
            atendido.print()

        cola.printInfo()


if __name__ == "__main__":
    TestQueue.main()
