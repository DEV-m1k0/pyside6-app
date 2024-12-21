from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy import String, create_engine, ForeignKey


engine = create_engine("sqlite:///database.db", echo=True)
Session = sessionmaker(engine)

def create_db_and_tables():
	Base.metadata.create_all(engine)
 
class Base(DeclarativeBase):
	pass

class User(Base):
	__tablename__ = "users"

	id: Mapped[int] = mapped_column(primary_key=True)
	full_name: Mapped[str] = mapped_column(String(255))


class Item(Base):
	__tablename__ = "items"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column(String(255))


class UserItems(Base):
	__tablename__ = "user_items"

	id: Mapped[int] = mapped_column(primary_key=True)
	item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
	user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
	count: Mapped[int] = mapped_column()