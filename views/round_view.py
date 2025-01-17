class RoundView:
    """Vue pour l'affichage des informations liées aux rounds du tournoi."""

    def __init__(self):
        pass

    @staticmethod
    def display_round_match(idx, tournament, player1, player2):
        """Affiche les détails d'un match particulier (joueurs, score, etc.)."""
        print(f"{idx}. {player1.last_name} ({tournament.player_scores[player1.player_id]}) vs {player2.last_name} ({tournament.player_scores[player2.player_id]})")

    @staticmethod
    def prompt_for_continue():
        """Demander à l'utilisateur s'il souhaite continuer."""
        choice = input("\nSouhaitez-vous continuer ? (O/N): ").lower()
        return choice != "n"
