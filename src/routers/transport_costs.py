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


@router.post(
    "/transport_cost/", response_model=schemas.TransportCost, tags=["transport costs"]
)
def create_transport_cost(
    token: Annotated[str, Depends(oauth2_scheme)],
    transport_cost: schemas.TransportCostCreate,
    db: Session = Depends(get_db),
):
    return crud.create_transport_cost(db=db, transport_cost=transport_cost)


@router.get(
    "/transport_cost/{transport_cost_id}",
    response_model=schemas.TransportCost,
    tags=["transport costs"],
)
def read_transport_cost(
    token: Annotated[str, Depends(oauth2_scheme)],
    transport_cost_id: int,
    db: Session = Depends(get_db),
):
    db_transport_cost = crud.get_transport_cost(db, transport_cost_id=transport_cost_id)
    if db_transport_cost is None:
        raise HTTPException(status_code=404, detail="Transport Cost not found")
    return db_transport_cost


@router.get(
    "/transport_costs/",
    response_model=List[schemas.TransportCost],
    tags=["transport costs"],
)
def read_transport_costs(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    transport_costs = crud.get_transport_costs(db, skip=skip, limit=limit)
    return transport_costs
