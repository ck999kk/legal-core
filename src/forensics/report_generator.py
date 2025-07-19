from datetime import datetime
from src.forensics.risk_profiler import build_risk_profile

def generate_forensic_report(document_text: str, source: str = "Unknown") -> str:
    profile = build_risk_profile(document_text)

    template = f'''
    === FORENSIC ANALYSIS REPORT ===

    📄 Source: {source}
    📅 Generated: {datetime.utcnow().isoformat()} UTC

    🧠 Machiavellian Index: {profile["traits"]["machiavellian_index"]}
    🛑 Risk Score: {profile["risk_score"]} / 3
    🚩 Flags:
    {chr(10).join(["- " + f for f in profile["flags"]])}

    🧬 Breakdown:
      Deception: {profile["traits"]["deception"]}
      Strategic Vagueness: {profile["traits"]["strategic vagueness"]}
      Emotional Control: {profile["traits"]["emotional_control"]}
      Dominance Cue: {profile["traits"]["dominance_cue"]}

    Summary: This document contains linguistic traits that may indicate manipulative or strategic behavior. Consider expert review if used in legal arguments.

    '''
    return template.strip()
