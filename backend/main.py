from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import sort, quickselect, median
from config import CORS_SETTINGS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_SETTINGS["allow_origins"],
    allow_credentials=CORS_SETTINGS["allow_credentials"],
    allow_methods=CORS_SETTINGS["allow_methods"],
    allow_headers=CORS_SETTINGS["allow_headers"],
)

app.include_router(sort.router)
app.include_router(quickselect.router)
app.include_router(median.router)