meme_dict = {
            "CRINGE": "Algo raro o embarazoso",
            "LOL": "Respuesta a algo gracioso",
            "NPC": "Persona que actúa como un robot o personaje de videojuego",
            "XD": "Significa risa",
            "BUGUEADO": "Cuando algo no funciona como debería",
            "NT": "Nice try que significa buen intento",
            "CREEPY":"algo aterrador que da miedo",
            "BOOMER":"Persona que se aferra mucho al pasado",
            "PA":"para",
            "TROLlEAR": "hacer una broma"
            }

word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("No se encuentra esa palabra")
