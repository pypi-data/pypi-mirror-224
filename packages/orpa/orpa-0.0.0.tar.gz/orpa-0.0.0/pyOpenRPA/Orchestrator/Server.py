#     inRequest.OpenRPA = {}
#     inRequest.OpenRPA["AuthToken"] = None
#     inRequest.OpenRPA["Domain"] = None
#     inRequest.OpenRPA["User"] = None

# lResponseDict = {"Headers": {}, "SetCookies": {}, "Body": b"", "StatusCode": None}
# self.OpenRPAResponseDict = lResponseDict

#from http.client import HTTPException
import threading
import typing

from pyOpenRPA.Tools import CrossOS


from http import cookies
from . import ServerBC

# объявление import
from fastapi import FastAPI, Form, Request, HTTPException, Depends, Header, Response, Body
from fastapi.responses import PlainTextResponse, HTMLResponse, FileResponse, RedirectResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from starlette.datastructures import MutableHeaders
from pydantic import BaseModel
import uvicorn
import io
from starlette.responses import StreamingResponse
from typing import Union
from pyOpenRPA import __version__

import requests
import base64
import uuid
import datetime

# ИНИЦИАЛИЗАЦИЯ FASTAPI!
app = FastAPI(
        title = "pyOpenRPA (ORPA) Orchestrator",
        description = "Сервер оркестратора pyOpenRPA Orchestrator",
        version = __version__,
        openapi_url="/orpa/fastapi/openapi.json", 
        docs_url = "/orpa/fastapi/docs",
        redoc_url = "/orpa/fastapi/redoc",
        swagger_ui_oauth2_redirect_url = "/orpa/fastapi/docs/oauth2-redirect",
    )      



