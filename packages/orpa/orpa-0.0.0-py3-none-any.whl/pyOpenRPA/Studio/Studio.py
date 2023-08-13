import argparse

parser = argparse.ArgumentParser(description='pyOpenRPA (ORPA) CLI')
parser.add_argument('file', help='Путь к файлу конфигурации')
parser.add_argument('--mode', choices=['app', 'web'], default="app", help='Режим запуска: app - запуск в качестве приложения, web - запуск в качестве веб сервера')
args = parser.parse_args()
from ..Utils import CrossOS
if CrossOS.IS_WINDOWS_BOOL:
    import win32gui
    import win32con
    # Получение дескриптора окна консоли
    hwnd = win32gui.GetForegroundWindow()

from http.server import BaseHTTPRequestHandler
import json
import os
import sys
import traceback
if args.mode=="app": 
    os.environ["PYOPENRPA_NODISP"]="TRUE"
from . import RobotConnector
from . import JSONNormalize
from ..Robot import Window
from ..Tools import Usage
print(f"ЧЕРЕЗ НЕСКОЛЬКО СЕКУНД ОКТРОЕТСЯ ИНТЕРФЕЙС СТУДИИ PYOPENRPA | ORPA")
import importlib
import logging
import datetime
from PIL import Image
import pytesseract

from fastapi import FastAPI, Form, Request, HTTPException, Depends, Header, Response, Body
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import io
import importlib.util
from starlette.responses import StreamingResponse
from typing import Union
import threading
import pickle

from ..Robot import UIWeb
from ..Robot import GPT
import time
import requests
lRepoPathStr = CrossOS.PathJoinList(CrossOS.PathSplitList(__file__)[:-4])
lTesseractExeStr = None
if CrossOS.IS_WINDOWS_BOOL:
    lTesseractExeStr = os.path.join(lRepoPathStr, "Resources", "WTesseract64-400", "tesseract.exe")
else:
    lTesseractExeStr = "tesseract"
pytesseract.pytesseract.tesseract_cmd = lTesseractExeStr #old 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
lPackagePathStr = CrossOS.PathJoinList(CrossOS.PathSplitList(__file__)[:-2])
lResourcePathStr = os.path.join(lPackagePathStr, "Resources")
#Единый глобальный словарь (За основу взять из Settings.py)
global gSettingsDict
#Call Settings function from argv[1] file
################################################
lSubmoduleFunctionName = "Settings"
lFileFullPath = args.file
lModuleName = (lFileFullPath.split("\\")[-1])[0:-3]
lTechSpecification = importlib.util.spec_from_file_location(lModuleName, lFileFullPath)
lTechModuleFromSpec = importlib.util.module_from_spec(lTechSpecification)
lTechSpecificationModuleLoader = lTechSpecification.loader.exec_module(lTechModuleFromSpec)
gSettingsDict = None
if lSubmoduleFunctionName in dir(lTechModuleFromSpec):
    # Run SettingUpdate function in submodule
    gSettingsDict = getattr(lTechModuleFromSpec, lSubmoduleFunctionName)()
sys.modules["config"]=lTechModuleFromSpec
############################################ # # # # #
gS = gSettingsDict
# INIT LOGGER #
#Создать файл логирования
# add filemode="w" to overwrite
if not os.path.exists(gS["LoggerPathStr"]):
    os.makedirs(gS["LoggerPathStr"])
##########################
#Подготовка логгера Robot
#########################
gLogger=logging.getLogger("Studio")
gLogger.setLevel(gSettingsDict.get("LoggerLevel", logging.INFO))
# create the logging file handler
gPathStr = os.path.join(gS["LoggerPathStr"], datetime.datetime.now().strftime(gS["LoggerFileFormatStr"])+"."+gS["LoggerExtStr"])
gLoggerFH = logging.FileHandler(gPathStr)
gLoggerFormatter = logging.Formatter(gS["LoggerRowFormatStr"])
gLoggerFH.setFormatter(gLoggerFormatter)
# add handler to logger object
gLogger.addHandler(gLoggerFH)
############################################

import config

#ORPA LAB проверка пути
config.orpa_lab_path_str = os.path.abspath("project")
if os.path.exists("OrpaLabPath.json"):
    with open("OrpaLabPath.json", "r", encoding="utf8") as f:
        location_str = f.read()
        if os.path.exists(location_str):
            config.orpa_lab_path_str = location_str

