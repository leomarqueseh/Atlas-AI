from fastapi import FastAPI


app = FastAPI(
    title="ATLAS AI",
    description="The Intelligence Behind Software Creation",
    version="0.1.0"
)


@app.get("/")
def home():

    return {
        "name": "ATLAS AI",
        "status": "online",
        "version": "0.1.0"
    }