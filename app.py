from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging
from api.system import router as system_router
from api.predict import router as predict_router
from core.logging import setup_logging
from core.exceptions import add_exception_handlers

setup_logging()
logger = logging.getLogger("core")

app = FastAPI(title="Complaint-Severity API")

origins = [
    "http://127.0.0.1:5500",
    "http://localhost:5500",
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

add_exception_handlers(app)
logger.info("Application startup complete")

app.include_router(system_router)
app.include_router(predict_router)

if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
