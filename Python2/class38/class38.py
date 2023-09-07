# import sqlite3
#
# with sqlite3.connect('cars_dump.db') as con:
#     cur = con.cursor()
#
#     with open('sql_dump.sql', 'r') as f:
#         sql = f.read()
#         cur.executescript(sql)


#  ...........................ORM - SQLAlchemy..................................
# pip install sqlalchemy


import os
from sqlalchemy import and_, or_, not_
from git_class.models.database import DATABASE_NAME, Session
import create_database as db_creator

from git_class.models.lesson import Lesson, association_table
from git_class.models.student import Student
from git_class.models.group import Group

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()

    # print(session.query(Lesson).all())
    # print("*" * 60)
    #
    # for it in session.query(Lesson):
    #     print(it)
    # print("*" * 60)
    #
    # print(session.query(Lesson).count())
    # print("*" * 60)
    #
    # print(session.query(Lesson).first())
    # print("*" * 60)

    for it in session.query(Lesson).filter(or_(Lesson.id > 3, Lesson.lesson_title.like('М%'))):
        print(it)
    print("*" * 60)