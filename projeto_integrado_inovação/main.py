from logging import info
import os,sys

class Utils:
    
    def validar_cpf(self):
        pass
    
    
    def validar_telefone(self):
        pass
    
    def validar_nome(self):
        pass
    
    
    def limpar_terminal(self):
        if os.name == "nt":#windows
            os.system("cls")
        else:
            os.system("clear")

    
class Pessoa:
    nome_completo:str
    idade:str
    
    def __init__(self,nome_completo,idade):
        self.nome_completo = nome_completo
        self.idade = idade



class Atendente(Pessoa):
    def __init__(self, nome_completo,idade):
        super().__init__(nome_completo,idade)

class Paciente(Pessoa):
    
    telefone:str
    
    def __init__(self,telefone,nome_completo,idade):
        super().__init__(nome_completo,idade)
        
        self.telefone= telefone
    
    
class Clinica:
    def __init__(self):
        pass

    
    def cadastrar_paciente(self):
        pass


    def analises_estatisticas(self):
        pass
    
    def buscar_paciente(self):
        pass
    
    def listar_todos_os_pacientes(self):
        pass
    

class Menu:
    def __init__(self):
        pass
    
    
    
    
    
    
    def sair(self):
        sys.exit(1)
    