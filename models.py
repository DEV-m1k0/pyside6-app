from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, sessionmaker
from sqlalchemy import String, create_engine, ForeignKey
from datetime import date


engine = create_engine("sqlite:///database.db")
Session = sessionmaker(engine)

def create_db_and_tables():
	Base.metadata.create_all(engine)
 
class Base(DeclarativeBase):
	pass

class User(Base):
	__tablename__ = "users"

	id: Mapped[int] = mapped_column(primary_key=True)
	full_name: Mapped[str] = mapped_column(String(255))

	def __repr__(self):
		return f"User<full_name={self.full_name}>"


class Item(Base):
	__tablename__ = "items"

	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column(String(255))

	def __repr__(self):
		return f"Item<title={self.title}>"


class UserItem(Base):
	__tablename__ = "user_items"

	id: Mapped[int] = mapped_column(primary_key=True)
	user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
	item_id: Mapped[int] = mapped_column(ForeignKey("items.id"))
	count: Mapped[int] = mapped_column()
	date_of_receipt: Mapped[date] = mapped_column()

	def __repr__(self):
		return f"UserItem<user_id={self.user_id}, item_id={self.item_id}, count={self.count}, date_of_receipt={self.date_of_receipt}>"