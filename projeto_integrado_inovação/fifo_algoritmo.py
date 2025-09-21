# logica de algoritmo FIFO simples

fila_vazia = []

# Inserir 3 pacientes
for i in range(0,4):
    nome = input("Digite o nome do paciente:")
    cpf = input("Digite o CPF do paciente:")
    
    fila_vazia.append((nome,cpf))
    
    

# Atender o primeiro paciente
paciente = fila_vazia.pop(0)
print("Paciente atendido: ",paciente)


# Mostrar pacientes restantes
print("Pacientes restantes na fila:")
for paciente in fila_vazia:
    print(paciente)