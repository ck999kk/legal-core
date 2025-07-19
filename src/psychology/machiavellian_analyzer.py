"""
Analyze documents or textual input for signs of manipulation, hidden intent,
strategic obfuscation, or power-seeking language.

Applies Machiavellian heuristics to legal texts, emails, and arguments.
"""

def score_machiavellian_traits(text: str) -> dict:
    score = {
        "deception": 0,
        "emotional_control": 0,
        "strategic vagueness": 0,
        "dominance_cue": 0
    }

    if "unforeseen circumstance" in text.lower():
        score["strategic vagueness"] += 1
    if "as per our agreement" in text.lower():
        score["dominance_cue"] += 1
    if "regrettably" in text.lower():
        score["emotional_control"] += 1
    if any(x in text.lower() for x in ["confidential", "subjective", "understanding"]):
        score["deception"] += 1

    total = sum(score.values())
    score["machiavellian_index"] = round(total / 4, 2)
    return score
