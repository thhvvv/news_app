import os
from app import create_app

if os.path.exists('.env'):
    print('Importing environment from .env file')
    from dotenv import load_dotenv
    load_dotenv()

config_name = os.getenv('FLASK_ENV') or 'default'

app = create_app(config_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
