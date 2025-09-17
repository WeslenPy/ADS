from matplotlib import pyplot as plt


class Livro:
    
    titulo:str
    autor:str
    genero:str
    qtd_disponivel:int
    
    
    def __init__(self,
                 titulo:str,
                 autor:str,
                 genero:str,
                 qtd_disponivel:int):
        
        
        self.titulo=titulo
        self.autor=autor
        self.autor=autor
        self.genero=genero
        self.qtd_disponivel=int(qtd_disponivel)
        
    def titulo_match(self,titulo:str)->bool:
        return True if titulo.lower() in self.titulo.lower() else False
    
    
    def saida_formatada(self):
        return  f"Livro: {self.titulo}\n Autor: {self.autor}\n Genero: {self.genero}\n Quantidade disponivel: {self.qtd_disponivel}\n"
        
    def __repr__(self)->str:
        return self.saida_formatada()
    
    def __str__(self)->str:
        return  self.saida_formatada()
    
    
    
class Biblioteca:
    
    def __init__(self):
        self.lista_de_livros:list[Livro] = [
            
        ]
        
        
    def listar_livros(self,livros:list[Livro]):
        nova_lista_de_livros = [livro.saida_formatada() for livro in list(livros)]
        print("\n".join(nova_lista_de_livros))
        
    
    def cadastrar_livro(self,livro:Livro):
        self.lista_de_livros.append(livro)
        
        
    def cadastrar_multiplos_livros(self,livros:Livro):
        self.lista_de_livros.extend(livros)
        
    
    def buscar_livro_pelo_titulo(self,titulo:str):
        livros_encontrados = filter(lambda livro: livro.titulo_match(titulo),self.lista_de_livros)
        
        self.listar_livros(livros_encontrados)
    
        
    def listar_todos_os_livros(self):
        self.listar_livros(self.lista_de_livros)
    
    
    
    def plot_dados(self):
        
        contagem_por_genero ={}
        for livro in self.lista_de_livros:
            if livro.genero not in contagem_por_genero:
                contagem_por_genero[livro.genero]= livro.qtd_disponivel
            else:
                contagem_por_genero[livro.genero] += livro.qtd_disponivel
                
                
        generos = list(contagem_por_genero.keys())
        quantidades = list(contagem_por_genero.values())
        
        plt.bar(generos, quantidades)
        plt.title("Quantidade de livros por gênero")
        plt.xlabel("Gênero")
        plt.ylabel("Quantidade de livros")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        
        
livros_data = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "genero": "Romance", "qtd_disponivel": 3},
    {"titulo": "O Senhor dos Anéis", "autor": "J. R. R. Tolkien", "genero": "Fantasia", "qtd_disponivel": 5},
    {"titulo": "1984", "autor": "George Orwell", "genero": "Ficção Científica", "qtd_disponivel": 4},
    {"titulo": "A Revolução dos Bichos", "autor": "George Orwell", "genero": "Sátira", "qtd_disponivel": 2},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "genero": "Infantil", "qtd_disponivel": 6}
]


biblioteca = Biblioteca()
for livro in livros_data:
    biblioteca.cadastrar_livro(Livro(**livro))
    
    
biblioteca.buscar_livro_pelo_titulo("o")

biblioteca.plot_dados()