from dependencies import (
    Annotated,
    APIRouter,
    Depends,
    HTTPException,
    status,
    List,
    Session,
    get_db,
    oauth2_scheme,
)

from src import schemas, crud

router = APIRouter()
# Payment


@router.get("/payments/", response_model=List[schemas.Payment], tags=["payments"])
def read_payments(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    payments = crud.get_payments(db, skip=skip, limit=limit)
    return payments


@router.get("/payment/{payment_id}", response_model=schemas.Payment, tags=["payments"])
def read_payment(
    token: Annotated[str, Depends(oauth2_scheme)],
    payment_id: int,
    db: Session = Depends(get_db),
):
    db_payment = crud.get_payment(db, payment_id=payment_id)
    if db_payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return db_payment


@router.post("/payment/", response_model=schemas.Payment, tags=["payments"])
def create_payment(
    token: Annotated[str, Depends(oauth2_scheme)],
    payment: schemas.PaymentCreate,
    db: Session = Depends(get_db),
):
    return crud.create_payment(db=db, payment=payment)
