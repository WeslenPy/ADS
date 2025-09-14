


# variavel principal para armazenar os dados de entrada
alunos_e_notas:dict[str,list] = {
    
}

#variavel para controle do loop
running = True


# Função responsavel por validar a entrada e verificar se esta em branco ou se é igual a y
def valida_pergunta(value:str):
    return True if  len(value.strip())==0 or value.lower().strip()[0] == "y" else False


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
    return sum(lista_de_notas)/len(lista_de_notas)


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
            nova_nota = input(f"\nDigite a nota que será adicionada para o aluno {nome_aluno}: ").strip()
            
            
            #armazena o resultado da funcao valida_entrada_de_notas
            nota_verificada =  valida_entrada_de_notas(nova_nota)
            
            
            # verifica se o resultado da funcao é None, ou seja, se deu erro na validação.
            if nota_verificada is None:
                print("Nota inserida é inválida, preencha apenas com digitos")
                continue
     
            
            # adiciona a nova nota ao aluno respectivo
            alunos_e_notas[nome_aluno].append(nota_verificada)
            print("\nNota adicionada com sucesso!")
            
            
            #Verifica se o usuario gostaria de adicionar uma nova nota
            quest_more_notas = input(f"\nDeseja adicionar mais notas ao aluno {nome_aluno} ?[Y/n]")
            if not valida_pergunta(quest_more_notas):
                print("Finalizando adição de notas ...")
                break
            
        #Verifica se o usuario gostaria de adicionar um novo aluno
        quest_more = input(f"\nDeseja adicionar mais alunos ?[Y/n] ")
        if not valida_pergunta(quest_more):
            print("Finalizando adição de alunos...")
            running = False
            break
        
    except KeyboardInterrupt:
        running = False
        break
    

for aluno,notas in alunos_e_notas.items():
    
    # calcula a media do aluno com base na lista de notas
    
    if len(notas)>0:
        media = calcular_media(notas)
    
        #mostra os dados no output
        print(f"\no aluno(a) {aluno} teve média: {media} e foi : {'REPROVADO' if media<7 else 'APROVADO'}")
        
    else:
        print(f"Não foram adicionadas notas suficiente para o aluno(a) {aluno}: REPROVADO ")