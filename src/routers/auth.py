from dependencies import (
    APIRouter,
    Depends,
    HTTPException,
    status,
    get_db,
    Session,
    ACCESS_TOKEN_EXPIRE_MINUTES,
    Annotated,
    OAuth2PasswordRequestForm,
)

from src import schemas

from datetime import timedelta

from src.authentication import authenticate_user, create_access_token, create_user

router = APIRouter()


# Authentication
@router.post("/token", response_model=schemas.Token, tags=["auth"])
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    db: Session = Depends(get_db),
) -> schemas.Token:
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


# Create User
@router.post("/signup/", response_model=schemas.User, tags=["auth"])
def create_an_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return create_user(db=db, user=user)
