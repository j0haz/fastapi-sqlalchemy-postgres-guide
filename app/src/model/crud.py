import logging
logging.basicConfig()
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

import sqlalchemy as sqla
from model import tables, schemas


def create_user(db: sqla.orm.Session, user: schemas.UserCreate) -> tables.User:
    """ creates a user in the database

    Args:
        db (sqlalchemy.orm.Session): SQL alchemy DB session object
        user (schemas.UserCreate): _description_

    Returns:
        db_user (model.tables.User): User that has been created
    """

    db_user = tables.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    
    return db_user


def read_users(db: sqla.orm.Session, skip: int = 0, limit: int = 10):
    """ reads users from the database

    Args:
        db (sqlalchemy.orm.Session): SQL alchemy DB session object
        skip (int, optional): number of entries to skip. Defaults to 0.
        limit (int, optional): number of entries to limit. Defaults to 10.

    Returns:
        db_users (list[model.tables.User]: list of queried users 
    """
    
    db_users = db.query(tables.User).offset(skip).limit(limit).all()
    
    return db_users


def update_user(db: sqla.orm.Session, user: schemas.UserUpdate):
    """ updates specified user in the database

    Args:
        db (sqlalchemy.orm.Session): SQL alchemy DB session object
        user (schemas.UserUpdate): user to update

    Returns:
        db_user (model.tables.User): updated user
    """

    db_user = db.query(tables.User).filter(tables.User.email == user.email).first()

    if not db_user:
        return None
    
    for field, value in user.dict(exclude_unset=True).items():
        setattr(db_user, field, value)
        print(field, value)


    db.commit()
    db.refresh(db_user)

    return db_user


def delete_user(db: sqla.orm.Session, user: schemas.UserDelete) -> None | tables.User:
    """ deletes specified user from the database

    Args:
        db (sqlalchemy.orm.Session): SQL alchemy DB session object
        user (model.schemas.UserDelete): user to delete

    Returns:
        None | model.tables.User: deleted user
    """
    
    db_user = db.query(tables.User).filter(tables.User.email == user.email).first()

    if not db_user:
        return None

    db.delete(db_user)
    db.commit()

    return db_user