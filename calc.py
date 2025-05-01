import pandas as pd

cards_precos = {
    1: 50.0,
    2: 49.0,
    3: 48.0,
    4: 47.0,
    5: 46.0,
    6: 45.0,
    7: 44.0,
    8: 43.0,
    9: 42.0,
    10: 41.0,
    11: 40.5,
    12: 40.0,
    13: 39.5,
    14: 39.0,
    15: 38.5,
    16: 38.0,
    17: 37.5,
    18: 37.0,
    19: 36.5,
    20: 36.0,
    21: 35.5,
    22: 35.0,
    23: 33.5,
    24: 32.0,
    25: 30.0
}

carrossel_precos = {
    1: 80.0,
    2: 78.0,
    3: 76.0,
    4: 74.0,
    5: 72.0,
    6: 70.0,
    7: 68.0,
    8: 66.0,
    9: 64.0,
    10: 62.0,
    11: 60.5,
    12: 59.0,
    13: 58.0,
    14: 57.0,
    15: 56.0,
    16: 55.0,
    17: 54.5,
    18: 54.0,
    19: 53.5,
    20: 53.0,
    21: 52.0,
    22: 51.0,
    23: 50.0,
    24: 49.0,
    25: 48.0
}

reels_precos = {
    1: 160.0,
    2: 156.0,
    3: 152.0,
    4: 148.0,
    5: 144.0,
    6: 140.0,
    7: 136.0,
    8: 132.0,
    9: 128.0,
    10: 124.0,
    11: 123.0,
    12: 122.0,
    13: 121.0,
    14: 120.0,
    15: 119.0,
    16: 118.0,
    17: 116.0,
    18: 114.0,
    19: 113.0,
    20: 112.0
}

opcoes = {
    1: ('Cards', cards_precos),
    2: ('Carrossel', carrossel_precos),
    3: ('Reels', reels_precos)
}

while True:
    print("Selecione a tabela desejada:")
    print("1 - Cards")
    print("2 - Carrossel")
    print("3 - Reels")
    print("4 - Sair")

    selecao = int(input("Digite a opção: "))

    if selecao == 4:
        print("Saindo...")
        break

    if selecao not in opcoes:
        print("Opção inválida.")
        continue

    quantidade = int(input("Digite a quantidade desejada: "))

    nome_tabela, precos = opcoes[selecao]

    def calcular_preco(quantidade):

        if quantidade in precos:
            preco_unitario = precos[quantidade]
        else:
            preco_unitario = precos[max(precos.keys())]

        preco_total = quantidade * preco_unitario

        return f"Tabela: {nome_tabela} - Quantidade: {quantidade}, Preço total: R$ {preco_total:.2f}. Preço unitário: R$ {preco_unitario:.2f}."

    resultado = calcular_preco(quantidade)
    print(resultado)
