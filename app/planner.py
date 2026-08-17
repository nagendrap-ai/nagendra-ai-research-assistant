import json
import re
#from app.llm import ask_llm
from langchain_core.messages import HumanMessage
from app.langchain_llm import invoke_llm

def decide_action(question):

    prompt = f"""
You are an AI Agent Planner.

Your ONLY responsibility is to decide which action should be executed.

You are NOT allowed to answer the user's question.

You must return exactly ONE valid JSON object.

Do NOT include:
- Explanations
- Markdown
- Code fences
- Comments
- Greetings
- Any extra text

Your response must start with '{{' and end with '}}'.

Supported actions:

ANSWER
SEARCH
CALCULATE
READ_PDF

Decision Rules:

- If the answer can be confidently answered from general knowledge, choose ANSWER.
- If the answer depends on current, changing, location-specific, or internet information, choose SEARCH.
- If mathematical evaluation is required, choose CALCULATE.
- If the user asks about a PDF, choose READ_PDF.
- If unsure between ANSWER and SEARCH, prefer SEARCH.

1. ANSWER
   - General knowledge questions.
   - Explanations.
   - Conversations.

2. SEARCH
   - Latest news.
   - Current information.
   - Stock prices.
   - Weather.
   - Gold price.
   - Live information.

3. CALCULATE
   - Mathematical calculations.

4. READ_PDF
   - Read a PDF.
   - Summarize a PDF.
   - Answer questions from a PDF.

Return JSON in this format:

{{
    "action": "...",
    "arguments": {{}}
}}

Examples:
Question:
What is RAG?

Response:
{{
    "action": "ANSWER",
    "arguments": {{}}
}}

Question:
What is Python?

Response:
{{
    "action": "ANSWER",
    "arguments": {{}}
}}

Question:
125 * 378

Response:
{{
    "action": "CALCULATE",
    "arguments": {{
        "expression": "125 * 378"
    }}
}}

Question:
Today's gold rate in Hyderabad

Response:
{{
    "action": "SEARCH",
    "arguments": {{
        "query": "Today's gold rate in Hyderabad"
    }}
}}

Question:
Summarize sample.pdf

Response:
{{
    "action": "READ_PDF",
    "arguments": {{
        "file": "sample.pdf"
    }}
}}

User Question:

"{question}"
JSON Response:
"""

    #response = ask_llm(prompt)

    #return json.loads(response)

    #response = ask_llm(prompt)
    response = invoke_llm([
        HumanMessage(content=prompt)
    ])
    

    try:
    # First, try parsing the response directly.
        return json.loads(response)

    except json.JSONDecodeError:

    # If that fails, try extracting the first JSON object.
        match = re.search(r"\{.*\}", response, re.DOTALL)

    if match:
        try:
            return json.loads(match.group())
        except json.JSONDecodeError:
            pass

    print("\n⚠ Planner returned invalid JSON.")
    print(response)

    return {
        "action": "ANSWER",
        "arguments": {}
    }