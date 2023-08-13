from selenium import *
from selenium import webdriver, common
from selenium.webdriver.common.by import By
from selenium.common.exceptions import JavascriptException
import os
import sys
import json
from pyOpenRPA.Tools import CrossOS
from pyOpenRPA.Robot import UIDesktop
if CrossOS.IS_WINDOWS_BOOL:
    import win32api
import time

# XPATH CSS CHEAT CHEET: https://devhints.io/xpath
# XPATH CSS CHEAT CHEET: https://devhints.io/css

UIO_WAIT_SEC_FLOAT = 60
UIO_WAIT_INTERVAL_SEC_FLOAT = 1.0

gBrowser:webdriver.Chrome = None
def BrowserChromeStart(inDriverExePathStr:str = None, inChromeExePathStr:str = None, inExtensionPathList:list = None, inProfilePathStr:str=None, inSaveAsPDFBool = False, inSavefileDefaultDirStr:str = None, inUrlStr:str = None, inModeStr: str = None, inMaximizeBool:bool = None, inDownloadAskBool=False) -> webdriver.Chrome:
    """L+,W+: Выполнить запуск браузера Chrome. Если вы скачали pyOpenRPA вместе с репозиторием, то будет использоваться встроенный браузер Google Chrome. Если установка pyOpenRPA производилась другим способом, то требуется указать расположение браузера Google Chrome и соответствующего WebDriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.BrowserClose()
		
    :param inDriverExePathStr: Путь до компонента webdriver.exe, по умолчанию None (путь до webdriver.exe, который расположен в репозитории pyOpenRPA)
    :type inDriverExePathStr: str, опционально
    :param inChromeExePathStr:Путь до компонента chrome.exe, по умолчанию None (путь до chrome.exe, который расположен в репозитории pyOpenRPA)
    :type inChromeExePathStr: str, опционально
    :param inExtensionPathList: Список путей, по которым располагаются расширения Chrome, по умолчанию None
    :type inExtensionPathList: list, опционально
    :param inProfilePathStr: Путь, по которому выполнить сохранения профиля Chrome (история, куки и т.д.), по умолчанию None (профиль не сохраняется)
    :type inProfilePathStr: str, опционально
    :param inSaveAsPDFBool: Флаг, который обеспечивает настройки окна печати вэб-страницы как "Сохранить как PDF", по умолчанию False (настройки по умолчанию)
    :type inSaveAsPDFBool: bool, опционально
    :param inSavefileDefaultDirStr: Путь, по которому выполнить сохранения файла (после работы с окном печать вэб-страницы браузера) (история, куки и т.д.), по умолчанию None (файл не сохраняется)
    :type inSavefileDefaultDirStr: str, опционально
    :param inUrlStr: Путь к странице, которую требуется открыть. По умолчанию адреса нет
    :type inUrlStr: str, опционально
    :param inModeStr: Формат запуска браузера. Доступные варианты: "NORMAL", "APP", "KIOSK". По умолчанию "NORMAL"
    :type inModeStr: str, опционально
    :param inMaximizeBool: True - развернуть на весь экран. False (по умолчанию) - не разворачивать.
    :type inMaximizeBool: bool, опционально
    :param inDownloadAskBool: True - Спрашивать папку для сохранения перед каждой загрузкой из браузера. False (по умолчанию) - не спрашивать.
    :type inDownloadAskBool: bool, опционально
    :return: Объект браузера Google Chrome
    :rtype: webdriver.Chrome
    """
    global gBrowser
    inDriverExePathStr = CrossOS.PathStr(inPathStr=inDriverExePathStr)
    inChromeExePathStr = CrossOS.PathStr(inPathStr=inChromeExePathStr)
    lExtensionPathList = []
    if inExtensionPathList is not None:
        for lItemStr in inExtensionPathList:
            lExtensionPathList.append(CrossOS.PathStr(inPathStr=lItemStr))
    inExtensionPathList = lExtensionPathList
    inChromeExePathStr = CrossOS.PathStr(inPathStr=inChromeExePathStr)
    inProfilePathStr = CrossOS.PathStr(inPathStr=inProfilePathStr)
    lResourcePathStr = os.path.abspath(os.path.join(sys.executable, "..","..", ".."))
    if CrossOS.IS_LINUX_BOOL: 
        if os.path.exists(os.path.join("..", 'Resources')): lResourcePathStr = os.path.abspath(os.path.join("..", 'Resources'))
        elif os.path.exists(os.path.join("..", "..", 'Resources')): lResourcePathStr = os.path.abspath(os.path.join("..", "..",'Resources'))
        elif os.path.exists(os.path.join("..", "..","..", 'Resources')): lResourcePathStr = os.path.abspath(os.path.join("..", "..",".." 'Resources'))
        elif os.path.exists('Resources'): lResourcePathStr = os.path.abspath('Resources')
    # Путь по умолчанию к портативному браузеру и драйверу (если скачивался репозиторий pyOpenRPA'
    if inDriverExePathStr == None: 
        if CrossOS.IS_WINDOWS_BOOL: inDriverExePathStr = os.path.join(lResourcePathStr, "SeleniumWebDrivers", "Chrome", "chromedriver_win32 v84.0.4147.30", "chromedriver.exe")
        elif CrossOS.IS_LINUX_BOOL: inDriverExePathStr = os.path.join(lResourcePathStr, "SeleniumWebDrivers", "Chrome", "chromedriver_lin64 v103.0.5060.53", "chromedriver")
    if inChromeExePathStr == None: 
        if CrossOS.IS_WINDOWS_BOOL: inChromeExePathStr = os.path.join(lResourcePathStr, "WChrome64-840414730", "App", "Chrome-bin", "chrome.exe")
        elif CrossOS.IS_LINUX_BOOL: inChromeExePathStr = os.path.join(lResourcePathStr, "LChrome64-10305060114", "data", "chrome")
    if inExtensionPathList == None: inExtensionPathList = []
    if inModeStr==None: inModeStr="NORMAL"
    if inMaximizeBool==None: inMaximizeBool=False
    # Установка настроек окна печати, если необходимо
    lWebDriverChromeOptionsInstance = webdriver.ChromeOptions()
    lWebDriverChromeOptionsInstance.add_experimental_option("excludeSwitches", ["enable-automation"])
    if inSaveAsPDFBool == True and inSavefileDefaultDirStr is not None:
        print_settings = {
        "recentDestinations": [{
            "id": "Save as PDF",
            "origin": "local",
            "account": "",
        }],
        "selectedDestinationId": "Save as PDF",
        "version": 2, # в chrome - это номер варинта "сохранить как PDF"
        "isHeaderFooterEnabled": False, # хедеры HTML на странице
        "isLandscapeEnabled": False # ориентация (True - альбомная)
        }
        prefs = {'printing.print_preview_sticky_settings.appState': json.dumps(print_settings),
                 "download.prompt_for_download": False,
                 "profile.default_content_setting_values.automatic_downloads": 1,
                 "download.default_directory": inSavefileDefaultDirStr,
                 "savefile.default_directory": inSavefileDefaultDirStr,
                 "download.directory_upgrade": True,
                 "safebrowsing.enabled": True}
        if inDownloadAskBool==True:
            prefs["download.prompt_for_download"]=True
        lWebDriverChromeOptionsInstance.add_experimental_option('prefs', prefs)
        lWebDriverChromeOptionsInstance.add_argument('--kiosk-printing')
    else:
        if inDownloadAskBool==True:
            prefs = {'download.prompt_for_download': True}
            lWebDriverChromeOptionsInstance.add_experimental_option('prefs', prefs)
    lWebDriverChromeOptionsInstance.add_argument("disable-infobars")
    # Set full path to exe of the chrome
    lWebDriverChromeOptionsInstance.binary_location = inChromeExePathStr
    #lWebDriverChromeOptionsInstance2 = webdriver.ChromeOptions()
    if inProfilePathStr is not None:
        inProfilePathStr = os.path.abspath(inProfilePathStr)
        lWebDriverChromeOptionsInstance.add_argument(f"user-data-dir={os.path.abspath(inProfilePathStr)}")
    # Add extensions
    for lExtensionItemFullPath in inExtensionPathList:
        lWebDriverChromeOptionsInstance.add_extension (os.path.abspath(lExtensionItemFullPath))
    
    if inModeStr.upper()=="APP" and inUrlStr!=None:
        lWebDriverChromeOptionsInstance.add_argument(f'--app={inUrlStr}')
    elif inModeStr.upper()=="KIOSK" and inUrlStr!=None:
        lWebDriverChromeOptionsInstance.add_argument(f'--kiosk {inUrlStr}')
    if inMaximizeBool==True:
        lWebDriverChromeOptionsInstance.add_argument('--start-maximized')
    #if inDriverExePathStr == "built-in":
    # Run with specified web driver path
    if CrossOS.IS_LINUX_BOOL:
        lPathStr = CrossOS.PathJoinList(CrossOS.PathSplitList(inDriverExePathStr)[:-1]) 
        os.environ["PATH"]+=f":{lPathStr}"
    gBrowser = webdriver.Chrome(executable_path = inDriverExePathStr, options=lWebDriverChromeOptionsInstance) 
    #from pyOpenRPA.Robot import Window
    #Window.DialogYesNo(inTitle="TEST", inBody="Далее взяли селектор")
    #else:
    #    lWebDriverInstance = webdriver.Chrome(options = lWebDriverChromeOptionsInstance)
    return gBrowser
