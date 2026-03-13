from sqlalchemy.orm import Session
from fastapi import HTTPException, status, Response, Depends
from ..models import models, schemas


def create(db: Session, recipe):
    # Create a new instance of the Order model with the provided data
    db_recipies = models.Recipe(
        sandwich_id = recipe.sandwiches.id,
        resource_id = recipe.resource.id,
        amount = recipe.amount
    )
    db.add(db_recipies)
    db.commit()
    db.refresh(db_recipies)
    return db_recipies


def read_all(db: Session):
    return db.query(models.Recipe).all()


def read_one(db: Session, recipe_id):
    return db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()


def update(db: Session, recipe_id, recipe):
    db_recipies = db.query(models.Recipe).filter(models.Recipe.id == recipe_id)
    update_data = recipe.model_dump(exclude_unset=True)
    db_recipies.update(update_data, synchronize_session=False)
    db.commit()
    return db_recipies.first()


def delete(db: Session, recipe_id):
    db_recipies = db.query(models.Recipe).filter(models.Order.id == recipe_id)
    db_recipies.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)
