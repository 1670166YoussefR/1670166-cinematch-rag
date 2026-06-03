# DECISIONS — `<1670166>`

Documenteu cada decisió no-òbvia amb el seu trade-off. **Avaluat al Canal C de
la rúbrica (15%)**. Cal almenys 5 decisions amb trade-off explícit per a la
nota completa. Sigueu breus; un bullet per decisió, sempre amb un **per què**.

## Retrieval
- **k / limit** = `5`. Why: `El limit es 5 ja que ofereixen prou context per respondre la consulta sense afegir massa informació irrellevant. Durant la cerca es recuperen alguns resultats adicionals per eliminar duplicats. Trade-off: Recuperar mes pelicules augmenta el context disponible, pero fa que el prompt sigui mes llarg produint mes soroll en la resposta`
- **numCandidates** = `max(150, limit * 10)`. Why (recall vs latency): `He escollit un minim de 150 perque permet avaluar prou candidats per obtenir resultats rellevants sense augmentar massa el temps de resposta. Quan limit *10 supera 150, es va escalant per a que el valor de numCandidates sigui sempre major a limit. Trade-off: més candidats milloren el recall pero incrementen la latència. Menys candidats son mes ràpids pero els resultats son pitjors`
- **similarity** = `cosine` / `dotProduct` / `euclidean`. Why: `S'ha utilitzat cosine perque es la metrica estandard per comparar embeddings de text i obtenir resultats semànticament similars. dotProduct serveix per comparar vectors normalitzats i euclidean serveix per comparar distàncies geometriques.`
- **pre-filter** used? on which field (`year`?): `No s'han utilitzat pre-filtres ni post-filtres`. Why pre- and not post-filter: `No s'ha utilitzat cap tipus de filtre`

## Embeddings
- **EMBED_MODEL** = `text-embedding-ada-002`. Why this exact model (not just 1536-d): `Perque el camp plot_embedding ja esta generat amb aquest model. No es té prou amb la dimensió, tambe es necesita un espai semàntic igual. Si l'espai semàntic es diferent, es pot generar resultats incorrectes o soroll en la cerca`

## RAG (N2+)
- **Chunking**: N/A (we use the precomputed plot embedding) / or describe: `N/A`
- **Defensive prompt**: what instruction prevents hallucination: `S'utilitzen les seguents instruccions: "Use only information contained in the context.\n" "If the context does not contain enough information to answer, say exactly:\n" "I don't know based on the provided context.\n" "Do not invent movies or use external knowledge.\n"`
`Es força el model a utilitzar només el context proporcionat i a respondre "I don't know based on the provided context" quan la informació és insuficient, evitant al·lucinacions i l'ús de coneixement extern.`
- **CHAT_MODEL** = `gpt-4o-mini`. Why: `S'ha escollit gpt-4o-mini perquè ofereix un bon equilibri entre qualitat de resposta, velocitat i cost. Com que el model només ha de generar una resposta a partir del context recuperat pel RAG, no és necessari utilitzar un model més gran i costós.`

## Agent / Multi-agent (N3/N4)
- **Tools defined**: `_____`
- **Architecture pattern** (chaining / routing / evaluator-optimizer / parallel): `_____`. Why: `_____`
- **Retry / stop condition** (N4): `_____`

## Alternatives considered and rejected
- `_____` rejected because `_____`
