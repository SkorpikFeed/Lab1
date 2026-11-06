from lab1 import g

PREFIXES = """
PREFIX ex: <http://example.org/myMysic/>
PREFIX schema: <http://schema.org/>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
"""

# 1. FILTER — альбоми, випущені після 2015 року
q1 = PREFIXES + """
SELECT ?albumName ?yearNum WHERE {
    ?album schema:name ?albumName ;
           ex:releasedIn ?year .
    ?year schema:name ?yearNum .
    FILTER (?yearNum > 2015)
}
"""

# 2. ORDER BY — усі альбоми за роком, спадання
q2 = PREFIXES + """
SELECT ?albumName ?yearNum WHERE {
    ?album schema:name ?albumName ;
           ex:releasedIn ?year .
    ?year schema:name ?yearNum .
}
ORDER BY DESC(?yearNum)
"""

# 3. Зв'язок між типами сутностей - пісні жанру Rock
q3 = PREFIXES + """
SELECT ?songName WHERE {
    ?song schema:genre <http://example.org/myMysic/genre/Rock> ;
          schema:name ?songName .
}
"""

# 4. Агрегатна функція — кількість альбомів на виконавця
q4 = PREFIXES + """
SELECT ?artistName (COUNT(?album) AS ?numAlbums) WHERE {
    ?album schema:byArtist ?artist .
    ?artist schema:name ?artistName .
}
GROUP BY ?artistName
ORDER BY DESC(?numAlbums)
"""

# 5. Перехід через 3+ зв'язки — Song -> Album -> Artist -> Country
q5 = PREFIXES + """
SELECT ?songName ?countryName WHERE {
    ?song   schema:inAlbum ?album ;
            schema:name ?songName .
    ?album  schema:byArtist ?artist .
    ?artist schema:location ?country .
    ?country schema:name ?countryName .
}
"""

# 6. Поєднання з відкритими даними (Локальний граф + Wikidata через owl:sameAs)
q6 = PREFIXES + """
SELECT ?localName ?wikiEntity ?wikiLabel WHERE {
    # Дані з локального графу
    ?artistUri schema:name ?localName ;
               owl:sameAs ?wikiEntity .


    # Федеративний запит до зовнішньої точки доступу Wikidata
    SERVICE <https://query.wikidata.org/sparql> {
        ?wikiEntity rdfs:label ?wikiLabel .
        FILTER(LANG(?wikiLabel) = "en")
    }
}
"""

for i, q in enumerate([q1, q2, q3, q4, q5, q6], start=1):
    print(f"\n--- Запит {i} ---")
    for row in g.query(q):
        print(row)