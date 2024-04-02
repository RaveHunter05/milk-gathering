from app.dependencies import (
    APIRouter,
    Depends,
    HTTPException,
    get_db,
    Session,
    List,
    Annotated,
    oauth2_scheme,
)

from app.src import schemas, crud

router = APIRouter(prefix="/milk_selled")


# Milk Selled
@router.get(
    "",
    response_model=List[schemas.MilkSelled],
    tags=["milk selled"],
)
def read_milk_selleds(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    milk_selled = crud.get_milk_selleds(db, skip=skip, limit=limit)
    return milk_selled


@router.get(
    "/{milk_selled_id}",
    response_model=schemas.MilkSelled,
    tags=["milk selled"],
)
def read_milk_selled(
    token: Annotated[str, Depends(oauth2_scheme)],
    milk_selled_id: int,
    db: Session = Depends(get_db),
):
    db_milk_selled = crud.get_milk_selled(db, milk_selled_id=milk_selled_id)
    if db_milk_selled is None:
        raise HTTPException(status_code=404, detail="Milk Sell not found")
    return db_milk_selled


@router.post(
    "", response_model=schemas.MilkSelled, tags=["milk selled"]
)
def create_milk_selled(
    token: Annotated[str, Depends(oauth2_scheme)],
    milk_selled: schemas.MilkSelledCreate,
    db: Session = Depends(get_db),
):
    return crud.create_milk_selled(db=db, milk_selled=milk_selled)


@router.put(
    "/{milk_selled_id}",
    response_model=schemas.MilkSelled,
    tags=["milk selled"],
)
def update_milk_selled(
    token: Annotated[str, Depends(oauth2_scheme)],
    milk_selled_id: int,
    milk_selled: schemas.MilkSelledUpdate,
    db: Session = Depends(get_db),
):
    db_milk_selled = crud.update_milk_selled(db=db, milk_selled=milk_selled)
    return db_milk_selled
