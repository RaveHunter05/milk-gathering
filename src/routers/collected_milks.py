from dependencies import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    get_db,
    Session,
    List,
    Annotated,
    oauth2_scheme,
)

from src import schemas, crud

router = APIRouter()


# Collected Milk
@router.get(
    "/collected_milk/",
    response_model=List[schemas.CollectedMilk],
    tags=["collected milk"],
)
def read_collected_milks(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    collected_milks = crud.get_collected_milks(db, skip=skip, limit=limit)
    return collected_milks


@router.get(
    "/collected_milk/{collected_milk_id}",
    response_model=schemas.CollectedMilk,
    tags=["collected milk"],
)
def read_collected_milk(
    token: Annotated[str, Depends(oauth2_scheme)],
    collected_milk_id: int,
    db: Session = Depends(get_db),
):
    db_collected_milk = crud.get_collected_milk(db, collected_milk_id=collected_milk_id)
    if db_collected_milk is None:
        raise HTTPException(status_code=404, detail="Collected Milk not found")
    return db_collected_milk


@router.post(
    "/collected_milk/", response_model=schemas.CollectedMilk, tags=["collected milk"]
)
def create_collected_milk(
    token: Annotated[str, Depends(oauth2_scheme)],
    collected_milk: schemas.CollectedMilkCreate,
    db: Session = Depends(get_db),
):
    return crud.create_collected_milk(db=db, collected_milk=collected_milk)


@router.put(
    "/collected_milk/{collected_milk_id}",
    response_model=schemas.CollectedMilk,
    tags=["collected milk"],
)
def update_collected_milk(
    token: Annotated[str, Depends(oauth2_scheme)],
    collected_milk_id: int,
    collected_milk: schemas.CollectedMilkUpdate,
    db: Session = Depends(get_db),
):
    db_collected_milk = crud.update_collected_milk(db=db, collected_milk=collected_milk)
    return db_collected_milk
