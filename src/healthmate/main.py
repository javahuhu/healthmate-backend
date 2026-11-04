
from fastapi import FastAPI

from healthmate.api.router import api_router
from healthmate.core.config import get_settings
from healthmate.core.exceptions import register_exception_handlers


def create_app() -> FastAPI:
    settings = get_settings()

    app = FastAPI(
        title=settings.APP_NAME,
        version=settings.APP_VERSION,
        description="HealthMate Enterprise REST API for iOS",
        debug=False,
    )

    # Register global exception handlers
    register_exception_handlers(app)

    # Register versioned API routes
    app.include_router(
        api_router,
        prefix=settings.API_V1_PREFIX,
    )

    # Application health check
    @app.get("/health", tags=["System"])
    async def health_check():
        return {
            "status": "healthy",
            "service": "healthmate-api",
        }

    return app


app = create_app()
