def create_app():
    from core.settings import create_logger

    create_logger()

    from fastapi import FastAPI

    app = FastAPI(root_path="/api")

    from core.routes import router

    app.include_router(router)

    return app


app = create_app()

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=5000)
