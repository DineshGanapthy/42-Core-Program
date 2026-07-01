import random


def gen_player_achievements(name: set) -> set:
    achievements = [
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Unstoppable',
        'First Steps',
        'Collector Supreme',
        'Untouchable',
        'Sharp Mind',
        'Boss Slayer'
    ]

    k = random.randint(1, len(achievements))
    name = set(random.sample(achievements, k))
    return (name)

    # 1. Set a random k between 1 and the length of your list
    # k = random.randint(1, len(my_list))


def ft_achievements_tracker() -> None:
    print("=== Achievement Tracker System ===\n")
    alice = set()
    alice = gen_player_achievements(alice)
    bob = set()
    bob = gen_player_achievements(bob)
    charles = set()
    charles = gen_player_achievements(charles)
    dylan = set()
    dylan = gen_player_achievements(dylan)

    achievements = {
        'Crafting Genius',
        'Strategist',
        'World Savior',
        'Speed Runner',
        'Survivor',
        'Master Explorer',
        'Treasure Hunter',
        'Unstoppable',
        'First Steps',
        'Collector Supreme',
        'Untouchable',
        'Sharp Mind',
        'Boss Slayer'
    }

    """ Getting each players Achievements """
    print(f"Player Alice: {alice}\n")
    print(f"Player Bob: {bob}\n")
    print(f"Player Charles: {charles}\n")
    print(f"Player Dylan: {dylan}\n")
    print(f"All distinct achivements {achievements}\n")

    """ Common Achievements """
    print(f"Common achievements: {alice.intersection(bob, charles, dylan)}\n")

    """ Unique Achievements """
    print(f"Only Alice has: {alice.difference(bob, charles, dylan)}")
    print(f"Only Bob has: {bob.difference(alice, charles, dylan)}")
    print(f"Only Charles has: {charles.difference(bob, alice, dylan)}")
    print(f"Only Dylan has: {dylan.difference(bob, charles, alice)}\n")

    """ What Achievement each player is missing """
    print(f"Alice is missing: {achievements.difference(alice)}")
    print(f"Bob is missing: {achievements.difference(bob)}")
    print(f"Charles is missing: {achievements.difference(charles)}")
    print(f"Dylan is missing: {achievements.difference(dylan)}\n")


if __name__ == "__main__":
    ft_achievements_tracker()
