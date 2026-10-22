from fastapi import FastAPI, HTTPException, status, Depends
from sqlmodel import Field, Session, SQLModel, create_engine, select
import jwt
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, ValidationError
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from typing import Annotated
from datetime import datetime, timedelta, timezone

app = FastAPI()

@app.get("/")
def hello():
    return {"text": "Helloo"}

# Định nghĩa model ứng với table
class Loai(SQLModel, table=True):    
    MaLoai: int | None = Field(default=None, primary_key=True)
    TenLoai: str = Field(index=True)

class HangHoa(SQLModel, table=True):  
    MaHH: int | None = Field(default=None, primary_key=True)
    TenHH: str = Field(index=True)
    Hinh: str = Field()
    MaLoai: int | None =  Field(foreign_key="loai.MaLoai")

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str
    email: str | None = None
    full_name: str | None = None
    role: int = Field(default=None)
    is_active: bool | None = Field(default=True)

#  Khai báo tạo table (nếu chưa có) ở start_up
engine = create_engine("mysql+pymysql://root:@localhost/2611comp180403")
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]


# to get a string like this run:
# openssl rand -hex 32
SECRET_KEY = "ae02e1e6bcb98eb22a397e9ba7fc428384297b0d859a1b79c56f2192019561a7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None
    scopes: list[str] = []


pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="token",
    scopes={"me": "Read information about the current user.", "items": "Read items."},
)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)


@app.post("/users/", tags=["user"])
def create_user(model: User, session: SessionDep) -> User:
    model.password = get_password_hash(model.password)
    print('Sau mã hóa', model)
    session.add(model)
    session.commit()
    session.refresh(model)
    return model

def authenticate_user(session: SessionDep, username: str, password: str):
    users = session.exec(select(User)).all() # optimize
    # Check username
    user = None
    for u in users:
        if u.username == username:
            user = u
            break
    if not user:
        return False
    
    if not verify_password(password, user.password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


@app.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    session: SessionDep
) -> Token:

    user = authenticate_user(
        session, form_data.username, form_data.password
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={
            "username": user.username,
            "email": user.email
        },
        expires_delta=access_token_expires
    )

    return Token(access_token=access_token, token_type="bearer")