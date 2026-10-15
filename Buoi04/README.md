# Buổi 04 (15/10/2026)

# FASTAPI

## Cài

```
pip install "fastapi[standard]"
```

## Demo

```
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
```

LAB:

- https://www.hcmue.io.vn/courses/web-technology/fastapi-01
- https://www.hcmue.io.vn/courses/web-technology/fastapi-02
- https://www.hcmue.io.vn/courses/web-technology/fastapi-03

Swagger: http://localhost:8000/docs
