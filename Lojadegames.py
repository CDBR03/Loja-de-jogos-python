#Programador: César Xavier Cavalcanti Donato 01/11/2023
nomeEmpresa='LOJA DE JOGOS'
print('=+='*15)
print (f'{nomeEmpresa:^40}')

listaDeJogos=['LORDS OF THE FALLEN','SPIDER-MAN 2','UNCHARTED','THE SIMS 4','SPIDER-MAN REMASTERED','THE LAST OF US Pt1']
ListaPreco=[350,300,150,50,250,300]
print('COD=+==+JOGOS=+==+==+==+==+==+==+==+==+=VALOR')
#laço de repetiçao para mostrar a lista de jogos e seus devidos preços
for i in range(len(listaDeJogos)):
    print(f'{i}  {listaDeJogos[i]:<25}:          R${ListaPreco[i]}') 
print('=+='*15)
carrinho=[]
#função criada para salvar em txt
def salvar_carrinho(carrinho):
    with open('carrinho.txt', 'a') as texto:
        texto.write(f' {carrinho}')
        
#laço de repetição para o menu interativo
while True:
    menu=input('Menu:\n1. Adicionar jogo ao carrinho\n2. Remover jogo do carrinho\n3. Exibir carrinho\n4. Calcular total\n5. Sair')
    if menu == '1':        
        print("\nLista de jogos disponíveis:")
        for i in range(len(listaDeJogos)):
            print(f'{i} - {listaDeJogos[i]}: R${ListaPreco[i]}')
        escolha = int(input("Digite o número do jogo que deseja adicionar ao carrinho: "))
        if escolha >= 0 and escolha < len(listaDeJogos):
            #append funçao para adicionar o jogo e o preço dele no carrinho
            carrinho.append((listaDeJogos[escolha], ListaPreco[escolha]))
            print(f'{listaDeJogos[escolha]} foi adicionado ao carrinho.')
    elif menu == '2':
        if len(carrinho) == 0:
            print("O carrinho está vazio.")
        else:
            print("\nItens no carrinho:")
            for i, (jogo, preco) in enumerate(carrinho):
                print(f'{i} - {jogo}: R${preco}')
            escolha = int(input("Digite o número do jogo que deseja remover do carrinho: "))
            if escolha >= 0 and escolha < len(carrinho):
                # pop, função para tirar o jogo que nao deseja no carrinho
                jogo_removido, _ = carrinho.pop(escolha)
                print(f'{jogo_removido} foi removido do carrinho.')

    elif menu == '3':
        if len(carrinho) == 0:
            print("O carrinho está vazio.")
        else:
            print("\nItens no carrinho:")
            for i, (jogo, preco) in enumerate(carrinho):
                print(f'{i} - {jogo}: R${preco}')

    elif menu == '4':
        #  o underline que coloquei, é uma palavra reservada que usei para que a soma seja efetuada só com o preço
        total = sum(preco for _, preco in carrinho)
        print(f"\nTotal a pagar: R${total:.2f}")

    elif menu == '5':
        print("Obrigado por fazer compras na LOJA DE JOGOS. Volte sempre!")
        salvar_carrinho(carrinho)
        break


