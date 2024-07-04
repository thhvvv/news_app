import os
from app import create_app

if os.path.exists('.env'):
    print('Importing environment from .env file')
    from dotenv import load_dotenv
    load_dotenv()

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
