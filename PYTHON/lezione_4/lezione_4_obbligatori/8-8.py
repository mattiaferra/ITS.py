def make_album(nome_artista ,titolo_album ,numero_brani=None):
    
    dict_album = {
       
    'artista' : nome_artista,
    'album'   : titolo_album,
    'numero brani' : numero_brani
    }
    return dict_album


while True :
    
    nome_artista = str(input("inserisci l'artista :"))
    titolo_album = str(input("inserisci il titolo dell' album :"))
    numero_brani = int(input("iserire numero brani :"))
    
    
    
    dict_album = {"artista": nome_artista, "album": titolo_album}
    
    album_1 = make_album(nome_artista, titolo_album, numero_brani)
    
    esci = input("vuoi inserire un altro album ? :").lower()
    
    
    if esci == "exit":
        print(album_1)
        break

  
    print(album_1)