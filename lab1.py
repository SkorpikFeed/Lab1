from rdflib import Graph, Literal, RDF, URIRef, Namespace, OWL
from rdflib.namespace import FOAF, XSD

# Ініціалізація порожнього графа
g = Graph()

# Створення просторів імен
ex = Namespace("http://example.org/myMysic/")
schema = Namespace("http://schema.org/")
owl = Namespace("http://www.w3.org/2002/07/owl#")

g.bind("ex", ex)
g.bind("schema", schema, override=True, replace=True)
g.bind("owl", OWL)

# =====================================================================
# 1. СТВОРЕННЯ СУТНОСТЕЙ
# =====================================================================

# Тип 1: Музичні гурти (клас зі Schema.org)
g.add((ex["artist/Starset"], RDF.type, schema["MusicGroup"]))
g.add((ex["artist/Architects"], RDF.type, schema["MusicGroup"]))
g.add((ex["artist/ImagineDragons"], RDF.type, schema["MusicGroup"]))

# Тип 2: Музичні альбоми
g.add((ex["album/Transmissions"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Vessels"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Horizons"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Daybreaker"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/HolyHell"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Evolve"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Origins"], RDF.type, schema["MusicAlbum"]))

# Тип 3: Роки
g.add((ex["year/2017"], RDF.type, ex["Year"]))
g.add((ex["year/2018"], RDF.type, ex["Year"]))
g.add((ex["year/2012"], RDF.type, ex["Year"]))
g.add((ex["year/2014"], RDF.type, ex["Year"]))
g.add((ex["year/2021"], RDF.type, ex["Year"]))

# Тип 4: Музичні треки
g.add((ex["song/MyDemons"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Satellite"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Disappear"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/HolyHell"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Doomsday"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Believer"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Natural"], RDF.type, schema["MusicRecording"]))

# Тип 5: Музичні жанри
g.add((ex["genre/Rock"], RDF.type, ex["MusicGenre"]))
g.add((ex["genre/Metalcore"], RDF.type, ex["MusicGenre"]))

# Тип 6: Країни походження
g.add((ex["country/UK"], RDF.type, schema["Country"]))
g.add((ex["country/USA"], RDF.type, schema["Country"]))

# =====================================================================
# 2. ЗВ'ЯЗКИ МІЖ СУТНОСТЯМИ
# =====================================================================

# Зв'язок 1: Альбом належить виконавцю
g.add((ex["album/Transmissions"], schema["byArtist"], ex["artist/Starset"]))
g.add((ex["album/Vessels"], schema["byArtist"], ex["artist/Starset"]))
g.add((ex["album/Horizons"], schema["byArtist"], ex["artist/Starset"]))
g.add((ex["album/Daybreaker"], schema["byArtist"], ex["artist/Architects"]))
g.add((ex["album/HolyHell"], schema["byArtist"], ex["artist/Architects"]))
g.add((ex["album/Evolve"], schema["byArtist"], ex["artist/ImagineDragons"]))
g.add((ex["album/Origins"], schema["byArtist"], ex["artist/ImagineDragons"]))

# Зв'язок 2: Трек входить до альбому
g.add((ex["song/MyDemons"], schema["inAlbum"], ex["album/Transmissions"]))
g.add((ex["song/Satellite"], schema["inAlbum"], ex["album/Vessels"]))
g.add((ex["song/Disappear"], schema["inAlbum"], ex["album/Horizons"]))
g.add((ex["song/HolyHell"], schema["inAlbum"], ex["album/HolyHell"]))
g.add((ex["song/Doomsday"], schema["inAlbum"], ex["album/HolyHell"]))
g.add((ex["song/Believer"], schema["inAlbum"], ex["album/Evolve"]))
g.add((ex["song/Natural"], schema["inAlbum"], ex["album/Origins"]))

