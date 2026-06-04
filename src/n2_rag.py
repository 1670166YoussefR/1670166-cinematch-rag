import sys
from .config import CHAT_MODEL, openai_client
from .n1_semantic_search import semantic_search

def retrieve_context(question: str) -> list[dict]:
    return semantic_search(question)

def build_prompt(question: str, movies: list[dict]) -> list[str]:
    context = ""

    for movie in movies:
        context += (
            f"Title: {movie['title']}\n"
            f"Year: {movie['year']}\n"
            f"Plot: {movie.get('plot')}\n\n"
        )

    prompt = [
    "You are a movie recommendation assistant.\n\n"
    "Do NOT use information that is not provided in the context.\n"
    "You have NO knowledge outside the context.\n"
    "Do not answer general knowledge questions.\n"
    "First, determine whether any movie in the context actually answers the question.\n"
    "Do NOT recommend a movie if its plot is not clearly related to the question.\n"
    "If none of the movies in the context answer the question, say exactly:\n"
    "I don't know based on the provided context.\n"
    "Do not add any other text in that case.\n"
    "Do not invent movies or use external knowledge.\n\n",
    f"Context:\n{context}\n\n"
    f"Question: \n{question}\n\n"
    ]

    return prompt

def generate_answer(prompt: list[str]) -> str:
    response = openai_client.chat.completions.create(
        model = CHAT_MODEL,
        messages = [
            {
                "role": "system",
                "content": prompt[0]
            },
            {
                "role": "user",
                "content": prompt[1]
            }
        ]
    )

    return response.choices[0].message.content

def ask(question: str) -> str:
    movies = retrieve_context(question)

    if not movies:
        return "I don't know based on the provided context."

    prompt = build_prompt(
        question,
        movies
    )

    return generate_answer(prompt)

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "space movies where humanity is in danger"
    print(f"Query: {q!r}\n")
    print(ask(q))
