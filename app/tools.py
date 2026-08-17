from app.search import search_web
from app.calculator import calculate
from app.pdf_reader import read_pdf


TOOLS = {
    "SEARCH": search_web,
    "CALCULATE": calculate
}


def execute_tool(action, arguments):

    tool = TOOLS.get(action)

    if tool is None:
        return None

    if action == "SEARCH":
        return tool(arguments["query"])

    elif action == "CALCULATE":
        return tool(arguments["expression"])

    

    return None