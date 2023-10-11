import dotenv
import os

dotenv.load_dotenv()

host = os.environ.get('host')
port = os.environ.get('port')
address = os.environ.get('homepage', default='127.0.0.1:8000')
expelled = os.environ.get('expelled', default='Noskov')

for var in (host, port, address, expelled):
    print(f'type: {type(var)}, value: {var}')
    