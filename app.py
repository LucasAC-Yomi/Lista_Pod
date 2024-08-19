from bs4 import BeautifulSoup

listaNome = []
listaPreco = []

file = open("index.txt", "r", encoding='UTF8')
texto = file.read()
dados = BeautifulSoup(texto, "html.parser")
for item in dados.findAll("h6", class_="titulo-produto"):
    nome = item.find("div").text.replace("POD Descartável ","").replace("Pod Descartável ","")
    precos = item.findAll("div", class_="preco-produto")
    if precos[2].text.find("TABELA 1") == 1:
        preco =precos[2].text.replace(" TABELA 1 (R$ 300) ","")
    if precos[1].text.find("TABELA 1") == 1:
        preco =precos[1].text.replace(" TABELA 1 (R$ 300) ","")
    if precos[0].text.find("TABELA 1") == 1:
        preco =precos[0].text.replace(" TABELA 1 (R$ 300) ","")
    listaNome.append(nome)
    listaPreco.append(nome+" "+preco)
file.close()

listaNome.sort()
listaPreco.sort()

with open("Produto.txt", "w", encoding='UTF8') as x:
    for item in listaNome:
        x.write('{}\n'.format(item))

with open("ProdutoPreco.txt", "w", encoding='UTF8') as x:
    for item in listaPreco:
        x.write('{}\n'.format(item))