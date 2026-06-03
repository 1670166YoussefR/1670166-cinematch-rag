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
            f"Plot: {movie.get('plot', 'No plot available')}\n\n"
        )

    prompt = [
    "You are a movie recommendation assistant.\n\n"
    "Use only information contained in the context.\n"
    "When answering, mention all movies provided in the context. \n"
    "If the context does not contain enough information to answer, say exactly:\n"
    "I don't know based on the provided context.\n"
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
