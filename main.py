from random import randint 

lista_npcs = []

def criar_npc():
    level = randint(0, 50)

    novo_npc = {
        
        'nome': f'monstro #{level}',
        'level': level,
        'dano': 5 * level,
        'Hp': 100 * level,
    }

    lista_npcs.append(novo_npc)

def exibir_npcs():
    for npc in lista_npcs:
        print(f"Nome: {npc['nome']} // Level: {npc['level']} // Dano: {npc['dano']} // Hp: {npc['Hp']}")


def gerar_npcs(n_npcs):
    for x in range(n_npcs):
        criar_npc()





gerar_npcs(5)


