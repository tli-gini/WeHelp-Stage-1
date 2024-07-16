
# Home page
# @app.get("/")


# 註冊系統
# @app.post("/signup")
# if there is any repeating username in the member table ＝> "/error?message=帳號重複", Don't insert any data to the member table. 
# If no, insert input data to the member table. ＝> "/"

# 登入系統
# @app.post("/signin")


# 會員畫面   
# @app.get("/member")

# CreateMessage (Member Page 的留言板）
# @app.post("/createMessage")
# click the submit button to connect to the CreateMessage Endpoint for leaving a new message.

# 登出系統
# @app.get("/signout")
# In the Member Page, we should always verify the recorded user state in the back-end logic.
# If it does not pass the verification, force redirecting the user to the Home Page without showing any content on the member page.
# If this sign out link/button is clicked, we have to clear recorded member data in the user state and redirect to the Home Page.

# Error Page
# @app.get("/error")

# 註冊系統註冊後沒有跳回首頁，Alice 登出後沒有清除 user state
# 密碼要隱藏

# request header / body