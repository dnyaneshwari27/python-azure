from fastapi import FastAPI
app=FastAPI()

@app.get("/home")
def home():
    return{"success":True,"message":"hello world"}

@app.get("/about")
def  about():
    return{"name":"Dnyaneshwari","location":"mumbai"}
