from git_class.models_new.database import DATABASE_NAME, Session
import os
import create_base as db_creator

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

    session = Session()
