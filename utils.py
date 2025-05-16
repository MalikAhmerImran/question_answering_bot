from dotenv import dotenv_values
from fastapi_mail import FastMail,MessageSchema,ConnectionConfig
from models import User
from auth import create_token
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

    token=create_token(token=token_data)

    template = f"http://localhost:8000/user/verification/?token={token}"

    message=MessageSchema(
        subject="Account Verification",
        recipients=[email],
        body=template,
        subtype="plain"
    )

    fn=FastMail(conf)
    await fn.send_message(message=message)


