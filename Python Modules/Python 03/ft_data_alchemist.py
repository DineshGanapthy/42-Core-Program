
import random

def ft_data_alchemist() -> None:
    print("=== Game Data Alchemist ===\n")

    """ Part 1 : Creating lists using List Comprehensions """
    player_names = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory", "john", "kevin", "Liam"]
    player_names_capitilized = [player_name.title() for player_name in player_names]
    capitilized_names_only = [player_name for player_name in player_names if player_name.istitle()]
    print("Initial list of players: ", player_names)
    print("New list with all names capitalized: ", player_names_capitilized)
    print("New list of capitalized names only: ", capitilized_names_only)
    print()

    """ Part 2 : Creating Dicts using Dict Comprehensions """
    score_dict = {names: random.randrange(1, 1000) for names in player_names_capitilized}
    average = (sum(score_dict.values())) / len(score_dict)
    high_scores = {k: v for k, v in score_dict.items() if v > average}
    print("Score dict: ", score_dict)
    print(f"Score average is {average:.2f}")
    print("High scores: ", high_scores)


if __name__ == "__main__":
    ft_data_alchemist()