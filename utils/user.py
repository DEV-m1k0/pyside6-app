from sqlalchemy.sql import select
import models
from typing import *
from .logging import logging


def get_all_users() -> Sequence[models.User]:
    with models.Session() as session:
        return session.scalars(select(models.User)).all()
    

def get_user_by_full_name(full_name: str) -> Optional[models.User | None]:
    with models.Session() as session:
        user = session.scalar(select(models.User).where(models.User.full_name==full_name))
    if not user:
        return None
    return user


def get_user_by_id(id: int) -> Optional[models.User | None]:
    with models.Session() as session:
        user = session.scalar(select(models.User).where(models.User.id==id))
    if not user:
        return None
    return user


class User:
    __USER: models.User

    def __init__(self, full_name: str):
        self.__USER = models.User(full_name=full_name)

    def get_name(self) -> str:
        return self.__USER.full_name
    
    def get(self) -> models.User:
        return self.__USER

    def save(self):
        if not self.__check_exist():
            try:
                with models.Session() as session:
                    session.add(self.__USER)
                    session.commit()
                    logging.debug(f"{self.__USER} был добавлен в базу данных")
            except Exception as e:
                logging.error(f"{self.__USER} не был добавлен {e}", exc_info=True)
        else:
            logging.warning(f"{self.__USER} уже существует")
        with models.Session() as session:
            saved_user = session.scalar(select(models.User).where(models.User.full_name==self.__USER.full_name))
            self.id = saved_user.id
            self.full_name = saved_user.full_name

    def __check_exist(self) -> bool:
        user_sql = select(models.User).where(models.User.full_name==self.__USER.full_name)
        with models.Session() as session:
            user_obj = session.scalar(user_sql)

        if not user_obj:
            return False
        return True