
from fastapi import FastAPI,File, UploadFile, HTTPException


app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    if len(file) < 1:
        raise HTTPException(
            status_code=422,
            detail="error"
        )
    return {"filename": file.filename}