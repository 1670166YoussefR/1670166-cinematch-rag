"""N1 — Semantic Search over sample_mflix.embedded_movies.

End-to-end working example: embed a natural-language query and retrieve the
most semantically similar movies via Atlas `$vectorSearch`.

Prerequisite: the vector index must exist (see README, "Create the vector
index"). Run:  uv run python -m src.n1_semantic_search "your query here"
"""
import sys

from .config import VECTOR_INDEX_NAME, collection, embed


def semantic_search(query: str, limit: int = 5) -> list[dict]:
    query_vector = embed(query)
    pipeline = [
        {
            "$vectorSearch": {
                "index": VECTOR_INDEX_NAME,
                "path": "plot_embedding",
                "queryVector": query_vector,
                "numCandidates": max(150, limit * 10),
                "limit": limit + 10,
            }
        },
        {
            "$project": {
                "_id": 0,
                "title": 1,
                "year": 1,
                "plot": 1,
                "genres": 1,
                "score": {"$meta": "vectorSearchScore"},
            }
        },
    ]

    results = list(collection.aggregate(pipeline))
    seen_titles = set()
    final_results = []

    for movie in results:
        title = movie.get("title")
        if title not in seen_titles:
            seen_titles.add(title)
            final_results.append(movie)

        if len(final_results) == limit:
            break

    return final_results

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else "space movies where humanity is in danger"
    print(f"Query: {q!r}\n")
    for r in semantic_search(q):
        print(f"  {r['score']:.4f}  ({r.get('year', '?')})  {r['title']}")
