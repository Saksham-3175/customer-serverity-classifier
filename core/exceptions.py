import logging
from fastapi import Request
from fastapi.responses import JSONResponse

logger = logging.getLogger("core")

def add_exception_handlers(app):
    @app.exception_handler(ValueError)
    async def value_error_handler(request: Request, exc: ValueError):
        logger.warning(f"ValueError at {request.url}: {exc}")
        return JSONResponse(status_code=400, content={"detail": str(exc)})

    @app.exception_handler(RuntimeError)
    async def runtime_error_handler(request: Request, exc: RuntimeError):
        logger.error(f"RuntimeError at {request.url}: {exc}", exc_info=True)
        return JSONResponse(status_code=500, content={"detail": str(exc)})

    @app.exception_handler(Exception)
    async def generic_exception_handler(request: Request, exc: Exception):
        logger.error(f"Unhandled Exception at {request.url}: {exc}", exc_info=True)
        return JSONResponse(status_code=500, content={"detail": str(exc)})
