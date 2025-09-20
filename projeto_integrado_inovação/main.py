from logging import info
import os,sys

class Utils:
    
    def validar_cpf(self):
        pass
    
    
    def validar_telefone(self):
        pass
    
    def validar_nome(self):
        pass
    
    
    def validar_entrada(self,value:str)->bool:
        
        try:
            int(value)
            return True
        
        except Exception as erro:
            return False
    
    
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
        self.pacientes:list[Paciente] = [
            
        ]

    
    def cadastrar_paciente(self):
        pass


    def ver_estatisticas(self):
        pass
    
    def buscar_paciente(self):
        pass
    
    def listar_todos_os_pacientes(self):
        pass
    



class Menu:
    def __init__(self):
        
        self.clinica = Clinica()
        self.utils = Utils()
        
        
        self.map_menus = {
            "1": {"title":"Cadastrar pacientes","function":self.clinica.cadastrar_paciente} ,
            "2": {"title":"Ver estatísticas","function":self.clinica.ver_estatisticas} ,
            "3": {"title":"Buscar paciente","function":self.clinica.buscar_paciente} ,
            "4": {"title":"Listar todos os pacientes","function":self.clinica.listar_todos_os_pacientes} ,
            "5": {"title":"Sair","function":self.sair} ,
        }
        
        
        self.menu_montado  = self.montar_menu()
        
    def montar_menu(self):
        return "\n".join(map(lambda items:f"{items[0]}. {items[1]['title']}",list(self.map_menus.items())))
    
    
    def call_op(self,op:str):
        if(str(op) in self.map_menus):
            menu_function =  self.map_menus.get(op,{})
            return menu_function.get("function",self.sair)()
        
        return None
            
            
    def show(self):
        
        while True:
            print(self.menu_montado)
            op_escolhida = input("\nEscolha uma opção: ").strip()
            if not self.utils.validar_entrada(op_escolhida):
                print("Escolha uma opção valida.")
                
            
            self.call_op(op_escolhida)                
    
    
    def sair(self):
        sys.exit(1)
        
        
        
menu = Menu()
menu.show()
    