from ..Utils import __define__
def BrowserFocus():
    """L+,W+: Выполнить фокусировку на окно браузера

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.BrowserFocus()
    """
    import psutil
    global gBrowser
    try:
        driver_pid = gBrowser.service.process.pid
        process = psutil.Process(driver_pid)
        browser_pid = None
        for child in process.children(recursive=True):
            if browser_pid==None: browser_pid = child.pid
            #if child.name() == "chrome.exe":
            #    chrome_pid = child.pid
            #    brea
        if browser_pid!=None: 
            if CrossOS.IS_WINDOWS_BOOL:
                UIBrowserSelector = [
                    {
                        "process": browser_pid,
                        "backend": "win32"
                    }
                ]
                UIDesktop.UIOSelector_Get_UIO(UIBrowserSelector).set_focus()
            else:
                UIBrowserSelector=[{"pid": browser_pid,"backend": "wnck"}]
                UIDesktop.UIOSelector_Focus(UIBrowserSelector)
    except Exception as e:
        pass

def BrowserChange(inBrowser):
    """L+,W+: Выполнить смену активного браузера (при необходимости).

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        lBrowser1 = UIWeb.BrowserChromeStart()
        UIWeb.BrowserChange(inBrowser=None)
        lBrowser2 = UIWeb.BrowserChromeStart()
        UIWeb.BrowserClose()
        UIWeb.BrowserChange(inBrowser=lBrowser1)
        UIWeb.BrowserClose()

    :param inBrowser: Объект браузера
    :type inBrowser: webdriver.Chrome
    """
    global gBrowser
    gBrowser = inBrowser


def PageNew(inURLStr: str = ""):
    """L+,W+: Открыть новую вкладку в браузере

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.PageNew("https://pyopenrpa.ru")

    :param inURLStr: URL адрес страницы, по умолчанию страница пустая, ""
    :type inURLStr: str, опциональный
    """
    global gBrowser
    if gBrowser is None: 
        BrowserChromeStart()
        if inURLStr!="": PageOpen(inURLStr)
    else:
        gBrowser.execute_script(f"window.open('{inURLStr}');")
        gBrowser.switch_to.window(gBrowser.window_handles[-1])


def PageCount():
    """L+,W+: Вернуть количество открытых вкладок в браузере

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        tab_count_int = UIWeb.PageCount()

    :return: Количество открытых вкладок в браузере 
    :rtype: int
    """
    global gBrowser
    if gBrowser is None: return 0
    return len(gBrowser.window_handles)

def PageClose(inIndexInt=None):
    """L+,W+: Закрыть текущую вкладку или вкладку, расположенную по индексу inIndexInt. После выключения вкладки вернуть на текущую активную вкладку.

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.PageClose(inTabIndexInt=1)

    :param inIndexInt: Индекс вкладки, которую требуется закрыть
    :type: int
    """
    global gBrowser
    tab_len_int = PageCount()
    if inIndexInt!=None: #Указан индекс закрываемой вкладки
        current_handle = gBrowser.current_window_handle
        close_handle = gBrowser.window_handles[inIndexInt]
        gBrowser.switch_to.window(close_handle)
        gBrowser.close()
        if current_handle!=close_handle: gBrowser.switch_to.window(current_handle)
    else: # Закрыть текущую вкладку
        if tab_len_int==1:
            BrowserClose()
        else: gBrowser.close()
        if tab_len_int>1: PageSwitch(inTabIndexInt = tab_len_int-2)


def PageSwitch(inTabIndexInt: int):
    """L+,W+: Переключить вкладку по индексу inTabIndexInt

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.PageSwitch(inTabIndexInt=1)

    :param inTabIndexInt: Индекс вкладки, на которую требуется переключиться
    :type inTabIndexInt: int
    """
    global gBrowser
    if inTabIndexInt<PageCount(): gBrowser.switch_to.window(gBrowser.window_handles[inTabIndexInt])

def PageOpen(inURLStr: str):
    """L+,W+: Открыть страницу inURLStr в браузере и дождаться ее загрузки.

    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        UIWeb.BrowserClose()

    :param inURLStr: URL адрес страницы
    :type inURLStr: str
    """
    global gBrowser
    if gBrowser is not None: gBrowser.get(inURLStr)
    else: 
        BrowserChromeStart()
        gBrowser.get(inURLStr)

    
def PagePrint():
    """L+,W+: Открыть окно печати браузера.

    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        import time
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        time.sleep(1)
        UIWeb.PagePrint()
        UIWeb.BrowserClose()

    """
    PageJSExecute(inJSStr=f"window.print()")

def PageScrollTo(inVerticalPxInt=0, inHorizontalPxInt=0):
    """L+,W+: Выполнить прокрутку страницы (по вертикали или по горизонтали)
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        UIWeb.PageScrollTo(inVerticalPxInt=100)
        UIWeb.BrowserClose()

    :param inVerticalPxInt: Величина вертикальной прокрутки страницы в пикселях, по умолчанию 0
    :type inVerticalPxInt: int, опционально
    :param inHorizontalPxInt: Величина горизонтальной прокрутки страницы в пикселях, по умолчанию 0
    :type inHorizontalPxInt: int, опционально
    """
    PageJSExecute(inJSStr=f"scroll({inHorizontalPxInt},{inVerticalPxInt})")

def PageJSExecute(inJSStr, *inArgList):
    """L+,W+: Отправить на выполнение на сторону браузера код JavaScript.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    !ВНИМАНИЕ! Данная функция поддерживает передачу переменных в область кода JavaScript (*inArgList). Обратиться к переданным переменным из JavaScript можно с помощью ключевого слова: arguments[i], где i - это порядковый номер переданной переменной

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        UIWeb.PageJSExecute(alert('arguments[0]);", "hello world!")
        UIWeb.BrowserClose()

    :param inJSStr: Код JavaScript, отправляемый на сторону браузера
    :type inJSStr: str
    :param *inArgList: Перечисление аргументов, отправляемых на сторону браузера
    :type *inArgList: str
    :return: Результат отработки кода JavaScript, если он заканчивался оператором "return"
    :rtype: str | int | bool | float
    """
    # arguments[0], arguments[1] etc
    global gBrowser
    if gBrowser is not None: return gBrowser.execute_script(inJSStr, *inArgList)
    
def BrowserClose():
    """L+,W+: Закрыть браузер

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        UIWeb.BrowserClose()

    """
    global gBrowser
    if gBrowser is not None: 
        gBrowser.close() # ранее был gBrowser.close(), но он трактуется браузером как принудительное завершение
        gBrowser=None

