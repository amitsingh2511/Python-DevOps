from fastapi import FastAPI, Request,HTTPException,Body
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
templates = Jinja2Templates(directory="templates")

origins = [
    "http://localhost",
    "http://127.0.0.1:8000/submit/"
    "http://127.0.0.1:8000",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class JSONInput(BaseModel):
    json_data: str


json_data = None
@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.get("/")
async def read_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/submit/")
async def submit_json(json_input: dict = Body(...)):
    global json_data
    print("amit")
    json_data = json_input
    return json_data


@app.get("/api/")
async def get_json_response():
    global json_data
    return json_data
