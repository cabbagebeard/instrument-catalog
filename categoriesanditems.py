from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Category, Item, User

engine = create_engine('sqlite:///categorieswithusers.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

User1 = User(name="Superuser", email="kevin@kevw.in",
             picture='http://2.bp.blogspot.com/-MsCyesmbgL0/Tpo2Q0wPthI/AAAAAAAABHU/RAQd1j6nm4U/s1600/Jim-Halpert-786091-1.png')
session.add(User1)
session.commit()

category1 = Category(user_id=1, name="Percussion")

session.add(category1)
session.commit()

item1 = Item(user_id=1, name="Acoustic Drum Set", description="Kick drum, snare, double high toms, floor tom, hi-hat, crash, and ride cymbals.",
                     category=category1)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Electric Drum Set", description="Kick drum, snare, double high toms, floor tom, hi-hat, crash, and ride cymbals - ELECTRIFIED!",
                     category=category1)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Tambourine", description="The best instrument for someone who likes to waste space on stage.",
                     category=category1)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Cowbell", description="You already know exactly what joke is going to be made.",
                     category=category1)

session.add(item4)
session.commit()

category2 = Category(user_id=1, name="Woodwind")

session.add(category2)
session.commit()

item1 = Item(user_id=1, name="Flute", description="Like a whistle but even more piercing.",
                     category=category2)

session.add(item1)
session.commit()

item2 = Item(user_id=1, name="Clarinet", description="Look like the silhouette from Zatarain's!",
                     category=category2)

session.add(item2)
session.commit()

item3 = Item(user_id=1, name="Saxophone", description="The best instrument for collecting change in a hat on the street.",
                     category=category2)

session.add(item3)
session.commit()

item4 = Item(user_id=1, name="Ocarina", description="For when you want to play a tune that can turn back time or summon a horse.",
                     category=category2)

session.add(item4)
session.commit()