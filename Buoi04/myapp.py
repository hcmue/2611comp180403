from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/") # GET host/
def read_root():
    return {"Hello": "World"}


# GET host/hello
# GET host/hello?name=David
@app.get("/hello") 
def say_hello(name: str = "Tom"):
    return f"Hello {name}"

# from pydantic import BaseModel
class Student(BaseModel):
    id: str
    name: str
    gpa: float
    is_active: bool | None = None

@app.post("/students")
def create(model: Student):
    return model


@app.get("/items/", response_class=HTMLResponse)
async def read_items():
    return """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """