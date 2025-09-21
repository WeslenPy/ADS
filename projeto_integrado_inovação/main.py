import os,sys
import re
from time import sleep

class Utils:
    
    def validar_cpf(self):
        pass
    
    
    def validar_telefone(self,value:str)->bool:
        pattern=   re.compile(r"^\(\d{2}\)\s?\d{4,5}-\d{4}$")# exemplo (11) 99999-8888
        return bool(pattern.match(value))
    
    def validar_nome(self):
        pass
    
    
    def validar_entrada(self,value:str)->bool:
        
        try:
            int(value)
            return True
        
        except Exception as erro:
            return False
    
    def montar_menu(self,map_menu:dict[str,dict]):
        return "\n".join(map(lambda items:f"{items[0]}. {items[1]['title']}",list(map_menu.items())))
    
    
    def limpar_terminal(self)->None:
        if os.name == "nt":#windows
            os.system("cls")
        else:
            os.system("clear")


    def next_step(self)->str:
        return input("\nPressione enter para continuar....")
    
    
    
class ControleDeAcessos:
    pass


class Pessoa:
    nome_completo:str
    idade:str
    
    def __init__(self,nome_completo:str,idade:int):
        self.nome_completo = nome_completo.strip().title()
        self.idade = int(idade)


class Atendente(Pessoa):
    
    tipo_acesso:str = "atendente"
    
    def __init__(self, nome_completo:str,idade:str,
                        login:str,senha:str):
        super().__init__(nome_completo,idade)
        
        self.login = login
        self.senha = senha

class Medico(Pessoa):
    tipo_acesso:str = "medico"
    def __init__(self, nome_completo:str,idade:str,
                        login:str,senha:str):
        super().__init__(nome_completo,idade)

        self.login = login
        self.senha = senha
        
        
class Paciente(Pessoa):
    
    telefone:str
    tipo_acesso:str = "paciente"
    
    def __init__(self,telefone:str,nome_completo:str,idade:int):
        super().__init__(nome_completo,idade)
        
        self.telefone= telefone
        
        
    def nome_match(self,nome:str)->bool:
        return True if nome.lower() in self.nome_completo.strip().lower() else False
    
        
    def saida_formatada(self)->str:
        
        return f"""
            \nNome do paciente: {self.nome_completo}\
            \nIdade: {self.idade}\
            \nTelefone: {self.telefone}\
            """
    
    def __repr__(self)->str:
        return self.saida_formatada()
    
    
    def __str___(self)->str:
        return self.saida_formatada()
     
class Clinica(Utils):
    def __init__(self):
        
        
        self.pacientes:list[Paciente] = [
            
        ]
        
        self.medicos:list[Medico]= [
            
        ]
        
        self.atendentes:list[Atendente] = [
            
        ]
        
        
    def cadastrar_paciente(self,nome:str,idade:str,telefone:str)->None:
        novo_paciente = Paciente(telefone=telefone,
                                       nome_completo=nome,
                                       idade=idade)
        self.pacientes.append(novo_paciente) 
        
        print("\nPaciente cadastrado com sucesso!") 
        return novo_paciente
    
    def pre_cadastro_do_paciente(self)->None:
        
        step = 0
        
        self.limpar_terminal()
        
        print("\n--- Cadastro de paciente ---\n")
        while step <=2:
            
            if step == 0:
                nome = input("Nome do paciente: ").strip()
                if len(nome)<=1:
                    print("Nome incorreto, preencha com um nome valido!")
                    continue
                else:
                    step+=1
                    
            if step ==1:
                idade = input("Idade: ").strip()
                if not self.validar_entrada(idade):
                    print("Idade invalida, preencha com uma idade valida!")
                    continue
                
                else:
                    step+=1
                
                
            if step == 2:
                telefone = input("Telefone: ").strip()
                if not self.validar_telefone(telefone):
                    print("Telefone invalido, preencha com um telefone valido, exemplo esperado: (11) 99999-8888" )
                    
                    continue
                
                else:
                    step+=1
                    
                    
            
            self.cadastrar_paciente(nome,idade,telefone)
            

    def ver_estatisticas(self):
        self.limpar_terminal()
    
        total_pacientes = len(self.pacientes)
        idades_organizadas = sorted(self.pacientes,key=lambda paciente:paciente.idade)
        
        idade_media = sum([paciente.idade for paciente in idades_organizadas])//total_pacientes
        
        paciente_mais_novo =idades_organizadas[0]
        paciente_mais_velho = idades_organizadas[-1]
        
        print("--- Estatísticas ---")
        
        
        print(f"""\
              \nNúmero total de pacientes cadastrados: {total_pacientes}\
              \nIdade média dos pacientes: {idade_media}\
              \nPaciente mais novo: {paciente_mais_novo.nome_completo} | Idade: {paciente_mais_novo.idade}\
              \nPaciente mais velho: {paciente_mais_velho.nome_completo} | Idade: {paciente_mais_velho.idade}\
              """)
                
    
    def buscar_paciente(self,nome:str):
        self.limpar_terminal()
        pacientes_encontrados = list(filter(lambda paciente: paciente.nome_match(nome),self.pacientes))
        self.listar_pacientes(pacientes_encontrados)
        
        return pacientes_encontrados
    
    
    def pre_buscar_paciente(self):
        
        while True:
            paciente = input("\nDigite o nome do paciente que deseja buscar: ")
            if paciente and ( paciente.isdigit() or paciente.isdecimal()):
                print("Preencha o campo de busca com um nome valido!")
                continue
            
            break
            
            
        print("\n--- Pacientes encontrados ---")
        self.buscar_paciente(paciente)


    def listar_pacientes(self,pacientes:list[Paciente]):
        if not pacientes or len(pacientes)<=0:
            print("Nenhum paciente encontrado.")
            return 
        
        for paciente in pacientes:
            print(paciente)
        
    def listar_todos_os_pacientes(self):
        self.limpar_terminal()
        print("--- Listagem de pacientes ---")
        self.listar_pacientes(self.pacientes)
    



class Menu:
    def __init__(self):
        
        self.clinica = Clinica()
        self.utils = Utils()
        
        
        self.map_menu = {
            "1": {"title":"Cadastrar pacientes","function":self.clinica.pre_cadastro_do_paciente} ,
            "2": {"title":"Ver estatísticas","function":self.clinica.ver_estatisticas} ,
            "3": {"title":"Buscar paciente","function":self.clinica.pre_buscar_paciente} ,
            "4": {"title":"Listar todos os pacientes","function":self.clinica.listar_todos_os_pacientes} ,
            "5": {"title":"Sair","function":self.sair} ,
        }
        
        
        self.menu_montado  = self.utils.montar_menu(self.map_menu)
  
    def call_op(self,op:str):
        if(str(op) in self.map_menu):
            menu_function =  self.map_menu.get(op,{})
            return menu_function.get("function",self.sair)()
        
        return None
            
            
    def show(self):
        
        while True:
            self.utils.limpar_terminal()
            print(self.menu_montado)
            op_escolhida = input("\nEscolha uma opção: ").strip()
            if not self.utils.validar_entrada(op_escolhida):
                print("Escolha uma opção valida.")
                sleep(1)
                continue
                
            
            self.call_op(op_escolhida)             
            self.utils.next_step()   
    
    
    def sair(self):
        sys.exit(1)
        
        
        
menu = Menu()
menu.show()
    