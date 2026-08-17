from langchain_core.messages import HumanMessage

from app.summarizer import summarize_search_results
from app.pdf_qa import answer_pdf_question

from app.planner import decide_action
from app.tools import execute_tool

from app.memory import ConversationMemory
from app.langchain_llm import invoke_llm


# ======================================================
# CONVERSATION MEMORY
# ======================================================

memory = ConversationMemory()


# ======================================================
# CLEAN ANSWER
# ======================================================

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


# ======================================================
# SAVE CONVERSATION
# ======================================================

def save_conversation(question, answer):

    memory.add_user_message(question)
    memory.add_ai_message(answer)


# ======================================================
# ANSWER USING CONVERSATION MEMORY
# ======================================================

def answer_with_memory(question):

    messages = memory.get_messages()

    messages.append(
        HumanMessage(content=question)
    )

    answer = invoke_llm(messages)

    return clean_answer(answer)


# ======================================================
# PROCESS QUESTION
# ======================================================

def process_question(question):

    try:

        # --------------------------------------------------
        # Step 1: Get previous conversation
        # --------------------------------------------------

        conversation_history = memory.get_messages()

        print(
            f"\n🧠 Conversation history: "
            f"{len(conversation_history)} message(s)"
        )


        # --------------------------------------------------
        # Step 2: Ask planner
        # --------------------------------------------------

        plan = decide_action(
            question,
            conversation_history
        )

        action = plan["action"]
        arguments = plan["arguments"]

        print(f"🤖 Action: {action}")


        # --------------------------------------------------
        # Step 3: Execute tool
        # --------------------------------------------------

        tool_result = execute_tool(
            action,
            arguments
        )


        # ==================================================
        # SEARCH
        # ==================================================

        if action == "SEARCH":

            answer = summarize_search_results(
                question,
                tool_result
            )

            answer = clean_answer(answer)

            save_conversation(
                question,
                answer
            )

            return {
                "answer": answer,
                "tool": "Web Search"
            }


        # ==================================================
        # READ PDF
        # ==================================================

        elif action == "READ_PDF":

            result = answer_pdf_question(
                question
            )

            if result["found"]:

                answer = clean_answer(
                    result["answer"]
                )

                save_conversation(
                    question,
                    answer
                )

                return {
                    "answer": answer,
                    "tool": "Knowledge Base"
                }

            answer = (
                "No relevant information was found "
                "in the Knowledge Base."
            )

            save_conversation(
                question,
                answer
            )

            return {
                "answer": answer,
                "tool": "Knowledge Base"
            }


        # ==================================================
        # CALCULATOR
        # ==================================================

        elif action == "CALCULATE":

            answer = str(tool_result)

            save_conversation(
                question,
                answer
            )

            return {
                "answer": answer,
                "tool": "Calculator"
            }


        # ==================================================
        # ANSWER
        # ==================================================

        elif action == "ANSWER":

            answer = answer_with_memory(
                question
            )

            save_conversation(
                question,
                answer
            )

            return {
                "answer": answer,
                "tool": "LLM"
            }


        # ==================================================
        # DEFAULT
        # ==================================================

        answer = answer_with_memory(
            question
        )

        save_conversation(
            question,
            answer
        )

        return {
            "answer": answer,
            "tool": "LLM"
        }


    # ======================================================
    # ERROR HANDLING
    # ======================================================

    except Exception as e:

        print(
            f"❌ Agent Error: {e}"
        )

        return {
            "answer": f"Agent Error: {e}",
            "tool": "System"
        }
