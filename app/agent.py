from app.llm import ask_llm
from app.summarizer import summarize_search_results
from app.pdf_qa import answer_pdf_question

from app.planner import decide_action
from app.tools import execute_tool


def clean_answer(answer: str):

    if not answer:
        return ""

    return (
        answer.replace("<br>", "\n")
              .replace("<br/>", "\n")
              .replace("<br />", "\n")
              .replace("|", "\n")
              .strip()
    )


def process_question(question):

    try:

        # Step 1: Ask the planner
        plan = decide_action(question)

        action = plan["action"]
        arguments = plan["arguments"]

        print(f"\n🤖 Action: {action}")

        # Step 2: Execute tool if needed
        tool_result = execute_tool(action, arguments)

        # SEARCH
        if action == "SEARCH":

            answer = summarize_search_results(
                question,
                tool_result
            )

            return {
                "answer": clean_answer(answer),
                "tool": "Web Search"
            }

        # READ PDF
        elif action == "READ_PDF":

            result = answer_pdf_question(question)

            if result["found"]:

                return {
                    "answer": clean_answer(result["answer"]),
                    "tool": "Knowledge Base"
                }

            return {
                "answer": "No relevant information was found in the Knowledge Base.",
                "tool": "Knowledge Base"
            }

        # CALCULATOR
        elif action == "CALCULATE":

            return {
                "answer": str(tool_result),
                "tool": "Calculator"
            }

        # ANSWER
        elif action == "ANSWER":

            result = answer_pdf_question(question)

            if result["found"]:

                return {
                    "answer": clean_answer(result["answer"]),
                    "tool": "Knowledge Base"
                }

            print("🌐 Falling back to LLM...")

            answer = ask_llm(question)

            return {
                "answer": clean_answer(answer),
                "tool": "LLM"
            }

        # Default
        answer = ask_llm(question)

        return {
            "answer": clean_answer(answer),
            "tool": "LLM"
        }

    except Exception as e:

        return {
            "answer": f"Agent Error: {e}",
            "tool": "System"
        }