class Restaurante:
    def __init__(self, nome: str):
        self.nome = nome
        self.pedidos: list['Pedido'] = []
    
    def adicionar_pedido(self, pedido: 'Pedido'):
        self.pedidos.append(pedido)

class Cliente:
    def __init__(self, nome: str, endereco: str):
        self.nome = nome
        self.endereco = endereco
        self.restaurantes_favoritos: list[Restaurante] = []
    
    def adicionar_restaurante_favorito(self, restaurante: Restaurante):
        self.restaurantes_favoritos.append(restaurante)

class Pedido:
    def __init__(self, cliente: Cliente, itens: dict[str, float]):
        self.cliente = cliente
        self.itens = itens
    
    def calcular_valor_total(self):
        soma = sum(self.itens.values())
        return soma

    def exibir_detalhes(self):
        detalhes = f"""
        Cliente: {self.cliente.nome}
        Endereço: {self.cliente.endereco}
        Itens:
        """

        for item, preco in self.itens.items():
            detalhes += f"- {item}, R$ {preco}\n"

        return detalhes

    def exibir_detalhes_com_list_comprehension(self):
        return f"""
        Cliente: {self.cliente.nome}
        Endereço: {self.cliente.endereco}
        Itens:
        {[f"- {item}, R$ {preco}\n" for item, preco in self.itens.items()]}
        """

maninhos_grill = Restaurante("Maninhos Grill")
saldoce = Restaurante("Saldoce")

cliente_1 = Cliente("Diego", "Rua Endereço do Diego, 123")
cliente_1.adicionar_restaurante_favorito(saldoce)

itens_do_diego = {
    "Margheritta Grande": 70.0,
    "Coquinha Zero Lata": 7.5,
}

pedido_123 = Pedido(cliente_1, itens_do_diego)

saldoce.adicionar_pedido(pedido_123)

valor_total = pedido_123.calcular_valor_total()
print(f"O valor total do pedido é: R$ {valor_total}")
print(pedido_123.exibir_detalhes())
