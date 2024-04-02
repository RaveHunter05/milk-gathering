from app.dependencies import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    get_db,
    Session,
    List,
    Annotated,
    Depends,
    oauth2_scheme,
)

from app.src import schemas, crud

router = APIRouter(prefix="/cheese_maker")


@router.get("", response_model=List[schemas.CheeseMaker], tags=["cheese_makers"])
def read_cheese_make(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    cheese_makers = crud.get_cheese_makers(db, skip=skip, limit=limit)
    return cheese_makers


@router.get(
    "/{cheese_maker_id}", response_model=schemas.CheeseMaker, tags=["cheese_makers"]
)
def read_cheese_maker(
    token: Annotated[str, Depends(oauth2_scheme)],
    cheese_maker_id: int,
    db: Session = Depends(get_db),
):
    db_cheese_maker = crud.get_cheese_maker(db, cheese_maker_id=cheese_maker_id)
    if db_cheese_maker is None:
        raise HTTPException(status_code=404, detail="Cheese maker not found")
    return db_cheese_maker


@router.post("", response_model=schemas.CheeseMaker, tags=["cheese_makers"])
def create_cheese_maker(
    token: Annotated[str, Depends(oauth2_scheme)],
    cheese_maker: schemas.CheeseMakerCreate,
    db: Session = Depends(get_db),
):
    return crud.create_cheese_maker(db=db, cheese_maker=cheese_maker)


@router.put(
    "/{cheese_maker_id}", response_model=schemas.CheeseMaker, tags=["cheese_makers"]
)
def update_cheese_maker(
    token: Annotated[str, Depends(oauth2_scheme)],
    cheese_maker_id: int,
    cheese_maker: schemas.CheeseMakerUpdate,
    db: Session = Depends(get_db),
):
    db_cheese_maker = crud.update_cheese_maker(db=db, cheese_maker=cheese_maker)
    return db_cheese_maker
