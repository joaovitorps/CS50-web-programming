characters = [
    {"name": "Rock Lee", "justsu_style":"Taijustu"}, 
    {"name": "Itachi","justsu_style": "Genjutsu"}, 
    {"name": "Naruto", "justsu_style": "Ninjutsu"}
]

# def sort_characters(characters):
#     return characters["justsu_style"]

# characters.sort(key=sort_characters)

characters.sort(key=lambda character: character["name"])

print(characters)