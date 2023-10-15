from fastapi_mail import ConnectionConfig
import app.config.constants as config
from pathlib import Path


mail_config = ConnectionConfig(
        MAIL_USERNAME = config.MAILDEV_USERNAME,
        MAIL_PASSWORD = config.MAILDEV_PASSWORD,
        MAIL_FROM = config.MAILDEV_EMAIL_FROM,
        MAIL_PORT = config.MAILDEV_PORT,
        MAIL_SERVER = config.MAILDEV_HOST,
        MAIL_FROM_NAME = config.EMAIL_FROM_NAME,
        MAIL_STARTTLS = False,#config.EMAIL_STARTTLS,
        MAIL_SSL_TLS = config.EMAIL_SSL_TLS,
        USE_CREDENTIALS = False,#config.EMAIL_USE_CREDENTIALS,
        VALIDATE_CERTS = config.EMAIL_USE_CREDENTIALS,
        TEMPLATE_FOLDER = Path(__file__).parent.joinpath("templates")
    ) 