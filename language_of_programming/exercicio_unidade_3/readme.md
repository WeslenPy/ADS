# ATIVIDADE PROPOSTA:

Você trabalha em uma empresa de varejo e precisa analisar os dados de vendas do último ano
para identificar padrões e insights para melhorar o desempenho. Os dados estão armazenados
em um banco de dados SQLite, e você utilizará a biblioteca Pandas para manipular e analisar
esses dados, além de gerar visualizações utilizando Matplotlib e Seaborn.

## Passo 1: Conectar ao banco de dados SQLite e criar uma tabela
• Primeiro, você precisa estabelecer uma conexão com o banco de dados SQLite e carregar
os dados relevantes para análise.

```python
import sqlite3
```

## Passo 1.1: Conectar ao banco de dados (ou criar, se não existir)

```python
conexao = sqlite3.connect('dados_vendas.db')
```

## Passo 1.2: Criar um cursor

```python
cursor = conexao.cursor()
```

## Passo 1.3: Criar uma tabela (se não existir)

```python
cursor.execute('''
CREATE TABLE vendas1 (
id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
data_venda DATE,
produto TEXT,
categoria TEXT,
valor_venda REAL
)
''')
```

## Passo 1.4: Inserir alguns dados

```python
cursor.execute('''
INSERT INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
('2023-01-01', 'Produto A', 'Eletrônicos', 1500.00),
('2023-01-05', 'Produto B', 'Roupas', 350.00),
('2023-02-10', 'Produto C', 'Eletrônicos', 1200.00),
('2023-03-15', 'Produto D', 'Livros', 200.00),
('2023-03-20', 'Produto E', 'Eletrônicos', 800.00),
('2023-04-02', 'Produto F', 'Roupas', 400.00),
('2023-05-05', 'Produto G', 'Livros', 150.00),
('2023-06-10', 'Produto H', 'Eletrônicos', 1000.00),
('2023-07-20', 'Produto I', 'Roupas', 600.00),
('2023-08-25', 'Produto J', 'Eletrônicos', 700.00),
('2023-09-30', 'Produto K', 'Livros', 300.00),
('2023-10-05', 'Produto L', 'Roupas', 450.00),
('2023-11-15', 'Produto M', 'Eletrônicos', 900.00),
('2023-12-20', 'Produto N', 'Livros', 250.00);
''') 
```

# Passo 1.5: Confirmar as mudanças
```python
conexao.commit()
```

## Passo 2: Explorar e preparar os dados
* Agora que os dados estão carregados em um DataFrame do Pandas (df_vendas), você
pode explorá-los e prepará-los para análise.

## Passo 3: Análise dos dados
* Realize análises específicas para extrair insights sobre as vendas.

## Passo 4: Visualização dos dados
* Utilize Matplotlib e Seaborn para criar visualizações que ajudem na interpretação dos
resultados.

## Passo 5: Conclusão e análise de insights
* Finalize o exercício com uma breve análise dos insights obtidos e sugestões para a empresa com base nos dados analisados.


## Tipos de graficos

1. Evolução temporal (linha ou área)

    * data_venda no eixo X e valor_venda no Y.

    * Mostra como as vendas variaram ao longo do ano.

2. Distribuição por categoria (pizza ou barras)

    * Soma de valor_venda por categoria.

    * Dá pra ver qual categoria gera mais receita (ex: Eletrônicos vs Roupas vs Livros).

3. Ranking de produtos (barras horizontais)

    * Top produtos que mais venderam em valor (SUM(valor_venda) GROUP BY produto).

4. Ticket médio mensal (linha)

    * Média de valor_venda por mês.

    * Indica se os clientes estão comprando produtos mais caros ou baratos ao longo do tempo.

5. Proporção de vendas por mês (heatmap ou barras empilhadas)

    * Comparar categorias em cada mês.

    * Ex: janeiro teve mais eletrônicos, março mais livros.