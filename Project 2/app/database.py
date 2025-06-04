from tinydb import TinyDB, Query

db = TinyDB('../data/app_data.json')

db.insert({'Deck': 'Definitions','front': 'Dip', 'back': 'To put something into another thing'})

Flashcard = Query()
result = db.search(db.search(Flashcard.number == 1))
print(result)