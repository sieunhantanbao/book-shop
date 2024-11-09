from fastapi import UploadFile
import os
from werkzeug.utils import secure_filename
import uuid
from app.database import redis_client

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in os.environ['ALLOWED_EXTENSIONS']
           
def upload_file(uploadfile: UploadFile):
    filename = secure_filename(uploadfile.filename)
    file_name = f'{uuid.uuid4()}_{filename}'
    file_path = os.path.join(ROOT_DIR, os.environ['UPLOAD_FOLDER'], file_name)
    with open(file_path, "wb") as buffer:
            buffer.write(uploadfile.file.read())
    return file_name

def remove_file(file_name: str):
    file_path = os.path.join(ROOT_DIR, os.environ['UPLOAD_FOLDER'], file_name)
    if os.path.isfile(file_path):
        os.remove(file_path)

def clear_redis_cache(cache_keys: list):
    try:
        for key in cache_keys:
            if redis_client.exists(key):
                redis_client.delete(key)
    except Exception as e:
        print(e)

def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))
        return True
    except ValueError:
        return False

        