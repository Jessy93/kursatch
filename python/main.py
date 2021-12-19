from typing import Optional

from fastapi import FastAPI, File, UploadFile
import shutil
import pysftp
from aes.aes import AESCrypt

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/models/upload")
async def upload(file: UploadFile = File(...)):
    print(file.filename)
    path = "media/"+file.filename

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        encryted_path = AESCrypt().encrypt(path, '000')
        with pysftp.Connection('192.168.1.6', username='macbook', password='Jessy93') as sftp:
            print("connected")
            with sftp.cd("/Users/macbook/Desktop/media-users/"):
                print("ready to upload")
                sftp.put(encryted_path)
                print("file successfully upload")
    return {"filename": file.filename}
