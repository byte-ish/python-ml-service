"""
Custom exception handlers for the microservice.
"""
from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from app.logger import LOGGER

async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    """
    Handles HTTP exceptions.
    
    Args:
        request (Request): The incoming request object.
        exc (HTTPException): The HTTP exception raised.
    
    Returns:
        JSONResponse: Custom response for HTTP exceptions.
    """
    LOGGER.error("HTTPException: %s - Path: %s", exc.detail, request.url)
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )

async def global_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    """
    Handles all unhandled exceptions globally.
    
    Args:
        request (Request): The incoming request object.
        exc (Exception): The unhandled exception raised.
    
    Returns:
        JSONResponse: Custom response for unhandled exceptions.
    """
    LOGGER.critical("Unhandled Exception: %s - Path: %s", str(exc), request.url, exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "An internal server error occurred. Please try again later."},
    )