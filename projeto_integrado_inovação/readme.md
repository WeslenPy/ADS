# Situação Problema: Desenvolvimento de uma Plataforma de Saúde


## Contexto:

* A cidade de São Lucas tem crescido rapidamente, e com ela, também cresceu a demanda por serviços de saúde
de qualidade. A Clínica Vida+, especializada em atendimentos médicos e exames laboratoriais, está
enfrentando dificuldades para organizar suas rotinas: agendamentos são feitos manualmente, os médicos não
conseguem acompanhar os históricos dos pacientes de forma eficiente e, frequentemente, há erros nas
cobranças e nos relatórios.

Preocupada com esses problemas, a diretora da clínica, Sra. Helena, decide contratar você para criar
um sistema de gestão da clínica.
O sistema deverá permitir:
* Cadastro de pacientes, médicos e exames;
* Agendamento de consultas e exames, com controle de horários disponíveis;
* Registro de atendimentos, com histórico de evolução por paciente;
* Geração de relatórios mensais para a administração;

Com base na história da Clínica Vida+, você deverá aplicar os conhecimentos adquiridos nas diferentes
disciplinas para propor soluções que atendam às necessidades do cenário apresentado. A partir da situação-problema, serão desenvolvidas atividades específicas que envolvem análise, planejamento, modelagem e implementação de soluções voltadas à área de tecnologia da informação.

# 📌 Projeto Integrado – Clínica Vida+

## ✅ Entregas do Projeto

### 🔹 Passo 1 – Organização no Trello
- Criar um **quadro Scrum no Trello** com as listas:  
  - Backlog  
  - Sprint Atual  
  - Em Progresso  
  - Concluído  
- Definir objetivos e duração das sprints.  
- Mover tarefas entre as listas conforme evolução.  
- **Entrega:** Prints do quadro + relatório final de cada sprint.  
- **Observação:** Não envolve programação, é gestão do projeto.  

---

### 🔹 Passo 2 – Sistema em Python
- Desenvolver programa em **Python** que permita:  
  - Cadastrar pacientes (nome, idade, telefone).  
  - Exibir estatísticas:  
    - Número total de pacientes.  
    - Idade média.  
    - Paciente mais novo e mais velho.  
  - Buscar paciente pelo nome.  
  - Listar todos os pacientes cadastrados.  
  - Menu interativo em loop até a saída.  
- **Entrega:** Código Python funcional.  

---

### 🔹 Passo 3 – Controle de Acesso (Lógica Booleana)
- Criar expressões lógicas para **Consulta Normal** e **Emergência**.  
- Construir as **tabelas verdade** (16 linhas cada).  
- Analisar em quantas situações o paciente é atendido.  
- Testar situação prática dada no enunciado.  
- **Entrega:**  
  - Expressões lógicas escritas.  
  - Tabelas verdade (em texto ou planilha).  
  - *(Opcional: Código Python para gerar automaticamente as tabelas)*.  

---

### 🔹 Passo 4 – Algoritmo de Fila
- Desenvolver em **pseudocódigo** um algoritmo que:  
  - Insira 3 pacientes na fila (nome + CPF).  
  - Remova o primeiro paciente (atendimento).  
  - Mostre quem ainda está na fila.  
- **Entrega:** Pseudocódigo (ou implementação em Python se desejar).  

---

### 🔹 Passo 5 – Diagrama de Casos de Uso
- Criar **diagrama UML de Casos de Uso** para o sistema de gestão de consultas:  
  - **Atores:** Secretária, Médico, Paciente.  
  - **Funcionalidades:** cadastrar paciente, agendar consulta, confirmar consulta, cancelar consulta, gerar receita, imprimir receita.  
- **Entrega:** Imagem do diagrama UML.  
- **Observação:** Não é programação, é modelagem de sistema.  

---

## 🚀 Resumo Final
👉 Deve ser **programado**:  
- Passo 2 (Python)  
- Passo 3 (opcional em Python)  
- Passo 4 (pseudocódigo/Python)  

👉 Deve ser **documentado/modelado**:  
- Passo 1 (Trello)  
- Passo 3 (expressões/tabelas verdade)  
- Passo 5 (diagrama de casos de uso)  


### 🖥️ Exemplo de Execução
```text
=== SISTEMA CLÍNICA VIDA+ ===
1. Cadastrar paciente
2. Ver estatísticas
3. Buscar paciente
4. Listar todos os pacientes
5. Sair
Escolha uma opção: 1
Nome do paciente: João Silva
Idade: 45
Telefone: (11) 99999-9999
Paciente cadastrado com sucesso!
```

# ✅ Checklist do Projeto Integrado – Clínica Vida+

## Passo 1 – Organização no Trello
- [ ] Criar quadro Scrum no Trello  
- [ ] Configurar listas (Backlog, Sprint Atual, Em Progresso, Concluído)  
- [ ] Definir objetivos e duração das sprints  
- [ ] Mover tarefas conforme evolução  
- [ ] Tirar prints do quadro  
- [ ] Elaborar relatório final de cada sprint  

---

