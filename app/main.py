from fastapi import FastAPI

from app import routers

app = FastAPI()
app.include_router(routers.api.v1.level.router, prefix="/api/v1/levels", tags=["Levels"])
app.include_router(routers.api.v1.token.router, prefix="/api/v1/token", tags=["Token"])
app.include_router(routers.api.v1.user.router, prefix="/api/v1/user", tags=["User"])
