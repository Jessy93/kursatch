from typing import Optional

from fastapi import FastAPI, File, UploadFile
from fastapi.responses import FileResponse
import shutil
import pysftp
from aes.aes import AESCrypt
import os


app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/models/upload")
async def upload(file: UploadFile = File(...)):
    print(file.filename)
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


@app.post("/models/decrypt")
async def decrypt(file_url: str, file_pwd: str):
    file_localpath = 'media/{}'.format(file_url.split('/')[-1])
    print(file_url)
    print(file_localpath)
    with pysftp.Connection('192.168.1.6', username='macbook', password='Jessy93') as sftp:
        print("connected")
        sftp.get(file_url, file_localpath)
    if os.path.exists(file_localpath):
        print('file exists')
        # AESCrypt().decrypt(file_localpath, file_pwd)
        # return FileResponse(os.path.splitext(file_localpath)[0])
        return FileResponse(file_localpath)
    return {"filename doed not exists"}
