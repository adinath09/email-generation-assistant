from groq import Groq
from config import GROQ_API_KEY

client = Groq(api_key=GROQ_API_KEY)


# Metric 1: Fact Coverage
def fact_coverage(output, facts):
    score = 0
    for fact in facts:
        if fact.lower() in output.lower():
            score += 1
    return score / len(facts)


# Generic LLM Judge
def llm_judge(prompt):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    return response.choices[0].message.content.strip()


# Metric 2: Tone Alignment
def tone_score(email, tone):
    prompt = f"""
Rate how well this email matches the tone '{tone}' from 1 to 5.
Only return a number.

Email:
{email}
"""
    try:
        return float(llm_judge(prompt)) / 5
    except:
        return 0


# Metric 3: Structure & Quality
def quality_score(email):
    prompt = f"""
Rate this email from 1 to 5 based on:
- structure
- grammar
- clarity

Only return a number.

Email:
{email}
"""
    try:
        return float(llm_judge(prompt)) / 5
    except:
        return 0