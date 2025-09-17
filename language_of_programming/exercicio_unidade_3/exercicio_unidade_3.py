import sqlite3
import pandas as pd
from matplotlib import pyplot as plt


# classe que implementa e abstrai a logica de acesso e cadastro de dados 
class Database:
    
    
    #nome do banco de dados
    DB_NAME:str = 'dados_vendas.db'

    def __init__(self):
        #cria uma instancia de conexão ao banco
        self.conn = sqlite3.connect(self.DB_NAME)

        #cria uma instancia do cursor para execução de comandos sql
        self.cursor = self.conn.cursor()
        
        
        #chama a função que cria as tabelas 
        self.criar_tabelas()
        
    def criar_tabelas(self):
        
        #executa o sql que cria a tabela caso ela não exista
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas1 (
            id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            data_venda DATE,
            produto TEXT,
            categoria TEXT,
            valor_venda REAL
            )
        ''')
        
        #efetua o commit que salva as alterações efetuadas no sql anterior
        self.conn.commit()
        
    # função que adiciona os dados principais para manipulação e geração de insights
    def adicionar_dados_iniciais(self):
        
        #adiciona os dados com um INSERT
        self.cursor.execute('''
            INSERT OR IGNORE INTO  vendas1 (data_venda, produto, categoria, valor_venda) VALUES
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
        
        #efetua o commit que salva as alterações efetuadas no sql anterior
        self.conn.commit()
        
#classe que abstrai e implementa a logica de geração e analise de graficos para insights
class Dados:
    
    def __init__(self,db:Database):
        # carrega todos os dados em um DataFrame
        self.df = pd.read_sql(sql="SELECT * FROM vendas1",con=db.conn)
    
    
    # mostra o cabeçalho dos dados contidos no DataFrame
    def head(self):
        print(self.df.head())
    
    
    #função que gera um grafico em linha para analise de evolução temporal
    def evolucao_temporal(self):
        plt.figure(figsize=(10,5))

        #define os dados que serão plotados no grafico,
        # de barras sendo eles a data_venda e valor_venda respectivamente
        plt.plot(self.df['data_venda'], self.df['valor_venda'], marker='o')  
        
        # define a label do eixo X
        plt.xlabel("Data")
        # define a label do eixo Y
        plt.ylabel("Valor de Vendas")
        # define o titulo ou proposito do grafico
        plt.title("Evolução Temporal das Vendas")

    #função que gera um grafico em barra para analise de distribuição de vendas por categaria
    def distribuicao_por_categoria(self):
                
        # efetua o groupby da categoria e soma o valor de vendas por categoria
        soma = self.df.groupby("categoria")["valor_venda"].sum().reset_index()
        #define os dados que serão plotados no grafico de barras
        plt.bar(soma["categoria"], soma["valor_venda"])
        # define a label do eixo X
        plt.xlabel("Categoria")
        # define o titulo ou proposito do grafico
        plt.ylabel("Soma das Vendas")
        # define o titulo ou proposito do grafico
        plt.title("Vendas por Categoria")

    #função que gera um grafico em barra para analise de produtos mais vendidos
    def ranking_de_produtos(self):
        
        # efetua o groupby do produto e soma o valor de vendas por produto
        ranking = self.df.groupby("produto")["valor_venda"].sum().reset_index()
        
        #define os dados que serão plotados no grafico de barras
        plt.bar(ranking["produto"], ranking["valor_venda"])
        # define a label do eixo X
        plt.xlabel("Produto")
        # define o titulo ou proposito do grafico
        plt.ylabel("Soma das Vendas")
        # define o titulo ou proposito do grafico
        plt.title("Vendas por Produto")
        
    #função que gera um grafico em barra para analise do ticket medio mensal dos produtos
    def ticket_medio_mensal(self):
        
        # converte as datas contidas em data_venda para datetime, garantindo que todas estão no mesmo formato
        self.df["data_venda"] = pd.to_datetime(self.df["data_venda"])


        # efetua o groupby da data_venda com periodo mensal e efetuando a media do mês
        ticket_mes = (
            self.df.groupby(self.df["data_venda"].dt.to_period("M"))["valor_venda"].mean().reset_index()
        )

        #converte novamente a data_venda para string
        ticket_mes["data_venda"] = ticket_mes["data_venda"].astype(str)

        #define os dados que serão plotados no grafico de barras
        plt.bar(ticket_mes["data_venda"], ticket_mes["valor_venda"])
        # define a label do eixo X
        plt.xlabel("Mês")
        # define o titulo ou proposito do grafico
        plt.ylabel("Ticket médio")
        # define o titulo ou proposito do grafico
        plt.title("Ticket médio mensal")
        
        
        
    def show(self):
        #rotaciona todos os textos no eixo X para melhor adequação ao grafico
        plt.xticks(rotation=45)
        #mostra o grafico
        plt.show()
        


#instancia a classe Database
db = Database()
#adicionar os dados iniciais ao banco de dados
db.adicionar_dados_iniciais()

#instancia a classe Dados
dados = Dados(db=db)
# mostra o cabeçalho dos dados
dados.head()

# gera um grafico com o ticket medio mensal 
dados.ticket_medio_mensal()
