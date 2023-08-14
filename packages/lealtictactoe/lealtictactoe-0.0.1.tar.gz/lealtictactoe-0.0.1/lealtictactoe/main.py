import random

class LealTicTacToe():
    def __init__(self):
        pass

    def bestgame(jogador_locais: list, robo_locais: list):
        todos_locais = ['A1', 'A2', 'A3',
                        'B1', 'B2', 'B3', 'C1', 'C2', 'C3']

        ocupados_locais = jogador_locais + robo_locais

        locais_livres = []
        for local in todos_locais:
            if local not in ocupados_locais:
                locais_livres.append(local)

        palpite = None
        # HORIZONTAL
        # A3
        if 'A1' in jogador_locais and 'A2' in jogador_locais and 'A3' in locais_livres:
            palpite = 'A3'
        # A2
        elif 'A1' in jogador_locais and 'A3' in jogador_locais and 'A2' in locais_livres:
            palpite = 'A2'
        # A1
        elif 'A2' in jogador_locais and 'A3' in jogador_locais and 'A1' in locais_livres:
            palpite = 'A1'
        # B3
        elif 'B1' in jogador_locais and 'B2' in jogador_locais and 'B3' in locais_livres:
            palpite = 'B3'
        # B2
        elif 'B1' in jogador_locais and 'B3' in jogador_locais and 'B2' in locais_livres:
            palpite = 'B2'
        # B1
        elif 'B2' in jogador_locais and 'B3' in jogador_locais and 'B1' in locais_livres:
            palpite = 'B1'
        # C3
        elif 'C1' in jogador_locais and 'C2' in jogador_locais and 'C3' in locais_livres:
            palpite = 'C3'
        # C2
        elif 'C1' in jogador_locais and 'C3' in jogador_locais and 'C2' in locais_livres:
            palpite = 'C2'
        # C1
        elif 'C2' in jogador_locais and 'C3' in jogador_locais and 'C1' in locais_livres:
            palpite = 'C1'

        # VERTICAL
        # A1
        elif 'B1' in jogador_locais and 'C1' in jogador_locais and 'A1' in locais_livres:
            palpite = 'A1'
        # A2
        elif 'B2' in jogador_locais and 'C2' in jogador_locais and 'A2' in locais_livres:
            palpite = 'A2'
        # A3
        elif 'B3' in jogador_locais and 'C3' in jogador_locais and 'A3' in locais_livres:
            palpite = 'A3'
        # B1
        elif 'A1' in jogador_locais and 'C1' in jogador_locais and 'B1' in locais_livres:
            palpite = 'B1'
        # B2
        elif 'A2' in jogador_locais and 'C2' in jogador_locais and 'B2' in locais_livres:
            palpite = 'B2'
        # B3
        elif 'A3' in jogador_locais and 'C3' in jogador_locais and 'B3' in locais_livres:
            palpite = 'B3'
        # C1
        elif 'A1' in jogador_locais and 'B1' in jogador_locais and 'C1' in locais_livres:
            palpite = 'C1'
        # C2
        elif 'A2' in jogador_locais and 'B2' in jogador_locais and 'C2' in locais_livres:
            palpite = 'C2'
        # C3
        elif 'A3' in jogador_locais and 'B3' in jogador_locais and 'C3' in locais_livres:
            palpite = 'C3'

        # DIAGONAL
        # A1
        elif 'B2' in jogador_locais and 'C3' in jogador_locais and 'A1' in locais_livres:
            palpite = 'A1'
        # A3
        elif 'C1' in jogador_locais and 'B2' in jogador_locais and 'A3' in locais_livres:
            palpite = 'A3'
        # B2
        elif ('A1' in jogador_locais and 'C3' in jogador_locais) or ('A3' in jogador_locais and 'C1' in jogador_locais):
            if 'B2' in locais_livres:
                palpite = 'B2'
        # C1
        elif 'A3' in jogador_locais and 'B2' in jogador_locais and 'C1' in locais_livres:
            palpite = 'C1'
        # C3
        elif 'A1' in jogador_locais and 'B2' in jogador_locais and 'C3' in locais_livres:
            palpite = 'C3'
        else:
            try:
                palpite = random.choice(locais_livres)
            except Exception as error:
                pass
        return palpite
