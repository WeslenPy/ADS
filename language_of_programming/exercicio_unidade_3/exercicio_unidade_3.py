import sqlite3
import pandas as pd
from matplotlib import pyplot as plt


class Database:
    
    DB_NAME:str = 'dados_vendas.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.DB_NAME)
        self.cursor = self.conn.cursor()
        
        self.criar_tabelas()
        
    def criar_tabelas(self):

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS vendas1 (
            id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
            data_venda DATE,
            produto TEXT,
            categoria TEXT,
            valor_venda REAL
            )
        ''')
        
        self.conn.commit()
        
    def adicionar_dados_iniciais(self):
        
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
        
        self.conn.commit()
        
class Dados:
    
    def __init__(self,db:Database):
        self.df = pd.read_sql(sql="SELECT * FROM vendas1",con=db.conn)
    
    
    def head(self):
        print(self.df.head())
    
    def evolucao_temporal(self):
        plt.figure(figsize=(10,5))
        plt.plot(self.df['data_venda'], self.df['valor_venda'], marker='o')  
        plt.xlabel("Data")
        plt.ylabel("Valor de Vendas")
        plt.title("Evolução Temporal das Vendas")
        plt.xticks(rotation=45)  
        plt.show()


    def distribuicao_por_categoria(self):
                
        soma = self.df.groupby("categoria")["valor_venda"].sum().reset_index()
        plt.bar(soma["categoria"], soma["valor_venda"])
        plt.xlabel("Categoria")
        plt.ylabel("Soma das Vendas")
        plt.title("Vendas por Categoria")
        plt.xticks(rotation=45)
        plt.show()

    def ranking_de_produtos(self):
        
        ranking = self.df.groupby("produto")["valor_venda"].sum().reset_index()
        plt.bar(ranking["produto"], ranking["valor_venda"])
        plt.xlabel("Produto")
        plt.ylabel("Soma das Vendas")
        plt.title("Vendas por Produto")
        plt.xticks(rotation=45)
        plt.show()
        
        
    def ticket_medio_mensal(self):
        self.df["data_venda"] = pd.to_datetime(self.df["data_venda"])

        ticket_mes = (
            self.df.groupby(self.df["data_venda"].dt.to_period("M"))["valor_venda"].mean().reset_index()
        )

        ticket_mes["data_venda"] = ticket_mes["data_venda"].astype(str)

        plt.bar(ticket_mes["data_venda"], ticket_mes["valor_venda"])
        plt.xlabel("Mês")
        plt.ylabel("Ticket médio")
        plt.title("Ticket médio mensal")
        plt.xticks(rotation=45)
        plt.show()

                
db = Database()
db.adicionar_dados_iniciais()

dados = Dados(db=db)
dados.head()
dados.ticket_medio_mensal()
