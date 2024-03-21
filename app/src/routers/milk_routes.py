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

router = APIRouter(prefix="/route")


@router.post("", response_model=schemas.MilkRoute, tags=["milk routes"])
def create_route(
    token: Annotated[str, Depends(oauth2_scheme)],
    route: schemas.MilkRouteCreate,
    db: Session = Depends(get_db),
):
    return crud.create_route(db=db, route=route)


@router.get("/{route_id}", response_model=schemas.MilkRoute, tags=["milk routes"])
def read_route(
    token: Annotated[str, Depends(oauth2_scheme)],
    route_id: int,
    db: Session = Depends(get_db),
):
    db_route = crud.get_route(db, route_id=route_id)
    if db_route is None:
        raise HTTPException(status_code=404, detail="Route not found")
    return db_route


@router.get("", response_model=List[schemas.MilkRoute], tags=["milk routes"])
def read_routes(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    routes = crud.get_routes(db, skip=skip, limit=limit)
    return routes


@router.put("/{route_id}", response_model=schemas.MilkRoute, tags=["milk routes"])
def update_route(
    token: Annotated[str, Depends(oauth2_scheme)],
    route_id: int,
    route: schemas.MilkRouteUpdate,
    db: Session = Depends(get_db),
):
    db_route = crud.update_route(db=db, item_id=route_id, route=route)
    return db_route


@router.delete(
    "/{route_id}", response_model=schemas.MilkRoute, tags=["milk routes"]
)
def delete_route(
    token: Annotated[str, Depends(oauth2_scheme)],
    route_id: int,
    db: Session = Depends(get_db),
):
    db_route = crud.delete_route(db=db, route_id=route_id)
    return db_route
