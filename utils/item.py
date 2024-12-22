from sqlalchemy.sql import select
import models
from typing import *
import logging


def get_item_by_id(id: int) -> Optional[models.Item | None]:
    item_sql = select(models.Item).where(models.Item.id==id)
    with models.Session() as session:
        item = session.scalar(item_sql)
    if not item:
        return None
    return item


class Item:
    __ITEM: models.Item

    def __init__(self, title: str):
        self.__ITEM = models.Item(title=title)

    def get_item_name(self) -> str:
        return self.__ITEM.title
    
    def save(self):
        if not self.__check_exist():
            try:
                item_obj = models.Item(title=self.__ITEM.title)
                with models.Session() as session:
                    session.add(item_obj)
                    session.commit()
                    logging.debug(f"{self.__ITEM} добавлен в базу данных")
            except Exception as e:
                logging.error(f"{self.__ITEM} не был добавлен по причине: {e}", exc_info=True)
        else:
            logging.warning(f"{self.__ITEM} уже существует")
        with models.Session() as session:
            saved_item = session.scalar(select(models.Item).where(models.Item.title==self.__ITEM.title))
            self.id = saved_item.id
            self.title = saved_item.title

    def __check_exist(self) -> bool:
        item_sql = select(models.Item).where(models.Item.title==self.__ITEM.title)
        with models.Session() as session:
            item_obj = session.scalar(item_sql)

        if not item_obj:
            return False
        return True