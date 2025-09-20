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


# 🏥 PROJETO INTEGRADO – Clínica Vida+

## 📌 Passo 2: Sistema de Cadastro e Estatísticas

### 🎯 Situação
A **Sra. Helena** precisa de um sistema simples para cadastrar pacientes e calcular estatísticas básicas da clínica.

### 🛠️ Problema
Desenvolver um programa em **Python** que:

1. 📋 **Cadastro de pacientes**  
   - Nome  
   - Idade  
   - Telefone  

2. 📊 **Estatísticas**  
   - Número total de pacientes cadastrados  
   - Idade média dos pacientes  
   - Paciente mais novo e mais velho  

3. 🔍 **Busca de paciente** pelo nome  

4. 📑 **Exibição de todos os pacientes** de forma organizada  

---

### ⚙️ Requisitos Técnicos
- Usar **listas** e **dicionários** para armazenar dados  
- Implementar um **menu simples** para navegação  
- Tratar possíveis **erros de entrada**  
- O programa deve funcionar em **loop** até o usuário escolher sair  

---

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


# ✅ Checklist do Projeto

## 🏗️ Estrutura do Sistema
- [x] Criar menu principal
- [x] Implementar cadastro de pacientes
- [ ] Implementar estatísticas básicas
- [x] Implementar busca por nome
- [x] Implementar listagem de pacientes
- [x] Tratar erros de entrada

## 📊 Estatísticas
- [ ] Mostrar número total de pacientes
- [ ] Calcular idade média
- [ ] Identificar paciente mais novo
- [ ] Identificar paciente mais velho

## 🔐 Controle de Acesso
- [ ] Definir variáveis lógicas (A, B, C, D)
- [ ] Implementar regra de Consulta Normal
- [ ] Implementar regra de Emergência
- [ ] Criar tabela verdade no código

## 🧪 Testes
- [ ] Testar cadastro com dados válidos
- [ ] Testar cadastro com dados inválidos
- [ ] Testar busca por paciente existente
- [ ] Testar busca por paciente inexistente
- [ ] Validar regras de acesso em diferentes cenários

## 📦 Entrega
- [ ] Documentar no README
- [ ] Subir código para o GitHub
- [ ] Revisar checklist antes da entrega