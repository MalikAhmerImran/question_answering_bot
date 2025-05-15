import jwt
from fastapi.exceptions import HTTPException
from fastapi_mail import FastMail,MessageSchema,ConnectionConfig
from dotenv import dotenv_values
from models import Email,User
from database import get_collection

config_credentials=dotenv_values(".env")
conf = ConnectionConfig(
    MAIL_USERNAME =config_credentials["EMAIL"],
    MAIL_PASSWORD = config_credentials["PASS"],
    MAIL_FROM = config_credentials["EMAIL"],
    MAIL_PORT = 465,
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_STARTTLS = False,
    MAIL_SSL_TLS=True,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)


async def send_email(email:str,instance:User):
    token_data={
        "username":email
    }

    token=jwt.encode(token_data,config_credentials["SECRET"],algorithm="HS256")

    template = f"http://localhost:8000/user/verification/?token={token}"

    message=MessageSchema(
        subject="Account Verification",
        recipients=[email],
        body=template,
        subtype="plain"
    )

    fn=FastMail(conf)
    await fn.send_message(message=message)


def verify_token(token:str):
    try:
     
        payload=jwt.decode(token,config_credentials["SECRET"], algorithms="HS256")
        user=get_collection(collection_name="users").find_one({"email":payload.get("username")})
    except Exception as e:
        print("JWT Decode Error:", e)
        raise HTTPException(status_code=404,detail="User does not exits or invalid token")
    return user
