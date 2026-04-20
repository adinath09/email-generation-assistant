import pandas as pd
import time
from scenarios import scenarios
from prompt import build_prompt
from generator import generate_email
from metrics import fact_coverage, tone_score, quality_score
from config import MODEL_A, MODEL_B


def evaluate(model):
    results = []

    for s in scenarios:
        prompt = build_prompt(s["intent"], s["facts"], s["tone"])

        output = generate_email(prompt, model)

        time.sleep(1.5)

        fcs = fact_coverage(output, s["facts"])
        tas = tone_score(output, s["tone"])
        qs = quality_score(output)

        final = (fcs + tas + qs) / 3

        results.append({
            "Scenario": s["id"],
            "Model": model,
            "FCS": round(fcs, 2),
            "TAS": round(tas, 2),
            "QS": round(qs, 2),
            "Final": round(final, 2)
        })

    return results


def run():
    all_results = []

    for model in [MODEL_A, MODEL_B]:
        all_results.extend(evaluate(model))

    df = pd.DataFrame(all_results)
    df.to_csv("outputs/results.csv", index=False)

    print("Evaluation complete → outputs/results.csv")