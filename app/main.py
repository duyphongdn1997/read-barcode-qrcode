"""Start Application."""
import os

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from starlette.middleware.base import BaseHTTPMiddleware, RequestResponseEndpoint
from starlette.requests import Request
from starlette.responses import Response

from app.api.routes.api import routes as api_router
from app.core.config import ALLOWED_HOSTS, API_PREFIX, DEBUG, VERSION
from app.logger.logger import configure_logging

logger = configure_logging(__name__)


class LoggingMiddleware(BaseHTTPMiddleware):
    """Logging All API request."""

    async def set_body(self, request: Request):
        """Set body."""
        receive_ = await request._receive()

        async def receive():
            """Receive body."""
            return receive_

        request._receive = receive

    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        """Dispatch."""
        await self.set_body(request)

        # Log the request
        logger.info("Received request: %s %s", request.method, request.url)
        logger.debug("Request headers: %s", request.headers)
        logger.debug("Request body: %s", await request.body())

        # Call the next middleware or route handler
        response = await call_next(request)

        # Log the response
        logger.info("Response status code: %s", response.status_code)
        logger.debug("Response headers: %s", response.headers)

        return response


def get_application() -> FastAPI:
    """Get application.

    Returns:
        FastAPI application.
    """
    application = FastAPI(debug=DEBUG, version=VERSION, docs_url=None)
    application.add_middleware(
        CORSMiddleware,
        allow_origins=ALLOWED_HOSTS or ["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    application.include_router(api_router, prefix=API_PREFIX)

    return application


app = get_application()
templates = Jinja2Templates(directory="app/frontend/templates")


@app.get("/")
def home(request: Request):
    """Returns html jinja2 template render for home page form"""

    return templates.TemplateResponse("index.html", {"request": request})


if __name__ == "__main__":
    HOST = os.getenv("APP_HOST")
    PORT = os.getenv("APP_PORT")
    uvicorn.run(app, host="0.0.0.0", port=5000)
