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

router = APIRouter(prefix="/producer")


@router.get("", response_model=List[schemas.Producer], tags=["producers"])
def read_producers(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    producers = crud.get_producers(db, skip=skip, limit=limit)
    return producers


@router.get(
    "/{producer_id}", response_model=schemas.Producer, tags=["producers"]
)
def read_producer(
    token: Annotated[str, Depends(oauth2_scheme)],
    producer_id: int,
    db: Session = Depends(get_db),
):
    db_producer = crud.get_producer(db, producer_id=producer_id)
    if db_producer is None:
        raise HTTPException(status_code=404, detail="Producer not found")
    return db_producer


@router.post("", response_model=schemas.Producer, tags=["producers"])
def create_producer(
    token: Annotated[str, Depends(oauth2_scheme)],
    producer: schemas.ProducerCreate,
    db: Session = Depends(get_db),
):
    return crud.create_producer(db=db, producer=producer)


@router.put(
    "/{producer_id}", response_model=schemas.Producer, tags=["producers"]
)
def update_producer(
    token: Annotated[str, Depends(oauth2_scheme)],
    producer_id: int,
    producer: schemas.ProducerUpdate,
    db: Session = Depends(get_db),
):
    db_producer = crud.update_producer(db=db, producer=producer)
    return db_producer