def IdentifyAuthorize(inRequest:Request, inResponse:Response,
    inCookiesStr: Union[str, None] = Header(default=None,alias="Cookie"), 
    inAuthorizationStr: Union[str, None] = Header(default="",alias="Authorization")):
    if __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("FlagCredentialsAsk", False)==True:
        lResult={"Domain": "", "User": ""}
        ######################################
        #Way 1 - try to find AuthToken
        lCookies = cookies.SimpleCookie(inCookiesStr) # inRequest.headers.get("Cookie", "")
        __Orchestrator__.GSettingsGet()
        lHeaderAuthorization = inAuthorizationStr.split(" ")
        if "AuthToken" in lCookies:
            lCookieAuthToken = lCookies.get("AuthToken", "").value
            if lCookieAuthToken:
                #Find AuthToken in GlobalDict
                if lCookieAuthToken in __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("AuthTokensDict", {}):
                    #Auth Token Has Been Founded
                    lResult["Domain"] = __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lCookieAuthToken]["Domain"]
                    lResult["User"] = __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lCookieAuthToken]["User"]
                    #Set auth token
                    mOpenRPA={}
                    mOpenRPA["AuthToken"] = lCookieAuthToken
                    mOpenRPA["Domain"] = lResult["Domain"]
                    mOpenRPA["User"] = lResult["User"]
                    mOpenRPA["IsSuperToken"] = __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("AuthTokensDict", {}).get(mOpenRPA["AuthToken"], {}).get("FlagDoNotExpire", False)
                    return lCookieAuthToken
        ######################################
        #Way 2 - try to logon
        if lHeaderAuthorization != ['']:
            if "AuthExc" in lCookies:
                raise AuthException()
            else:
                llHeaderAuthorizationDecodedUserPasswordList = base64.b64decode(lHeaderAuthorization[0]).decode("utf-8").split(":")
                lUser = llHeaderAuthorizationDecodedUserPasswordList[0]
                lPassword = llHeaderAuthorizationDecodedUserPasswordList[1]
                lDomain = ""
                if "\\" in lUser:
                    lDomain = lUser.split("\\")[0]
                    lUser = lUser.split("\\")[1]
                elif "@" in lUser:
                    lDomain = lUser.split("@")[1]
                    lUser = lUser.split("@")[0]
                lLogonBool = __Orchestrator__.OSCredentialsVerify(inUserStr=lUser, inPasswordStr=lPassword, inDomainStr=lDomain)
                #Check result
                if lLogonBool: # check user in gsettings rules
                    lLogonBool = False
                    gSettings = __Orchestrator__.GSettingsGet()  # Set the global settings
                    lUserTurple = (lDomain.upper(),lUser.upper()) # Create turple key for inGSettings["ServerDict"]["AccessUsers"]["RuleDomainUserDict"]
                    lUserTurple2 = ("",lUser.upper()) # Create turple key for inGSettings["ServerDict"]["AccessUsers"]["RuleDomainUserDict"]
                    if lUserTurple in gSettings.get("ServerDict",{}).get("AccessUsers", {}).get("RuleDomainUserDict", {}): lLogonBool = True
                    elif lUserTurple2 in gSettings.get("ServerDict",{}).get("AccessUsers", {}).get("RuleDomainUserDict", {}): lLogonBool = True
                    if lLogonBool: # If user exists in UAC Dict
                        lResult["Domain"] = lDomain
                        lResult["User"] = lUser
                        #Create token
                        lAuthToken=str(uuid.uuid1())
                        __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken] = {}
                        __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken]["Domain"] = lResult["Domain"]
                        __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken]["User"] = lResult["User"]
                        __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken]["FlagDoNotExpire"] = False
                        __Orchestrator__.GSettingsGet()["ServerDict"]["AccessUsers"]["AuthTokensDict"][lAuthToken]["TokenDatetime"] = datetime.datetime.now()
                        #Set-cookie
                        inResponse.set_cookie(key="AuthToken",value=lAuthToken)
                        mOpenRPA={}
                        mOpenRPA["AuthToken"] = lAuthToken
                        mOpenRPA["Domain"] = lResult["Domain"]
                        mOpenRPA["User"] = lResult["User"]
                        mOpenRPA["IsSuperToken"] = __Orchestrator__.GSettingsGet().get("ServerDict", {}).get("AccessUsers", {}).get("AuthTokensDict", {}).get(mOpenRPA["AuthToken"], {}).get("FlagDoNotExpire", False)
                        raise ReloadPage(token=lAuthToken)
                        #inRequest.OpenRPASetCookie = {}
                        #New engine of server
                        #inRequest.OpenRPAResponseDict["SetCookies"]["AuthToken"] = lAuthToken
                    else:
                        errorMsg = "Попытка авторизации не прошла успешно (для пользователя не заявлен доступ к оркестратору pyOpenRPA. Обратитесь в техническую поддержку)"
                        raise ErrorException(text=errorMsg)
                else:
                    errorMsg = "Попытка авторизации не прошла успешно (неверная пара логин / пароль)"
                    raise ErrorException(text=errorMsg)    
        else:
            raise AuthException()
    else: return None # Credentials are not required - return none


# Перевод встроенных fastapi функций на авторизацию
lRouteList =[]
for lItem in app.router.routes:
    lRouteList.append(lItem)
app.router.routes=[]
for lItem in lRouteList:
    app.add_api_route(
        path=lItem.path,
        endpoint=lItem.endpoint,
        methods=["GET"],
        dependencies=[Depends(IdentifyAuthorize)],
        tags=["FastAPI"]
    )

# объявление классов для дальнейшей обработки вызываемых исключений (обязательно должны наследоваться от EXception)
class ErrorException(Exception):
    def __init__(self, text :str, name: str="AuthExc"):
        self.name = name
        self.text = text

class AuthException(Exception):
    def __init__(self,  name: str="AuthTryWindowCreate"):
        self.name = name

class ReloadPage(Exception):
    def __init__(self, token :str, name: str="AuthToken"):
        self.name = name
        self.token = token


templates = Jinja2Templates(directory=CrossOS.PathJoinList(CrossOS.PathSplitList(__file__)[:-2] + ["Resources","Web","orpa"]))

