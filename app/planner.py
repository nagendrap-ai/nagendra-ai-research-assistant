import json
import re

from langchain_core.messages import HumanMessage

from app.langchain_llm import invoke_llm


def decide_action(question, conversation_history=None):

    if conversation_history is None:
        conversation_history = []

    # --------------------------------------------------
    # Build conversation context
    # --------------------------------------------------

    conversation_text = ""

    for message in conversation_history:

        if hasattr(message, "type"):

            if message.type == "human":
                role = "User"

            elif message.type == "ai":
                role = "Assistant"

            else:
                role = "Message"

            conversation_text += (
                f"{role}: {message.content}\n"
            )

    # --------------------------------------------------
    # Planner Prompt
    # --------------------------------------------------

    prompt = f"""
You are an AI Agent Planner.

Your ONLY responsibility is to decide which action
should be executed.

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

- If the answer can be confidently answered from
  general knowledge or the conversation history,
  choose ANSWER.

- If the answer depends on current, changing,
  location-specific, or internet information,
  choose SEARCH.

- If mathematical evaluation is required,
  choose CALCULATE.

- If the user asks about a PDF or uploaded document,
  choose READ_PDF.

- If the user asks a follow-up question about
  something already discussed in the conversation,
  use the conversation history to understand it.

- If unsure between ANSWER and SEARCH,
  prefer SEARCH.


1. ANSWER

Use ANSWER for:

- General knowledge questions.
- Explanations.
- Conversations.
- Greetings.
- Personal information already provided by the user
  in the conversation.
- Follow-up questions that can be answered using
  previous conversation context.


2. SEARCH

Use SEARCH for:

- Latest news.
- Current information.
- Stock prices.
- Weather.
- Gold price.
- Live information.
- Current internet information.


3. CALCULATE

Use CALCULATE for:

- Mathematical calculations.


4. READ_PDF

Use READ_PDF for:

- Reading a PDF.
- Summarizing a PDF.
- Answering questions from a PDF.


--------------------------------------------------
CONVERSATION HISTORY
--------------------------------------------------

{conversation_text}


--------------------------------------------------
CURRENT USER QUESTION
--------------------------------------------------

"{question}"


--------------------------------------------------
RETURN JSON
--------------------------------------------------

Return JSON in this exact format:

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


JSON Response:
"""

    # --------------------------------------------------
    # Call LLM
    # --------------------------------------------------

    response = invoke_llm([
        HumanMessage(content=prompt)
    ])

    # --------------------------------------------------
    # Parse JSON
    # --------------------------------------------------

    try:

        return json.loads(response)

    except json.JSONDecodeError:

        match = re.search(
            r"\{.*\}",
            response,
            re.DOTALL
        )

        if match:

            try:

                return json.loads(
                    match.group()
                )

            except json.JSONDecodeError:
                pass

    print("\n⚠ Planner returned invalid JSON.")
    print(response)

    return {
        "action": "ANSWER",
        "arguments": {}
    }
