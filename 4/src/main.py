from fastapi import FastAPI, Cookie

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/language")
def lang(language: str = Cookie(default=None)):
    if language != None:
        return {"language": language}
    return {"message": "Language not set"}
# END
