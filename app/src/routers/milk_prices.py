from app.dependencies import (
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

from app.src import schemas, crud

router = APIRouter(prefix="/milk_price")


# Milk Price
@router.get(
    "", response_model=List[schemas.MilkPrice], tags=["milk prices"]
)
def read_milk_prices(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    milk_prices = crud.get_milk_prices(db, skip=skip, limit=limit)
    return milk_prices


@router.get(
    "/{milk_price_id}",
    response_model=schemas.MilkPrice,
    tags=["milk prices"],
)
def read_milk_price(
    token: Annotated[str, Depends(oauth2_scheme)],
    milk_price_id: int,
    db: Session = Depends(get_db),
):
    db_milk_price = crud.get_milk_price(db, milk_price_id=milk_price_id)
    if db_milk_price is None:
        raise HTTPException(status_code=404, detail="Milk Price not found")
    return db_milk_price


@router.post("", response_model=schemas.MilkPrice, tags=["milk prices"])
def create_milk_price(
    token: Annotated[str, Depends(oauth2_scheme)],
    milk_price: schemas.MilkPriceCreate,
    db: Session = Depends(get_db),
):
    return crud.create_milk_price(db=db, milk_price=milk_price)


@router.put(
    "/{milk_price_id}",
    response_model=schemas.MilkPrice,
    tags=["milk prices"],
)
def update_milk_price(
    token: Annotated[str, Depends(oauth2_scheme)],
    milk_price_id: int,
    milk_price: schemas.MilkPriceUpdate,
    db: Session = Depends(get_db),
):
    db_milk_price = crud.update_milk_price(db=db, milk_price=milk_price)
    return db_milk_price
