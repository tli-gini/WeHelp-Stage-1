from fastapi import FastAPI, Request, Form
from fastapi.responses import  RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from fastapi.templating import Jinja2Templates

app = FastAPI()

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

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


@app.post("/signin")
async def signin(request: Request, username: str = Form(None), password: str = Form(None)):
    if not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號密碼", status_code=303)
    elif username == "test" and password == "test":
        request.session["SIGNED-IN"] = True
        print(request.session["SIGNED-IN"])
        return RedirectResponse(url="/member", status_code=303)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼輸入錯誤", status_code=303)
    
@app.get("/member")
async def member(request: Request):
    if not request.session.get("SIGNED-IN"):
        return RedirectResponse(url="/", status_code=303)
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/signout")
async def signout(request: Request):
    request.session["SIGNED-IN"] = False
    return RedirectResponse(url="/", status_code=303)

@app.get("/error")
def error(request: Request, message: str = ""):
    return templates.TemplateResponse("error.html", {"request": request, "message": message})
