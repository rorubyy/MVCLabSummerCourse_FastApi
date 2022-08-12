import os
import json
import random
import shutil
from urllib import response
from fastapi import FastAPI, HTTPException, UploadFile, Request
from fastapi.responses import JSONResponse
from typing import  Union
from pyquery import PyQuery
from pydantic import BaseModel
from uuid import uuid4 # Universally Unique Identifierfrom fastapi import FastAPI

# BaseModel
class StudentInfo(BaseModel):
    name:str
    gender:str

# define exception
class FileLoadFail(Exception):
    def __init__(self, name:str):
        self.name=name

app=FastAPI()

studentInfos = []
studentInfo_file='studentInfo.json'
upload_file = []

#locad local json file if exist
if os.path.exists(studentInfo_file):
    with open(studentInfo_file, "r") as f:
        studentInfos=json.load(f)


@app.get('/')
def read_root():
    return {"Hi, There are some student information"}

# get method
@app.get('/list-all-members')
def listAllMembers():
    return {'Student Information:' : studentInfos}

@app.get('/show-female-members')
def showFemaleMembers():
    femaleStudents=[]
    for s in studentInfos:
        if s['gender']=="female":
            femaleStudents.append(s)
    return {'Female Students:' : femaleStudents}

@app.get('/show-male-members')
def showMaleMembers():
    maleStudents=[]
    for s in studentInfos:
        if s['gender']=="male":
            maleStudents.append(s)
    return {'Male Students:' : maleStudents}

# post method
@app.post('/add-student', response_model=StudentInfo)
def addStudent(studentInfo: StudentInfo):
    studentInfo_dict = studentInfo.dict()
    studentInfo_dict.update()
    studentInfos.append(studentInfo_dict)
    #save a new student into local json file
    with open(studentInfo_file, "w") as f:
        json.dump(studentInfo_file, f, indent=2)
    return studentInfo_dict

@app.post('/upload-file')
def upload_file(file: Union[UploadFile, None] = None):
    if not file: 
        return {"Message" : "No file upload."}
    try:
        file_location = './' + file.filename
        with open(file_location, "wb") as f:
            shutil.copyfileobj(file.file, f)
            file.close()
        upload_file.append(file.filename)
        return {"Result" : f"Upload File {file.filename} Success!"}
    except:
        raise FileLoadFail(name=f'{file.filename}')

# exception handler
@app.exception_handler(FileLoadFail)
def not_found(request : Request, exc : FileLoadFail):
    return JSONResponse(
        status_code=499,
        content={
            'Message' : f'Sorry, seems like {exc.name} isnt been loead.'
        },
    )
