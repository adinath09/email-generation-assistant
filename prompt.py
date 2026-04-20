def build_prompt(intent, facts, tone):
    facts_text = "\n".join([f"- {f}" for f in facts])

    return f"""
You are a senior corporate communication expert with 15+ years of experience.

Write a professional email.

Intent: {intent}

Facts:
{facts_text}

Tone: {tone}

Instructions:
- Include ALL facts
- Match tone strictly
- Keep email concise (100-180 words)
- Use Subject, Greeting, Body, Closing

Examples:

Example 1:
Intent: Request leave
Facts:
- Leave from Oct 5–10
- Family function
Tone: Formal

Output:
Subject: Leave Request
Dear Manager,
I would like to request leave from October 5 to October 10 due to a family function...

---

Example 2:
Intent: Apology
Facts:
- Missed deadline
- System issue
- New deadline April 18
Tone: Empathetic

Output:
Subject: Apology for Delay
Dear Sir/Madam,
I sincerely apologize for missing the deadline due to a system issue...

---

Output Format:
Subject:
Email Body:
"""