## Passo 2 – Sistema em Python
- [x] Implementar cadastro de pacientes (nome, idade, telefone)  
- [ ] Armazenar dados em listas e dicionários  
- [x] Exibir estatísticas:  
  - [x] Número total de pacientes  
  - [x] Idade média  
  - [x] Paciente mais novo e mais velho  
- [x] Implementar busca por nome  
- [x] Listar todos os pacientes cadastrados  
- [x] Criar menu interativo em loop  
- [x] Tratar erros de entrada  

---

## Passo 3 – Controle de Acesso (Lógica Booleana)
- [x] Escrever expressão lógica para **Consulta Normal**  
- [x] Escrever expressão lógica para **Emergência**  
- [x] Construir tabela verdade (16 linhas) para **Consulta Normal**  
- [x] Construir tabela verdade (16 linhas) para **Emergência**  
- [x] Analisar situações em que há atendimento  
- [x] Testar situação prática fornecida  
- [x] *(Opcional: Implementar em Python para automatizar)*  

---

## Passo 4 – Algoritmo de Fila
- [x] Criar pseudocódigo para inserir 3 pacientes  
- [x] Implementar remoção do primeiro paciente (atendimento)  
- [x] Mostrar pacientes restantes na fila  
- [x] *(Opcional: Implementar em Python)*  

---

## Passo 5 – Diagrama de Casos de Uso
- [x] Identificar atores (Secretária, Médico, Paciente)  
- [x] Definir funcionalidades (cadastrar, agendar, confirmar, cancelar, gerar receita, imprimir receita)  
- [x] Criar diagrama UML de Casos de Uso  
- [x] Inserir imagem do diagrama no README  

---

## 🚀 Entrega Final
- [x] Subir código Python para o repositório  
- [ ] Incluir prints do Trello no README  
- [x] Incluir tabelas verdade no README ou anexo  
- [x] Incluir pseudocódigo no README  
- [ ] Incluir diagrama UML no README  
- [ ] Revisar README antes da entrega  

## Logica Booleana para Consulta Normal e Emergência

* Expressão booleana
```text
Operadores: AND (∧), OR (∨) e NOT (¬)

Consulta Normal: (A ∧ B ∧ C) ∨ (B ∧ C ∧ D)
Emergência: C ∧ (B ∨ D)
```

* Em python 

```python
def consulta_normal(a,b,c,d):
   return  (a and b and c) or (b and c and d)

def emergencia(b,c,d):
   return c and (b or d)
```



## Tabela verdade 

```python

'''product(
    [True,False], # aqui eu passo as variações ou seja, cada variavel pode ser True ou False
    repeat=4 # aqui eu passo a quantidade de variaveis 
)# essa função me retorna um produto cartesiano contendo todas as variacões, o que gera 16(2**4) combinações
'''

print("| A | B | C | D | CN | Emergência |")
for a, b, c, d in product([True, False], repeat=4):
    cn = consulta_normal(a, b, c, d)
    em = emergencia(b, c, d)
    
    if cn:consulta_count +=1
    if em: emergencia_count+=1

    conv = lambda x: "V" if x else "F"
    print(f"| {conv(a)} | {conv(b)} | {conv(c)} | {conv(d)} | {conv(cn)} | {conv(em)} |")
    
#SAIDA:

| A | B | C | D | CN | Emergência |
| V | V | V | V | V |      V      |
| V | V | V | F | V |      V      |
| V | V | F | V | F |      F      |
| V | V | F | F | F |      F      |
| V | F | V | V | F |      V      |
| V | F | V | F | F |      F      |
| V | F | F | V | F |      F      |
| V | F | F | F | F |      F      |
| F | V | V | V | V |      V      |
| F | V | V | F | F |      V      |
| F | V | F | V | F |      F      |
| F | V | F | F | F |      F      |
| F | F | V | V | F |      V      |
| F | F | V | F | F |      F      |
| F | F | F | V | F |      F      |
| F | F | F | F | F |      F      |
```


## Analise de atendimentos

```python
Situações em que há atendimento:
Consulta Normal: 3 de 16
Emergência: 6 de 16
```


## Algoritmo FIFO (First-In, First-Out)


* Pseudocódigo 
```text
// logica de algoritmo FIFO simples
INÍCIO
    CRIAR fila_vazia

    // Inserir 3 pacientes
    PARA i = 1 ATÉ 3 FAÇA
        ESCREVA "Digite o nome do paciente:"
        LER nome
        ESCREVA "Digite o CPF do paciente:"
        LER cpf
        ADICIONE (nome, cpf) NA fila_vazia
    FIM_PARA

    // Atender o primeiro paciente
    REMOVA paciente_atendido DE fila_vazia
    ESCREVA "Paciente atendido:", paciente_atendido

    // Mostrar pacientes restantes
    ESCREVA "Pacientes restantes na fila:"
    PARA CADA paciente EM fila_vazia FAÇA
        ESCREVA paciente
    FIM_PARA
FIM

```

* FIFO com python
```python 
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

```


## Diagrma UML com casos de uso

![Diagrama de casos de uso do sistema](./uml.png)