# Зв'язок 3: Трек належить жанру
g.add((ex["song/MyDemons"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/Satellite"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/Disappear"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/Believer"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/Natural"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/HolyHell"], schema["genre"], ex["genre/Metalcore"]))
g.add((ex["song/Doomsday"], schema["genre"], ex["genre/Metalcore"]))

# Зв'язок 4: Албом випущений у певному році
g.add((ex["album/Transmissions"], ex["releasedIn"], ex["year/2014"]))
g.add((ex["album/Vessels"], ex["releasedIn"], ex["year/2017"]))
g.add((ex["album/Horizons"], ex["releasedIn"], ex["year/2021"]))
g.add((ex["album/Daybreaker"], ex["releasedIn"], ex["year/2012"]))
g.add((ex["album/HolyHell"], ex["releasedIn"], ex["year/2018"]))
g.add((ex["album/Evolve"], ex["releasedIn"], ex["year/2017"]))
g.add((ex["album/Origins"], ex["releasedIn"], ex["year/2018"]))

# Зв'язок 5: Артист із певної країни
g.add((ex["artist/Starset"], schema["location"], ex["country/USA"]))
g.add((ex["artist/ImagineDragons"], schema["location"], ex["country/USA"]))
g.add((ex["artist/Architects"], schema["location"], ex["country/UK"]))

# Зв'язок 6: Подальші літерали
# Для артистів
g.add((ex["artist/Starset"], schema["name"], Literal("Starset")))
g.add((ex["artist/Architects"], schema["name"], Literal("Architects")))
g.add((ex["artist/ImagineDragons"], schema["name"], Literal("Imagine Dragons")))

# Для пісень
g.add((ex["song/MyDemons"], schema["name"], Literal("My Demons")))
g.add((ex["song/Satellite"], schema["name"], Literal("Satellite")))
g.add((ex["song/Disappear"], schema["name"], Literal("Disappear")))
g.add((ex["song/Believer"], schema["name"], Literal("Believer")))
g.add((ex["song/Natural"], schema["name"], Literal("Natural")))
g.add((ex["song/HolyHell"], schema["name"], Literal("Holy Hell")))
g.add((ex["song/Doomsday"], schema["name"], Literal("Doomsday")))

# Для альбомів
g.add((ex["album/Transmissions"], schema["name"], Literal("Transmissions")))
g.add((ex["album/Horizons"], schema["name"], Literal("Horizons")))
g.add((ex["album/Daybreaker"], schema["name"], Literal("Daybreaker")))
g.add((ex["album/Evolve"], schema["name"], Literal("Evolve")))
g.add((ex["album/Origins"], schema["name"], Literal("Origins")))
g.add((ex["album/Vessels"], schema["name"], Literal("Vessels")))
g.add((ex["album/HolyHell"], schema["name"], Literal("Holy Hell")))

# Для жанрів
g.add((ex["genre/Rock"], schema["name"], Literal("Rock")))
g.add((ex["genre/Metalcore"], schema["name"], Literal("Metalcore")))

# Для країн
g.add((ex["country/USA"], schema["name"], Literal("USA")))
g.add((ex["country/UK"], schema["name"], Literal("UK")))

# Для років
g.add((ex["year/2017"], schema["name"], Literal(2017)))
g.add((ex["year/2018"], schema["name"], Literal(2018)))
g.add((ex["year/2012"], schema["name"], Literal(2012)))
g.add((ex["year/2014"], schema["name"], Literal(2014)))
g.add((ex["year/2021"], schema["name"], Literal(2021)))

# Зовнішній ресурс із Wikidata 
wikidata_starset = URIRef("http://www.wikidata.org/entity/Q17386735")
wikidata_architects = URIRef("http://www.wikidata.org/entity/Q620454")
wikidata_imaginedragons = URIRef("http://www.wikidata.org/entity/Q391348")

# Створення семантичного зв'язку між локальним графом і Wikidata
g.add((ex["artist/Starset"], OWL.sameAs, wikidata_starset))
g.add((ex["artist/Architects"], OWL.sameAs, wikidata_architects))
g.add((ex["artist/ImagineDragons"], OWL.sameAs, wikidata_imaginedragons))

# Серріалізація графа у форматі turtle
g.serialize(destination="MyMusic_graph.ttl", format="turtle")

# Серріалізація графа у форматі xml
g.serialize(destination="music_graph.xml", format="xml")

# Створюємо новий граф і завантажуємо туди дані з файлу
g_new = Graph()
g_new.parse("MyMusic_graph.ttl", format="turtle")

# Вносимо зміни вручну: додаємо новий трек до файлового графу
new_song = ex["song/NewTestSong"]
g_new.add((new_song, RDF.type, schema["MusicRecording"]))
g_new.add((new_song, schema["name"], Literal("Test Song")))
print(f"3. Прочитано файл та внесено зміни. Нова кількість трійок у g_new: {len(g_new)}")

# Виведення вибраних трійок графу на консоль 
print("\n4. Приклад виведення перших 5 трійок графу:")
for count, (s, p, o) in enumerate(g_new, start=1):
    print(f"[{count}] {s} -> {p} -> {o}")
    if count >= 5:
        print("... (далі пропущено)")
        break

# Отримання трійок, пов'язаних із конкретною сутністю 
print("\n5. Трійки, пов'язані з конкретною сутністю (гурт Starset):")
starset_uri = ex["artist/Starset"]
for p, o in g.predicate_objects(subject=starset_uri):
    print(f"Предикат: {p} ---> Об'єкт: {o}")

# Серіалізація відредагованого графа
g_new.serialize(destination="MyMusic_graph_edited.ttl", format="turtle")