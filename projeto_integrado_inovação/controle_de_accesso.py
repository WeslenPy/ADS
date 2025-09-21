from itertools import product

agendamento = False         #A
documentos = True           #B
medico_disponivel = True    #C
pagamentos_atrasados =False #D

#AND (∧), OR (∨) e NOT (¬)
#Consulta Normal: (A ∧ B ∧ C) ∨ (B ∧ C ∧ D)
def consulta_normal(a,b,c,d):
    return  (a and b and c) or (b and c and d)
    

#Emergência: C ∧ (B ∨ D)
def emergencia(b,c,d):
    return c and (b or d)
    
    
"""
5. Situação prática: Se um paciente chega com as seguintes condições, ele será atendido?
Sem agendamento (A = F)
Documentos OK (B = V)
Médico disponível (C = V)
Pagamentos atrasados (D = F)

Em caso de Emergência: sim 
Em caso de consulta normal: não

"""




# print(consulta_normal(agendamento,documentos,medico_disponivel,pagamentos_atrasados))
# print(emergencia(documentos,medico_disponivel,pagamentos_atrasados))



consulta_count = 0
emergencia_count = 0

'''product(
    [True,False], # aqui eu passo as variações ou seja, cada variavel pode ser True ou False
    repeat=4 # aqui eu passo a quantidade de variaveis 
)# essa função me retorna um produto cartesiano contendo todas as variacões, o que gera 16 (2**4) combinações
'''



# logica para criar um produto cartesiano booleano
def produto_cartesiano(conjunto_inicial):
    
    #criar uma lista com outra lista dentro
    resultado = [[]]
    #iterar sobre o conjunto_inicial
    for elementos in conjunto_inicial:
        #a cada iteração uma nova lista é criada com base na lista de elementos e na lista de resultados anterior
        resultado = [a+[b] for a in resultado for b in elementos]
        '''
        "b" recebe a iteração de "elementos", 
        onde na mesma situação "a" recebe uma iteração de "resultados",
        onde "a" é uma lista de booleanos, por fim tem uma concatenação de "a+[b]",
        onde "b" é transformada em uma lista para ser concatenado corretamente com a lista "a"
        '''
        
    return resultado

conjunto_inicial = [[False, True]] * 4  

print(produto_cartesiano(conjunto_inicial))


print("| A | B | C | D | CN | Emergência |")
for a, b, c, d in product([True, False], repeat=4):
    cn = consulta_normal(a, b, c, d)
    em = emergencia(b, c, d)
    
    if cn:consulta_count +=1
    if em: emergencia_count+=1

    conv = lambda x: "V" if x else "F"
    print(f"| {conv(a)} | {conv(b)} | {conv(c)} | {conv(d)} | {conv(cn)} | {conv(em)} |")
    
    
# Analisar situações em que há atendimento  
print("\nSituações em que há atendimento:")
print("Consulta Normal:", consulta_count, "de 16")
print("Emergência:", emergencia_count, "de 16")