def UIOSelectorList(inUIOSelectorStr=None, inUIO=None) -> list:
    """L+,W+: Получить список UIO объектов по UIO селектору.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIOList = UIWeb.UIOSelectorList(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.BrowserClose()

    :param inUIOSelectorStr: XPATH или CSS селектор UI объекта на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    :param inUIO: Объект UIO, от которого выполнить поиск UIO объектов по селектору, по умолчанию None
    :type inUIO: WebElement, опционально
    :return: Список UIO объектов
    :rtype: list
    """
    lResultList = []
    lUIOVersionStr = UIOSelectorDetect(inUIOSelectorStr=inUIOSelectorStr)
    if lUIOVersionStr == "UIO": 
        inUIOSelectorStr = UIOSelector_To_XPATH(inUIOSelector=inUIOSelectorStr)
        lUIOVersionStr="XPATH"
    if inUIO is None:
        global gBrowser
        if gBrowser is not None:
            if lUIOVersionStr == "CSS":
                lResultList = gBrowser.find_elements(By.CSS_SELECTOR, inUIOSelectorStr)
            else:
                lResultList = gBrowser.find_elements(By.XPATH,inUIOSelectorStr)
    else: 
        if lUIOVersionStr == "CSS":
            lResultList = inUIO.find_elements(By.CSS_SELECTOR, inUIOSelectorStr)
        else:
            lResultList = inUIO.find_elements(By.XPATH,inUIOSelectorStr)
    if __define__.DEFINE_ACCEPTED==True: return lResultList
    else: []

def UIOSelectorFirst(inUIOSelectorStr=None, inUIO=None) -> list:
    """L+,W+: Получить UIO объект по UIO селектору.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorFirst(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.BrowserClose()

    :param inUIOSelectorStr: XPATH или CSS селектор UI объекта на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    :param inUIO: Объект UIO, от которого выполнить поиск UIO объектов по селектору, по умолчанию None
    :type inUIO: WebElement, опционально
    :return: Первый подходящий UIO объект
    :rtype: UIO объект
    """
    lResult = None
    lUIOList = UIOSelectorList(inUIOSelectorStr=inUIOSelectorStr, inUIO=inUIO)
    if len(lUIOList) > 0: lResult = lUIOList[0]
    return lResult

def UIOAttributeDictGet(inUIO):
    """L+,W+: Получить словарь атрибутов UI объекта. title - наименование тэга, class_list, style_dict

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorFirst(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.UIOAttributeDictGet(lUIO)

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    :return: Пример: {'class_list': [], 'lang': 'ru', 'style_dict': {'--ph-color-background-accent': None,'width': "100%",'color': "black"}, 'title': 'html', "nodeName": null}
    :rtype: dict
    """

    lJSStr = """

    // Get the attributes of the element
    var t = arguments[0] //document.getElementById("orpa_utils_list_html_template")
    var ui_property_dict = {"title":t.localName , "class_list":[], "style_dict":{}, "node_name": t.nodeName}

    var attributes = t.attributes;
    if (attributes!=null) {
        for (var i = 0; i < attributes.length; i++) {
            var name = attributes[i].name;
            if (name!="style" && name!="class") {
                var value = attributes[i].value;
                ui_property_dict[name]=value
                //console.log(name + " = " + value);
            }
        }
    }

    //CLASSES
    var classes = t.classList;
    if (classes!=null) {
        for (var i = 0; i < classes.length; i++) {
            var name = classes[i];
            //console.log(name);
            ui_property_dict.class_list.push(name)
        }
    }
    //STYLES
    var style = t.style
    if (style!=null) {
        for (var i = 0; i < style.length; i++) {
            var value = style[style[i]]
            if (value!=null) {
                ui_property_dict.style_dict[style[i]]=value        
            }
        }
    }
    return ui_property_dict

    """
    return PageJSExecute(lJSStr, inUIO)

def UIOSelectorChildListAttributeDictGet(inUIOSelector=None):
    """L+,W+: Получить список словарей атриботов детей UI объекта, определенного по inUIOSelector

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorFirst(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.UIOAttributeDictGet(lUIO)

    :param inUIOSelector: XPATH или CSS селектор UI элемента на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelector: str
    :return: Вернуть список детей [{'class_list': [], 'lang': 'ru', 'style_dict': {'--ph-color-background-accent': None,'width': "100%",'color': "black"}, 'title': 'html'}]
    :rtype: list
    """
    lUIO = UIOSelectorFirst(inUIOSelectorStr=inUIOSelector)
    return UIOChildListAttributeDictGet(inUIO=lUIO)

import copy

def UIOSelectorListAttributeDictGet(inUIOSelector=None):
    """L+,W+: Получить словарь атрибутов для UI объектов, которые удовлетворяют inUIOSelector селектору

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lAttributeList = UIWeb.UIOSelectorListAttributeDictGet(inUIOSelector = lUIOSelectorStr)

    :param inUIOSelector: XPATH или CSS селектор UI элемента на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelector: str
    :return: Список словарей UI объектов по селектору [{'class_list': [], 'lang': 'ru', 'style_dict': {'--ph-color-background-accent': None,'width': "100%",'color': "black"}, 'title': 'html'}]
    :rtype: list
    """
    lAttrList = []
    #lUIOSelectorTypesStr = UIOSelectorDetect(inUIOSelector)
    lUIOSelector = SelectorConvert(inUIOSelector, "UIO")
    lUIOList = UIOSelectorList(inUIOSelectorStr=inUIOSelector)
    lIndex = 0
    for lItem in lUIOList:
        lItemSelector = copy.deepcopy(lUIOSelector)
        if len(lUIOList)>1:
            lItemSelector[-1]["ctrl_index"]=lIndex
        lAttrDict = UIOAttributeDictGet(inUIO=lItem)
        if lAttrDict["node_name"]!="#text":
            lAttrDict["selector"]=lItemSelector
            lAttrDict["ctrl_index"]=lIndex
            lAttrList.append(lAttrDict)
            lIndex+=1
    return lAttrList

def UIOSelectorLevelInfoList(inUIOSelector):
    """L+,W+: Получить список свойств всех уровней до UI объекта, обнаруженного с помощью селектора inUIOSelector.
    
    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIOLevelList = UIWeb.UIOSelectorLevelInfoList(inUIOSelector = inUIOSelector)

    :param inUIOSelector: Селектор на UIO объект (CSS | XPATH | UIO).
    :type inUIOSelector: list, обязательный
    :return: список уровней UIO объектов
    """  

    lUIO = UIOSelectorFirst(inUIOSelector)

    lJSStr = """

    // Get the attributes of the element
    var child = arguments[0]
    var t = child
    var ui_level_list = []
    while (t.parentNode !=null) {
        var ui_property_dict = {"title":t.localName , "class_list":[], "style_dict":{}, "node_name": t.nodeName}
        var attributes = t.attributes;
        if (attributes!=null) {
            for (var i = 0; i < attributes.length; i++) {
                var name = attributes[i].name;
                if (name!="style" && name!="class") {
                    var value = attributes[i].value;
                    ui_property_dict[name]=value
                    //console.log(name + " = " + value);
                }
            }
        }

        //CLASSES
        var classes = t.classList;
        if (classes!=null) {
            for (var i = 0; i < classes.length; i++) {
                var name = classes[i];
                //console.log(name);
                ui_property_dict.class_list.push(name)
            }
        }
        //STYLES
        var style = t.style
        if (style!=null) {
            for (var i = 0; i < style.length; i++) {
                var value = style[style[i]]
                if (value!=null) {
                    ui_property_dict.style_dict[style[i]]=value        
                }
            }
        }
        ui_level_list.unshift(ui_property_dict)
        t = t.parentNode
    }
    return ui_level_list

    """
    return PageJSExecute(lJSStr, lUIO)


def UIOChildListAttributeDictGet(inUIO):
    """L+,W+: Получить список словарь атрибутов для детей UI объекта inUIO. title - наименование тэга, class_list, style_dict

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorFirst(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.UIOAttributeDictGet(lUIO)

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    :return: Пример: {"ctrl_index": 0, 'class_list': [], 'lang': 'ru', 'style_dict': {'--ph-color-background-accent': None,'width': "100%",'color': "black"}, 'title': 'html'}
    :rtype: dict
    """
    lJSStr = """
    var ui_child_property_list=[]
    var t_child_list = arguments[0].childNodes
    var ctrl_index = 1
    for (var ii=0; ii<t_child_list.length; ii++) {
        // Get the attributes of the element
        var t = t_child_list[ii]
        if (t.nodeName!="#text") {
            var ui_property_dict = {"title":t.localName , "class_list":[], "style_dict":{}, "ctrl_index": ctrl_index}

            var attributes = t.attributes;
            if (attributes!=null) {
                for (var i = 0; i < attributes.length; i++) {
                    var name = attributes[i].name;
                    if (name!="style" && name!="class") {
                        var value = attributes[i].value;
                        ui_property_dict[name]=value
                        //console.log(name + " = " + value);
                    }
                }
            }

            //CLASSES
            var classes = t.classList;
            if (classes!=null) {
                for (var i = 0; i < classes.length; i++) {
                    var name = classes[i];
                    //console.log(name);
                    ui_property_dict.class_list.push(name)
                }
            }
            //STYLES
            var style = t.style
            if (style!=null) {
                for (var i = 0; i < style.length; i++) {
                    if (value!=null) {
                        ui_property_dict.style_dict[style[i]]=value        
                    }
                }
            }
            ui_child_property_list.push(ui_property_dict)
            ctrl_index+=1
        }

        
    }
    return ui_child_property_list

    """
    return PageJSExecute(lJSStr, inUIO)

