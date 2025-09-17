import sqlite3
import pandas as pd
from matplotlib import pyplot as plt


class Database:
    
    DB_NAME:str = 'dados_vendas.db'

    def __init__(self):
        self.db = sqlite3.connect(self.DB_NAME)
        self.cursor = self.db.cursor()
        
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
        
        self.db.commit()
        
    def adicionar_dados_iniciais(self):
        
        self.cursor.execute('''
            INSERT IGNORE INTO vendas1 (data_venda, produto, categoria, valor_venda) VALUES
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
        
        self.db.commit()
        




db = Database()
db.criar_tabelas()
db.adicionar_dados_iniciais()