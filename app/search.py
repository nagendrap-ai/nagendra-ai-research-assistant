import requests

from app.config import (
    TAVILY_API_KEY,
    TAVILY_URL
)


def search_web(query):

    print("\n🔍 Searching the Web...\n")

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "search_depth": "basic",
        "max_results": 3
    }
    try:

        response = requests.post(
        TAVILY_URL,
        headers=headers,
        json=payload,
        timeout=10
    )

    except requests.exceptions.RequestException as e:

        return f"Search Error: {e}"

    if response.status_code != 200:
        return f"Search Error: {response.status_code}\n{response.text}"

    data = response.json()

    results = []

    for item in data.get("results", []):
        title = item.get("title", "")
        content = item.get("content", "")
        url = item.get("url", "")

        results.append(
            f"Title: {title}\n"
            f"Content: {content}\n"
            f"Source: {url}\n"
        )

    return "\n".join(results)