import inspect
def UIOSelectorActivityArgGet(inUIOSelector, inActionStr):
    """L+,W+: Сформировать преднастроенный список/словарь аргументов, передаваемый в функцию inActionStr, которая будет вызываться у объекта UIO, полученного по inUIOSelector

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIOArgDict = UIWeb.UIOSelectorActivityArgGet(inUIOSelector = lUIOSelectorStr, inActionStr="type_keys")

        #Возвращаемый результат
        {'Selector': [{'title': 'UIDesktop.py - ORPA - Visual Studio Code',
        'class_name': 'Chrome_WidgetWin_1',
        'backend': 'uia'}],
        'ArgList': ['keys', None, False, False, False, True, True, True],
        'ArgDict': {'keys': None,
        'pause': None,
        'with_spaces': False,
        'with_tabs': False,
        'with_newlines': False,
        'turn_off_numlock': True,
        'set_foreground': True,
        'vk_packet': True}}
        
    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inUIOSelector: list, обязательный
    :param inActionStr: Наименование метода, к которому выполнить подбор аргументов
    :type inActionStr: str, обязательный
    """

    l_uio = UIOSelectorFirst(inUIOSelector)

    lResultDict = {
        "Selector": inUIOSelector,
        "ArgList": [],
        "ArgDict": {}
    }
    lModuleDefList = dir(l_uio)
    lDef = None
    if inActionStr in lModuleDefList:
        lItemDef = getattr(l_uio,inActionStr)
        if callable(lItemDef): lDef=lItemDef
        else: 
            lResultDict["ArgDict"] = None
            lResultDict["ArgList"] = None
            return lResultDict
        lDefSignature = inspect.signature(lDef)
        for lItemKeyStr in lDefSignature.parameters:
            lItemValue = lDefSignature.parameters[lItemKeyStr]
            if lItemValue.default is inspect._empty:
                lResultDict["ArgDict"][lItemKeyStr] = None
                lResultDict["ArgList"].append(f"{lItemValue.name}{':'+lItemValue.annotation if lItemValue.annotation!=inspect._empty else ''}")
            else:
                lResultDict["ArgDict"][lItemKeyStr] = lItemValue.default
                lResultDict["ArgList"].append(lItemValue.default)

    return lResultDict



