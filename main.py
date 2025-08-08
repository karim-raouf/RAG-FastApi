from fastapi import FastAPI

app = FastAPI()

@app.get("/welcome")
def welcome_msg():
    return {
        "message" : "welcome boss!"
    }