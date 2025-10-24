# A list of fun facts about sea creatures, unlocked at different streak milestones.
ANIMAL_FACTS = [
    (1, "Seahorse", "Seahorses are among the only species where the male carries and gives birth to the young."),
    (5, "Clownfish (Nemo)", "Clownfish live in symbiosis with sea anemones, whose stinging tentacles protect them from predators."),
    (10, "Starfish", "Starfish can regenerate lost arms, and a single arm can grow into a whole new starfish."),
    (25, "Octopus", "Octopuses have three hearts, blue blood, and can squeeze through any opening larger than their beak."),
    (50, "Dolphin", "Dolphins sleep with one eye open, allowing one half of their brain to rest while the other remains alert."),
    (100, "Orca (Killer Whale)", "Orcas, also known as 'wolves of the sea,' are highly intelligent predators that hunt in organized pods using complex strategies.")
]

def get_animal_streak(streak_length):
    """Finds the highest achievement unlocked for a given streak length."""
    achieved_animal_info = None
    for required_distance, name, fact in ANIMAL_FACTS:
        if streak_length >= required_distance:
            achieved_animal_info = (required_distance, name, fact)
        else:
            break
    return achieved_animal_info