def UIOSelectorActivityListGet (inUIOSelector):
    """L+,W+: Получить список доступных действий/функций по UIO селектору inUIOSelector. Описание возможных активностей см. ниже.

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lActivityList = UIDesktop.UIOSelectorActivityListGet(lUIOSelectorStr) # Получить список активностей по UIO селектору.

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inUIOSelector: list, обязательный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    """
    #Список исключений для отображения
    ignore_list = {
        "find_element",
        "find_element_by_class_name",
        "find_element_by_css_selector",
        "find_element_by_id",
        "find_element_by_link_text",
        "find_element_by_name",
        "find_element_by_partial_link_text",
        "find_element_by_tag_name",
        "find_element_by_xpath",
        "find_elements",
        "find_elements_by_class_name",
        "find_elements_by_css_selector",
        "find_elements_by_id",
        "find_elements_by_link_text",
        "find_elements_by_name",
        "find_elements_by_partial_link_text",
        "find_elements_by_tag_name",
        "find_elements_by_xpath",
        "parent"
    }
    #Конвертация селектора в формат UIO
    inUIOSelector = SelectorConvert(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Получить объект
    lObject=UIOSelectorFirst(inUIOSelector)
    lActionList=dir(lObject)
    lResult=dir(lObject)
    #Выполнить чистку списка от неактуальных методов
    for lActionItem in lActionList:
        #Удалить те, которые начинаются на _
        if lActionItem[0]=='_':
            lResult.remove(lActionItem)
        # Удалить те, которые в ignore списке
        if lActionItem in ignore_list:
            lResult.remove(lActionItem)
    return lResult


def UIOTextGet(inUIO) -> str:
    """L+,W+: Получить текст UI элемента.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorList(inUIOSelectorStr = lUIOSelectorStr)[0]
        lTextStr = UIWeb.UIOTextGet(inUIO=lUIO)
        UIWeb.BrowserClose()

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    :return: Текст UI элемента
    :rtype: str
    """
    return inUIO.text

def UIOAttributeGet(inUIO, inAttributeStr) -> str:
    """L+,W+: Получить обычный (нестилевой) атрибут у UI элемента.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorList(inUIOSelectorStr = lUIOSelectorStr)[0]
        UIWeb.UIOAttributeGet(inUIO=lUIO, inAttributeStr = "href")
        UIWeb.BrowserClose()

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    :param inAttributeStr: Наименование обычного (нестилевого) атрибута
    :type inAttributeStr: str
    :return: Значение обычного (нестилевого) атрибута
    :rtype: str
    """
    return inUIO.get_attribute(inAttributeStr)

def UIOAttributeStyleGet(inUIO, inAttributeStr) -> str:
    """L+,W+: Получить стилевой атрибут у UI элемента.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorList(inUIOSelectorStr = lUIOSelectorStr)[0]
        UIWeb.UIOAttributeStyleGet(inUIO=lUIO, inAttributeStr = "href")
        UIWeb.BrowserClose()

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    :param inAttributeStr: Наименование стилевого атрибута
    :type inAttributeStr: str
    :return: Значение стилевого атрибута
    :rtype: str
    """
    return inUIO.value_of_css_property(inAttributeStr)

def UIOAttributeSet(inUIO, inAttributeStr, inValue):
    """L+,W+: Установить обычный (нестилевой) атрибут у UI элемента.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorList(inUIOSelectorStr = lUIOSelectorStr)[0]
        UIWeb.UIOAttributeSet(inUIO=lUIO, inAttributeStr = "href", inValue = "https://mail.ru")
        UIWeb.BrowserClose()

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    :param inAttributeStr: Наименование обычного (нестилевого) атрибута
    :type inAttributeStr: str
    :param inValue: Устанавливаемое значение обычного (нестилевого) атрибута
    :type inValue: str
    """
    lJSStr = \
        f"arguments[0].setAttribute(arguments[1], arguments[2]);"
    gBrowser.execute_script(lJSStr,inUIO, inAttributeStr, inValue)

def UIOAttributeRemove(inUIO, inAttributeStr):
    """L+,W+: Удалить обычный (нестилевой) атрибут у UI элемента.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorList(inUIOSelectorStr = lUIOSelectorStr)[0]
        UIWeb.UIOAttributeRemove(lUIO, "href")
        UIWeb.BrowserClose()

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    :param inAttributeStr: Наименование обычного (нестилевого) атрибута
    :type inAttributeStr: str
    """
    lJSStr = \
        f"arguments[0].removeAttribute(arguments[1]);"
    gBrowser.execute_script(lJSStr,inUIO, inAttributeStr)

def UIOAttributeStyleSet(inUIO, inAttributeStr, inValue):
    """L+,W+: Установить стилевой атрибут у UI элемента.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorList(inUIOSelectorStr = lUIOSelectorStr)[0]
        UIWeb.UIOAttributeStyleSet(inUIO=lUIO, inAttributeStr = "color", inValue = "grey")
        UIWeb.BrowserClose()

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    :param inAttributeStr: Наименование стилевого атрибута
    :type inAttributeStr: str
    :param inValue: Устанавливаемое значение стилевого атрибута
    :type inValue: str
    """
    lJSStr = \
        f"arguments[0].style[arguments[1]]=arguments[2];"
    gBrowser.execute_script(lJSStr,inUIO, inAttributeStr, inValue)

def UIOAttributeStyleRemove(inUIO, inAttributeStr:str):
    """L+,W+: Удалить стилевой атрибут у UI элемента.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorList(inUIOSelectorStr = lUIOSelectorStr)[0]
        UIWeb.UIOAttributeStyleRemove(lUIO, "color")
        UIWeb.BrowserClose()

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    :param inAttributeStr: Наименование стилевого атрибута
    :type inAttributeStr: str
    """
    lJSStr = \
        f"arguments[0].style[arguments[1]]=\"\";"
    gBrowser.execute_script(lJSStr,inUIO, inAttributeStr)

def UIOClick(inUIO):
    """L+,W+: Выполнить нажатие по элементу inUIO.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIWeb.UIOSelectorList(inUIOSelectorStr = lUIOSelectorStr)[0]
        UIOClick(inUIO = lUIO)
        UIWeb.BrowserClose()

    :param inUIO: UIO элемент. Получить его можно с помощью функций UIOSelectorList или UIOSelectorFirst
    :type inUIO: WebElement
    """
    inUIO.click()

def UIOSelectorActivityRun(inUIOSelector, inActionName, inArgumentList=None, inkwArgumentObject=None):
    """L+,W+: Выполнить активность inActionName над UIO объектом, полученным с помощью UIO селектора inUIOSelector. Описание возможных активностей см. ниже.

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lActivityResult = UIWeb.UIOSelectorActivityRun(lUIOSelectorStr, "click") # выполнить действие над UIO объектом с помощью UIO селектора.

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inUIOSelector: list, обязательный
    :param inActionName: наименование активности, которую требуется выполнить над UIO объектом
    :type inActionName: str, обязательный
    :param inArgumentList: список передаваемых неименованных аргументов в функцию inActionName
    :type inArgumentList: list, необязательный
    :param inkwArgumentObject: словарь передаваемых именованных аргументов в функцию inActionName
    :type inkwArgumentObject: dict, необязательный
    :return: возвращает результат запускаемой функции с наименованием inActionName над UIO объектом
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = SelectorConvert(inSelector=inUIOSelector, inToTypeStr="UIO")
    if inArgumentList is None: inArgumentList=[] # 2021 02 22 Minor fix by Ivan Maslov
    if inkwArgumentObject is None: inkwArgumentObject={} # 2021 02 22 Minor fix by Ivan Maslov
    lResult={}
    #Определить объект
    lObject=UIOSelectorFirst(inUIOSelector)
    #Получить метод для вызова
    lFunction = getattr(lObject, inActionName)
    if callable(lFunction):
        #Выполнить действие
        #Обернуто в безопасную обработку, тк для некоторых объектов метод не работает и может выдавать ошибку типа: NotImplementedError: This method not work properly for WinForms DataGrid, use cells()
        try:
            return lFunction(*inArgumentList,**inkwArgumentObject)
        except Exception as e:
            #Если ошибка возникла на action get_properties
            if inActionName=="get_properties":
                lResult={}
                #Ручное формирование
                lResult["class_name"]=lObject.class_name()
                lResult["friendly_class_name"]=lObject.friendly_class_name()
                lResult["texts"]=lObject.texts()
                lResult["control_id"]=lObject.control_id()
                lResult["control_count"]=lObject.control_count()
                lResult["automation_id"]=lObject.automation_id()
                return lResult
            else:
                raise e
    else:
        return lFunction


def UIOHighlight(inUIO, inIsFirst:bool=False, inDurationSecFloat:float=3.0, inColorStr:str="green"):
    """L+,W+: Выполнить подсвечивание UI элемента с UIO.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIO = UIOSelectorFirst(lUIOSelectorStr)
        UIWeb.UIOHighlight(inUIO = lUIO)
        UIWeb.BrowserClose()

    :param inUIOSelectorStr: XPATH или CSS селектор UI элемента на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    :param inIsFirst: True - подсветить только первый элемент, который удовлетворяет селектору. По умолчанию False
    :type inIsFirst: bool, опционально
    :param inDurationSecFloat: Длительность подсвечивания. По умолчанию 3.0 сек.
    :type inDurationSecFloat: float, опционально
    :param inColorStr: Цвет подсвечания Варианты: "red", "blue", "grey", "yellow". По умолчанию "green" (зеленый)
    :type inColorStr: str, опционально
    """
    global gBrowser
    if inIsFirst == True:
        lUIOList = [inUIO]
        lJSStr = \
            f"var lElementList = arguments[0];" \
            f"if (lElementList.length>0) {{ lElementList=[lElementList[0]]; }}" \
            f"for (var lIndexInt=0; lIndexInt<lElementList.length;lIndexInt++) {{" \
            f"  lElement=lElementList[lIndexInt];" \
            f"  lElement.ORPABackupStyleOutline = lElement.style[\"outline\"];" \
            f"  lElement.style[\"outline\"]=\"2px solid {inColorStr}\";" \
            f"}}" \
            f"window.ORPAOutlineList = lElementList;"
        PageJSExecute(lJSStr, lUIOList)
    else:
        lUIOList = [inUIO]
        lJSStr = \
            f"var lElementList = arguments[0];" \
            f"for (var lIndexInt=0; lIndexInt<lElementList.length;lIndexInt++) {{" \
            f"  lElement=lElementList[lIndexInt];" \
            f"  lElement.ORPABackupStyleOutline = lElement.style[\"outline\"];" \
            f"  lElement.style[\"outline\"]=\"2px solid {inColorStr}\";" \
            f"}}" \
            f"window.ORPAOutlineList = lElementList;"
        PageJSExecute(lJSStr, lUIOList)
    time.sleep(inDurationSecFloat)
    lJSStr = \
        f"var lElementList = window.ORPAOutlineList;" \
        f"for (var lIndexInt=0; lIndexInt<lElementList.length;lIndexInt++) {{" \
        f"  lElement=lElementList[lIndexInt];" \
        f"  lElement.style[\"outline\"]=lElement.ORPABackupStyleOutline;" \
        f"}}" \
        f"delete window.ORPAOutlineList;"
    PageJSExecute(inJSStr=lJSStr)


def UIOSelectorHighlight(inUIOSelectorStr: str, inIsFirst:bool=False, inDurationSecFloat:float=3.0, inColorStr:str="green"):
    """L+,W+: Выполнить подсвечивание UI элемента с селектором inUIOSelectorStr.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        UIWeb.UIOSelectorHighlight(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.BrowserClose()

    :param inUIOSelectorStr: UIO,  XPATH или CSS селектор UI элемента на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    :param inIsFirst: True - подсветить только первый элемент, который удовлетворяет селектору. По умолчанию False
    :type inIsFirst: bool, опционально
    :param inDurationSecFloat: Длительность подсвечивания. По умолчанию 3.0 сек.
    :type inDurationSecFloat: float, опционально
    :param inColorStr: Цвет подсвечания Варианты: "red", "blue", "grey", "yellow". По умолчанию "green" (зеленый)
    :type inColorStr: str, опционально
    """
    global gBrowser
    if inIsFirst == True:
        lUIOList = [UIOSelectorFirst(inUIOSelectorStr=inUIOSelectorStr)]
        lJSStr = \
            f"var lElementList = arguments[0];" \
            f"if (lElementList.length>0) {{ lElementList=[lElementList[0]]; }}" \
            f"for (var lIndexInt=0; lIndexInt<lElementList.length;lIndexInt++) {{" \
            f"  lElement=lElementList[lIndexInt];" \
            f"  lElement.ORPABackupStyleOutline = lElement.style[\"outline\"];" \
            f"  lElement.style[\"outline\"]=\"2px solid {inColorStr}\";" \
            f"}}" \
            f"window.ORPAOutlineList = lElementList;"
        PageJSExecute(lJSStr, lUIOList)
    else:
        lUIOList = UIOSelectorList(inUIOSelectorStr=inUIOSelectorStr)
        lJSStr = \
            f"var lElementList = arguments[0];" \
            f"for (var lIndexInt=0; lIndexInt<lElementList.length;lIndexInt++) {{" \
            f"  lElement=lElementList[lIndexInt];" \
            f"  lElement.ORPABackupStyleOutline = lElement.style[\"outline\"];" \
            f"  lElement.style[\"outline\"]=\"2px solid {inColorStr}\";" \
            f"}}" \
            f"window.ORPAOutlineList = lElementList;"
        PageJSExecute(lJSStr, lUIOList)
    time.sleep(inDurationSecFloat)
    lJSStr = \
        f"var lElementList = window.ORPAOutlineList;" \
        f"for (var lIndexInt=0; lIndexInt<lElementList.length;lIndexInt++) {{" \
        f"  lElement=lElementList[lIndexInt];" \
        f"  lElement.style[\"outline\"]=lElement.ORPABackupStyleOutline;" \
        f"}}" \
        f"delete window.ORPAOutlineList;"
    PageJSExecute(inJSStr=lJSStr)

def UIOSelectorFocusHighlight(inUIOSelectorStr: str, inIsFirst:bool=False, inDurationSecFloat:float=3.0, inColorStr:str="green"):
    """L+,W+: Выполнить подсвечивание UI элемента с селектором inUIOSelectorStr.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        UIWeb.UIOSelectorFocusHighlight(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.BrowserClose()

    :param inUIOSelectorStr: XPATH или CSS селектор UI элемента на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    :param inIsFirst: True - подсветить только первый элемент, который удовлетворяет селектору. По умолчанию False
    :type inIsFirst: bool, опционально
    :param inDurationSecFloat: Длительность подсвечивания. По умолчанию 3.0 сек.
    :type inDurationSecFloat: float, опционально
    :param inColorStr: Цвет подсвечания Варианты: "red", "blue", "grey", "yellow". По умолчанию "green" (зеленый)
    :type inColorStr: str, опционально
    """
    BrowserFocus()
    UIOSelectorHighlight(inUIOSelectorStr=inUIOSelectorStr, inIsFirst=inIsFirst, inDurationSecFloat=inDurationSecFloat, inColorStr=inColorStr)

def UIOSelectorClick(inUIOSelectorStr: str):
    """L+,W+: Выполнить нажатие по элементу с селектором inUIOSelectorStr.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        UIWeb.UIOSelectorClick(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.BrowserClose()

    :param inUIOSelectorStr: UIO, XPATH или CSS селектор UI элемента на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    """
    if UIOSelectorDetect(inUIOSelectorStr=inUIOSelectorStr) == "CSS":
        PageJSExecute(inJSStr=f"document.querySelector('{inUIOSelectorStr}').click()")
    else:
        inUIOSelectorStr = SelectorConvert(inSelector=inUIOSelectorStr, inToTypeStr="XPATH") # 2023 08 01 FIX
        PageJSExecute(inJSStr=f"document.evaluate('{inUIOSelectorStr}', document, null , XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()")

def UIOSelectorSetValue(inUIOSelectorStr: str, inValue: str):
    """L+,W+: Установить значение элемента с селектором inUIOSelectorStr.
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://www.google.com/")
        lUIOSelectorStr = "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input"
        lValue = "pyOpenRPA"
        UIWeb.UIOSelectorSetValue(inUIOSelectorStr = lUIOSelectorStr, inValue = lValue)
        UIWeb.BrowserClose()

    :param inUIOSelectorStr: UIO, XPATH или CSS селектор UI элемента на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    :param inValue: Значение, которое необходимо установить 
    :type inValue: str
    """
    
    if UIOSelectorDetect(inUIOSelectorStr=inUIOSelectorStr) == "CSS":
        PageJSExecute(inJSStr=f"document.querySelector('{inUIOSelectorStr}').value='{inValue}'")
    else:
        inUIOSelectorStr = SelectorConvert(inSelector=inUIOSelectorStr, inToTypeStr="XPATH") # 2023 08 01 FIX
        PageJSExecute(inJSStr=f"document.evaluate('{inUIOSelectorStr}', document, null , XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.value='{inValue}'")
        
def UIOSelectorWaitAppear(inUIOSelectorStr:str, inWaitSecFloat:float=UIO_WAIT_SEC_FLOAT, inWaitIntervalSecFloat:float = UIO_WAIT_INTERVAL_SEC_FLOAT):
    """L+,W+: Ожидать появление UI элемента на веб странице (блокирует выполнение потока), заданного по UIO селектору inUIOSelectorStr. Выполнять ожидание на протяжении inWaitSecFloat (по умолчанию 60 сек.). Проверка производится с интервалом inWaitIntervalSecFloat (по умолчанию 1 сек.)
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver
    
    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lAppearUIOList = UIWeb.UIOSelectorWaitAppear(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.BrowserClose()
    
    :param inUIOSelectorStr: XPATH или CSS селектор UI элемента на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    :param inWaitSecFloat: Время ожидания на исчезновение UI элемента, по умолчанию UIO_WAIT_SEC_FLOAT (60 сек)
    :type inWaitSecFloat: float, опциональный
    :param inWaitIntervalSecFloat: Интервал проверки исчезновения, по умолчанию UIO_WAIT_INTERVAL_SEC_FLOAT (1 сек)
    :type inWaitIntervalSecFloat: float, опциональный
    :raises Exception: Время ожидания превышено
    :return: Список UI элементов, которые удовлетворяют селектору и появились на странице
    :rtype: list
    """
    lStartSecFloat = time.time()
    lResultList=[]
    while time.time() - lStartSecFloat < inWaitSecFloat:
        lResultList = UIOSelectorList(inUIOSelectorStr=inUIOSelectorStr)
        if len(lResultList)>0: break
        time.sleep(inWaitIntervalSecFloat)
    if time.time() - lStartSecFloat > inWaitSecFloat: raise Exception(f"Wait time is over. No element has been appear")
    return lResultList

def UIOSelectorWaitDisappear(inUIOSelectorStr:str, inWaitSecFloat:float=UIO_WAIT_SEC_FLOAT, inWaitIntervalSecFloat:float = UIO_WAIT_INTERVAL_SEC_FLOAT):
    """L+,W+: Ожидать исчезновение UI элемента с веб страницы (блокирует выполнение потока), заданного по UIO селектору inUIOSelectorStr. Выполнять ожидание на протяжении inWaitSecFloat (по умолчанию 60 сек.). Проверка производится с интервалом inWaitIntervalSecFloat (по умолчанию 1 сек.)
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver
    
    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        UIWeb.UIOSelectorWaitDisappear(inUIOSelectorStr = lUIOSelectorStr)
        UIWeb.BrowserClose()
        
    :param inUIOSelectorStr: XPATH или CSS селектор UI элемента на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    :param inWaitSecFloat: Время ожидания на исчезновение UI элемента, по умолчанию UIO_WAIT_SEC_FLOAT (60 сек)
    :type inWaitSecFloat: float, опциональный
    :param inWaitIntervalSecFloat: Интервал проверки исчезновения, по умолчанию UIO_WAIT_INTERVAL_SEC_FLOAT (1 сек)
    :type inWaitIntervalSecFloat: float, опциональный
    :raises Exception: Время ожидания превышено
    """
    lStartSecFloat = time.time()
    while time.time() - lStartSecFloat < inWaitSecFloat:
        lResultList = UIOSelectorList(inUIOSelectorStr=inUIOSelectorStr)
        if len(lResultList)==0: break
        time.sleep(inWaitIntervalSecFloat)
    if time.time() - lStartSecFloat > inWaitSecFloat: raise Exception(f"Wait time is over. No element has been disappear")


def SelectorConvert(inSelector, inToTypeStr):
    """L+,W+: Перевести селектор в заданный тип. Доступно: UIO, CSS и XPATH

    .. code-block:: python

        # UIWeb: Взаимодействие с UI объектами браузера
        from pyOpenRPA.Robot import UIWeb
        lToType = "XPATH"
        lUIOSelector = [{}]
        lXPATHSelector = UIDesktop.Selector_Convert_Selector(inSelector=lUIOSelector, inToTypeStr=lToType) 

    :param inSelector: Селектор, который необходимо преобразовать
    :type inSelector: str или list, обязательный
    :param inToTypeStr: Тип, в который необходимо преобразовать селектор
    :type inToTypeStr: str, обязательный
    :return: Селектор
    """

        #Определяем вид селектора
    lFromTypeStr = UIOSelectorDetect(inSelector)
    if lFromTypeStr ==  "ERROR": raise TypeError("Selector type couldn't be determined")

    #При конвертации в UIO
    if inToTypeStr == "UIO":
        try:
            if lFromTypeStr == "XPATH": #Отрабатываем приобразование XPath -> UIO
                lUIOSelector = XPATH_To_UIOSelector(inSelector)
            elif lFromTypeStr == "CSS": #Отрабатываем приобразование CSS -> UIO
                pass#lUIOSelector = CSS_To_UIOSelector(inSelector)
            elif lFromTypeStr == "UIO": 
                lUIOSelector = inSelector
                if lUIOSelector is None: lUIOSelector=[{}]
            return lUIOSelector
        except Exception as e: raise e
    
    #При конвертации в XPATH
    if inToTypeStr == "XPATH":
        try:
            if lFromTypeStr == "UIO":#Отрабатываем приобразование UIO -> XPath 
                lXPATHSelector = UIOSelector_To_XPATH(inSelector)
            elif lFromTypeStr == "CSS":#Отрабатываем приобразование CSS -> XPath
                pass#lCSSSelector = CSS_To_UIOSelector(inSelector)
                lXPATHSelector = UIOSelector_To_XPATH(lCSSSelector)
            elif lFromTypeStr == "XPATH": lXPATHSelector = inSelector
            return lXPATHSelector
        except Exception as e: raise e
    
    #При конвертации в CSS
    if inToTypeStr == "CSS":
        try:
            if lFromTypeStr == "UIO": #Отрабатываем приобразование UIO -> CSS
                pass#lCSSSelector = UIOSelector_To_CSS(inSelector)
            elif lFromTypeStr == "XPATH": #Отрабатываем приобразование XPATH -> CSS
                lXPATHSelector = XPATH_To_UIOSelector(inSelector)
                pass#lCSSSelector = UIOSelector_To_CSS(lXPATHSelector)
            elif lFromTypeStr == "CSS": lCSSSelector = inSelector
            return lCSSSelector
        except Exception as e: raise e

from lxml import etree
from io import StringIO
gXML = etree.parse(StringIO('<foo><bar></bar></foo>'))

def UIOSelectorDetect(inUIOSelectorStr:str) -> str:
    """L+,W+: Идентифицировать стиль селектора (CSS или XPATH или UIO)

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        lUIOSelectorStr = "#grid > div.grid-middle > div.grid__main-col.svelte-2y66pa > div.grid_newscol.grid_newscol__more-pulse.svelte-1yvqfic > div.grid__ccol.svelte-1yvqfic > ul > li:nth-child(5) > div > a"
        lUIOSelectorStr = "//*[@id=\'grid\']/div[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lResultStr = UIWeb.UIOSelectorDetect(inUIOSelectorStr = lUIOSelectorStr)

    :param inUIOSelectorStr: XPATH или CSS селектор UI объекта на web странице. Подсказки по CSS: https://devhints.io/css Подсказки по XPath: https://devhints.io/xpath 
    :type inUIOSelectorStr: str
    :return: "CSS" или "XPATH" или "UIO"
    :rtype: str
    """
    global gXML
    lResultStr = "CSS"
    if inUIOSelectorStr is None: return "UIO"
    if isinstance(inUIOSelectorStr, list): 
        return "UIO"
    elif isinstance(inUIOSelectorStr, str): 
        try:
            parse_result = json.loads(inUIOSelectorStr)
            if isinstance(parse_result, list): return "UIO"
        except:
            pass
        try:
            gXML.xpath(inUIOSelectorStr)
            lResultStr = "XPATH"
        except etree.XPathEvalError as e:
            lResultStr = "CSS"
    return lResultStr
import re

def XPATH_To_UIOSelector(inXPATHSelector=None):
    """L+,W+: Выполнить конвертацию селектора из XPATH в UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIWeb
        lXPATHSelector = "//*[@id=\'grid\']/*[2]/div[2]/div[3]/div[1]/ul/li[5]/div/a"
        lUIOSelector = UIDesktop.XPATH_To_UIOSelector(inXPATHSelector=lXPATHSelector)

    :param inUIOSelector: Селектор в формате XPATH
    :type inUIOSelector: str, обязательный
    """
    if inXPATHSelector is None: inXPATHSelector="/"
    inUIOSelector = [{}]
    #Обрабатываем возможную замену // -> depth_start:1, depth_end:99
    if "//" in inXPATHSelector:
        lSelectorList = inXPATHSelector.split("/")
        lSelectorList.pop(0)
        lSelectorListTmp = lSelectorList
        for lIndex, lItem in enumerate(lSelectorList):
            if lItem == "": lSelectorListTmp[lIndex+1]='[@depth_start="1"][@depth_end="99"]' + lSelectorList[lIndex+1] 
        lSelectorListTmp = [x for x in lSelectorListTmp if x != '']
        inXPATHSelector = "/".join(lSelectorListTmp)
        if inXPATHSelector[0] != "/": inXPATHSelector = "/"+inXPATHSelector

    #Разбиваем селектор по уровням
    lUIOSelectorList = inXPATHSelector.split("/")
    lUIOSelectorList.pop(0)
    for lItem in lUIOSelectorList:
        #Обрабатываем возможную замену .. -> go_up:1
        if lItem == "..": lItem = '[@go_up="1"]'
        #Отделяем атрибуты на одном уровне друг от друга
        lParams = re.split('[\[\]]', lItem)
        lOneLevelDict = {}
        #Приводим к виду UIOSelector
        for lParam in lParams:
            lParam = lParam.rstrip(" ").lstrip(" ")
            lCtrlIndexInt = None
            try:
                lCtrlIndexInt = int(lParam)
            except: pass
            if lParam == "*" or lParam == "": pass
            elif lCtrlIndexInt!=None:
                lOneLevelDict["ctrl_index"] = lCtrlIndexInt
            elif "@" in lParam: 
                lParam = lParam.replace("@","")
                if "'" in lParam: lParam = lParam.replace("'","")
                elif '"' in lParam: lParam = lParam.replace('"',"")
                lParamList = lParam.split("=")
                try: lParamList[1] = int(lParamList[1])
                except: pass
                lOneLevelDict[lParamList[0]] = lParamList[1]
            else:
                lOneLevelDict["title"] = lParam
        if lOneLevelDict != {}:inUIOSelector.append(lOneLevelDict)

    return inUIOSelector

def UIOSelector_To_XPATH(inUIOSelector=None):
    """L+,W+: Выполнить конвертацию селектора из UIO в XPATH

    .. code-block:: python

        # UIWeb: Взаимодействие с UI объектами вкладки
        from pyOpenRPA.Robot import UIWeb
        lUIOSelector = [{'depth_start': 1, 'depth_end': 99, 'id': 'grid'},
            {'ctrl_index': 2},
            {'depth_start': 1, 'depth_end': 99, 'title': 'div', 'ctrl_index': 2},
            {'title': 'div', 'ctrl_index': 3},
            {'title': 'div', 'ctrl_index': 1},
            {'title': 'ul'},
            {'title': 'li', 'ctrl_index': 5},
            {'title': 'div'},
            {'title': 'a'}]
        lXPATHSelector = UIWeb.UIOSelector_To_XPATH(inUIOSelector=lUIOSelector)

    :param inUIOSelector: Селектор в формате UIO
    :type inUIOSelector: list, обязательный
    """
    if inUIOSelector is None: inUIOSelector = []
    if inUIOSelector == "": inUIOSelector = []
    if isinstance(inUIOSelector, str): inUIOSelector = json.loads(inUIOSelector)
    if len(inUIOSelector)==0: return "/html"
    lSelectorTmpStr = ""
    inXPATHSelector = ""
    #Цикл по уровням
    for lItem in inUIOSelector:
        lOneLevelAttrStr = ""
        lDelimiter = "/"
        lTitleFlag = False
        #Цикл по атрибутам внутри уровня
        for key in lItem:
            if key == "depth_end": lDelimiter = "//"
            elif key == "depth_start":pass
            elif key == "go_up": 
                for i in range(int(lItem[key])):
                    lOneLevelAttrStr += "../"
                lOneLevelAttrStr = lOneLevelAttrStr[:-1]
                lTitleFlag = True
                break
            elif key == "title": 
                lTitleFlag = True
                lOneLevelAttrStr = lItem[key] + lOneLevelAttrStr
            elif key == "ctrl_index": lOneLevelAttrStr += f'[{lItem[key]}]'
            else: lOneLevelAttrStr += f'[@{key}="{lItem[key]}"]'
        #Составление итогового XPath селектора    
        if lTitleFlag: lSelectorTmpStr = lSelectorTmpStr + lDelimiter + lOneLevelAttrStr
        else: lSelectorTmpStr = lSelectorTmpStr + lDelimiter + "*" + lOneLevelAttrStr
    inXPATHSelector = lSelectorTmpStr

    return inXPATHSelector

gMouseIsInitBool = False
def UIOMouseSearchInit():
    """L+,W+: Инициализирует процесс поиска UI элемента с помощью мыши. После инициализации необходимо переместить указатель мыши на искомый элемент. Для прекращения поиска необходимо использовать функцию: UIOMouseSearchReturn
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        import time
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        UIWeb.UIOMouseSearchInit()
        time.sleep(3)
        UIWeb.UIOMouseSearchReturn()
        UIWeb.BrowserClose()
    """   
    global gMouseIsInitBool
    gMouseIsInitBool=True 
    lJSStr = """
        document.ORPAMouseXInt=0;
        document.ORPAMouseYInt=0;
        document.ORPASearch = function(e){
            document.ORPAMouseXInt = e.clientX;
            document.ORPAMouseYInt = e.clientY;
        }

        document.addEventListener('mousemove', document.ORPASearch, {
            passive: true})
    """
    PageJSExecute(lJSStr)


def UIOMouseSearchIsInited():
    global gMouseIsInitBool
    return gMouseIsInitBool

def UIOMouseSearchReturn(inStopSearchBool = True):
    """L+,W+: Возвращает UIO объект, над которым находится указатель мыши. Предварительно должна быть вызвана функция UIWeb.UIOMouseSearchInit
    
    !ВНИМАНИЕ! Для работы необходимо проинициализировать webdriver

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        import time
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        UIWeb.UIOMouseSearchInit()
        time.sleep(3)
        UIWeb.UIOMouseSearchReturn()
        UIWeb.BrowserClose()

    :param inStopSearchBool: True - остановить режим поиска
    :return: UIO объект
    :rtype: webelement
    """    
    lJSStr = """
        document.removeEventListener('mousemove', document.ORPASearch);    
        return document.elementFromPoint(document.ORPAMouseXInt,document.ORPAMouseYInt);
    """
    if inStopSearchBool==False:
        lJSStr = """   
            return document.elementFromPoint(document.ORPAMouseXInt,document.ORPAMouseYInt);
        """
    try:
        global gMouseIsInitBool
        gMouseIsInitBool = False
        return PageJSExecute(lJSStr)
    except JavascriptException: raise JavascriptException("Отсутствуют координаты для идентификации веб-элемента. Пожалуйста, в следующий раз двигайте мышью")

from . import Keyboard

def MouseSearchChild():
    """L+,W+: Инициировать визуальный поиск UIO объекта с помощью указателя мыши. При наведении указателя мыши UIO объект выделяется зеленой рамкой. Остановить режим поиска можно с помощью зажима клавиши ctrl left на протяжении нескольких секунд. После этого в веб окне студии будет отображено дерево расположения искомого UIO объекта.

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        import time
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIO = MouseSearchChild()
        UIWeb.BrowserClose()

    :return: UIO объект или None (если UIO не был обнаружен)
    """
    lGUISearchElementSelected=None
    #Настройка - частота обновления подсвечивания
    lTimeSleepSeconds=0.3
    #Ветка поиска в режиме реального времени
    #Сбросить нажатие Ctrl, если оно было
    #Инициализация
    UIOMouseSearchInit()
    lFlagLoop = True
    lElementFounded=None
    while lFlagLoop:
        #Проверить, нажата ли клавиша Ctrl (код 17)
        lFlagKeyPressedCtrl=Keyboard.IsDown("shift")
        lAltBool=Keyboard.IsDown("ctrl")
        #Подсветить объект, если мышка наведена над тем объектом, который не подсвечивался в прошлый раз
        if not lFlagKeyPressedCtrl:
            #Получить координаты мыши
            if lAltBool == False: # СВЕТИТЬ, НО НЕ ВЫБИРАТЬ
                lElementFounded=UIOMouseSearchReturn(False)
            #Подсветить объект, если он мышь раньше стояла на другом объекте
            if lGUISearchElementSelected != lElementFounded:
                lGUISearchElementSelected = lElementFounded
                UIOHighlight(lElementFounded)
        else:
            #Была нажата клавиша Ctrl - выйти из цикла
            lFlagLoop=False
            lElementFounded=UIOMouseSearchReturn(True)
        #Заснуть до следующего цикла
        time.sleep(lTimeSleepSeconds)
    #Вернуть результат поиска
    return lGUISearchElementSelected


def MouseSearchChildTree(inWaitBeforeSec=0.0):
    """L-,W+: Получить список уровней UIO объекта с указнием всех имеющихся атрибутов.

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIWeb: Взаимодействие с ui web
        from pyOpenRPA.Robot import UIWeb
        import time
        UIWeb.BrowserChromeStart()
        UIWeb.PageOpen("https://mail.ru")
        lUIO = MouseSearchChildTree()
        UIWeb.BrowserClose()

    :param inWaitBeforeSec: Время ожидания перед началом поиска и перефокусировки. Данный аргумент может быть полезен для отображения полезной информации перед инициализацией режима поиска
    :type inWaitBeforeSec: float, необязательный
    :return: list, список атрибутов на каждом уровне UIO объекта
    """
    time.sleep(inWaitBeforeSec)
    lItemInfo = []
    #Получить UI объект, на котором сейчас установлен фокус
    lUIOInitFocused = UIDesktop.GetFocused_UIO()
    #print(f"ФОКУС КОРНЕВОГО ОБЪЕКТА: {lUIOInitFocused}")
    # Установить фокус по родительскому элементу
    BrowserFocus()
    #Запустить функцию поиска элемента по мыши
    lElement = MouseSearchChild()
    #Если объект имеется (не None), то выполнить построение иерархии
    if lElement is not None:
        lJSStr = """
        var deepCopyList = function (list) {
            return JSON.parse(JSON.stringify(list));
        }
        // Get the attributes of the element
        var child = arguments[0]
        var t = child
        var parent_property_dict = null
        var selector_previous = null
        while (t.parentNode !=null) {
            var ui_property_dict = {"title":t.localName , "class_list":[], "style_dict":{}, "node_name": t.nodeName}
            var attributes = t.attributes;
            //DETECT INDEX
            var child_list = t.parentNode.children
            var index = 1
            for (let i in child_list){if (child_list[i] == t){ui_property_dict["ctrl_index"]=index; break;}; index+=1}
            //CREATE SELECTOR
            //if (selector_previous!=null) {
            //    selector_previous = deepCopyList(selector_previous)
            //    selector_previous.unshift({"ctrl_index":ui_property_dict["ctrl_index"]});
            //} else {
            //    selector_previous=[{"ctrl_index":ui_property_dict["ctrl_index"]}]
            // }
            //ui_property_dict["selector"]=selector_previous;
            //ATTR FILL
            if (attributes!=null) {
                for (var i = 0; i < attributes.length; i++) {
                    var name = attributes[i].name;
                    if (name!="style" && name!="class") {
                        var value = attributes[i].value;
                        ui_property_dict[name]=value
                        //console.log(name + " = " + value);
                    }
                }
            }

            //CLASSES
            var classes = t.classList;
            if (classes!=null) {
                for (var i = 0; i < classes.length; i++) {
                    var name = classes[i];
                    //console.log(name);
                    ui_property_dict.class_list.push(name)
                }
            }
            //STYLES
            var style = t.style
            if (style!=null) {
                for (var i = 0; i < style.length; i++) {
                    var value = style[style[i]]
                    if (value!=null) {
                        ui_property_dict.style_dict[style[i]]=value        
                    }
                }
            }
            t = t.parentNode
            //Добавление в результат
            if (parent_property_dict==null) {
                parent_property_dict = ui_property_dict
                parent_property_dict["child_list"]=[]
            } else {
                ui_property_dict["child_list"] = [parent_property_dict]
                parent_property_dict = ui_property_dict
            }
        }
        return [parent_property_dict]

        """
        return PageJSExecute(lJSStr, lElement)

    #Вернуть фокус исходному окну по итогу отработки
    try:
        #print(f"ВЕРНУТЬ ФОКУС НА КОРНЕВОЙ ОБЪЕКТ СТУДИЮ")
        lUIOInitFocused.set_focus()
    except Exception as e:
        pass
    #Вернуть результат
    return lItemInfo
