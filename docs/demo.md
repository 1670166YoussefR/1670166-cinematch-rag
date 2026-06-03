# demo.md — `<1670166>`

Aquest fitxer és **obligatori**. Conté dues parts:

1. **Traça d'execució** per cada nivell lliurat (captures, exemples, sortides reals)
2. **Defensa escrita (Q&A)** — 5 preguntes obligatòries (Canal D del rúbric, 15%)

---

## 1. Traça d'execució per nivell

### N1 — Semantic Search

Comanda executada:

```bash
uv run python -m src.n1_semantic_search "space movies where humanity is in danger"
```

Sortida real (top-5 pel·lícules amb `vectorSearchScore`):

```
0.9381  (1979)  Buck Rogers in the 25th Century
0.9341  (2000)  Titan A.E.
0.9302  (1986)  Aliens
0.9275  (1984)  V: The Final Battle
0.9272  (1983)  Space Raiders
```

```bash
uv run python -m src.n1_semantic_search "romantic movies about impossible love"
```

Sortida real (top-5 pel·lícules amb `vectorSearchScore`):

```
0.9231  (1989)  Always
0.9201  (2009)  The Time Traveler's Wife
0.9171  (2012)  Ruby Sparks
0.9161  (1964)  Frosty
0.9132  (2004)  Hulchul
```

```bash
uv run python -m src.n1_semantic_search "crime movies with detectives and murder investigations"
```

Sortida real (top-5 pel·lícules amb `vectorSearchScore`):

```
0.9350  (2012)  Alex Cross
0.9332  (1989)  Kill Me Again
0.9331  (2008)  Righteous Kill
0.9328  (1984)  City Heat
0.9315  (1998)  Snake Eyes
```

### N2 — RAG (si arribeu)

**Cas positiu** (resposta basada al context):

- Query: `space movies where humanity is in danger`
- Top-k títols recuperats: `Buck Rogers in the 25th Century, Titan A.E., Aliens, V: The Final Battle, Space Raiders`
- Resposta de l'LLM (ha de citar títols): 
`Here are some space movies where humanity is in danger based on the provided context:

1. **Buck Rogers in the 25th Century** - Earth is threatened by alien invaders.
2. **Titan A.E.** - A young man must find a hidden Earth ship to secure the survival of humanity against an enemy alien species.
3. **Aliens** - A rescue team faces the challenge of contact loss on a colonized planet, with uncertain outcomes.
4. **V: The Final Battle** - Human resistance fighters are engaged in a guerilla war against genocidal extra-terrestrials dominating Earth.

I don't think "Space Raiders" specifically fits the theme of humanity being in danger based on the context provided.`

**Cas negatiu** (sense context → ha de dir "no ho sé"):

- Query: `How can i pass the ATS subject?`
- Resposta esperada: `I don't know based on the provided context.`
- Resposta obtinguda: `I don't know based on the provided context.`

### N3 — Tools + Structured Outputs (si arribeu)

3 casos que exerciten **rutes diferents** (cerca / filtre / no trobat):

1. `_____`
2. `_____`
3. `_____`

Esquema de sortida (Pydantic o JSON schema):

```python
_____
```

Exemple de sortida estructurada:

```json
_____
```

### N4 — Multi-agent (si arribeu)

Diagrama del flux d'agents (ASCII o referència a `agent_flow_diagram.png`):

```
_____
```

Traça d'una execució amb **reintent** (cas evaluator-optimizer):

```
_____
```

---

## 2. Defensa escrita (Q&A) — **OBLIGATÒRIA**

Responeu OBLIGATÒRIAMENT aquestes **5 preguntes**. Cadascuna avaluada de
0 / 1,5 / 3 punts segons completitud de la resposta (veure rúbrica). Sigueu
breus i precisos.

### Q1 · Què passa si embeus la query amb `text-embedding-3-small` en lloc d'`ada-002`?

La cerca no funcionaria correctament perquè la query i les pel·lícules estarien embeddings amb models diferents. Per obtenir bons resultats, tots dos han d'utilitzar el mateix model.

### Q2 · Per què `numCandidates` ha de ser > `limit`? Què passa si poses `numCandidates == limit`?

numCandidates ha de ser mes gran que limit ja que MongoDB no retorna titols buits, sino que llança un error directament. Si el valor de numCandidates fos igual a limit, es te menys marge per fer la cerca i podrien empitjorar els resultats.

### Q3 · Si el `$vectorSearch` NO troba res rellevant, què retorna el teu RAG? Per què?

Si el $vectorSearch no troba res rellevant, el meu RAG retorna "I don't know based on the provided context.". Això passa perquè el prompt indica que només pot utilitzar la informació proporcionada i que no ha d'inventar res ni utilitzar informació externa

### Q4 · Per què trieu `cosine` i NO `euclidean` / `dotProduct`?

_____

### Q5 (trieu UNA segons el vostre nivell màxim)

**Si heu fet N4:** Quina condició fa que l'orquestrador reintenti? Com evites el bucle infinit?

**Si heu arribat fins a N3 o inferior:** Per què la sortida estructurada (JSON schema) val més que una resposta en text lliure? Posa un exemple concret on un text lliure us hauria fallat.

_____
