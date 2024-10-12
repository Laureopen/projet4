import random
from models.player import Player
from models.tournament import Tournament
from models.match import Match
from models.round import Round

"""Liste des joueurs"""
players_list = [
    Player("Dupont", "Jean", "1990-05-12", "AB 02468"),
    Player("Martin", "Claire", "1985-11-23", "CD 13579"),
    Player("Durand", "Lucas", "2000-01-15", "EF 03377"),
    Player("Leroy", "Sophie", "1992-07-30", "GH 15792"),
    Player("Moreau", "Thomas", "1995-09-05", "IJ 23456"),
    Player("Simon", "Marie", "1988-03-20", "KL 98765"),
    Player("Michel", "Julien", "1996-12-01", "MN 01035"),
    Player("Cruise", "Emma", "1983-04-14", "OP 84159"),
]

"""Affichage du premier joueur pour vérifier"""
print(players_list[0])

"""Création d'un tournoi et ajout d'un joueurs au tournoi"""
tournament =[
    Tournament("Championship 2024", "Paris", "2024-05-01", "2024-05-07"),
    Tournament("Spring Open 2024", "Lyon", "2024-03-15", "2024-03-20"),
    Tournament("Winter Chess Classic", "Nice", "2024-12-01", "2024-12-07"),
    Tournament("Grandmaster Blitz Cup", "Marseille", "2024-08-10", "2024-08-12"),
]
"""Ajout  des joueurs à chaque tournoi"""
for tournament in tournament:
    for player in players_list:
        tournament.players.append([player,0,[]])

"""Création d'un tour et ajout de joueurs et du match"""
round = Round(1,"2024-05-01","2024-05-01")
round = Round( 2, "2024-11-25", "2024-11-26")
round = Round(3, "2024-12-07", "2024-12-07")
round = Round(4, "2025-01-10", "2025-01-13")

# Ajout du round au tournoi
tournament.rounds.append(round)

# Fonction pour générer un match avec des scores aléatoires
def create_match(player1, player2):
    score1 = random.randint(0, 3)  # Score pour le joueur 1 (0-3)
    score2 = random.randint(0, 3)  # Score pour le joueur 2 (0-3)
    return Match(player1, score1, player2, score2)

# Fonction pour éviter les doublons de matchs
def generate_round(players):
    random.shuffle(players)  # Mélanger les joueurs
matches = []

# Affichage des résultats des matchs
for i in range(0, len(players_list), 2):  # On s'assure que chaque joueur est apparié
    if i + 1 < len(players_list):
        match = create_match(players_list[i], players_list[i + 1])
        matches.append(match)

# Affichage des résultats des matchs
for i, match in enumerate(matches, start=1):
    print(f"Match {i}: {match}")

print("Le joueur " + tournament.players[0][0].last_name + " à " + str(tournament.players[0][1]) + " point")


"""Liste des scores de matchs (exemple: score1, score2)"""
match_scores = [(1, 0), (0.5, 0.5), (0, 1)]

# Mélanger la liste des scores
random.shuffle(match_scores)

# Sélectionner un score aléatoire après le mélange
selected_score = match_scores[0]

# Afficher le score sélectionné pour vérification
print(f"Score sélectionné : {selected_score}")

# Convertir chaque valeur du score en flottant
score1 = float(selected_score[0])
score2 = float(selected_score[1])

"""Création d'un match"""
match1 = Match(players_list[0],3,players_list[1],2)
print("résultat du match:", match1)

# Fonction pour éviter les doublons de matchs
def generate_round(players):
    random.shuffle(players)  # Mélanger les joueurs
    matches = []
    for i in range(0, len(players), 2):  # On s'assure que chaque joueur est apparié
        if i + 1 < len(players):
            match = create_match(players[i], players[i + 1])
            matches.append(match)
    return matches

# Fonction pour afficher les résultats d'un round
def display_round_results(round_number, matches):
    print(f"\n--- Championship 2024 - Round {round_number} ---")
    for match in matches:
        print(match)

# Fonction pour mettre à jour les scores des joueurs
def update_scores(matches):
    for match in matches:
        print(f"Match: {match.player1.first_name} vs {match.player2.first_name}")
        print(f"Score: {match.score1} - {match.score2}")
        if hasattr(match.player1, 'points') and hasattr(match.player2, 'points'):
            match.player1.points += match.score1
            match.player2.points += match.score2
        else:
            print("Erreur : Les joueurs n'ont pas d'attribut 'points'")

# Fonction pour afficher les résultats finaux du tournoi
def display_final_results(players):
    print("\n--- Résultats finaux du tournoi: Championship 2024 ---")
    for player in players:
        print(f"{player.first_name} {player.last_name} - Points: {player.points}")

# Exécution des rounds
for round_num in range(1, 5):  # 4 rounds
    print(f"\n--- Matchs Round {round_num} ---")
    matches = generate_round(players_list)
    display_round_results(round_num, matches)
    update_scores(matches)

display_final_results(players_list)