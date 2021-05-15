import userservice.core.settings


def create_app():
    from fastapi import FastAPI

    app = FastAPI()

    from userservice.core.routes import router

    app.include_router(router)

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
