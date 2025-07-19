from src.psychology.machiavellian_analyzer import score_machiavellian_traits

def build_risk_profile(text: str) -> dict:
    mach = score_machiavellian_traits(text)

    profile = {
        "risk_score": 0,
        "flags": [],
        "traits": mach
    }

    if mach["machiavellian_index"] >= 1:
        profile["risk_score"] += 1
        profile["flags"].append("High Machiavellian traits")
    if mach["deception"] >= 1:
        profile["risk_score"] += 1
        profile["flags"].append("Potential deception")
    if "withhold" in text.lower():
        profile["risk_score"] += 1
        profile["flags"].append("Intent to obscure information")

    return profile
