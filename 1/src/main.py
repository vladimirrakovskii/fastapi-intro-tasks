from fastapi import FastAPI

app = FastAPI()

# BEGIN (write your solution here)
@app.get("/reverse/{text}")
def reverse_text(text):
    reversed_text = ''.join(reversed(text))
    return {"reversed": f"{reversed_text}"}
# END
