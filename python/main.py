from typing import Optional

from fastapi import FastAPI, File, UploadFile
import shutil
import pysftp

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/models/upload")
async def upload(file: UploadFile = File(...)):
    print(file.filename)
    with open("media/"+file.filename, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
        with pysftp.Connection('192.168.1.6', username='macbook', password='Jessy93') as sftp:
          print("connected")
          with sftp.cd("/Users/macbook/Desktop/media-users/"): # temporarily chdir to public
              print("ready to upload")
              sftp.put("media/"+file.filename) # upload file to public/ on remote
              print("file successfully upload")
    return {"filename": file.filename}