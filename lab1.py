from rdflib import Graph, Literal, RDF, URIRef, Namespace
from rdflib.namespace import FOAF, XSD

g = Graph()

ex = Namespace("http://example.org/myMysic/")
schema = Namespace("http://schema.org/")
owl = Namespace("http://www.w3.org/2002/07/owl#")

g.bind("ex", ex)
g.bind("schema", schema)
g.bind("owl", owl)

g.add((ex["artist/Starset"], RDF.type, schema["MusicGroup"]))
g.add((ex["artist/Architects"], RDF.type, schema["MusicGroup"]))
g.add((ex["artist/ImagineDragons"], RDF.type, schema["MusicGroup"]))

g.add((ex["album/Transmissions"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Vessels"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Horizons"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Daybreaker"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/HolyHell"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Evolve"], RDF.type, schema["MusicAlbum"]))
g.add((ex["album/Origins"], RDF.type, schema["MusicAlbum"]))

g.add((ex["year/2017"], RDF.type, ex["Year"]))
g.add((ex["year/2018"], RDF.type, ex["Year"]))
g.add((ex["year/2012"], RDF.type, ex["Year"]))
g.add((ex["year/2014"], RDF.type, ex["Year"]))
g.add((ex["year/2021"], RDF.type, ex["Year"]))

g.add((ex["song/MyDemons"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Satellite"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Disappear"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/HolyHell"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Doomsday"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Believer"], RDF.type, schema["MusicRecording"]))
g.add((ex["song/Natural"], RDF.type, schema["MusicRecording"]))

g.add((ex["genre/Rock"], RDF.type, ex["MusicGenre"]))
g.add((ex["genre/Metalcore"], RDF.type, ex["MusicGenre"]))

g.add((ex["country/UK"], RDF.type, schema["Country"]))
g.add((ex["country/USA"], RDF.type, schema["Country"]))

g.add((ex["album/Transmissions"], schema["byArtist"], ex["artist/Starset"]))
g.add((ex["album/Vessels"], schema["byArtist"], ex["artist/Starset"]))
g.add((ex["album/Horizons"], schema["byArtist"], ex["artist/Starset"]))
g.add((ex["album/Daybreaker"], schema["byArtist"], ex["artist/Architects"]))
g.add((ex["album/HolyHell"], schema["byArtist"], ex["artist/Architects"]))
g.add((ex["album/Evolve"], schema["byArtist"], ex["artist/ImagineDragons"]))
g.add((ex["album/Origins"], schema["byArtist"], ex["artist/ImagineDragons"]))

g.add((ex["song/MyDemons"], schema["inAlbum"], ex["album/Transmissions"]))
g.add((ex["song/Satellite"], schema["inAlbum"], ex["album/Vessels"]))
g.add((ex["song/Disappear"], schema["inAlbum"], ex["album/Horizons"]))
g.add((ex["song/HolyHell"], schema["inAlbum"], ex["album/HolyHell"]))
g.add((ex["song/Doomsday"], schema["inAlbum"], ex["album/HolyHell"]))
g.add((ex["song/Believer"], schema["inAlbum"], ex["album/Evolve"]))
g.add((ex["song/Natural"], schema["inAlbum"], ex["album/Origins"]))

g.add((ex["song/MyDemons"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/Satellite"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/Disappear"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/Believer"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/Natural"], schema["genre"], ex["genre/Rock"]))
g.add((ex["song/HolyHell"], schema["genre"], ex["genre/Metalcore"]))
g.add((ex["song/Doomsday"], schema["genre"], ex["genre/Metalcore"]))

g.add((ex["album/Transmissions"], ex["releasedIn"], ex["year/2014"]))
g.add((ex["album/Vessels"], ex["releasedIn"], ex["year/2017"]))
g.add((ex["album/Horizons"], ex["releasedIn"], ex["year/2021"]))
g.add((ex["album/Daybreaker"], ex["releasedIn"], ex["year/2012"]))
g.add((ex["album/HolyHell"], ex["releasedIn"], ex["year/2018"]))
g.add((ex["album/Evolve"], ex["releasedIn"], ex["year/2017"]))
g.add((ex["album/Origins"], ex["releasedIn"], ex["year/2018"]))

g.add((ex["artist/Starset"], schema["name"], Literal("Starset")))
g.add((ex["artist/Architects"], schema["name"], Literal("Architects")))
g.add((ex["artist/ImagineDragons"], schema["name"], Literal("Imagine Dragons")))

g.add((ex["song/MyDemons"], schema["name"], Literal("My Demons")))
g.add((ex["song/Satellite"], schema["name"], Literal("Satellite")))
g.add((ex["song/Disappear"], schema["name"], Literal("Disappear")))
g.add((ex["song/Believer"], schema["name"], Literal("Believer")))
g.add((ex["song/Natural"], schema["name"], Literal("Natural")))
g.add((ex["song/HolyHell"], schema["name"], Literal("Holy Hell")))
g.add((ex["song/Doomsday"], schema["name"], Literal("Doomsday")))

g.add((ex["artist/Starset"], schema["location"], ex["country/USA"]))
g.add((ex["artist/ImagineDragons"], schema["location"], ex["country/USA"]))
g.add((ex["artist/Architects"], schema["location"], ex["country/UK"]))

g.add((ex["album/Transmissions"], schema["name"], Literal("Transmissions")))
g.add((ex["album/Horizons"], schema["name"], Literal("Horizons")))
g.add((ex["album/Daybreaker"], schema["name"], Literal("Daybreaker")))
g.add((ex["album/Evolve"], schema["name"], Literal("Evolve")))
g.add((ex["album/Origins"], schema["name"], Literal("Origins")))
g.add((ex["album/Vessels"], schema["name"], Literal("Vessels")))
g.add((ex["album/HolyHell"], schema["name"], Literal("Holy Hell")))

g.add((ex["genre/Rock"], schema["name"], Literal("Rock")))
g.add((ex["genre/Metalcore"], schema["name"], Literal("Metalcore")))

g.add((ex["country/USA"], schema["name"], Literal("USA")))
g.add((ex["country/UK"], schema["name"], Literal("UK")))

g.add((ex["year/2017"], schema["name"], Literal(2017)))
g.add((ex["year/2018"], schema["name"], Literal(2018)))
g.add((ex["year/2012"], schema["name"], Literal(2012)))
g.add((ex["year/2014"], schema["name"], Literal(2014)))
g.add((ex["year/2021"], schema["name"], Literal(2021)))


g.serialize(destination="MyMusic_graph.ttl", format="turtle")

g.serialize(destination="music_graph.xml", format="xml")

print(f"Загальна кількість трійок у графі: {len(g)}")

print("\nТрійки для гурту Starset:")
for p, o in g.predicate_objects(subject=ex["artist/Starset"]):
    print(f"{p} -> {o}")

    print("\nАльбоми гурту Starset (через subjects):")
for s in g.subjects(predicate=schema["byArtist"], object=ex["artist/Starset"]):
    print(f"Альбом: {s}")
