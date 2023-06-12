import sqlalchemy as DB
from sqlalchemy.orm import Session
from models import Base, Items, Accounts

engine = DB.create_engine('sqlite:///store_bot.db')
connection = engine.connect()


async def db_start():
    Base.metadata.create_all(bind=engine)


async def add_item(state):
    async with state.proxy() as data:
        with Session(autoflush=False, bind=engine) as db:
            new = Items(name=data['name'],
                        desc=data['desc'],
                        price=data['price'],
                        photo=data['photo'],
                        type=data['type'])
            db.add(new)
            db.commit()


async def add_item2(n, d, pr, ph, t):
    with Session(autoflush=False, bind=engine) as db:
        new = Items(name=n,
                    desc=d,
                    price=pr,
                    photo=ph,
                    type=t)
        db.add(new)
        db.commit()


async def get_category_items(cat):
    result = []
    with Session(autoflush=False, bind=engine) as db:
        a = DB.select(Items).where(Items.type == cat)
        for item in db.scalars(a):
            result.append(
                {"id": item.id,
                 "name": item.name,
                 "desc": item.desc,
                 "price": item.price,
                 "photo": item.photo,
                 'type': item.type})
    return result


async def cmd_start_db(user_id, username):
    with Session(autoflush=False, bind=engine) as db:
        user = db.query(Accounts).filter(Accounts.tg_id == user_id).all()
        if not user:
            new_user = Accounts(tg_id=user_id, username=username)
            db.add(new_user)
            db.commit()
