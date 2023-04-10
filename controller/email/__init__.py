from fastapi_mail import FastMail, MessageSchema,ConnectionConfig
from env import appConfig as mailConfig

if mailConfig.CONNECT_MAIL :
  conf = ConnectionConfig(
    MAIL_USERNAME = mailConfig.MAIL_USERNAME,
    MAIL_PASSWORD = mailConfig.MAIL_PASSWORD,
    MAIL_FROM = mailConfig.MAIL_FROM,
    MAIL_PORT = mailConfig.MAIL_PORT, #Encrypted SMTP port
    MAIL_SERVER = mailConfig.MAIL_SERVER,
    MAIL_TLS = True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True)


async def sendEmail(email,subject,message):
        message = MessageSchema(
        subject=subject,
        recipients=[email],
        html=message,
        subtype="html"
        )
        fm = FastMail(conf)
        await fm.send_message(message)
        return True