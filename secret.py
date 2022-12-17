from dotenv import load_dotenv   # dotenv 
import os                        # os 환경변수

load_dotenv()

mysql_connection_string = os.environ.get('MYSQL_CONNECTION_STRING')
crypto_key = os.environ.get('CRYPTO_KEY')
# crypto_key = int(os.environ.get('CRYPTO_KEY')).to_bytes(16, byteorder='big')
print(crypto_key)
jwt_key = int(os.environ.get('JWT_KEY')).to_bytes(32, byteorder='big')
jwt_alorithm = os.environ.get('JWT_ALGORITHM')
access_token_expire_minutes = int(os.environ.get('ACCESS_TOKEN_EXPIRE_MINUTES'))

mail_form_name = os.environ.get('MAIL_FORM_NAME')
mail_username = os.environ.get('MAIL_USERNAME')
mail_password = os.environ.get('MAIL_PASSWORD')
mail_from = os.environ.get('MAIL_FROM')
smtp_server = os.environ.get('SMTP_SERVER')

