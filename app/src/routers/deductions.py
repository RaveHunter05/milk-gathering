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

router = APIRouter(prefix="/deduction")


# Deductions
@router.get("", response_model=List[schemas.Deduction], tags=["deductions"])
def read_deductions(
    token: Annotated[str, Depends(oauth2_scheme)],
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
):
    deductions = crud.get_deductions(db, skip=skip, limit=limit)
    return deductions


@router.get(
    "/{deduction_id}", response_model=schemas.Deduction, tags=["deductions"]
)
def read_deduction(
    token: Annotated[str, Depends(oauth2_scheme)],
    deduction_id: int,
    db: Session = Depends(get_db),
):
    db_deduction = crud.get_deduction(db, deduction_id=deduction_id)
    if db_deduction is None:
        raise HTTPException(status_code=404, detail="Deduction not found")
    return db_deduction


@router.post("", response_model=schemas.Deduction, tags=["deductions"])
def create_deduction(
    token: Annotated[str, Depends(oauth2_scheme)],
    deduction: schemas.DeductionCreate,
    db: Session = Depends(get_db),
):
    return crud.create_deduction(db=db, deduction=deduction)


@router.put(
    "/{deduction_id}", response_model=schemas.Deduction, tags=["deductions"]
)
def update_deduction(
    token: Annotated[str, Depends(oauth2_scheme)],
    deduction_id: int,
    deduction: schemas.DeductionUpdate,
    db: Session = Depends(get_db),
):
    db_deduction = crud.update_deduction(db=db, deduction=deduction)
    return db_deduction
