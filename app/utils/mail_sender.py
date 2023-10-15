import app.config.constants as config
from app.config.mail_config import mail_config
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from app.model.email import Email


class MailSender:

    async def send_verification_email(self, email: Email):
        message = MessageSchema(
            subject="Registration in Transportation App",
            recipients=email.model_dump().get("email"),
            template_body=email.model_dump().get("body"),
            subtype=MessageType.html
        )

        mail_client = FastMail(mail_config)
        await mail_client.send_message(message, template_name="user_verification_template.html")
        
    async def send_selected_route_data_email(self, email: Email):
        message = MessageSchema(
            subject="Your confirmation of route selection",
            recipients=email.model_dump().get("email"),
            template_body=email.model_dump().get("body"),
            subtype=MessageType.html
        )
        
        mail_client = FastMail(mail_config)
        await mail_client.send_message(message, template_name="select_route_data_template.html")