RobotConnector.mGlobalDict = gSettingsDict
#Init the robot
RobotConnector.UIDesktop.Utils.ProcessBitness.SettingsInit(gSettingsDict["ProcessBitness"])

from pyOpenRPA.Utils.Render import Render
from pyOpenRPA.Tools import CrossOS # https://schedule.readthedocs.io/en/stable/examples.html
lFileStr = CrossOS.PathJoinList(CrossOS.PathSplitList(__file__)[:-2] + ["Resources","Web","orpa","std.xhtml"])
gRender = Render(inTemplatePathStr=lFileStr,inTemplateRefreshBool=True)
from pyOpenRPA import __version__


import time
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import json
import os
import base64
from pyOpenRPA.Tools import CrossOS
import subprocess
import sys
import pyOpenRPA
import requests
gProgramDataPathStr=""
if CrossOS.IS_WINDOWS_BOOL: gProgramDataPathStr = "C:\\ProgramData"
if CrossOS.IS_LINUX_BOOL: gProgramDataPathStr = os.path.expanduser("~/.config")
gProgramDataPORPathStr = os.path.join(gProgramDataPathStr, "pyOpenRPA")

if not os.path.exists(gProgramDataPORPathStr): os.makedirs(gProgramDataPORPathStr, exist_ok=True)
DEFINE = None
# ПАКЕТ ДЛЯ ВСТАВКИ В МОДУЛИ
def cert_validate(in_cert_path_str = "orpa.key", in_version_str="1.4.0"):
    l_data = cert_load(in_cert_path_str = in_cert_path_str)
    result = False
    if l_data != None:
      required_fields = ["pc_str", "ver_str", "time_from_float", "time_to_float", "is_ee_bool", "is_online_bool"]
      if all(field in l_data for field in required_fields):
          current_time = time.time()
          if current_time>=l_data["time_from_float"] and current_time<=l_data["time_to_float"] and l_data["ver_str"]==in_version_str and guid()==l_data["pc_str"]:
            result = True
    return result

