from dependencies import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    get_db,
    Session,
    List,
    oauth2_scheme,
    Annotated,
)

from src import schemas, crud

router = APIRouter()


@router.post("/driver/", response_model=schemas.Driver, tags=["drivers"])
def create_driver(
    token: Annotated[str, Depends(oauth2_scheme)],
    driver: schemas.DriverCreate,
    db: Session = Depends(get_db),
):
    return crud.create_driver(db=db, driver=driver)


@router.get("/driver/{driver_id}", response_model=schemas.Driver, tags=["drivers"])
def read_driver(
    token: Annotated[str, Depends(oauth2_scheme)],
    driver_id: int,
    db: Session = Depends(get_db),
):
    db_driver = crud.get_driver(db, driver_id=driver_id)
    if db_driver is None:
        raise HTTPException(status_code=404, detail="Driver not found")
    return db_driver


@router.get("/drivers/", response_model=List[schemas.Driver], tags=["drivers"])
def read_drivers(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    drivers = crud.get_drivers(db, skip=skip, limit=limit)
    return drivers


@router.put("/driver/{driver_id}", response_model=schemas.Driver, tags=["drivers"])
def update_driver(
    token: Annotated[str, Depends(oauth2_scheme)],
    driver_id: int,
    driver: schemas.DriverUpdate,
    db: Session = Depends(get_db),
):
    db_driver = crud.update_driver(db=db, driver=driver)
    return db_driver
