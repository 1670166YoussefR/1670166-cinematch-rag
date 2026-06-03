# IA_REPORT — `<1670166>`

**Obligatori.** Honest i específic.

## Política d'IA del curs

L'única IA permesa per al desenvolupament d'aquesta pràctica és el bot **PROFE**
del curs (Discord). **NO** està permès usar cap altra IA (Claude Code, Claude
Copilot, ChatGPT, GitHub Copilot, etc.). **NO s'accepta lliurar codi que NO
sapigueu explicar.**

## Registre d'ús del bot PROFE

| Data | Pregunta feta a PROFE | Resposta resumida | Què hem verificat nosaltres |
|---|---|---|---|
|28/05| Estic fent el N1 de la pràctica CineMatch i ja tinc el  $vectorSearch funcionant correctament. Quan faig una query semàntica, a vegades em retorna pel·lícules repetides (per exemple Ruby Sparks surt dues vegades al top-5). Això es considera acceptable per al lliurable N1?| Comprobar primer quin es el motiu de que surtin dos cops la mateixa pelicula i decidir a partir d'aixo|He executat la comanda que m'ha proporcionat i efectivament, la mateixa pelicula sortia dos vegades, que era una de les hipotesis que m'ha proporcionat|
|28/05| Li he pasat el codi que he realitzat de N1| M'ha respost amb un error que tenia ja que he posat limit: limit * 3 i en aquest cas limit pot ser mes gran que numCandidates, produint un error| Hem verificat el posible error posant limit sigui 60, fent que numCandidates sigui mes petit que limit|
|28/05|Proporciono una posible solucio d'aquest error fent dient de multiplicar tambe numCandidates * 3|Em respon dient que la idea esta bé pero que una idea millor seria posant un max() per a que no fasi moltes busquedes
|03/06|Li explico les diferents funcions que implemento a n2_rag i el seu contingun|Em pregunta quin rol assignaria al context a la crida del LLM||
|03/06|Li demano que m'expliqui els diferents rols que existeixen per poder tenir una idea|M'explica cada rol.|He llegit que tingui sentit la explicació de cada rol buscant a internet|
|03/06|Li torno a pasar el codi del build_prompt|Em diu que hauria de separar instruccions estatiques de instruccions dinamiques i assignarli un rol a cada una|Verifico que aixo es veritat ja que les instruccions estatiques les hauria de pasar per system i les dinamiques les hauria de pasar per user|
|03/06|Em pregunta quin seria el prompt defensiu|Li paso les linies de codi que fant que el prompt sigui defensiu en cas de una pregunta fora de context|Comprovo executant n2_rag|
|03/06|Li pregunto perque podria fallar C3 en el N2|Em respon dient que pot ser que comprovi el comportament rellevant quan vectorSearch no troba res |Miro el meu codi i realment no tinc cap comprobador en el cas de que el vectorSearch no retorni res|


> Afegiu una fila per cada interacció substantiva amb PROFE. Si no hi ha
> interaccions, escriviu "Cap consulta a PROFE durant el desenvolupament".

## Resum honest

- **Parts del codi que cada membre del grup pot explicar línia a línia:**
  `Puc explicar mes o menys tot el codi`
- **Quelcom que hem fet servir però NO entenem del tot** (sigueu honestos):
  `Sent honest, crec que entenc tot el que he desenvolupat`
- **Errors / suggeriments incorrectes de PROFE que hem rebutjat:**
  `He rebutjat una sugerencia que era filtrar el score abans de construir el prompt per veure si el resultat era rellevant.`

## Declaració

Per la present, els membres del grup `Youssef Rabouz` declarem que:

- [ x ] **NO** hem usat cap IA diferent del bot PROFE per desenvolupar aquest projecte.
- [ x ] Tot el codi del repositori l'entenem i podem explicar-lo.
- [ x ] El registre anterior reflecteix totes les interaccions substantives amb PROFE.

**Signat (NIUs):** `1670166`
