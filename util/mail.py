from secret import *
from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
import uuid
from urllib.parse import urlencode
import base64

conf = ConnectionConfig(
        MAIL_FROM_NAME=mail_form_name,
        MAIL_USERNAME=mail_username,
        MAIL_PASSWORD=mail_password,
        MAIL_FROM = mail_from,
        MAIL_PORT=465,
        MAIL_SERVER=smtp_server,
        MAIL_TLS=False,
        MAIL_SSL=True
    )

async def send_mail(route:str,params: dict,email:str):
    for key in params:
        params[key] = base64.b64encode(params[key])

    query = urlencode(params)
    
    html = f"""<a href="http://localhost:8000{route}?{query}">Verify</a>"""

    fm = FastMail(conf)
    message = MessageSchema(
        subject="Verify Mail to sign up VodkaMahjongCompetition",
        recipients=[email],  # List of recipients, as many as you can pass 
        body=html,
        subtype="html",
        multipart_subtype="alternative"
        )

    fm = FastMail(conf)
    res = await fm.send_message(message)