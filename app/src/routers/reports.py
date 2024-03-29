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

router = APIRouter(prefix="/reports")

# Path: /route-report-by-date/

# Collected milk report by starting and end date
@router.get("/collected-milk-report-by-date", response_model=List[schemas.CollectedMilk], tags=["reports"])
def collected_milk_report_by_date(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: Annotated[str, "Start date"],
    end_date: Annotated[str, "End date"],
    db: Session = Depends(get_db),
):
    return crud.get_collected_milk_report_by_date(db, start_date, end_date)

# Payments report by starting and end date
@router.get("/payments-report-by-producer-and-date", response_model=List[schemas.PaymentsByProducer], tags=["reports"])
def payments_report_by_date(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: Annotated[str, "Start date"],
    end_date: Annotated[str, "End date"],
    db: Session = Depends(get_db),
):
    return crud.get_payments_report_by_date(db, start_date, end_date)

# Collected milk by route, driver and date
@router.get("/collected-milk-by-route-driver-and-date", response_model=List[schemas.CollectedMilkReportByRouteAndDriver], tags=["reports"])
def get_collected_milk_by_route_driver_and_date(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: Annotated[str, "Start date"],
    end_date: Annotated[str, "End date"],
    db: Session = Depends(get_db),
):
    return crud.get_collected_milk_by_route_driver_and_date(db, start_date, end_date)

# Collected milk by route and date
@router.get("/collected-milk-by-route-and-date", response_model=List[schemas.CollectedMilkReportByRoute], tags=["reports"])
def get_collected_milk_by_route_and_date(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: Annotated[str, "Start date"],
    end_date: Annotated[str, "End date"],
    db: Session = Depends(get_db),
):
    return crud.get_collected_milk_by_route_and_date(db, start_date, end_date)



# Collected report by producer and startting and end date
@router.get("/collected-report-by-producer-and-date", response_model=List[schemas.CollectedMilkReport], tags=["reports"])
def collected_report_by_producer_and_date(
    token: Annotated[str, Depends(oauth2_scheme)],
    start_date: Annotated[str, "Start date"],
    end_date: Annotated[str, "End date"],
    db: Session = Depends(get_db),
):
    return crud.get_collected_report_by_producer_and_date(db, start_date, end_date)
