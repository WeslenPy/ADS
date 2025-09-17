


# variavel principal para armazenar os dados de entrada
alunos_e_notas:dict[str,list] = {
    
}

#variavel para controle do loop
running = True


# Função responsavel por validar a entrada e verificar se esta em branco ou se é igual a y
def valida_resposta(resposta:str):
    return True if  len(resposta.strip())==0 or resposta.lower().strip()[0] == "y" else False


# Função responsavel por validar a entrada e verificar se é um digito
def valida_entrada_de_notas(nota:str)->float:
    
    try:
        #tenta converter para float, caso não consiga a exceção ValueError é lançada
        return float(nota)
    
    except ValueError:
        return None
    
    except Exception as erro:
        return None
    
# Função responsavel por calcular a media do aluno com base em uma lista de notas
    
def calcular_media(lista_de_notas:list[float]):
    
    
    ''' usa o built-in sum para somar todos os itens contidos 
        dentro de lista_de_notas e depois divide pela quantidade de notas  '''
    return round(sum(lista_de_notas)/len(lista_de_notas),2)


print("---- Sistema de gestão de notas! ----")



# loop principal
while running:
    
    try:
    
    
        #recebe como entrada uma string nome_aluno    
        nome_aluno = input("\nDigite o nome do aluno: ").strip().title()
        
        #verifica se é um nome valido, necessario ser 2 ou mais caracteres
        if len(nome_aluno) <=1 or nome_aluno.isdigit() or nome_aluno.isdecimal():
            print("Nome incorreto, preencha com um nome adequado.")
            continue
        
        # checa se o aluno ja existe
        if not nome_aluno in alunos_e_notas:
            # adiciona o novo aluno na lista de alunos
            alunos_e_notas[nome_aluno]= []
            
            
        # loop para adicionar notas
        while running:
        
        
            #recebe como entrada uma string nova_nota    
            nova_nota = input(f"\nDigite a nota que será adicionada para o aluno {nome_aluno} de 0 a 10: ").strip()
            
            
            #armazena o resultado da funcao valida_entrada_de_notas
            verifica_nota =  valida_entrada_de_notas(nova_nota)
            
            # verifica se o resultado da funcao é None, ou seja, se deu erro na validação.
            if verifica_nota is None:
                print("Nota inserida é inválida, preencha apenas com digitos")
                continue
            
            # verifica se verifica_nota esta dentro do range esperado A.
            if verifica_nota >10 or verifica_nota <0:
                print("Insira uma nota de 0 a 10")
                continue
            
            # adiciona a nova nota ao aluno respectivo
            alunos_e_notas[nome_aluno].append(verifica_nota)
            print("\nNota adicionada com sucesso!")
            
            
            #Verifica se o usuario gostaria de adicionar uma nova nota
            quest_more_notas = input(f"\nDeseja adicionar mais notas ao aluno {nome_aluno} ?[Y/n]")
            if not valida_resposta(quest_more_notas):
                print("Finalizando adição de notas ...")
                break
            
        #Verifica se o usuario gostaria de adicionar um novo aluno
        quest_more = input(f"\nDeseja adicionar mais alunos ?[Y/n] ")
        if not valida_resposta(quest_more):
            print("Finalizando adição de alunos...")
            running = False
            break
        
    except KeyboardInterrupt:
        running = False
        break
    



print("\n*** Relatorio de todos os alunos *** \n")
for aluno,notas in alunos_e_notas.items():
    
    print(f"ALUNO: {aluno}")
    print(f"NOTAS: {notas}")
    
    if len(notas)>0:
        # calcula a media do aluno com base na lista de notas
        media = calcular_media(notas)

        #verifica a situacao do aluno e armazena em situacao_aluno            
        situacao_aluno = 'REPROVADO' if media<7 else 'APROVADO'
        #mostra os dados do relatorio
        print(f"MEDIA: {media}")
        print(f"SITUACAO: {situacao_aluno}\n\n")
        
    else:
        print(f"MEDIA: {0}")
        print(f"SITUACAO: REPROVADO\n\n")
        