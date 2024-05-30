# https://www.youtube.com/watch?v=CS_Th38ADug
# JOGO COM PYTHON  Brincando com funções, listas e dicionários
import random

# Criando jogador:
nome_jogador= input ('Digite o Nick do seu Char:')
jogador= {
    'nome_jogador': nome_jogador,
    'level': 2,
    'dano': 35, 
    'hp_maximo': 120,
    'hp': 120,
    'exp': 0,
    'exp_max': 100,
    }
print ('Jogador Criado! Bem vindo(a)', {jogador['nome_jogador']})
print (f"Nome: {jogador['nome_jogador']} // Level: {jogador['level']} // HP: {jogador['hp']} // Experiência: {jogador['exp']}")

print('-----------------------------------------------------------------------------------------------------------')
lista_npcs= []
level= 1    
# posso atribuir um nome para cada level com if depois
def criar_npc (level):
    # level_npc = (random.randint(1,15))  
    novo_npc= {
        'nome': f"Monstro #{level}", 
        'level': level, 
        'dano': level * 20, 
        'hp': level * 100,
        'hp_max': level * 100,
        'exp': 15 * level
    }
    return novo_npc


def criar_varios_npc (n_npcs):
    for x in range (n_npcs): 
        npc= criar_npc(level)
        lista_npcs.append(npc)

# Eu dito o número de npcs que eu quero criar

def exibir_npc(npc):
    print(
        f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // HP: {npc['hp']} // EXP: {npc['exp']}"
    )


def exibir_npcs():
    for npc in lista_npcs:
        exibir_npc(npc)


def exibir_jogador():
    print (
        f"Nome: {jogador['nome_jogador']} // Level: {jogador['level']} // HP: {jogador['hp']} // Experiência: {jogador['exp']}"
        )
    

criar_npc(level)
criar_varios_npc(10)
exibir_npcs()
    



    
def atacar_npc(npc):
    npc['hp'] -= jogador['dano']
    atacar_jogador()


def atacar_jogador(npc):
    jogador['hp'] -= npc['dano']
    
def exibir_batalha (npc):
    print (f"Jogador: {jogador['hp']} / {jogador['hp_max']}")
    print (f"Monstro: {npc['nome']}: {npc['hp']} / {npc['hp_max']}")








# Criar batalha (npc, jogador)
npc_selecionado= lista_npcs[0]
print( "Target", npc_selecionado)
print("Target", npc_selecionado)

def iniciar_batalha (npc):
    print('Challenge Accepted : ')
    while {jogador["hp"]} or {npc_selecionado["hp"]} != 0:
        atacar_npc(npc)
        atacar_jogador(npc)
        exibir_batalha(npc)
    
    print ('Batalha Finalizada!')
    
    if {jogador["hp"]} > 0:
        {jogador["exp"]} += {npc['exp']}
        print ('Você adquiriu:', {jogador['exp'] "/" {jogador['exp_max']}})
    else:
        print ('Você morreu.')
    
    


criar_batalha(npc)

# if exp == exp_max:
#     # level up, quando exp for igual a exp maxima; hp volta a 100%;
#     level+=1
#     hp+= hp_max