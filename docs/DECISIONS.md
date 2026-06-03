# DECISIONS — `<1670166>`

Documenteu cada decisió no-òbvia amb el seu trade-off. **Avaluat al Canal C de
la rúbrica (15%)**. Cal almenys 5 decisions amb trade-off explícit per a la
nota completa. Sigueu breus; un bullet per decisió, sempre amb un **per què**.

## Retrieval
- **k / limit** = `5`. Why: `Perque son les demanades al enunciat`
- **numCandidates** = `max(150, limit * 10)`. Why (recall vs latency): `numCandidates ha de ser major a limit perque MongoDB no tingui problemes. Mes candidats milloren el recall pero poden augmentar la latencia`
- **similarity** = `cosine` / `dotProduct` / `euclidean`. Why: `_____`
- **pre-filter** used? on which field (`year`?): `No s'han utilitzat pre-filtres ni post-filtres`. Why pre- and not post-filter: `_____`

## Embeddings
- **EMBED_MODEL** = `text-embedding-ada-002`. Why this exact model (not just 1536-d): `Poerque el camp plot_embedding ja esta generat amb aquest model. No es té prou amb la dimensió, tambe es necesita un espai semàntic igual. Si l'espai semàntic es diferent, es pot produir soroll`

## RAG (N2+)
- **Chunking**: N/A (we use the precomputed plot embedding) / or describe: `N/A`
- **Defensive prompt**: what instruction prevents hallucination: `La instrucció principal és Use only information contained in the context i If the context does not contain enough information to answer, say exactly: I don't know based on the provided context`
- **CHAT_MODEL** = `gpt-40-mini`. Why: `Es el model configurat al .env per generar la resposta. Aquest model es suficient per redactar recomenacions curtes amb baix cost`

## Agent / Multi-agent (N3/N4)
- **Tools defined**: `_____`
- **Architecture pattern** (chaining / routing / evaluator-optimizer / parallel): `_____`. Why: `_____`
- **Retry / stop condition** (N4): `_____`

## Alternatives considered and rejected
- `_____` rejected because `_____`
