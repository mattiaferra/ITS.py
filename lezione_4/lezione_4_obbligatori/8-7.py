def make_album(nome_artista ,titolo_album ,numero_brani=None):
    
    dict_album = {"artista": nome_artista, "album": titolo_album}
   
    return dict_album
    
album_1 = make_album("SferaEbbasta","FAMOSO", "17")
album_2 = make_album("GUE","Tropico del Capricorno", "18")
album_3 = make_album("Lazza","Sirio","14")

print(album_1)
print(album_2)
print(album_3)


    