from matplotlib import pyplot as plt




# classe para abstrair o livro
class Livro:
    
    
    #atributos base da classe
    titulo:str
    autor:str
    genero:str
    qtd_disponivel:int
    
    
    #contrutor da classe
    def __init__(self,
                 titulo:str,
                 autor:str,
                 genero:str,
                 qtd_disponivel:int):
        
        
        self.titulo=titulo
        self.autor=autor
        self.genero=genero
        self.qtd_disponivel=int(qtd_disponivel)
        
        
    # encontrar livro com base no titulo
    def titulo_match(self,titulo:str)->bool:
        return True if titulo.lower() in self.titulo.lower() else False
    
    # formatação de saida
    def saida_formatada(self)->str:
        return  f"Livro: {self.titulo} \
                  \n - Autor:{self.autor} \
                    \n - Genero: {self.genero} \
                    \n - Quantidade disponivel: {self.qtd_disponivel}"
        
        
    #permite que a saida do objeto no output seja formatada
    def __repr__(self)->str:
        return self.saida_formatada()
    
    #permite que a classe ao ser chamada dentro do print a saida seja formatada com a função saida_formatada
    def __str__(self)->str:
        return  self.saida_formatada()
    
    
    
#classe que implementa e abstrai a logica da biblioteca
class Biblioteca:
    
    def __init__(self):
        
        #lista de livros
        self.lista_de_livros:list[Livro] = [
            
        ]
        
        
    #função que abstrai a listagem de livros
    def listar_livros(self,livros:list[Livro]):
        nova_lista_de_livros = [livro.saida_formatada() for livro in list(livros)]
        print("\n".join(nova_lista_de_livros))
        
    #função para mostrar todos os livros disponiveis 
    def listar_todos_os_livros(self):
        # lista todos os livros encontrados
        print("Listando todos os livros cadastrados: ")
        self.listar_livros(self.lista_de_livros)
        
        
    #função para cadastrar novos livros
    def cadastrar_livro(self,livro:Livro):
        print(f"Novo livro adicionado com sucesso: {livro.titulo}")
        self.lista_de_livros.append(livro)
        
        
    #função para cadastrar novos multiplos livros de uma unica vez
    def cadastrar_multiplos_livros(self,livros:list[Livro]):
        self.lista_de_livros.extend(livros)
        
    
    #função para buscar/filtrar livros com base no titulo
    def buscar_livro_pelo_titulo(self,titulo:str):
        #filtra os dados usando o built-in filter e uma função lambda 
        livros_encontrados = filter(lambda livro: livro.titulo_match(titulo),self.lista_de_livros)
        
        # lista os livros encontrados
        print(f"Listando livros encontrados com base na busca: {titulo} ")
        self.listar_livros(livros_encontrados)
    
   
    
    
    #função que gerar o grafico de barrar usando a lib matplotlib
    def plot_dados(self):
        
        #cria um dicionario para armazenar os dados que serão usados no grafico
        contagem_por_genero ={}
        
        #itera sobre a lista de livros atual
        for livro in self.lista_de_livros:
            #verifica se o genero ja existe dentro de contagem_por_genero
            if livro.genero not in contagem_por_genero:
                #caso nao exista ele adiciona a quantidade disponivel sem somar
                contagem_por_genero[livro.genero]= livro.qtd_disponivel
            else:
                #caso exista ele adiciona a quantidade disponivel somando com a anterior
                contagem_por_genero[livro.genero] += livro.qtd_disponivel
                
                
        #gera a lista de generos
        generos = list(contagem_por_genero.keys())
        
        #gera a lista de quantidade por genero
        quantidades = list(contagem_por_genero.values())
        
        #
        plt.bar(generos, quantidades)
        plt.title("Quantidade de livros por gênero")
        plt.xlabel("Gênero")
        plt.ylabel("Quantidade de livros")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
        
        
#lista de livros inicial
livros_data = [
    {"titulo": "Dom Casmurro", "autor": "Machado de Assis", "genero": "Romance", "qtd_disponivel": 3},
    {"titulo": "Memórias Póstumas de Brás Cubas", "autor": "Machado de Assis", "genero": "Romance", "qtd_disponivel": 2},
    {"titulo": "O Senhor dos Anéis", "autor": "J. R. R. Tolkien", "genero": "Fantasia", "qtd_disponivel": 5},
    {"titulo": "Harry Potter e a Pedra Filosofal", "autor": "J. K. Rowling", "genero": "Fantasia", "qtd_disponivel": 7},
    {"titulo": "1984", "autor": "George Orwell", "genero": "Ficção Científica", "qtd_disponivel": 4},
    {"titulo": "Admirável Mundo Novo", "autor": "Aldous Huxley", "genero": "Ficção Científica", "qtd_disponivel": 3},
    {"titulo": "A Revolução dos Bichos", "autor": "George Orwell", "genero": "Sátira", "qtd_disponivel": 2},
    {"titulo": "O Pequeno Príncipe", "autor": "Antoine de Saint-Exupéry", "genero": "Infantil", "qtd_disponivel": 6},
    {"titulo": "Alice no País das Maravilhas", "autor": "Lewis Carroll", "genero": "Infantil", "qtd_disponivel": 5},
    {"titulo": "O Hobbit", "autor": "J. R. R. Tolkien", "genero": "Fantasia", "qtd_disponivel": 4},
    {"titulo": "Senhora", "autor": "José de Alencar", "genero": "Romance", "qtd_disponivel": 3},
    {"titulo": "O Guia do Mochileiro das Galáxias", "autor": "Douglas Adams", "genero": "Ficção Científica", "qtd_disponivel": 6}
]



#instancia a biblioteca
biblioteca = Biblioteca()
for livro in livros_data:
    #cadastra todos os livros da base inicial
    
    biblioteca.cadastrar_livro(Livro(**livro))#aqui foi ultilizado também o packing do python usando **

#biblioteca.listar_todos_os_livros()
    
#busca um titulo
#biblioteca.buscar_livro_pelo_titulo("dos")

#mostra os dados do grafico
biblioteca.plot_dados()