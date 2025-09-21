from itertools import product

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

agendamento = False         #A
documentos = True           #B
medico_disponivel = True    #C
pagamentos_atrasados =False #D


# print(consulta_normal(agendamento,documentos,medico_disponivel,pagamentos_atrasados))
# print(emergencia(documentos,medico_disponivel,pagamentos_atrasados))



consulta_count = 0
emergencia_count = 0

'''product(
    [True,False], # aqui eu passo as variações ou seja, cada variavel pode ser True ou False
    repeat=4 # aqui eu passo a quantidade de variaveis 
)# essa função me retorna um produto cartesiano contendo todas as variacões, o que gera 16 (2**4) combinações
'''
for a, b, c, d in product([True, False], repeat=4):
    cn = consulta_normal(a, b, c, d)
    em = emergencia(b, c, d)
    
    if cn:consulta_count +=1
    if em: emergencia_count+=1

    conv = lambda x: "V" if x else "F"
    print(f"| {conv(a)} | {conv(b)} | {conv(c)} | {conv(d)} | {conv(cn)} | {conv(em)} |")
    
    
# Analisar situações em que há atendimento  
print("Situações em que há atendimento:")
print("Consulta Normal:", consulta_count, "de 16")
print("Emergência:", emergencia_count, "de 16")