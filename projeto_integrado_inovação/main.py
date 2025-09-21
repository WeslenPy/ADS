from time import sleep
import os,sys
import re
from typing import Union
import bcrypt


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
        super().__init__(nome_completo=nome_completo,idade=idade)
        
        self.login = login.strip().replace(" ","_").lower()
        
        #https://github.com/pyca/bcrypt/
        self.senha =  bcrypt.hashpw(password=str.encode(senha), salt=bcrypt.gensalt())

    def check_pwd(self,senha_entrada):
        
        if bcrypt.checkpw(password=str.encode(senha_entrada), 
                          hashed_password=self.senha):
            
            return True
        
        return False
        
class Medico(Atendente):
    tipo_acesso:str = "medico"
    
        
class Admin(Atendente):
    tipo_acesso:str = "admin"
        
        
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
        
        
        self.logged = None
        
        
        self.pacientes:list[Paciente] = [
            
        ]
        
        
        self.atendentes_e_medicos:list[Union[Atendente,Medico]] = [
            Atendente(nome_completo="Weslen",idade=45,login="weslenpy",senha="weslen123")
        ]
        
        
        
    def login(self,login:str,senha:str) -> Atendente | Medico | None:
        
        for user in self.atendentes_e_medicos:
            if user.login==login:
                if user.check_pwd(senha_entrada=senha):
                    self.logged= user
                    return user
                
        self.logged = None
        return None
        
        
        
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
        
        self.logged: Atendente | Medico | None = None
        
        
        
        self.comum_menu = {
            "5": {"title":"Sair","function":self.sair}
        }
                
        self.map_menu_atendente = {
            "1": {"title":"Cadastrar pacientes","function":self.clinica.pre_cadastro_do_paciente} ,
            "2": {"title":"Ver estatísticas","function":self.clinica.ver_estatisticas} ,
            "3": {"title":"Buscar paciente","function":self.clinica.pre_buscar_paciente} ,
            "4": {"title":"Listar todos os pacientes","function":self.clinica.listar_todos_os_pacientes} ,
            **self.comum_menu
        }
        
        self.map_menu_medico = {
            
        }
        
        self.menu_montado_atendente  = self.utils.montar_menu(self.map_menu_atendente)
        self.menu_montado_medico  = self.utils.montar_menu(self.map_menu_medico)
        
        
        self.control_access = {
            Atendente.tipo_acesso: [self.map_menu_atendente,self.menu_montado_atendente],
            Medico.tipo_acesso: [self.map_menu_medico,self.menu_montado_medico],
        }
        
        
  
    def call_op(self,op:str,mapped_menu:dict[str,dict]):
        if(str(op) in mapped_menu):
            menu_function = mapped_menu.get(op,{})
            return menu_function.get("function",self.sair)()
        
        return None
    
    
    def login(self):
        
        self.utils.limpar_terminal()
        print("---- Sistema Login Clinica ---")
        
        
        tentativas = 0
        max_tentativas = 5
        
        while True:
            
            if tentativas>=max_tentativas:
                print('Você excedeu a quantidade de tentativas.')
                self.sair()
            
            login = input("Digite seu login: ")
            senha = input("Digite sua senha: ")
            
            logged = self.clinica.login(login=login,senha=senha)
            if not logged:
                tentativas +=1
                print(f"\nLogin ou senha inválidos, preencha com seu login e senha corretos, você possui {max_tentativas-tentativas} tentativas.\n")
                continue
            
            self.logged: Atendente | Medico = logged
            return logged
            
            
    def show(self):
        
        current_menu_mapeado,current_menu_montado,*_ = self.control_access[self.logged.tipo_acesso]
        
        while True:
            self.utils.limpar_terminal()
            
            print(f"---- Menu Sistema Clinica ({self.logged.tipo_acesso.title()}: {self.logged.login}) ----")
            print(current_menu_montado)
            
            op_escolhida = input("\nEscolha uma opção: ").strip()
            if not self.utils.validar_entrada(op_escolhida):
                print("Escolha uma opção valida.")
                sleep(1)
                continue
                
            
            self.call_op(op=op_escolhida,mapped_menu=current_menu_mapeado)             
            self.utils.next_step()   
    
    
    def sair(self):
        print("Fechando sistema...")
        sleep(2)
        sys.exit(1)
        
        
        
menu = Menu()
menu.login()
menu.show()
    