class Produto:
    def __init__(
            self,
            nome_produto: str,
            preco: float,
            qnt_estoque: int
        ):

        self.nome_produto = nome_produto
        self.preco = preco
        self.qnt_estoque = qnt_estoque
        


class ItemDoPedido:
    def __init__(
            self,
            produto: Produto, # aqui vai utilizar o nome do produto referente a classe "Produto"
            quantidade: int
        ):
        
        self.produto = produto
        self.quantidade = quantidade


    def calcular_valor(self):
        return self.produto.preco * self.quantidade



class Pedido:
    def __init__(self):
        self.itens = [] # aqui uma lista vazia é criada para armazenar os itens do pedido

    def adicionar_item(self, item: ItemDoPedido):
        self.itens.append(item)

    def calcular_valor_total(self):
        return sum(item.calcular_valor() for item in self.itens) # aqui o método realizará uma soma dos itens da lista utilizando a estrutura for para percorer a lista
    
    def listar_itens(self):
        print("Resumo do pedido: ")
        for item in self.itens:
            print(f"Produto: {item.produto.nome_produto} \n Quantidade: {item.quantidade} \n Preco unitario: R${item.produto.preco:.2f}")
    

class Pagamento:
    def __init__(
            self,
            pedido: Pedido
            ):
        
        self.pedido = pedido

    def pagar(self, metodo: str):
        total = self.pedido.calcular_valor_total()
        print(f"Valor total do pedido: R${total:.2f}")
        if metodo.lower() == "dinheiro":
            print("Pagamento efetuado em dinheiro.")
        elif metodo.lower() == "cheque":
            print("Pagamento efetuado em cheque.")
        elif metodo.lower() == "cartão":
            print("Pagamento efetuado em cartão.")
        else:
            print("Método de pagamento inválido.")
        


produto1 = Produto("Arroz", 20.0, 10)
produto2 = Produto("Feijão", 10.0, 5)
produto3 = Produto("Macarrão", 5.0, 20)


item1 = ItemDoPedido(produto1, 2)
item2 = ItemDoPedido(produto2, 3)
item3 = ItemDoPedido(produto3, 1)


pedido = Pedido()
pedido.adicionar_item(item1)
pedido.adicionar_item(item2)
pedido.adicionar_item(item3)


pedido.listar_itens()

total = pedido.calcular_total()
print(f"Total do pedido: R${total:.2f}")


pagamento = Pagamento(pedido)
pagamento.pagar("cartão")