def cert_load(in_cert_path_str = "orpa.key"):
    log = b"LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBd1Q0a3ZzcWxtM2xSRFZibyt2SVdWQkk2MkNENXNXZDVQSjF6V3lHRlBMTzVNSlEwCitxOXMzK0VYWGd1NWEvODBNZnJlaGlka1JDQThtbWhtbW51b1BWeERUb3ZvbUhhdWoxVDdrYVRUYXFwd3pHV0MKY29DeHdKaVd2MUMxQWU0T1VDaWNZZ05YRXBLVlA4RmpmZzAxQTI1a3FTVFVZWlRXV01CNlZGL3ZDS29oUXNNRApZVXpHcWo4TWtoTHZYWTl4UmdEOXIyOVNXdWU4Z3ZYTDFOaXdacU1pUVZxRGpVQS9IVzk4MHV4MnBxdGhGRVFNClNKTXdnZmROcWZVak1ZVVlCalg1UDRkT0tCT2RVWEU0K2pBYlpOQUVaU0FaN0JTNkRQT3hpeC9UODdyVnFHYjIKM2FlK0prOXhBS2pZeWFrOEFxY3hScTlmSThCbFZBOUpsdG1WM1FJREFRQUJBb0lCQUNKb1F6aXBjbVZGYTVZWgpkSEJDTEpHWmtWcXNQR2xIQ0VJdnNydDJNM2dFZENQZkw3TzNDb2F1V0cvSlhLR0xGaXNVQlEwVDlIbGcyQW1TCkx6cXdhOXRKRXo3b0VHa2RNS1dhdHhST3Fjb2pRT1JUNnE4aWxRTzY1NVIyOVZPN3BGYkhkRmpMU1hTb0h1VDAKTlJmYm1DWGRRUlVRMXJQdFFXRWFIRzNyaXU4YXM5c0c5UUpib3ZtQ0gvTFRha2p3K3FPcy9ZS1lBRHU2VjRqbgp2bjVnQWpoVXR5RWRUWk8yZUxmSFFVcFBDSnhOL21RVk96eVlLcVB0Y3NFTWZNVmlaR2g0T3dnOFdnZC9vdWMrCnp3b1hUcGl5OVVHWWU2eFNhWkxienZYdjM0K2Nmb2pmZjR2QlNHVkg0bHdjS0cwVXB3ZmVXb0s3YURsck53L0cKV2lmMmFZRUNnWUVBd3JWazNJTHQ4YURHc2dlRm9IUE1uV2hrbWxDVkpuRHFlZHlsbnlLMUdOOUt5dzFUcHlFcwp0ODB3K0JrTmVRK3ZnRWNMZ3FMT0FybWJSYS9FL3lRWnlBUU1jSDdvYXFTU2g3V0VmVEQ0OXdjMUM4cmdaNUpwCnR1b3lxem9wNlh0cDVkV2YyRHE0WnpFdlZFdERiMCtoNjNzOWk5TWhScWVVdW80bWg1b1ZjVDBDZ1lFQS9oS2cKUzZjTXBMUVB2YlJGWHB6K0Y3VDlMVGFyODNOS0lJSUs4ekZJaTVDVkpOdXhhdDVKY2FIOHo2MXN3ajBoOHJPbQpIUU1XYnd3clcwK0YvWEdLODgzWXo4SE1BcVhOS0lBdHkvcVJ3VG0rNkVTbWoyMnlLcDU2aExXWWxDZEdOS2lBCmJMdGJMNVpwTW5NaGIxUTZFK2JLNzJIVW9QZlQvWXdTQU93RHdTRUNnWUJCYXZhWFMvb3IrNnVtZHZhRGdVU1gKQWxNQ3NkNWF5d2RNcUVDUkpmVVloVFU0NGFKZ2ZibnJpeXBQd1FNUTBKOVRod3NyK2cwalJ6OE8rODVCTnR6ZQpvZFdZR2x0Mk1STDJPNXRuQUlRMVl4dUVlY1pKcGh5VWt6MHc0RnJpa2s5ekpBSVBnVE1ob0puWlJXeER3c3FSCk5wZm9HYWlOZDVKMTEzckVocFY3dFFLQmdDSnVBYnpld1U3Y2U3bVlZVUltQWlUU1NQREVsTjZqdytyTjFKQUsKSUt1UkJ6VDhkSGxuOEFudkNxUlYrd1FEWnNOTjV2Zk5nRS9DRldvRlI4SUZqZS9sK0RpSEtZOCtTcVB2WXNWZQppanZtQ0dIUFU4Ymg5Wi9pNC9WeDZtQkJSamxDa0V5cnd2cWE1bHlJejRJWHB0c2xqbUNNSUZWRDREMWVxdDNuCkhjY2hBb0dBRmpCUFlnSkNRc3dwdmsxUi9SN2h0NS9nckVYRGd2eWdoRFRCeDd1anozZkdiZG1GblIyLytpSmgKa3NWZ3QwaUNLaCt0SjFtN1NPVUZGWVpzRllYS1pCcVBqMDVQUjR2Rk5xLzh5MVAyeGlJVzVIdy9MdG4zOXRIdwpDMFNXdGZJOXBmSjcyT3dUNUNvN1pRajdTYk1BSWIyT05EcGY5d1IwSlNYY1FqZHE1ZTQ9Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t"
    decipher = PKCS1_OAEP.new(RSA.importKey(base64.b64decode(log)))
    message = None
    try:
      with open(in_cert_path_str, "rb") as f: message = f.read()
      return json.loads(decipher.decrypt(message).decode())
    except: return None
    
def cert_find_load(in_folder_path_str=None):
  orpa_ver_str = pyOpenRPA.__version__
  if in_folder_path_str is None: in_folder_path_str = gProgramDataPORPathStr
  file_list = os.listdir(os.path.abspath(in_folder_path_str))
  for file_item in file_list:
     file_path_str = os.path.join(in_folder_path_str, file_item)
     if file_path_str.endswith(".key"):
        if cert_validate(file_path_str, orpa_ver_str):
           return cert_load(file_path_str)
  return {
        "pc_str": guid(), 
        "ver_str": orpa_ver_str, 
        "time_from_float": time.time(), 
        "time_to_float": time.time()+32140800, 
        "is_ee_bool": False, 
        "is_online_bool": True
    }

def is_online():
    try:
      ret = requests.get("https://pyopenrpa.ru", verify=True)
      if ret.status_code==200: return True
      else: return False
    except Exception as e:
      return False

