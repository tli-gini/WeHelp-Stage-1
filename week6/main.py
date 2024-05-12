from fastapi import FastAPI, Request, Form
from fastapi.responses import  JSONResponse, RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates
from database import connect_db
from user import create_user, get_user, login_user, create_msg, get_msg
from pydantic import BaseModel

import uvicorn

app = FastAPI()

conn = connect_db()
cursor = conn.cursor()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

class MessageData(BaseModel):
    name: str
    message: str
    

app.add_middleware(SessionMiddleware, secret_key="Xk9*Lw2$9x!zQm3#pF8vB7yC1eJ6tH0s")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"], 
)


templates = Jinja2Templates(directory="templates")

# Home page
@app.get("/")
def index(request: Request):
    request.session["SIGNED-IN"] = False
    return templates.TemplateResponse("index.html", {"request": request}) 

@app.post("/signup")
async def signup(request: Request,name:str = Form(None), username: str = Form(None), password: str = Form(None)):
    if not name or not username or not password:
        return RedirectResponse(url="/error?message=請輸入註冊姓名和帳號密碼", status_code=303)
    elif username and password:
        user = get_user(username)
        if user:    
            return RedirectResponse(url="/error?message=此帳號已重複", status_code=303) 
        else:
            user = create_user(name, username, password)
    
        return RedirectResponse(url="/?signup_success=true", status_code=303)
@app.post("/signin")
async def signin(request: Request, username: str = Form(None), password: str = Form(None)):
    if not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號密碼", status_code=303)
   
    name, valid = login_user(username, password)
    
    if not valid:
        return RedirectResponse(url="/error?message=帳號或密碼輸入錯誤", status_code=303)
    else:
        request.session["SIGNED-IN"] = True
        request.session["name"] = name
        request.session['username'] = username
        return RedirectResponse(url="/member", status_code=303)
    
    
@app.get("/member")
async def member_name(request: Request, name:str=Form(None)):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    name = request.session.get("name")
    if not name:
        return RedirectResponse(url="/error?message=用戶未登入", status_code=303)
    else:
        messages = get_msg() 
        return templates.TemplateResponse("member.html", {"request": request, "name": name, "messages": messages})

@app.get("/signout")
async def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/", status_code=303)

@app.post("/createMessage")
async def create_message(request: Request,  message: str = Form(...)):
    if not request.session.get("SIGNED-IN"):
        return JSONResponse(status_code=403, content={"message": "User not signed in"})
    username = request.session.get("username")
    
    name = request.session.get("name")
    print("Received message from:", username, "Message:", message)

    result = create_msg(username, message)
    
    if result:
        messages = get_msg()  # Refresh messages to include the new one
        return templates.TemplateResponse("member.html", {"request": request, "name": name, "messages": messages})
    else:
        
        return templates.TemplateResponse("error.html", {"request": request, "message": "fail to create message"})
    
# @app.get("/getMessage")
# async def get_message(request: Request):
#     if not request.session.get("SIGNED-IN"):    
#         return JSONResponse(status_code=403, content={"message": "User not signed in"})   
#     else:
#         messages = get_msg()
#         return templates.TemplateResponse(status_code=200, content={"messages": messages})
  
 

@app.get("/error")
def error(request: Request, message: str = ""):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})




if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
   
   