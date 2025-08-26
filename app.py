
from fastapi import FastAPI


app = FastAPI()

#@app.get("/")
#async def root():
#    return {"Docker": "The World of Container"
#            }


@app.get("/users/{user_id}")
async def get_userID(user_id: int):
    return {"user_id": user_id, "NAME": "BANALA"}

if __name__ == "__app__":
    import unicorn
    unicorn.run(app, host="127.0.0.1", port=8000)