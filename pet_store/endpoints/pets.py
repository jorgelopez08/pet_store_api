from fastapi import APIRouter, HTTPException
from fastapi import status, Path, Body, Query, Depends

from pet_store import models
from pet_store import schema as sql

from pet_store import database as db
from sqlalchemy.orm import Session


router = APIRouter()


@router.get(
    path='/',
    status_code=status.HTTP_200_OK,
    summary="List all pets",
    tags=['pets']
)
def list_all_pets(
    limit: int = Query(default=20, title="Limit", description="How many items to return at one time (max 100)"),
    db: Session = Depends(db.get_db)
):
    """Lista all pets

    Args:
        limit (int): How many items to return at once.
        db (Session): Database connedtion. 

    Returns:
        Pets: List of pets
    """
    return db.query(sql.Pet).limit(limit).all()

@router.post(
    path='/',
    status_code=status.HTTP_201_CREATED,
    summary='Create a pet',
    tags=['pets']
)
def create_pet(pet: models.Pet = Body(...), db: Session = Depends(db.get_db)):
    """Create a new pet

    Args:
        pet (models.Pet): Pet model
        db (Session): Database connedtion. 

    Returns:
        Pet: Created pet
    """
    new_pet = sql.Pet(**pet.dict())
    db.add(new_pet)
    db.commit()
    return pet

@router.get(
    path='/{pet_id}',
    status_code=status.HTTP_200_OK,
    summary='Info for a specific pet',
    tags=['pets']
)
def get_pet(
    pet_id: int = Path(..., title="Pet id", description="Pet identification number to retrieve"),
    db: Session = Depends(db.get_db)
):
    """Get specific pet

    Args:
        pet_id (int): Pet identification number to retrieve.
        db (Session): Database connedtion. 

    Raises:
        HTTPException: When pet not found

    Returns:
        Pet: The retieved pet information
    """
    pet = db.query(sql.Pet).filter(sql.Pet.id == pet_id).first()
    if pet is None:
        raise HTTPException(404, "Pet not found")
    return pet