# Обработчик ошибки авторизации (вывод информации о причинах неудачной авторизации)
@app.exception_handler(ErrorException)
async def unicorn_exception_handler(request: Request, exc:ErrorException):
    response = templates.TemplateResponse(status_code=401,name="badAuth.xhtml", context={"request":request, "errorMsg":exc.text, "title":"ОРКЕСТРАТОР PYOPENRPA", "subtitle":"АВТОРИЗАЦИЯ", "version":__version__})
    response.set_cookie(key="AuthExc",value="True")
    return response

# Обработчик успешной попытки авторизации (обновление страницы + установки куки-токена)
@app.exception_handler(ReloadPage)
async def unicorn_exception_handler_3(request: Request, exc:ReloadPage):
    response = HTMLResponse(content="", status_code=200)
    response.set_cookie(key=exc.name, value=exc.token)
    try:response.delete_cookie(key="AuthExc")
    except Exception:pass
    return response

# Обработчик попытки авторизации (отвечает за рендер формы для ввода пары логин / пароль)
@app.exception_handler(AuthException)
def unicorn_exception_handler_2(request: Request, exc: AuthException):
    response = templates.TemplateResponse(status_code=401,name="auth.xhtml", context={"request":request, "title":"ОРКЕСТРАТОР PYOPENRPA", "subtitle":"АВТОРИЗАЦИЯ", "version":__version__})
    try:response.delete_cookie(key="AuthExc")
    except Exception:pass
    return response



from . import ServerSettings  

async def BackwardCompatibility(inRequest:Request, inResponse:Response, inAuthTokenStr = None):
    lHTTPRequest = ServerBC.HTTPRequestOld(inRequest=inRequest, inResponse=inResponse, inAuthTokenStr=inAuthTokenStr)
    lHTTPRequest.path = inRequest.url.path
    #print(f"WEB START: {lHTTPRequest.path}")
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
    #print(f"WEB STOP: {lHTTPRequest.path}")
    if lHTTPRequest.OpenRPAResponseDict["Headers"]["Content-type"] != None:
        return StreamingResponse(io.BytesIO(lResult), media_type=lHTTPRequest.OpenRPAResponseDict["Headers"]["Content-type"])

#WRAPPERS!
async def BackwardCompatibityWrapperAuth(inRequest:Request, inResponse:Response,
    inAuthTokenStr:str=Depends(ServerSettings.IdentifyAuthorize)): # Old from v1.3.1 (updated to FastAPI)
    return await BackwardCompatibility(inRequest = inRequest, inResponse = inResponse, inAuthTokenStr=inAuthTokenStr)
async def BackwardCompatibityWrapperNoAuth(inRequest:Request, inResponse:Response): # Old from v1.3.1 (updated to FastAPI)
    return await BackwardCompatibility(inRequest = inRequest, inResponse = inResponse, inAuthTokenStr=None)
async def BackwardCompatibityBeginWrapperAuth(inBeginTokenStr, inRequest:Request, inResponse:Response,
    inAuthTokenStr:str=Depends(ServerSettings.IdentifyAuthorize)): # Old from v1.3.1 (updated to FastAPI)
    return await BackwardCompatibility(inRequest = inRequest, inResponse = inResponse, inAuthTokenStr=inAuthTokenStr)
async def BackwardCompatibityBeginWrapperNoAuth(inBeginTokenStr, inRequest:Request, inResponse:Response): # Old from v1.3.1 (updated to FastAPI)
    return await BackwardCompatibility(inRequest = inRequest, inResponse = inResponse, inAuthTokenStr=None)



from . import __Orchestrator__
import mimetypes
mimetypes.add_type("font/woff2",".woff2")
mimetypes.add_type("text/javascript",".js")
from typing import Union

def InitFastAPI():
    global app
    lL = __Orchestrator__.OrchestratorLoggerGet()
    __Orchestrator__.GSettingsGet()["ServerDict"]["ServerThread"] = app
    ServerSettings.SettingsUpdate()
    BCURLUpdate()