def run(cmd):
  try:
    return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                     .stdout \
                     .strip()
  except:
    return None

def guid():
  if sys.platform == 'darwin':
    return run(
      "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'",
    )
  if sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'msys':
    return run('wmic csproduct get uuid').split('\n')[2] \
                                         .strip()
  if sys.platform.startswith('linux'):
    return run('cat /var/lib/dbus/machine-id') or \
           run('cat /etc/machine-id')
  if sys.platform.startswith('openbsd') or sys.platform.startswith('freebsd'):
    return run('cat /etc/hostid') or \
           run('kenv -q smbios.system.uuid')
DEFINE = cert_find_load()
DEFINE_ACCEPTED = False
if DEFINE["is_online_bool"]==True and is_online(): DEFINE_ACCEPTED=True
if DEFINE["is_online_bool"]==False: DEFINE_ACCEPTED=True

# HTTP Studio web server class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    mRequest = None
    mResponse = None
    def __init__(self, inRequest, inResponse):
        self.mRequest = inRequest
        self.mResponse = inResponse
        self.mResponseContentType = None
        self.mResponseContentCode = None
    #ResponseContentTypeFile
    def SendResponseContentTypeFile(self,inContentType,inFilePath):
        # Send response status code
        # Send headers
        self.mResponseContentCode = 200
        self.mResponseContentType=inContentType
        inFilePath = CrossOS.PathStr(inPathStr = inFilePath)
        lFileObject = open(inFilePath, "rb") 
        lData = lFileObject.read()
        #Закрыть файловый объект
        lFileObject.close()       
        # Write content as utf-8 data
        return lData
 
    # GET
    def do_GET(self, inBodyStr):
        lStudioFolder = CrossOS.PathJoinList(CrossOS.PathSplitList(__file__)[:-1])
        #Мост между файлом и http запросом (новый формат)
        if self.path == "/":
            # Пример использования
            global gRender
            global DEFINE
            lVersionStr = __version__
            if DEFINE["is_ee_bool"]==True: lVersionStr+=" EE"
            else: lVersionStr+=" CE"
            if DEFINE["is_online_bool"]==True: lVersionStr+=" ONLINE"
            lStr = gRender.Generate(inDataDict={"title":"pyOpenRPA (ORPA)", "subtitle":"Студия", "version":lVersionStr , "is_ee_bool": DEFINE["is_ee_bool"], "is_linux_bool": CrossOS.IS_LINUX_BOOL})
            self.mResponseContentCode = 200
            self.mResponseContentType="text/html"
            # Write content as utf-8 data
            return bytes(lStr, "utf8")
        #Мост между файлом и http запросом (новый формат)
        if self.path == '/favicon.ico':
            return self.SendResponseContentTypeFile('image/x-icon', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\favicon.ico"))
		#Мост между файлом и http запросом (новый формат)
        if self.path == '/pyOpenRPA_logo.png' or self.path == '/orpa/resources/Web/orpa/logo.png':
            return self.SendResponseContentTypeFile('image/png', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\logo.png"))
        if self.path == '/metadata.json': return self.SendResponseContentTypeFile('application/json', os.path.join(lStudioFolder, "..\\Resources\\Web\\orpa\\styleset\\metadata.json"))

    # POST
    def do_POST(self, inBodyStr):
        #Restart studio
        if self.path == '/RestartStudio':
            os.execl(sys.executable,os.path.abspath(__file__),*sys.argv)
            sys.exit(0)
        if self.path == '/GUIAction':
            self.mResponseContentCode = 200
            self.mResponseContentType='application/json'
            try:
                #Превращение массива байт в объект
                lInputObject=json.loads(inBodyStr)
                lRequestObject=lInputObject
                #Отправить команду роботу
                lResponseObject=RobotConnector.ActivityRun(lRequestObject)
                #Normalize JSON before send in response
                lResponseObject=JSONNormalize.JSONNormalizeDictList(lResponseObject)
                #Dump DICT LIST in JSON
                message = json.dumps(lResponseObject)
            except Exception as e:
                #Установить флаг ошибки
                lProcessResponse={"Result":None}
                lProcessResponse["ErrorFlag"]=True
                #Зафиксировать traceback
                lProcessResponse["ErrorTraceback"]=traceback.format_exc()
                #Зафиксировать Error message
                lProcessResponse["ErrorMessage"]=str(e)
                #lProcessResponse["ErrorArgs"]=str(e.args)
                message = json.dumps(lProcessResponse)     
            finally:
                # Write content as utf-8 data
                pass
            return bytes(message, "utf8")
        if self.path == '/GUIActionList':
            #Превращение массива байт в объект
            lInputObject=json.loads(inBodyStr)
            # Send response status code
            self.mResponseContentCode = 200
            self.mResponseContentType='application/json'
            # Send message back to client
            #{'functionName':'', 'argsArray':[]}
            lRequestObject=lInputObject
            lOutputObject=[]
            lResponseObject=RobotConnector.ActivityListRun(lRequestObject)
            #Сформировать текстовый ответ
            message = json.dumps(lResponseObject)
            # Write content as utf-8 data
            return (bytes(message, "utf8")) 

# ИНИЦИАЛИЗАЦИЯ FASTAPI!
app = FastAPI(
        title = "pyOpenRPA (ORPA) Studio",
        description = "Сервер студии pyOpenRPA (ORPA)",
        version = __version__,
        openapi_url="/orpa/fastapi/openapi.json", 
        docs_url = "/orpa/fastapi/docs",
        redoc_url = "/orpa/fastapi/redoc",
        swagger_ui_oauth2_redirect_url = "/orpa/fastapi/docs/oauth2-redirect",
    )    
from . import Processor

# RestartOrpaLab
@app.post(path="/api/orpa-lab-restart",response_class=JSONResponse,tags=["API"])
def pyOpenRPA_OrpaLabRestart(inRequest:Request):
    # Recieve the data
    global gLogger
    if CrossOS.IS_WINDOWS_BOOL:
        os.system(f"taskkill /F /IM orpa-lab.exe")
        os.system(f"taskkill /F /IM jupyter-lab.exe")
        os.system("start /B orpa-lab.exe -m jupyter lab --config=\"..\Resources\WConfigure\Orpa_lab_config.py")
    else:
        os.system(f"killall -9 orpa-lab -u $USER")
        os.system(f'orpa-lab -m jupyterlab --config="../Resources/LConfigure/Orpa_lab_config.py" &')
    gLogger.info(f"Компонент orpa-lab перезапущен")
    
# SetNewPath for orpa lab + restart orpa
@app.post(path="/api/orpa-lab-set-path",response_class=JSONResponse,tags=["API"])
def pyOpenRPA_OrpaLabSetPath(inRequest:Request):
    # Recieve the data
    global gLogger
    location_str = Window.DialogFolderSelect("","Выбрать папку проекта...")
    if os.path.exists(location_str):
        with open("OrpaLabPath.json", "w", encoding="utf8") as f:
            f.write(location_str)
            config.orpa_lab_path_str = location_str
    # Create new folder path
    gLogger.info(f"Компонент orpa-lab: новый путь установлен {location_str}")
    pyOpenRPA_OrpaLabRestart(inRequest)

# OpenFolder in Explorer
@app.post(path="/api/orpa-lab-open-path",response_class=JSONResponse,tags=["API"])
def pyOpenRPA_OrpaLabOpenPath(inRequest:Request):
    # Recieve the data
    global gLogger
    location_str = config.orpa_lab_path_str
    if CrossOS.IS_WINDOWS_BOOL:
        location_str = location_str.replace("/","\\")
        os.system(f"explorer.exe {location_str}")
    else:
        os.system(f"xdg-open {location_str}")

# Execute activity list
@app.post(path="/api/activity-list-execute",response_class=JSONResponse,tags=["API"])
def pyOpenRPA_ActivityListExecute(inRequest:Request, inBodyStr:str = Body(...)):
    # Recieve the data
    global gLogger
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    # If list - operator plus
    if type(lInput) is list:
        # Execution
        lResultList = Processor.ActivityListExecute(inActivityList = lInput)
        return lResultList
    else:
        # Execution
        lResultList = Processor.ActivityListExecute(inActivityList = [lInput])
        return lResultList[0]
    
#Путь к локации project (все img)
@app.post(path="/api/orpa-screen-img-tree-location-path",tags=["API"])
def get_path():
    return [os.path.abspath(config.orpa_lab_path_str)]

#Список файлов в дирректории для рендеринга img tree
@app.post(path="/api/orpa-screen-img-tree",tags=["API"])
def img_tree_render(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    lPath = lInput['Path']
    onlyfiles = []
    try:
        for path, directories, files in os.walk(lPath): 
            for f in files:
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp')):
                    onlyfiles.append(os.path.join(path, f).replace(lPath, "")[1:])
        return onlyfiles
    except FileNotFoundError as e: return {"ErrorHeader":str(e), "ErrorTraceback":traceback.format_exc()}
    

#Вывод предпросмотра на вкладке mouse&screen
gSnipScreenPath = ""
@app.post(path="/api/snipingtool-screenshot-render",tags=["API"])
def snipingtool_screen_path(inRequest:Request, inBodyStr:str = Body(...)):
    global gSnipScreenPath
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    gSnipScreenPath = CrossOS.PathStr(lInput['Path']) 
@app.get(path="/api/snipingtool-screenshot-render",tags=["API"])
def snipingtool_screen_render(inRequest:Request):
    global gSnipScreenPath
    return FileResponse(gSnipScreenPath)

#Удаление элементов отображенных в img tree
@app.post(path="/api/orpa-screen-img-tree-item-delete",tags=["API"])
def img_tree_item_delete(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    lInput['Path'] = CrossOS.PathStr(lInput['Path'])
    try: os.unlink(lInput['Path'])
    except Exception as e: return {"ErrorHeader":str(e), "ErrorTraceback":traceback.format_exc()}

#Переименование элементов отображенных в img tree
@app.post(path="/api/orpa-screen-img-tree-item-rename",tags=["API"])
def img_tree_item_rename(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    lInput['Path'] = CrossOS.PathStr(lInput['Path'])
    lInput['NewPath'] = CrossOS.PathStr(lInput['NewPath'])
    try: os.rename(lInput['Path'], lInput["NewPath"])
    except Exception as e: return {"ErrorHeader":str(e), "ErrorTraceback":traceback.format_exc()}

#Инициация тессеракта по изображению
@app.post(path="/api/orpa-screen-tesseract-run",tags=["API"])
def tesseract_result(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    lPath = lInput['Path']
    lPath = CrossOS.PathStr(lPath)
    try:
        lTesseractResult = [pytesseract.image_to_string(Image.open(lPath), lang='rus+eng')]
        return lTesseractResult
    except Exception as e: return {"ErrorHeader":str(e), "ErrorTraceback":traceback.format_exc()}


#Запрос на перевод текста через GPT
@app.post(path="/api/orpa-gpt-text-translate",tags=["API"])
def gpt_translate(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    lResult = GPT.Translate(inMessageStr=lInput['message_str'], inToLangStr=lInput['to_lang_str'], inProviderStr=lInput['provider_str'].lower(), inOrpaKeyStr=lInput['orpa_key_str'])
    if isinstance(lResult['response'], dict): 
        for key in lResult['response']:
            tmp = lResult['response'][key]
        lResult['response'] = tmp
    elif isinstance(lResult['response'], list): lResult['response'] = lResult['response'][0]
    return lResult

#Запрос на склонение текста через GPT
@app.post(path="/api/orpa-gpt-name-modify-ru",tags=["API"])
def gpt_name_modify_ru(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    lResult = GPT.NameModify(inNameStr=lInput['name_str'], inCaseStr=lInput['case_str'], inProviderStr=lInput['provider_str'].lower(), inOrpaKeyStr=lInput['orpa_key_str'])
    if isinstance(lResult['response'], dict): 
        for key in lResult['response']:
            tmp = lResult['response'][key]
        lResult['response'] = tmp
    elif isinstance(lResult['response'], list): lResult['response'] = lResult['response'][0]
    return lResult

#Запрос на анализ текста на эмоции
@app.post(path="/api/orpa-gpt-text-classify-emotions",tags=["API"])
def gpt_classify_emotions(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    lResult = GPT.ClassifyEmotions(inMessageStr=lInput['message_str'], inProviderStr=lInput['provider_str'].lower(), inOrpaKeyStr=lInput['orpa_key_str'])
    return lResult

#Запрос на извлечение компонентов из текста
@app.post(path="/api/orpa-gpt-text-extract",tags=["API"])
def gpt_extract(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    lResult = GPT.Extract(inMessageStr=lInput['message_str'], inExtractList=lInput['extract_list'], inProviderStr=lInput['provider_str'].lower(), inOrpaKeyStr=lInput['orpa_key_str'])
    tmp_str = ""
    if isinstance(lResult['response'], dict): 
        for key in lResult['response']:
            tmp_str += f'{key} - {lResult["response"][key]}\n'
        lResult['response'] = tmp_str
    elif isinstance(lResult['response'], list): 
        for item in lResult['response']:
            for key in item:
                tmp_str += f'{key} - {item[key]}\n'
        lResult['response'] = tmp_str
    return lResult

#Прямой запрос
@app.post(path="/api/orpa-gpt-send",tags=["API"])
def gpt_extract(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    lResult = GPT.Send(inMessageList=lInput['message_list'], inContextList=lInput['context_list'], inProviderStr=lInput['provider_str'].lower(), inOrpaKeyStr=lInput['orpa_key_str'])
    return lResult

#Дамп истории запросов в файл
@app.post(path="/api/orpa-gpt-history-dump",tags=["API"])
def gpt_dump_download(inRequest:Request, inBodyStr:str = Body(...)):
    lValueStr = inBodyStr
    # Превращение массива байт в объект
    lInput = json.loads(lValueStr)
    with open('GPT-HISTORY.pickle', 'wb') as f:
        pickle.dump(lInput, f)

#Выгрузка дампа истории запросов на сервер
@app.get(path="/api/orpa-gpt-history-load",tags=["API"])
def gpt_dump_upload():
    with open('GPT-HISTORY.pickle', 'rb') as f:
        lHistory = pickle.load(f)
    return lHistory 
    
@app.get(path="/api/helper-def-list/{inTokenStr}",response_class=JSONResponse,tags=["API"])
def pyOpenRPA_Debugging_HelperDefList(inRequest:Request, inBodyStr:str = Body("")):
    # Parse query
    lResultDict = {
        "success": True,
        "results": []
    }
    # Get the path
    lPathSplitList = inRequest.url.path.split('/')
    lQueryStr = None
    if "HelperDefList" != lPathSplitList[-1] and "" != lPathSplitList[-1]: lQueryStr = lPathSplitList[-1]
    if lQueryStr != "" and lQueryStr is not None:
        lDefList = Processor.ActivityItemHelperDefList(inDefQueryStr=lQueryStr)
        for lDefStr in lDefList:
            lResultDict["results"].append({"name": lDefStr, "value": lDefStr, "text": lDefStr})
    return lResultDict

@app.get(path="/api/helper-def-autofill/{inTokenStr}",response_class=JSONResponse,tags=["API"])
def pyOpenRPA_Debugging_HelperDefAutofill(inRequest:Request, inBodyStr:str = Body("")):
    # Parse query
    # Get the path
    lPathSplitList = inRequest.url.path.split('/')
    lQueryStr = None
    if "HelperDefAutofill" != lPathSplitList[-1] and "" != lPathSplitList[-1]: lQueryStr = lPathSplitList[-1]
    lResultDict = Processor.ActivityItemHelperDefAutofill(inDef = lQueryStr)
    return lResultDict

# MOUNT PORTAL RESOURCES
lURLStr = f"/orpa/resources/Web"
lPathStr = os.path.join(lResourcePathStr, "Web")
app.mount(lURLStr, StaticFiles(directory=CrossOS.PathStr(lPathStr)), name=lURLStr.replace('/',"_"))
# MOUNT PORTAL RESOURCES (BC)
lURLStr = f"/3rdParty"
lPathStr = os.path.join(lResourcePathStr, "Web")
app.mount(lURLStr, StaticFiles(directory=CrossOS.PathStr(lPathStr)), name=lURLStr.replace('/',"_"))

async def BackwardCompatibility(inRequest:Request, inResponse:Response):
    lHTTPRequest = testHTTPServer_RequestHandler(inRequest=inRequest, inResponse=inResponse)
    lHTTPRequest.path = inRequest.url.path
    inBodyStr = await inRequest.body()
    if inBodyStr == None: inBodyStr = ""
    else: inBodyStr = inBodyStr.decode("utf8")
    lHTTPRequest.body = inBodyStr
    lHTTPRequest.client_address = [inRequest.client.host]
    threading.current_thread().request = lHTTPRequest
    if inRequest.method=="GET":
        lResult = lHTTPRequest.do_GET(inBodyStr=inBodyStr)
    elif inRequest.method=="POST":
        lResult = lHTTPRequest.do_POST(inBodyStr=inBodyStr)
    return StreamingResponse(io.BytesIO(lResult), media_type=lHTTPRequest.mResponseContentType)

#WRAPPERS!
async def BackwardCompatibityWrapperNoAuth(inRequest:Request, inResponse:Response):
    return await BackwardCompatibility(inRequest = inRequest, inResponse = inResponse)
async def BackwardCompatibityBeginWrapperNoAuth(inBeginTokenStr, inRequest:Request, inResponse:Response):
    return await BackwardCompatibility(inRequest = inRequest, inResponse = inResponse)

import mimetypes
mimetypes.add_type("font/woff2",".woff2")
mimetypes.add_type("text/javascript",".js")
from typing import Union

def InitFastAPI():
    global app
    global gLogger
    global gS
    lL = gLogger
    gS["Server"]["Thread"] = app
    lURLEqualGETList=["/",'/favicon.ico', '/pyOpenRPA_logo.png', '/orpa/resources/Web/orpa/logo.png', '/metadata.json']
    lURLEqualPOSTList=['/GUIActionList','/GUIAction',  '/RestartStudio']

    for lURL in lURLEqualGETList:
        app.add_api_route(
            path=lURL,
            endpoint=BackwardCompatibityWrapperNoAuth,
            response_class=PlainTextResponse,
            methods=["GET"],
            tags=["BackwardCompatibility"]
        )
    for lURL in lURLEqualPOSTList:
        app.add_api_route(
            path=lURL,
            endpoint=BackwardCompatibityWrapperNoAuth,
            response_class=PlainTextResponse,
            methods=["POST"],
            tags=["BackwardCompatibility"]
        )
browser_portable = None

def OpenChromePortable():
    global browser_portable
    while True:
        try:
            response = requests.get(f"http://localhost:{lPort}",timeout=0.5)
            break
        except requests.exceptions.RequestException as e:
            time.sleep(0.5)
    global args
    if args.mode=="app": 
        # Запуск адреса в браузере
        browser_portable = UIWeb.BrowserChromeStart(inMaximizeBool=True,inModeStr="APP", inUrlStr=f"http://localhost:{lPort}")
        UIWeb.gBrowser=None
        UIWeb.gBrowserHandle=None
        # Скрытие окна консоли
        if CrossOS.IS_WINDOWS_BOOL:
            global hwnd
            win32gui.ShowWindow(hwnd, win32con.SW_HIDE)
        CheckChromePortable()
        #UIWeb.PageOpen(f"http://127.0.0.1:{lPort}")
    else:
        if CrossOS.IS_WINDOWS_BOOL:
            # Запуск адреса в браузере
            os.system(f"explorer http://localhost:{lPort}")
        else:
            pass
            #print("send cmd")
            #os.system(f"xdg-open http://localhost:{lPort}")
        

def CheckChromePortable():
    global browser_portable
    while True:
        if browser_portable!=None:
            js_str = "2+2"
            try:
                browser_portable.execute_script(js_str)
            except Exception as e:
                break
        # Ожидание
        time.sleep(3)

    if browser_portable!=None:
        # Закрытие браузера
        pid = os.getpid()
        browser_portable.quit()
        global gLogger
        lL = gLogger
        if lL: lL.info(f"Отключен интерфейс студии - выполнить отключение серверной части студии")
        os.system(f"taskkill /F /IM orpa-lab.exe")
        os.system(f"taskkill /F /IM jupyter-lab.exe")
        os.system(f"taskkill /F /pid {pid}")


def InitUvicorn(inHostStr=None, inPortInt=None):
    if inHostStr is None: inHostStr="0.0.0.0"
    if inPortInt is None: inPortInt=1024
    global app
    global gLogger
    lL = gLogger
    if lL: lL.info(f"Сервер инициализирован успешно (без поддержки SSL):: Слушает URL: {inHostStr}, Слушает порт: {inPortInt}")
    threading.Thread(target=OpenChromePortable).start()
    uvicorn.run(app, host=inHostStr, port=inPortInt,)



lURL = gS["Server"]["ListenURL"]
lPort = gS["Server"]["ListenPort"]

#Инициализация сервера (инициализация всех интерфейсов)
InitFastAPI()
InitUvicorn(inHostStr=lURL, inPortInt=lPort)

