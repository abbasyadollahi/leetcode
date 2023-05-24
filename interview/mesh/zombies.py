"""
Zombies have attacked!

In this 'hypothetical' question, zombies have attacked and we've been tasked with constructing a system for tracking the spread of the zombiism (spelling?) through the population.

Our system will receive information about an attack (something like their name) and the victim. Assume that a zombie's bite is 100% transmissible.

We want our system to be able to receive the attack information (either singly, or in batches, your choice) and record it and be ready to report out information.

For now let's focus on these two questions.
1. Given a zombie, give me a list of the victims that they infected.
2. Given a zombie, tell me who first attacked them to turn them into a zombie.
3. Who is the first zombie?
4. Given a number, give me all the zombies that can be cured up to that generation.
"""

# (zombie, victim)
attackers = [
    (0, 1),
    (0, 2),
    (1, 3),
    (3, 4),
    (4, 5)
]


def victims(attackers: list[tuple[int, int]]) -> dict[int, set[int]]:
    zombie_victims = {}
    for zombie, victim in attackers:
        if zombie in zombie_victims:
            zombie_victims[zombie].add(victim)
        else:
            zombie_victims[zombie] = {victim}

    return zombie_victims


def who_attacked_me(name: int) -> int | None:
    for zombie, victim in attackers:
        if victim == name:
            return zombie
    return None


def zombie_zero(attackers: list[tuple[int, int]]) -> int:
    all_zombies = set()
    all_victims = set()
    for zombie, victim in attackers:
        all_zombies.add(zombie)
        all_zombies.add(victim)
        all_victims.add(victim)

    return (all_zombies - all_victims).pop()


def cure_generations(attackers: list[tuple[int, int]], generations: int) -> set[int]:
    zombie_victims = victims(attackers)
    generation_zero = zombie_zero(attackers)

    generation = 0
    cured_zombies = {generation_zero}
    current_generation_zombies = [generation_zero]
    while generation < generations:
        next_generation_zombies = []
        for zombie in current_generation_zombies:
            if zombie in zombie_victims:
                cured_zombies.update(zombie_victims[zombie])
                next_generation_zombies.extend(zombie_victims[zombie])
        current_generation_zombies = next_generation_zombies
        generation += 1

    return cured_zombies

print(cure_generations(attackers, 2))
print(cure_generations(attackers, 3))