def BCURLUpdate(inExceptionFlagBool:bool=True):
    for lConnectItemDict in __Orchestrator__.GSettingsGet()["ServerDict"]["URLList"]:
        if "BCBool" not in lConnectItemDict:
            if "ResponseFolderPath" in lConnectItemDict:
                try:
                    app.mount(lConnectItemDict["URL"], 
                StaticFiles(directory=CrossOS.PathStr(lConnectItemDict["ResponseFolderPath"])), 
                name=lConnectItemDict["URL"].replace('/',"_"))
                except:
                    if inExceptionFlagBool: raise RuntimeError("Fatal error. Bad FolderPath")
                    else: pass
            else:
                if lConnectItemDict.get("MatchType") in ["BeginWith", "EqualCase", "Equal","EqualNoParam"]:
                    if lConnectItemDict.get("UACBool",True):
                        app.add_api_route(
                            path=lConnectItemDict["URL"],
                            endpoint=BackwardCompatibityWrapperAuth,
                            response_class=PlainTextResponse,
                            methods=[lConnectItemDict["Method"]],
                            tags=["BackwardCompatibility"]
                        )
                    else:
                        app.add_api_route(
                            path=lConnectItemDict["URL"],
                            endpoint=BackwardCompatibityWrapperNoAuth,
                            response_class=PlainTextResponse,
                            methods=[lConnectItemDict["Method"]],
                            tags=["BackwardCompatibility"]
                        )
                elif lConnectItemDict.get("MatchType") in ["BeginWith", "Contains"]:
                    lURLStr = lConnectItemDict["URL"]
                    if lURLStr[-1]!="/": lURLStr+="/"
                    lURLStr+="{inBeginTokenStr}"
                    if lConnectItemDict.get("UACBool",True):
                        app.add_api_route(
                            path=lURLStr,
                            endpoint=BackwardCompatibityBeginWrapperAuth,
                            response_class=PlainTextResponse,
                            methods=[lConnectItemDict["Method"]],
                            tags=["BackwardCompatibility"]
                        )
                    else:
                        app.add_api_route(
                            path=lURLStr,
                            endpoint=BackwardCompatibityBeginWrapperNoAuth,
                            response_class=PlainTextResponse,
                            methods=[lConnectItemDict["Method"]],
                            tags=["BackwardCompatibility"]
                        )
        lConnectItemDict["BCBool"]=True
                
def InitUvicorn(inHostStr=None, inPortInt=None, inSSLCertPathStr=None, inSSLKeyPathStr=None, inSSLPasswordStr=None):
    if inHostStr is None: inHostStr="0.0.0.0"
    if inPortInt is None: inPortInt=1024
    if inSSLCertPathStr != None: inSSLCertPathStr=CrossOS.PathStr(inSSLCertPathStr)
    if inSSLKeyPathStr != None: inSSLKeyPathStr=CrossOS.PathStr(inSSLKeyPathStr)
    global app
    lL = __Orchestrator__.OrchestratorLoggerGet()
    #uvicorn.run('pyOpenRPA.Orchestrator.Server:app', host='0.0.0.0', port=1024)
    uvicorn.run(app, host=inHostStr, port=inPortInt,ssl_keyfile=inSSLKeyPathStr,ssl_certfile=inSSLCertPathStr,ssl_keyfile_password=inSSLPasswordStr)
    if lL and inSSLKeyPathStr != None: lL.info(f"Сервер инициализирован успешно (с поддержкой SSL):: Слушает URL: {inHostStr}, Слушает порт: {inPortInt}, Путь к файлу сертификата (.pem, base64): {inSSLCertPathStr}")
    if lL and inSSLKeyPathStr == None: lL.info(f"Сервер инициализирован успешно (без поддержки SSL):: Слушает URL: {inHostStr}, Слушает порт: {inPortInt}")

