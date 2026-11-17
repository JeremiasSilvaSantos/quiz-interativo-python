# ==========================================
# BANCO DE PERGUNTAS POR CATEGORIA
# ==========================================
perguntas_geografia = [
    ["Qual é a capital da Austrália?", "A) Sydney", "B) Melbourne", "C) Canberra", "D) Perth", "C"],
    ["Qual é o maior oceano do planeta Terra?", "A) Atlântico", "B) Índico", "C) Ártico", "D) Pacífico", "D"],
    ["Em qual continente fica o deserto do Saara?", "A) Ásia", "B) África", "C) América", "D) Oceania", "B"],
    ["Qual é o rio mais extenso do mundo?", "A) Rio Nilo", "B) Rio Amazonas", "C) Rio Yangtzé", "D) Rio Mississipi", "B"]
]

perguntas_python = [
    ["Quem é o criador da linguagem Python?", "A) Dennis Ritchie", "B) Guido van Rossum", "C) James Gosling", "D) Bjarne Stroustrup", "B"],
    ["Em que ano o Python foi lançado oficialmente pela primeira vez?", "A) 1989", "B) 1991", "C) 1995", "D) 2000", "B"],
    ["De onde surgiu a inspiração para o nome 'Python'?", "A) Da cobra píton", "B) Do grupo de comédia Monty Python", "C) De um livro de ficção", "D) De um projeto da NASA", "B"],
    ["Qual filosofia guia o design da linguagem Python?", "A) The Zen of Python", "B) Write Once, Run Anywhere", "C) Keep It Simple", "D) Código Aberto Total", "A"]
]

perguntas_biologia = [
    ["Qual organela celular é responsável pela respiração celular e produção de energia (ATP)?", "A) Ribossomo", "B) Complexo de Golgi", "C) Mitocôndria", "D) Lisossomo", "C"],
    ["Qual é o processo pelo qual as plantas produzem seu próprio alimento usando luz solar?", "A) Quimiossíntese", "B) Fotossíntese", "C) Fermentação", "D) Transpiração", "B"],
    ["Quantos cromossomos possui uma célula somática humana normal?", "A) 23", "B) 44", "C) 46", "D) 48", "C"],
    ["Qual biomolécula carrega a informação genética dos seres vivos?", "A) DNA", "B) Glicose", "C) Colágeno", "D) Hemoglobina", "A"]
]

perguntas_matematica = [
    ["Quanto é 7 x 8?", "A) 54", "B) 56", "C) 58", "D) 64", "B"],
    ["Qual é a raiz quadrada de 144?", "A) 10", "B) 11", "C) 12", "D) 14", "C"],
    ["Em um triângulo retângulo, a soma dos quadrados dos catetos é igual ao quadrado da:", "A) Altura", "B) Base", "C) Hipotenusa", "D) Mediana", "C"],
    ["Qual é o valor aproximado de Pi (π) com duas casas decimais?", "A) 3,12", "B) 3,14", "C) 3,16", "D) 3,18", "B"]
]

# ==========================================
# FUNÇÃO DE EXECUÇÃO SEGURA DO QUIZ
# ==========================================
def jogar_quiz(lista_perguntas, nome_categoria):
    pontos = 0
    total = len(lista_perguntas)
    
    print("\n" + "=" * 40)
    print(f"--- INICIANDO QUIZ: {nome_categoria.upper()} ---")
    print("=" * 40)
    
    for indice, p in enumerate(lista_perguntas, start=1):
        print(f"\nPergunta {indice}/{total}: {p[0]}")
        print(p[1])
        print(p[2])
        print(p[3])
        print(p[4])
        
      
        while True:
            resposta = input("Sua resposta (A, B, C ou D): ").strip().upper()
            if resposta in ["A", "B", "C", "D"]:
                break
            else:
                print(" Entrada inválida! Digite apenas A, B, C ou D.")
        
        if resposta == p[5]:
            print(" Acertou!")
            pontos += 1
        else:
            print(f" Errou! A resposta correta era a letra {p[5]}.")
            
    print("\n" + "-" * 40)
    print(f"Fim do Quiz de {nome_categoria}!")
    print(f"Sua pontuação final: {pontos} de {total} pontos.")
    print("-" * 40)
    
  
    while True:
        nome = input("Digite seu nome para salvar no ranking: ").strip()
        if len(nome) > 0:
            break
        else:
            print(" O nome não pode ficar em branco. Tente novamente.")
            
    return [nome, pontos, nome_categoria]

# ==========================================
# LOOP PRINCIPAL DO SISTEMA
# ==========================================
ranking = []

while True:
    print("\n" + "=" * 35)
    print("        --- MENU QUIZ ---        ")
    print("=" * 35)
    print("1 - Jogar Quiz de Geografia")
    print("2 - Jogar Quiz de História do Python")
    print("3 - Jogar Quiz de Biologia")
    print("4 - Jogar Quiz de Matemática")
    print("5 - Jogar Quiz Geral (Misto)")
    print("6 - Ver Ranking")
    print("7 - Sair")
    print("=" * 35)
    
    opcao = input("Escolha uma opção: ").strip()
    
    if opcao == "1":
        resultado = jogar_quiz(perguntas_geografia, "Geografia")
        ranking.append(resultado)
        
    elif opcao == "2":
        resultado = jogar_quiz(perguntas_python, "História do Python")
        ranking.append(resultado)
        
    elif opcao == "3":
        resultado = jogar_quiz(perguntas_biologia, "Biologia")
        ranking.append(resultado)
        
    elif opcao == "4":
        resultado = jogar_quiz(perguntas_matematica, "Matemática")
        ranking.append(resultado)
        
    elif opcao == "5":

        perguntas_gerais = (
            perguntas_geografia + 
            perguntas_python + 
            perguntas_biologia + 
            perguntas_matematica
        )
        resultado = jogar_quiz(perguntas_gerais, "Conhecimentos Gerais")
        ranking.append(resultado)
        
    elif opcao == "6":
        print("\n" + "=" * 45)
        print("              --- RANKING ---              ")
        print("=" * 45)
        if len(ranking) == 0:
            print("Nenhum jogador registrado ainda.")
        else:
       
            ranking_ordenado = sorted(ranking, key=lambda x: x[1], reverse=True)
            for pos, jogador in enumerate(ranking_ordenado, start=1):
                print(f"{pos}º | {jogador[0]} - {jogador[1]} pts ({jogador[2]})")
        print("=" * 45)
        
    elif opcao == "7":
        print("\nEncerrando o sistema de Quiz... Até logo!")
        break
        
    else:
        print("\n Opção inválida! Escolha um número de 1 a 7.")
