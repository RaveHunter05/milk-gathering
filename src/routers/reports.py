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

# Path: /route-report-by-date/

# Collected milk report by starting and end date
@router.get("/collected-milk-report-by-date/", response_model=List[schemas.CollectedMilk], tags=["reports"])
def collected_milk_report_by_date(
    start_date: Annotated[str, "Start date"],
    end_date: Annotated[str, "End date"],
    db: Session = Depends(get_db),
):
    return crud.get_collected_milk_report_by_date(db, start_date, end_date)

# Payments report by starting and end date
@router.get("/payments-report-by-date/", response_model=List[schemas.Payment], tags=["reports"])
def payments_report_by_date(
    start_date: Annotated[str, "Start date"],
    end_date: Annotated[str, "End date"],
    db: Session = Depends(get_db),
):
    return crud.get_payments_report_by_date(db, start_date, end_date)

# Collected report by producer and startting and end date
@router.get("/collected-report-by-producer-and-date/", response_model=List[schemas.CollectedMilkReport], tags=["reports"])
def collected_report_by_producer_and_date(
    start_date: Annotated[str, "Start date"],
    end_date: Annotated[str, "End date"],
    db: Session = Depends(get_db),
):
    return crud.get_collected_report_by_producer_and_date(db, start_date, end_date)
