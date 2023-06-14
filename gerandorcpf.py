# Importamos a biblioteca random que serve para gerar números.
# Depois  colocamos try/except para pegar erros .

import random

def gera():
      
        try:
            q_gerados=int(input('Digite quanto cpf você que : ')) # pegar através do imput quantas cpf o usuario deseja. 
            for _ in range (q_gerados): # cria um laço de repetição utilizando o valor do usuario.
                nove_digitos=''
                for i in range(9): # cria atraves do range 9 lugares
                    nove_digitos+= str(random.randint(0,9)) # Onde é gerado 9 digitos ALEATÓRIO que ficaram nos 9 lugares. 
                print(nove_digitos)#E para gera esses numeros aleatório indo de 0 a 9 utilizamos (random.randint)
               
        except:
                print('DIGITE APENAS NÚMEROS!!!')
        
        gera()    
gera()
