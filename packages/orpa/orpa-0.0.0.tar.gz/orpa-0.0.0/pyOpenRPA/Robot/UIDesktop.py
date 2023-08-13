from pyOpenRPA.Tools import CrossOS
if CrossOS.IS_WINDOWS_BOOL:
    from pywinauto import win32defines, win32structures, win32functions
    import pywinauto
    import win32api

import ctypes
import struct
import json
import time
from .Utils import ProcessCommunicator
from . import Utils #For ProcessBitness
from pyOpenRPA.Tools import Usage
from pyOpenRPA.Tools import License
import re, fnmatch
import copy
import psutil
import inspect

############################################
# When import UIDesktop init the other bitness python
# For this type
# UIDesktop.Utils.ProcessBitness.SettingsInit(inSettingsDict)
# inSettingsDict = {
#    "Python32FullPath": None, #Set from user: "..\\Resources\\WPy32-3720\\python-3.7.2\\OpenRPARobotGUIx32.exe"
#    "Python64FullPath": None, #Set from user
#    "Python32ProcessName": "OpenRPAUIDesktopX32.exe", #Config set once
#    "Python64ProcessName": "OpenRPAUIDesktopX64.exe" #Config set once
#}
############################################

#logging.basicConfig(filename="Reports\ReportRobotGUIRun_"+datetime.datetime.now().strftime("%Y_%m_%d")+".log", level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

####################################
#Info: GUI module of the Robot app (pyOpenRPA - Robot)
####################################
# GUI Module - interaction with Desktop application

#GUI Naming convention
#<InArgument>_<ActivityName>_<OutArgument - if exist>

#UIO - UI Object (class of pywinauto UI object)
#UIOSelector - List of dict (key attributes)
#PWA - PyWinAuto
#PWASpecification - List of dict (key attributes in pywinauto.find_window notation)
#UIOTree - Recursive Dict of Dict ... (UI Parent -> Child hierarchy)
#UIOInfo - Dict of UIO attributes
#UIOActivity - Activity of the UIO (UI object) from the Pywinauto module
#UIOEI - UI Object info object

#inActivitySpecificationDict:
#{
#   ModuleName: <"GUI", str>, - optional
#   ActivityName: <Function or procedure name in module, str>,
#   ArgumentList: [<Argument 1, any type>, ...] - optional,
#   ArgumentDict: {<Argument 1 name, str>:<Argument 1 value, any type>, ...} - optional
#}

#outActivityResultDict:
#{
#   ActivitySpecificationDict: {
#       ModuleName: <"GUI", str>, -optional
#       ActivityName: <Function or procedure name in module, str>,
#       ArgumentList: [<Argument 1, any type>, ...] - optional,
#       ArgumentDict: {<Argument 1 name, str>: <Argument 1 value, any type>, ...} - optional
#   },
#   ErrorFlag: <Boolean flag - Activity result has error (true) or not (false), boolean>,
#   ErrorMessage: <Error message, str> - required if ErrorFlag is true,
#   ErrorTraceback: <Error traceback log, str> - required if ErrorFlag is true,
#   Result: <Result, returned from the Activity, int, str, boolean, list, dict> - required if ErrorFlag is false
#}

#inUIOSelector:
#[
#   {
#       "index":<Позиция элемента в родительском объекте>,
#       "depth_start" - глубина, с которой начинается поиск (по умолчанию 1),
#       "depth_end" - глубина, до которой ведется поиск (по умолчанию 1),
#       "class_name" - наименование класса, который требуется искать,
#       "title" - наименование заголовка,
#       "rich_text" - наименование rich_text,
#       "backend": <"win32"||"uia", only for the 1-st list element> - if not specified, use mDefaultPywinautoBackend
#   },
#   { ... }
#
#]
from ..Utils import __define__
#Default parameters
mDefaultPywinautoBackend="win32"
if CrossOS.IS_WINDOWS_BOOL == False:
    mDefaultPywinautoBackend="at-spi"

############################
#Новая версия
############################
#Получить список элементов, который удовлетворяет условиям через расширенный движок поиска
#[
#   {
#       "index":<Позиция элемента в родительском объекте>,
#       "depth_start" - глубина, с которой начинается поиск (по умолчанию 1)
#       "depth_end" - глубина, до которой ведется поиск (по умолчанию 1)
#       "class_name" - наименование класса, который требуется искать
#       "title" - наименование заголовка
#       "rich_text" - наименование rich_text
#   }
#]


#old:PywinautoExtElementsGet
def UIOSelector_Get_UIOList (inSpecificationList,inElement=None,inFlagRaiseException=True):
    '''L+,W+: Получить список UIO объектов по UIO селектору
    
    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lDemoBaseUIOList = UIDesktop.UIOSelector_Get_UIOList(lDemoBaseUIOSelector) #Получить список UIO объектов, которые удовлетворяют требованиям UIO селектора. В нашем примере либо [], либо [UIO объект]

    :param inSpecificationList: UIO Селектор, который определяет критерии поиска UI элементов
    :type inSpecificationList: list, обязательный
    :param inElement: Родительский элемент, от которого выполнить поиск UIO объектов по заданному UIO селектору. Если аргумент не задан, платформа выполнит поиск UIO объектов среди всех доступных приложений windows, которые запущены на текущей сессии
    :type inElement: UIO объект, опциональный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    :return: Список UIO объектов, которые удовлетворяют условиям UIO селектора
    '''
    global mDefaultPywinautoBackend
    lResultList=[]
    if inSpecificationList==None: inSpecificationList=[]
    if inSpecificationList==[]:
        #Получить список объектов    
        lResultList=pywinauto.findwindows.find_elements(top_level_only=True,backend=mDefaultPywinautoBackend)
        return lResultList
    #Конвертация селектора в формат UIO
    inSpecificationList = Selector_Convert_Selector(inSelector=inSpecificationList, inToTypeStr="UIO")
    #Создать копию входного листа, чтобы не менять массив в других верхнеуровневых функциях
    inSpecificationList=copy.deepcopy(inSpecificationList)
    lResultList=[]
    lChildrenList=[]
    try:
        #Получить родительский объект если на вход ничего не поступило
        if inElement is None:
            #Обработка глубины depth
            if 'depth_end' in inSpecificationList[0]:
                    if inSpecificationList[0]['depth_end']>1:
                        #Поиск элемента на верхнем уровне
                        inSpecificationTmpList = copy.deepcopy(inSpecificationList)
                        inSpecificationTmpList[0].pop("depth_start")
                        inSpecificationTmpList[0].pop("depth_end")
                        lResultList.extend(UIOSelector_Get_UIOList(inSpecificationTmpList,inFlagRaiseException=False))

                        if lResultList == []:#На верхнем уровне элемент найти не удалось - поиск по дереву
                            for lElement in UIOSelector_GetChildList_UIOList(inBackend="uia"):
                                lChildrenItemNewSpecificationList=inSpecificationList.copy()
                                lChildrenItemNewSpecificationList[0]=lChildrenItemNewSpecificationList[0].copy()
                                lChildrenItemNewSpecificationList[0]["depth_end"]=lChildrenItemNewSpecificationList[0]["depth_end"]-1
                                if 'depth_start' in lChildrenItemNewSpecificationList[0]:
                                    lChildrenItemNewSpecificationList[0]["depth_start"]=lChildrenItemNewSpecificationList[0]["depth_start"]-1
                                #Циклический вызов для всех детей со скорректированной спецификацией
                                lElementTmpList=PWASpecification_Get_UIO([lElement])
                                lResultList.extend(UIOSelector_Get_UIOList(lChildrenItemNewSpecificationList,lElementTmpList[0],inFlagRaiseException))
            else:
                #сформировать спецификацию на получение элемента
                lRootElementSpecification=[inSpecificationList[0]]
                lRootElementList=PWASpecification_Get_UIO(lRootElementSpecification)
                if "ctrl_index" in inSpecificationList[0]:
                    lIndexInt = inSpecificationList[0]["ctrl_index"]
                    if lIndexInt<len(lRootElementList):
                        lChildrenList.append(lRootElementList[lIndexInt].wrapper_object())
                else:
                    for lRootItem in lRootElementList:
                        if lRootItem is not None:
                            lChildrenList.append(lRootItem.wrapper_object())
        #Елемент на вход поступил - выполнить его анализ
        else:
            #Обработка якоря go_up по необходимости
            if 'go_up' in inSpecificationList[0]:
                try:
                    #Поднимаемся по уровням наверх
                    for i in range(int(inSpecificationList[0]['go_up'])):
                        inElement = inElement.parent()
                    #Обработка случая наличия go_up (отключение дальнешей проверки на этом уровне)
                    lElementChildrenList = []
                    if inElement is None: raise AttributeError("Nonetype error")
                    lChildrenList.append(inElement)
                except AttributeError: 
                    if inFlagRaiseException: raise pywinauto.findwindows.ElementNotFoundError('Value of the "go_up" attribute is too large')
                    else: return []
            #Обработка якоря shift по необходимости
            elif 'shift' in inSpecificationList[0]:
                try:
                    #Поднимаемся на один уровень 
                    inElementParentChildrenList = inElement.parent().children()
                    for index, lNewChildren in enumerate(inElementParentChildrenList): #Ищем индекс текущего элемента внутри списка всех детей от родителя
                        if inElement == lNewChildren: #По нахождению делаем необходимый переход
                            if int(inSpecificationList[0]['shift']) > 0: inElement = inElementParentChildrenList[index+int(inSpecificationList[0]['shift'])]
                            else: 
                                if index-abs(int(inSpecificationList[0]['shift'])) < 0: raise IndexError("Bad value error")
                                inElement = inElementParentChildrenList[index-abs(int(inSpecificationList[0]['shift']))]
                            break
                    #Обработка случая наличия shift (отключение дальнешей проверки на этом уровне)
                    lElementChildrenList = []
                    lChildrenList.append(inElement)
                except IndexError: 
                    if inFlagRaiseException: raise pywinauto.findwindows.ElementNotFoundError('Value of the "shift" attribute is too large')
                    else: return []
            else: # если нет атрибута go_up и/или shift
                #Получить список элементов
                lElementChildrenList=inElement.children()
                #Если нет точного обозначения элемента
                lFlagGoCheck=True
            #Учесть поле depth_start (если указано)
            if 'depth_start' in inSpecificationList[0]:
                if inSpecificationList[0]["depth_start"]>1:
                    lFlagGoCheck=False

            #Циклический обход по детям, на предмет соответствия всем условиям
            lFilterList = []
            for index, lChildrenItem in enumerate(lElementChildrenList):
                #Обработка глубины depth (рекурсивный вызов для всех детей с занижением индекса глубины)
                #По умолчанию значение глубины 1
                if 'depth_end' in inSpecificationList[0]:
                    if inSpecificationList[0]['depth_end']>1:
                        #Подготовка новой версии спецификации
                        lChildrenItemNewSpecificationList=inSpecificationList.copy()
                        lChildrenItemNewSpecificationList[0]=lChildrenItemNewSpecificationList[0].copy()
                        lChildrenItemNewSpecificationList[0]["depth_end"]=lChildrenItemNewSpecificationList[0]["depth_end"]-1
                        if 'depth_start' in lChildrenItemNewSpecificationList[0]:
                            lChildrenItemNewSpecificationList[0]["depth_start"]=lChildrenItemNewSpecificationList[0]["depth_start"]-1
                        #Циклический вызов для всех детей со скорректированной спецификацией
                        lResultList.extend(UIOSelector_Get_UIOList(lChildrenItemNewSpecificationList,lChildrenItem,inFlagRaiseException))
                #Фильтрация
                if lFlagGoCheck:
                    lFlagAddChild=True
                    #Фильтрация по index
                    if 'index' in inSpecificationList[0]:
                        if inSpecificationList[0]['index']!= index:
                            lFlagAddChild=False
                    #Фильтрация по title
                    if 'title' in inSpecificationList[0]:
                        if lChildrenItem.element_info.name != inSpecificationList[0]["title"]:
                            lFlagAddChild=False
                    #Фильтрация по title_re (regexp)
                    if 'title_re' in inSpecificationList[0]:
                        if re.fullmatch(inSpecificationList[0]["title_re"],lChildrenItem.element_info.name) is None:
                            lFlagAddChild=False
                    #Фильтрация по title_wc (wildcard)
                    if 'title_wc' in inSpecificationList[0]:
                        if fnmatch.fnmatch(lChildrenItem.element_info.name, inSpecificationList[0]["title_wc"]) == False:
                            lFlagAddChild=False
                    #Фильтрация по rich_text
                    if 'rich_text' in inSpecificationList[0]:
                        if lChildrenItem.element_info.rich_text != inSpecificationList[0]["rich_text"]:
                            lFlagAddChild=False
                    #Фильтрация по rich_text_re (regexp)
                    if 'rich_text_re' in inSpecificationList[0]:
                        if re.fullmatch(inSpecificationList[0]["rich_text_re"],lChildrenItem.element_info.rich_text) is None:
                            lFlagAddChild=False
                    #Фильтрация по rich_text_wc (wildcard)
                    if 'rich_text_wc' in inSpecificationList[0]:
                        if fnmatch.fnmatch(lChildrenItem.element_info.rich_text, inSpecificationList[0]["rich_text_wc"]) == False:
                            lFlagAddChild=False
                    #Фильтрация по class_name
                    if 'class_name' in inSpecificationList[0]:
                        if lChildrenItem.element_info.class_name != inSpecificationList[0]["class_name"]:
                            lFlagAddChild=False
                    #Фильтрация по class_name_re (regexp)
                    if 'class_name_re' in inSpecificationList[0]:
                        if re.fullmatch(inSpecificationList[0]["class_name_re"],lChildrenItem.element_info.class_name) is None:
                            lFlagAddChild=False
                    #Фильтрация по class_name_wc (wildcard)
                    if 'class_name_wc' in inSpecificationList[0]:
                        if fnmatch.fnmatch(lChildrenItem.element_info.class_name, inSpecificationList[0]["class_name_wc"]) == False:
                            lFlagAddChild=False
                    #Фильтрация по friendly_class_name
                    if 'friendly_class_name' in inSpecificationList[0]:
                        if lChildrenItem.friendly_class_name() != inSpecificationList[0]["friendly_class_name"]:
                            lFlagAddChild=False
                    #Фильтрация по friendly_class_name_re (regexp)
                    if 'friendly_class_name_re' in inSpecificationList[0]:
                        if re.fullmatch(inSpecificationList[0]["friendly_class_name_re"],lChildrenItem.friendly_class_name()) is None:
                            lFlagAddChild=False
                    #Фильтрация по friendly_class_name_wc (wildcard)
                    if 'friendly_class_name_wc' in inSpecificationList[0]:
                        if fnmatch.fnmatch(lChildrenItem.friendly_class_name(), inSpecificationList[0]["friendly_class_name_wc"]) == False:
                            lFlagAddChild=False
                    #Фильтрация по control_type
                    if 'control_type' in inSpecificationList[0]:
                        if lChildrenItem.element_info.control_type != inSpecificationList[0]["control_type"]:
                            lFlagAddChild=False
                    #Фильтрация по control_type_re (regexp)
                    if 'control_type_re' in inSpecificationList[0]:
                        if re.fullmatch(inSpecificationList[0]["control_type_re"],lChildrenItem.element_info.control_type) is None:
                            lFlagAddChild=False
                    #Фильтрация по control_type_wc (wildcard)
                    if 'control_type_wc' in inSpecificationList[0]:
                        if fnmatch.fnmatch(lChildrenItem.element_info.control_type, inSpecificationList[0]["control_type_wc"]) == False:
                            lFlagAddChild=False
                    #Фильтрация по process_name
                    if 'process_name' in inSpecificationList[0]:
                        if psutil.Process(int(lChildrenItem.element_info.process_id)).name() != inSpecificationList[0]["process_name"]:
                            lFlagAddChild=False
                    #Фильтрация по process_name_re (regexp)
                    if 'process_name_re' in inSpecificationList[0]:
                        if re.fullmatch(inSpecificationList[0]["process_name_re"],psutil.Process(int(lChildrenItem.element_info.process_id)).name()) is None:
                            lFlagAddChild=False
                    #Фильтрация по process_name_wc (wildcard)
                    if 'process_name_wc' in inSpecificationList[0]:
                        if fnmatch.fnmatch(psutil.Process(int(lChildrenItem.element_info.process_id)).name(), inSpecificationList[0]["process_name_wc"]) == False:
                            lFlagAddChild=False
                    #Фильтрация по is_enabled (bool)
                    if 'is_enabled' in inSpecificationList[0]:
                        if lChildrenItem.is_enabled()!=inSpecificationList[0]["is_enabled"]:
                            lFlagAddChild=False
                    #Фильтрация по is_visible (bool)
                    if 'is_visible' in inSpecificationList[0]:
                        if lChildrenItem.is_visible()!=inSpecificationList[0]["is_visible"]:
                            lFlagAddChild=False
                    #####
                    #Все проверки пройдены - флаг добавления
                    if lFlagAddChild:
                        lFilterList.append(lChildrenItem)
            if "ctrl_index" in inSpecificationList[0]:
                lIndexInt = inSpecificationList[0]["ctrl_index"]
                if lIndexInt<len(lFilterList):
                    lChildrenList.append(lFilterList[lIndexInt])
            else:
                lChildrenList.extend(lFilterList)                
        #Выполнить рекурсивный вызов (уменьшение количества спецификаций), если спецификация больше одного элемента
        #????????Зачем в условии ниже is not None ???????????
        if len(inSpecificationList)>1 and len(lChildrenList)>0:
            #Вызвать рекурсивно функцию получения следующего объекта, если в спецификации есть следующий объект
            for lChildElement in lChildrenList:
                lResultList.extend(UIOSelector_Get_UIOList(inSpecificationList[1:],lChildElement,inFlagRaiseException))
        else:
            lResultList.extend(lChildrenList)
        #Условие, если результирующий список пустой и установлен флаг создания ошибки (и inElement is None - не следствие рекурсивного вызова)
        if inElement is None and len(lResultList)==0 and inFlagRaiseException:
            raise pywinauto.findwindows.ElementNotFoundError("Robot can't find element by the UIOSelector")
        if __define__.DEFINE_ACCEPTED==True: return lResultList
        else: return []

    except Exception as e:
        if inFlagRaiseException: raise e
        else: return []

#old:PywinautoExtElementGet
def UIOSelector_Get_UIO (inSpecificationList,inElement=None,inFlagRaiseException=True):
    '''L+,W+: Получить список UIO объект по UIO селектору. Если критериям UIO селектора удовлетворяет несколько UIO объектов - вернуть первый из списка
    
    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lDemoBaseUIOList = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) #Получить 1-й UIO объект, которые удовлетворяет требованиям UIO селектора. В нашем примере либо None, либо UIO объект

    :param inSpecificationList: UIO Селектор, который определяет критерии поиска UI элементов
    :type inSpecificationList: list, обязательный
    :param inElement: Родительский элемент, от которого выполнить поиск UIO объектов по заданному UIO селектору. Если аргумент не задан, платформа выполнит поиск UIO объектов среди всех доступных приложений windows, которые запущены на текущей сессии
    :type inElement: UIO объект, опциональный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай. По умолчанию True
    :type inFlagRaiseException: bool, опциональный
    :return: UIO объект, которые удовлетворяют условиям UIO селектора, или None
    '''
    #Конвертация селектора в формат UIO
    inSpecificationList = Selector_Convert_Selector(inSelector=inSpecificationList, inToTypeStr="UIO")
    lResult=None
    #Получить родительский объект если на вход ничего не поступило
    lResultList=UIOSelector_Get_UIOList(inSpecificationList,inElement,inFlagRaiseException)
    if len(lResultList)>0:
        lResult=lResultList[0]
    return lResult
    
#old:-
def UIOSelector_Exist_Bool (inUIOSelector, inFlagRaiseException=True):
    '''L+,W+: Проверить существование хотя бы 1-го UIO объекта по заданному UIO селектору
    
    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())
    
    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lDemoBaseUIOExistBool = UIDesktop.UIOSelector_Exist_Bool(lDemoBaseUIOSelector) # Получить булевый результат проверки существования UIO объекта

    :param inUIOSelector: UIO Селектор, который определяет критерии поиска UIO объектов
    :type inUIOSelector: list, обязательный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    :return: True - существует хотя бы 1 UIO объект. False - не существует ни одного UIO объекта по заданному UIO селектору
    '''
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    lResult=False
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        #Получить родительский объект если на вход ничего не поступило
        try:
            lResultList=UIOSelector_Get_UIOList(inUIOSelector, None, inFlagRaiseException)
        except pywinauto.findwindows.ElementNotFoundError: return False
        if len(lResultList)>0:
            lResult=True
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_Exist_Bool",
                            "ArgumentList": [inUIOSelector],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            lResult = lPIPEResponseDict["Result"]
    return lResult

#old: -
def UIOSelectorsSecs_WaitAppear_List (inSpecificationListList,inWaitSecs=86400.0,inFlagWaitAllInMoment=False, inFlagRaiseException=True):
    '''L+,W+: Ожидать появление хотя бы 1-го / всех UIO объектов по заданным UIO селекторам
    
    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())
    
    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lNotepadOKSelector = [{"title":"notepad"},{"title":"OK"}]
        lNotepadCancelSelector = [{"title":"notepad"},{"title":"Cancel"}]
        lDemoBaseUIOExistList = UIDesktop.UIOSelectorsSecs_WaitAppear_List([lDemoBaseUIOSelector, lNotepadOKSelector, lNotepadCancelSelector]) # Ожидать появление UIO объекта

    :param inSpecificationListList: Список UIO селекторов, которые определяют критерии поиска UIO объектов
            Пример: [
            [{"title":"notepad"},{"title":"OK"}],
            [{"title":"notepad"},{"title":"Cancel"}]
        ]
    :type inSpecificationListList: list, обязательный
    :param inWaitSecs: Количество секунд, которые отвести на ожидание UIO объектов. По умолчанию 24 часа (86400 секунд)
    :type inWaitSecs: float, необязательный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    :param inFlagWaitAllInMoment: True - Ожидать до того момента, пока не появятся все запрашиваемые UIO объекты на рабочей области
    :return: Список индексов, которые указывают на номер входящих UIO селекторов, которые были обнаружены на рабочей области. Пример: [0,2]
    '''
    #Конвертация селектора в формат UIO
    inSpecificationListList = Selector_Convert_Selector(inSelector=inSpecificationListList, inToTypeStr="UIO")
    lResultFlag=False
    lSecsSleep = 1 #Настроечный параметр
    lSecsDone = 0
    lResultList = None
    #Цикл проверки
    while lResultFlag == False and lSecsDone<inWaitSecs:
        #pdb.set_trace()
        lResultList=[]
        #Итерация проверки
        lIndex = 0
        for lItem in inSpecificationListList:
            lItemResultFlag=UIOSelector_Exist_Bool(lItem, inFlagRaiseException=True)
            #Если обнаружен элемент - добавить его индекс в массив
            if lItemResultFlag:
                lResultList.append(lIndex)
            #Инкремент индекса
            lIndex=lIndex + 1
        #Проверка в зависимости от флага
        if inFlagWaitAllInMoment and len(lResultList)==len(inSpecificationListList):
            #Условие выполнено
            lResultFlag=True
        elif not inFlagWaitAllInMoment and len(lResultList)>0:
            #Условие выполнено
            lResultFlag=True
        #Если флаг не изменился - увеличить время и уснуть
        if lResultFlag == False:
            lSecsDone=lSecsDone+lSecsSleep
            time.sleep(lSecsSleep)
    return lResultList

#old: -
def UIOSelectorsSecs_WaitDisappear_List (inSpecificationListList,inWaitSecs=86400.0,inFlagWaitAllInMoment=False, inFlagRaiseException=True):
    '''L+,W+:  Ожидать исчезновение хотя бы 1-го / всех UIO объектов по заданным UIO селекторам
    
    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())
    
    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lNotepadOKSelector = [{"title":"notepad"},{"title":"OK"}]
        lNotepadCancelSelector = [{"title":"notepad"},{"title":"Cancel"}]
        lDemoBaseUIOExistList = UIDesktop.UIOSelectorsSecs_WaitDisappear_List([lDemoBaseUIOSelector, lNotepadOKSelector, lNotepadCancelSelector]) # Ожидать исчезновение UIO объектов

    :param inSpecificationListList: Список UIO селекторов, которые определяют критерии поиска UIO объектов
            Пример: [
            [{"title":"notepad"},{"title":"OK"}],
            [{"title":"notepad"},{"title":"Cancel"}]
        ]
    :type inSpecificationListList: list, обязательный
    :param inWaitSecs: Количество секунд, которые отвести на ожидание исчезновения UIO объектов. По умолчанию 24 часа (86400 секунд)
    :type inWaitSecs: float, необязательный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    :param inFlagWaitAllInMoment: True - Ожидать до того момента, пока не исчезнут все запрашиваемые UIO объекты на рабочей области
    :return: Список индексов, которые указывают на номер входящих UIO селекторов, которые были обнаружены на рабочей области. Пример: [0,2]
    '''
    #Конвертация селектора в формат UIO
    inSpecificationListList = Selector_Convert_Selector(inSelector=inSpecificationListList, inToTypeStr="UIO")
    lResultFlag=False
    lSecsSleep = 1 #Настроечный параметр
    lSecsDone = 0
    lResultList = None
    #Цикл проверки
    while lResultFlag == False and lSecsDone<inWaitSecs:
        #pdb.set_trace()
        lResultList=[]
        #Итерация проверки
        lIndex = 0
        for lItem in inSpecificationListList:
            lItemResultFlag=UIOSelector_Exist_Bool(lItem,inFlagRaiseException=inFlagRaiseException)
            #Если обнаружен элемент - добавить его индекс в массив
            if not lItemResultFlag:
                lResultList.append(lIndex)
            #Инкремент индекса
            lIndex=lIndex + 1
        #Проверка в зависимости от флага
        if inFlagWaitAllInMoment and len(lResultList)==len(inSpecificationListList):
            #Условие выполнено
            lResultFlag=True
        elif not inFlagWaitAllInMoment and len(lResultList)>0:
            #Условие выполнено
            lResultFlag=True
        #Если флаг не изменился - увеличить время и уснуть
        if lResultFlag == False:
            lSecsDone=lSecsDone+lSecsSleep
            time.sleep(lSecsSleep)
    return lResultList

#old: -
def UIOSelectorSecs_WaitAppear_Bool (inSpecificationList,inWaitSecs, inFlagRaiseException=True):
    '''L+,W+: Ожидать появление 1-го UIO объекта по заданному UIO селектору
    
    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())
    
    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lDemoBaseUIOExistBool = UIDesktop.UIOSelectorSecs_WaitAppear_Bool(lDemoBaseUIOSelector) # Ожидать появление UIO объекта

    :param inSpecificationList: UIO селектор, который определяет критерии поиска UIO объекта
    :type inSpecificationList: list, обязательный
    :param inWaitSecs: Количество секунд, которые отвести на ожидание UIO объекта. По умолчанию 24 часа (86400 секунд)
    :type inWaitSecs: float, необязательный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    :return: True - UIO объект был обнаружен. False - обратная ситуациая
    '''
    #Конвертация селектора в формат UIO
    inSpecificationList = Selector_Convert_Selector(inSelector=inSpecificationList, inToTypeStr="UIO")
    lWaitAppearList=UIOSelectorsSecs_WaitAppear_List([inSpecificationList],inWaitSecs, inFlagRaiseException=inFlagRaiseException)
    lResult=False
    if len(lWaitAppearList)>0:
        lResult=True
    return lResult

#old name - -
def UIOSelectorSecs_WaitDisappear_Bool (inSpecificationList,inWaitSecs,inFlagRaiseException=True):
    '''L+,W+: Ожидать исчезновение 1-го UIO объекта по заданному UIO селектору
    
    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())
    
    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lDemoBaseUIOExistBool = UIDesktop.UIOSelectorSecs_WaitDisappear_Bool(lDemoBaseUIOSelector) # Ожидать исчезновение UIO объекта

    :param inSpecificationList: UIO селектор, который определяет критерии поиска UIO объекта
    :type inSpecificationList: list, обязательный
    :param inWaitSecs: Количество секунд, которые отвести на исчезновение UIO объекта. По умолчанию 24 часа (86400 секунд)
    :type inWaitSecs: float, необязательный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    :return: True - UIO объект был обнаружен. False - обратная ситуациая
    '''
    #Конвертация селектора в формат UIO
    inSpecificationList = Selector_Convert_Selector(inSelector=inSpecificationList, inToTypeStr="UIO")
    lWaitDisappearList=UIOSelectorsSecs_WaitDisappear_List([inSpecificationList],inWaitSecs,inFlagRaiseException=inFlagRaiseException)
    lResult=False
    if len(lWaitDisappearList)>0:
        lResult=True
    return lResult

#old: -
def UIOSelector_Get_BitnessInt (inSpecificationList):
    '''L+,W+: Определить разрядность приложения по UIO селектору. Вернуть результат в формате целого числа (64 или 32)

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lDemoBaseBitInt = UIDesktop.UIOSelector_Get_BitnessInt(lDemoBaseUIOSelector) # Определить разрядность приложения, в котором обнаружен UIO объект по селектору

    :param inSpecificationList: UIO селектор, который определяет критерии поиска UIO объекта
    :type inSpecificationList: list, обязательный
    :return: None - UIO объект не обнаружен; 64 (int) - разрядность приложения равна 64 битам; 32 (int) - разрядность приложения равна 32 битам
    '''
    #Конвертация селектора в формат UIO
    if CrossOS.IS_WINDOWS_BOOL==True:
        inSpecificationList = Selector_Convert_Selector(inSelector=inSpecificationList, inToTypeStr="UIO")
        lResult=None
        #Получить объект Application (Для проверки разрядности)
        lRootElement=PWASpecification_Get_PWAApplication(inSpecificationList)
        if lRootElement is not None:
            if lRootElement.is64bit():
                lResult=64
            else:
                lResult=32
        return lResult
    else: return 64


#old: -
def UIOSelector_Get_BitnessStr (inSpecificationList):
    """L+,W+: Определить разрядность приложения по UIO селектору. Вернуть результат в формате строки ("64" или "32")

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lDemoBaseBitStr = UIDesktop.UIOSelector_Get_BitnessStr(lDemoBaseUIOSelector) # Определить разрядность приложения, в котором обнаружен UIO объект по селектору

    :param inSpecificationList: UIO селектор, который определяет критерии поиска UIO объекта
    :type inSpecificationList: list, обязательный
    :return: None - UIO объект не обнаружен; "64" (str) - разрядность приложения равна 64 битам; "32" (str) - разрядность приложения равна 32 битам
    """
    if CrossOS.IS_WINDOWS_BOOL==True:
        #Конвертация селектора в формат UIO
        inSpecificationList = Selector_Convert_Selector(inSelector=inSpecificationList, inToTypeStr="UIO")
        lResult=None
        #Получить объект Application (Для проверки разрядности)
        lRootElement=PWASpecification_Get_PWAApplication(inSpecificationList)
        if lRootElement is not None:
            if lRootElement.is64bit():
                lResult="64"
            else:
                lResult="32"
        return lResult
    else:
        return "64"

#old: -
def Get_OSBitnessInt ():
    '''L+,W+: Определить разрядность робота, в котором запускается данная функция

    .. code-block:: python

        from pyOpenRPA.Robot import UIDesktop
        lRobotBitInt = UIDesktop.Get_OSBitnessInt() # Определить разрядность робота, в котором была вызвана это функция
    
    :return: 64 (int) - разрядность приложения равна 64 битам; 32 (int) - разрядность приложения равна 32 битам
    '''
    if CrossOS.IS_WINDOWS_BOOL==True:
        lResult=32
        if pywinauto.sysinfo.is_x64_OS():
            lResult=64
        return lResult
    else: return 64
#old: -
def UIOSelector_SafeOtherGet_Process(inUIOSelector):
    """L+,W+: Получить процесс робота другой разрядности (если приложение UIO объекта выполняется в другой разрядности). Функция возвращает None, если разрядность робота совпадает с разрядностью приложения UIO объекта, либо если при инициализации робота не устанавливался интерпретатор другой разрядности.

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"},{"title":"DEMO", "depth_start": 5, "depth_end": 5}]		
        lOtherBitnessProcess = UIDesktop.UIOSelector_SafeOtherGet_Process(lDemoBaseUIOSelector) # Вернуть процесс робота, схожей разрядности

    :param inUIOSelector: UIO селектор, который определяет критерии поиска UIO объекта
    :type inUIOSelector: list, обязательный
    :return: Процесс робота схожей разрядности
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Default value
    lResult = None
    return None # Функция доступна в рамках премиальной поддержки ОПЕН РПА
    #Go check bitness if selector exists
    if inUIOSelector:
        #Get selector bitness
        lUIOSelectorAppBitness = UIOSelector_Get_BitnessStr(inUIOSelector)
        if lUIOSelectorAppBitness and Utils.ProcessBitness.mSettingsDict["BitnessProcessCurrent"] != lUIOSelectorAppBitness:
            lResult = Utils.ProcessBitness.OtherProcessGet()
    return lResult
#old: GetControl
def PWASpecification_Get_UIO(inControlSpecificationArray):
    """L-,W+: Получить UIO объект по PWA (pywinauto) селектору. (https://pywinauto.readthedocs.io/en/latest/code/pywinauto.findwindows.html). Мы рекомендуем использовать метод UIOSelector_UIO_Get, так как UIO селектор обладает большей функциональностью.

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIOObject = UIDesktop.PWASpecification_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по PWA селектору

    :param inControlSpecificationArray: PWA селектор, который определяет критерии поиска UIO объекта
        Допустимые ключи PWA селектора:

        - class_name содержимое атрибута class UIO объекта
        - class_name_re содержимое атрибута class UIO объекта, которое удовлетворяет установленному рег. выражению
        - process идентификатор процесса, в котором находится UIO объект
        - title содержимое атрибута title UIO объекта
        - title_re содержимое атрибута title UIO объекта, которое удовлетворяет установленному рег. выражению
        - top_level_only признак поиска только на верхнем уровне приложения. По умолчанию True
        - visible_only признак поиска только среди видимых UIO объектов. По умолчанию True
        - enabled_only признак поиска только среди разблокированных UIO объектов. По умолчанию False
        - best_match содержимое атрибута title UIO объекта максимально приближено к заданному
        - handle идентификатор handle искомого UIO объекта 
        - ctrl_index индекс UIO объекта среди всех дочерних объектов в списке родительского
        - found_index индекс UIO объекта среди всех обнаруженных
        - predicate_func пользовательская функция проверки соответсвия UIO элемента
        - active_only признак поиска только среди активных UIO объектов. По умолчанию False
        - control_id идентификатор control_id искомого UIO объекта 
        - control_type тип элемента (применимо, если backend == "uia")
        - auto_id идентификатор auto_id искомого UIO объекта (применимо, если backend == "uia")
        - framework_id идентификатор framework_id искомого UIO объекта (применимо, если backend == "uia")
        - backend вид технологии подключения к поиску UIO объекта ("uia" или "win32")
    :type inControlSpecificationArray: list, обязательный
    :return: UIO объект
    """
    #Определение backend
    lBackend=mDefaultPywinautoBackend
    if "backend" in inControlSpecificationArray[0]:
        lBackend=inControlSpecificationArray[0]["backend"]
        inControlSpecificationArray[0].pop("backend")
    #Подготовка входного массива
    inControlSpecificationOriginArray=copy.deepcopy(inControlSpecificationArray)
    inControlSpecificationArray=UIOSelector_SearchProcessNormalize_UIOSelector(inControlSpecificationArray)
    #Выполнить идентификацию объектов, если передан массив
    lResultList=[]
    lTempObject=None
    if len(inControlSpecificationArray) > 0:
        #Сформировать выборку элементов, которые подходят под первый уровень спецификации
        lSpecDeepCopy = copy.deepcopy(inControlSpecificationArray)
        lSpecDeepCopy[0]["backend"]=lBackend
        lSpecificationLvL1List = pywinauto.findwindows.find_elements(**lSpecDeepCopy[0])
        for lItem in lSpecificationLvL1List:
            #Сделать независимую копию и установить информацию о process_id и handle
            lItemControlSpecificationArray=copy.deepcopy(inControlSpecificationArray)
            lItemControlSpecificationArray[0]["process_id"]=lItem.process_id
            lItemControlSpecificationArray[0]["handle"]=lItem.handle
            lItemControlSpecificationOriginArray=copy.deepcopy(inControlSpecificationOriginArray)
            lItemControlSpecificationOriginArray[0]["process_id"]=lItem.process_id
            lItemControlSpecificationOriginArray[0]["handle"]=lItem.handle
            #Выполнить подключение к объекту
            lRPAApplication = pywinauto.Application(backend=lBackend)
            #Проверка разрядности
            try:
                lRPAApplication.connect(**lItemControlSpecificationArray[0])
            except Exception as e:
                UIOSelector_TryRestore_Dict(lItemControlSpecificationArray)
                try:
                    lRPAApplication.connect(**lItemControlSpecificationArray[0])
                except Exception as e:
                    lRPAApplication = None
            if lRPAApplication is not None:
                #lTempObject=lRPAApplication.window(**lItemControlSpecificationArray[0])
                #Скорректировано из-за недопонимания структуры
                lTempObject=lRPAApplication
                #Нормализация массива для целей выборки объекта (удаление конфликтующих ключей)
                lItemControlSpecificationArray=UIOSelector_SearchUIONormalize_UIOSelector(lItemControlSpecificationOriginArray)
                #Циклическое прохождение к недрам объекта
                for lWindowSpecification in lItemControlSpecificationArray[0:]:
                    lTempObject=lTempObject.window(**lWindowSpecification)
                #Добавить объект в результирующий массив
                lResultList.append(lTempObject)
    return lResultList

def PWASpecification_Get_PWAApplication(inControlSpecificationArray):
    """L-,W+: Получить значение атрибута backend по PWA (pywinauto) селектору. Мы рекомендуем использовать метод UIOSelector_UIO_Get, так как UIO селектор обладает большей функциональностью.

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lBackendStr = UIDesktop.PWASpecification_Get_PWAApplication(lDemoBaseUIOSelector) # Получить backend по PWA селектору

    :param inControlSpecificationArray: PWA селектор, который определяет критерии поиска UIO объекта
        Допустимые ключи PWA селектора:

        - class_name содержимое атрибута class UIO объекта
        - class_name_re содержимое атрибута class UIO объекта, которое удовлетворяет установленному рег. выражению
        - process идентификатор процесса, в котором находится UIO объект
        - title содержимое атрибута title UIO объекта
        - title_re содержимое атрибута title UIO объекта, которое удовлетворяет установленному рег. выражению
        - top_level_only признак поиска только на верхнем уровне приложения. По умолчанию True
        - visible_only признак поиска только среди видимых UIO объектов. По умолчанию True
        - enabled_only признак поиска только среди разблокированных UIO объектов. По умолчанию False
        - best_match содержимое атрибута title UIO объекта максимально приближено к заданному
        - handle идентификатор handle искомого UIO объекта 
        - ctrl_index индекс UIO объекта среди всех дочерних объектов в списке родительского
        - found_index индекс UIO объекта среди всех обнаруженных
        - predicate_func пользовательская функция проверки соответсвия UIO элемента
        - active_only признак поиска только среди активных UIO объектов. По умолчанию False
        - control_id идентификатор control_id искомого UIO объекта 
        - control_type тип элемента (применимо, если backend == "uia")
        - auto_id идентификатор auto_id искомого UIO объекта (применимо, если backend == "uia")
        - framework_id идентификатор framework_id искомого UIO объекта (применимо, если backend == "uia")
        - backend вид технологии подключения к поиску UIO объекта ("uia" или "win32")
    :type inControlSpecificationArray: list, обязательный
    :return: "win32" или "uia"
    """
    inControlSpecificationArray=copy.deepcopy(inControlSpecificationArray)
    #Определение backend
    lBackend=mDefaultPywinautoBackend
    if "backend" in inControlSpecificationArray[0]:
        lBackend=inControlSpecificationArray[0]["backend"]
        inControlSpecificationArray[0].pop("backend")
    #Подготовка входного массива
    inControlSpecificationOriginArray=inControlSpecificationArray
    inControlSpecificationArray=UIOSelector_SearchProcessNormalize_UIOSelector(inControlSpecificationArray)
    #Выполнить идентификацию объектов, если передан массив
    lResultList=[]
    lTempObject=None
    if len(inControlSpecificationArray) > 0:
        #Выполнить подключение к объекту
        lRPAApplication = pywinauto.Application(backend=lBackend)
        #Проверка разрядности
        try:
            lRPAApplication.connect(**inControlSpecificationArray[0])
        except Exception as e:
            UIOSelector_TryRestore_Dict(inControlSpecificationArray)
            try:
                lRPAApplication.connect(**inControlSpecificationArray[0])
            except Exception as e:
                lRPAApplication = None
        if lRPAApplication is not None:
            #lTempObject=lRPAApplication.window(**inControlSpecificationArray[0])
            #Скорректировано из-за недопонимания структуры
            lTempObject=lRPAApplication
    return lTempObject

from . import Keyboard,Mouse

SEARCH_CHILD_BY_MOUSE_POINT_X = None
SEARCH_CHILD_BY_MOUSE_POINT_Y = None
SEARCH_CHILD_BY_MOUSE_ACTIVE = False
def __SEARCH_CHILD_BY_MOUSE_POINT_X_Y_LISTEN():
    global SEARCH_CHILD_BY_MOUSE_POINT_X, SEARCH_CHILD_BY_MOUSE_ACTIVE, SEARCH_CHILD_BY_MOUSE_POINT_Y
    SEARCH_CHILD_BY_MOUSE_ACTIVE = True
    while SEARCH_CHILD_BY_MOUSE_ACTIVE == True:
        lSavePositionBool=Keyboard.IsDown("ctrl") or Keyboard.IsDown("ctrl r")
        #Получить координаты мыши
        if lSavePositionBool == True and SEARCH_CHILD_BY_MOUSE_POINT_X is None: # ЗАПОМНИТЬ КООРДИНАТЫ ТАК КАК НАЖАТА SHIFT ИЛИ ALT L
            lMousePoint = Mouse.GetXY()
            (SEARCH_CHILD_BY_MOUSE_POINT_X,SEARCH_CHILD_BY_MOUSE_POINT_Y) = (lMousePoint.x, lMousePoint.y)
        elif lSavePositionBool==False: (SEARCH_CHILD_BY_MOUSE_POINT_X,SEARCH_CHILD_BY_MOUSE_POINT_Y)  = (None,None)
        time.sleep(0.3)
import threading
#old: AutomationSearchMouseElement
def UIOSelector_SearchChildByMouse_UIO(inElementSpecification):
    """L+,W+: Инициировать визуальный поиск UIO объекта с помощью указателя мыши. При наведении указателя мыши UIO объект выделяется зеленой рамкой. Остановить режим поиска можно с помощью зажима клавиши ctrl left на протяжении нескольких секунд. После этого в веб окне студии будет отображено дерево расположения искомого UIO объекта.

    !ВНИМАНИЕ! НАЧИНАЯ С ВЕРСИИ 1.4.1 ПОМЕНЯЛСЯ ВЫВОД ФУНКЦИИ С [{index, element}, {index, element}, {index, element}] на [ [{index, element}, {index, element}, {index, element}], [{index, element}, {index, element}, {index, element}]]. Данная мера позволила добавить функциональность по поиску множества Ui объектов по курсору мыши 
    
    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_SearchChildByMouse_UIO(lDemoBaseUIOSelector) # Инициировать поиск дочернего UIO объекта, который расположен внутри lDemoBaseUIOSelector.

    :param inElementSpecification: UIO селектор, который определяет критерии поиска родительского UIO объекта, в котором будет производиться поиск дочернего UIO объекта
    :type inElementSpecification: list, обязательный
    :return: UIO объект или None (если UIO не был обнаружен)
    """
    global SEARCH_CHILD_BY_MOUSE_POINT_X, SEARCH_CHILD_BY_MOUSE_ACTIVE, SEARCH_CHILD_BY_MOUSE_POINT_Y
    #Конвертация селектора в формат UIO
    inElementSpecification = Selector_Convert_Selector(inSelector=inElementSpecification, inToTypeStr="UIO")
    lGUISearchElementSelected=None
    #Настройка - частота обновления подсвечивания
    lTimeSleepSeconds=0.3
    lElementFoundedList=[]
    #Ветка поиска в режиме реального времени
    #Сбросить нажатие Ctrl, если оно было
    if CrossOS.IS_WINDOWS_BOOL:
        win32api.GetAsyncKeyState(16)
        win32api.GetAsyncKeyState(17)
        win32api.GetAsyncKeyState(18)
    #Оптимизация - получить объект для опроса единажды
    lUIORoot=UIOSelector_Get_UIO(inElementSpecification)
    lFlagLoop = True
    LISTEN_THREAD = threading.Thread(target=__SEARCH_CHILD_BY_MOUSE_POINT_X_Y_LISTEN)
    LISTEN_THREAD.start()
    while lFlagLoop:
        #Проверить, нажата ли клавиша Ctrl (код 17)
        lFlagKeyPressedExit=None
        #Получить координаты мыши
        (lX,lY) = (None, None)
        if SEARCH_CHILD_BY_MOUSE_POINT_X is None: # СВЕТИТЬ, НО НЕ ВЫБИРАТЬ
            lMousePoint = Mouse.GetXY()
            (lX,lY) = (lMousePoint.x, lMousePoint.y)
        else:
            (lX,lY) = (SEARCH_CHILD_BY_MOUSE_POINT_X,SEARCH_CHILD_BY_MOUSE_POINT_Y)
        lElementFounded=None
        #Создать карту пикселей и элементов
        #####Внимание! Функция UIOXY_SearchChild_ListDict не написана
        inFlagSearchAll = Keyboard.IsDown("alt r") or Keyboard.IsDown("alt l") 
        lElementFoundedList=UIOXY_SearchChild_ListDict(lUIORoot,lX,lY, inFlagSearchAll=inFlagSearchAll)
        lElementFounded=set()
        for item in lElementFoundedList:
            lElementFounded.add(item[-1]["element"])
        #Подсветить объект, если он мышь раньше стояла на другом объекте
        if lGUISearchElementSelected != lElementFounded:
            lGUISearchElementSelected = lElementFounded
        else: time.sleep(1)
        #Доработанная функция отрисовки
        if lElementFounded is not None:
            for item in lElementFounded:
                UIO_Highlight(item, inHighlightCountInt=1)
        FlagKeyPressedExit=Keyboard.IsDown("shift") or Keyboard.IsDown("shift r") or Keyboard.IsDown("shift l")
        #Подсветить объект, если мышка наведена над тем объектом, который не подсвечивался в прошлый раз
        if FlagKeyPressedExit:
            #Была нажата клавиша Ctrl - выйти из цикла
            lFlagLoop=False
        else:
            #Заснуть до следующего цикла
            time.sleep(lTimeSleepSeconds)
    SEARCH_CHILD_BY_MOUSE_ACTIVE = False
    LISTEN_THREAD.join()
    #Вернуть результат поиска
    return lElementFoundedList

#old: - AutomationSearchMouseElementHierarchy
def UIOSelector_SearchChildByMouse_UIOTree(inUIOSelector, inWaitBeforeSec=0.0):
    """L+,W+: Получить список уровней UIO объекта с указнием всех имеющихся атрибутов по входящему UIO селектору.

    ОБНОВЛЕНИЕ 1.4.0: Функция обновлена под использование в новой версии студии
    ОБНОВЛЕНИЕ 1.4.0: ПОСЛЕ ОТРАБОТКИ ВОЗВРАЩАЕТ ФОКУС НА ТО ОКНО, КОТОРОЕ БЫЛО ПРИ ИНИЦИАЛИЗАЦИИ ФУНКЦИИ

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lBackendStr = UIDesktop.UIOSelector_SearchChildByMouse_UIOTree(lDemoBaseUIOSelector) # Получить список атрибутов всех родительских элементов lDemoBaseUIOSelector.

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет произведено извлечение всех атрибутов на всех уровнях.
    :type inUIOSelector: list, обязательный
    :param inWaitBeforeSec: Время ожидания перед началом поиска и перефокусировки. Данный аргумент может быть полезен для отображения полезной информации перед инициализацией режима поиска
    :type inWaitBeforeSec: float, необязательный
    :param inFlagSearchAll: True - Поиск всех подходящих UI объектов нижних уровней. False - Только до первого подходящего. По умолчанию False
    :type inFlagSearchAll: bool, необязательный
    :return: list, список атрибутов на каждом уровне UIO объекта
    """
    time.sleep(inWaitBeforeSec)
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    lItemInfo = []
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        #Получить UI объект, на котором сейчас установлен фокус
        lUIOInitFocused = GetFocused_UIO()
        # Установить фокус по родительскому элементу
        UIOSelector_FocusHighlight(inUIOSelector)
        #Запустить функцию поиска элемента по мыши
        lElementListList = UIOSelector_SearchChildByMouse_UIO(inUIOSelector)
        for lElementList in lElementListList: # 2023 06 НОВАЯ ФУНКЦИОНАЛЬНО ПО ОТОБРАЖЕНИЮ НЕСКОЛЬКИХ ВЕТОК UI
            lElement = lElementList[-1]['element']
            #Detect backend of the elements
            lFlagIsBackendWin32 = True
            #Если объект имеется (не None), то выполнить построение иерархии
            if lElement is not None:
                if CrossOS.IS_WINDOWS_BOOL and lElement.backend.name == 'uia':
                    lFlagIsBackendWin32 = False
                #Циклическое создание дерева
                #while lElement is not None:
                lListIterator=0
                lItemInfo2=lItemInfo
                index = 0
                length = len(lElementList)
                for lListItem in lElementList:
                    lElement = lListItem["element"]
                    #Продолжать построение иерархии во всех случаях кроме бэк uia & parent() is None
                    #if not lFlagIsBackendWin32 and lElement.parent() is None:
                    #    lElement = None
                    #else:
                    #Получить информацию про объект
                    if CrossOS.IS_WINDOWS_BOOL:
                        lItemInfo2.append(UIOEI_Convert_UIOInfo(lElement.element_info))
                        if index==length-1: lItemInfo2[-1]["is_selected_bool"]=True
                        #Дообогатить информацией об индексе ребенка в родительском объекте
                        if "index" in lListItem:
                            if lListItem["index"] is not None:
                                lItemInfo2[-1]['ctrl_index']=lListItem["index"]
                            else:
                                if "ctrl_index" in lListItem:
                                    lItemInfo2[-1]['ctrl_index']=lListItem["ctrl_index"]
                        else:
                            if "ctrl_index" in lListItem:
                                lItemInfo2[-1]['ctrl_index']=lListItem["ctrl_index"]
                    else:
                        info = LCompatibility.get_attr_dict(lElement)
                        info["ctrl_index"]=lListItem["index"]
                        lItemInfo2.append(info)
                    #Оборачиваем потомка в массив, потому что у родителя по структуре интерфейса может быть больше одного наследников
                    lItemInfo2[-1]['child_list']=[]
                    lItemInfo2=lItemInfo2[-1]['child_list']
                    #Переход на родительский объект
                    #lElement = lElement.parent()
                    lListIterator=lListIterator+1
                    index+=1
                #Добавить информацию о Backend в первый объект
                if CrossOS.IS_WINDOWS_BOOL:
                    lItemInfo[0]["backend"]=lElement.backend.name
        #Вернуть фокус исходному окну по итогу отработки
        if lUIOInitFocused!=None: 
            try:
                lUIOInitFocused.set_focus()
            except Exception as e:
                pass
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_SearchChildByMouse_UIOTree",
                            "ArgumentList": [inUIOSelector],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            lItemInfo = lPIPEResponseDict["Result"]
    #Вернуть результат
    return lItemInfo
#old name - PywinautoExtElementCtrlIndexGet
def UIO_GetCtrlIndex_Int(inElement):
    """L-,W+: Получить индекс UIO объекта inElement в списке родительского UIO объекта.

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по UIO селектору.
        lUIOIndexInt = UIDesktop.UIO_GetCtrlIndex_Int(lUIO) # Получить индекс UIO объекта в списке у родительского UIO объекта.

    :param inElement: UIO объект, для которого требуется определить индекс в списке родительского UIO объекта.
    :type inElement: list, обязательный
    :return: int, индекс UIO объекта в списке родительского UIO объекта
    """
    lResult = None
    #Выполнить алгоритм, если есть Element
    if inElement is not None:
        lElementParent = inElement.parent()
        if lElementParent is not None:
            lResult = 0
            lFlagFind = True
            #Получить список потомков
            lElementParentChildrenList = lElementParent.children()
            #Циклический поиск до того момента, пока не упремся в текущий элемент
            while lFlagFind:
                if lResult<len(lElementParentChildrenList):
                    #Прекратить поиск, если элемент был обнаружен
                    if inElement == lElementParentChildrenList[lResult]:
                        lFlagFind = False
                    else:
                        #Прекратить поиски, если итератор вышел за пределы списка
                        if lResult>=len(lElementParentChildrenList):
                            lResult = None
                            lFlagFind = False
                        else:
                            lResult = lResult + 1
                else:
                    lResult=-1
                    lFlagFind=False
    #Вернуть результат    
    return lResult

#Поиск списка элементов по заданной строке (в любом из строковых атрибутов элемента)
def UIO_Search_UIOList(inFilterStr, inFilterType, inParentUIOSelector=None, inParentUIO=None, inFlagRaiseException=True, inRuntimeLimit=60, inTimeStartPoint=None):
    '''L-,W+: Получить список UIO объектов по заданной строке. Поиск производится по всем атрибутам UIO объектов строкового типа.
    
    .. code-block:: python
        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lFilterStr = "1С*"
        lFilterType = "WC"
        lSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]
        UIOList = UIDesktop.UIO_Search_UIOList(inFilterStr=lFilterStr, inFilterType=lFilterType, inParentUIOSelector=lSelector)

    :param inFilterStr: Строка, по которой производится поиск
    :type inFilterStr: str, обязательный
    :param inFilterType: Тип задаваемой для поиска строки. Доступно: STR (str), RE (regexp) и WC (wildcard)
    :type inFilterType: str, обязательный
    :param inParentUIOSelector: UIO Селектор, который определяет корень, от которого производить поиск. По умолчанию None (поиск UIO объектов среди всех доступных приложений windows, которые запущены на текущей сессии)
    :type inParentUIOSelector: list, опциональный
    :param inParentUIO: Родительский элемент, от которого выполнить поиск UIO объектов по заданной строке. По умолчанию None (поиск UIO объектов среди всех доступных приложений windows, которые запущены на текущей сессии)
    :type inParentUIO: UIO объект, опциональный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    :param inRuntimeLimit: Лимит времени, выделенный на поиск UIO объектов. По умолчанию - 60 (в сек.)
    :type inRuntimeLimit: float, опциональный
    :param inTimeStartPoint: Точка начала отсчета для контроля лимита времени, выделенного на поиск UIO объектов. По умолчанию None (самоопределяется при запуске функции)
    :type inTimeStartPoint: float, опциональный
    :return: Список UIO объектов, которые удовлетворяют заданной строке
    '''
    lResultList=[]
    lChildrenList=[]
    lUIOList=copy.deepcopy(inParentUIOSelector) 
    try:
        #Получить список UIOSelector, если он не был задан
        if inParentUIOSelector is None and inParentUIO is None:
            inTimeStartPoint = time.time()
            lUIOList = UIOSelector_GetChildList_UIOList(inBackend='uia')
        elif inParentUIOSelector is not None and inParentUIO is None:
            inTimeStartPoint = time.time() 

        for lUIOSelector in lUIOList:
            #Предел по времени превышен - выйти из поиска
            if time.time()-inTimeStartPoint > inRuntimeLimit: raise RuntimeError("Время Выполнения UIO_Search_UIOList превышено")
            #Получить родительский объект если на вход был задан UIOSelector (вручную)
            if inParentUIO is None:
                #Сформировать спецификацию на получение элемента
                lRootElementSpecification=[lUIOSelector]
                lRootElementList = PWASpecification_Get_UIO(lRootElementSpecification)
                for lRootItem in lRootElementList:
                    if lRootItem is not None:
                        lFlagAddChild=False
                        #Если тип искомой строки str
                        if inFilterType == "STR":
                            #Поиск по title
                            if inFilterStr == lRootItem.element_info.name:
                                lFlagAddChild=True
                            #Поиск по rich_text
                            if inFilterStr == lRootItem.element_info.rich_text:
                                lFlagAddChild=True
                            #Поиск по class_name
                            if inFilterStr == lRootItem.element_info.class_name:
                                lFlagAddChild=True
                            #Поиск по friendly_class_name
                            if inFilterStr == lRootItem.friendly_class_name():
                                lFlagAddChild=True
                            #Поиск по control_type
                            if inFilterStr == lRootItem.element_info.control_type:
                                lFlagAddChild=True
                        #Если тип искомой строки wildcard
                        elif inFilterType == "WC":
                            #Поиск по title
                            if fnmatch.fnmatch(lRootItem.element_info.name,inFilterStr) == True:
                                lFlagAddChild=True
                            #Поиск по rich_text
                            if fnmatch.fnmatch(lRootItem.element_info.rich_text,inFilterStr) == True:
                                lFlagAddChild=True
                            #Поиск по class_name
                            if fnmatch.fnmatch(lRootItem.element_info.class_name,inFilterStr) == True:
                                lFlagAddChild=True
                            #Поиск по friendly_class_name
                            if fnmatch.fnmatch(lRootItem.friendly_class_name(),inFilterStr) == True:
                                lFlagAddChild=True
                            #Поиск по control_type
                            if fnmatch.fnmatch(lRootItem.element_info.control_type,inFilterStr) == True:
                                lFlagAddChild=True
                        #Если тип искомой строки regexp
                        elif inFilterType == "RE":
                            #Поиск по title
                            if re.fullmatch(inFilterStr, lRootItem.element_info.name) is not None:
                                lFlagAddChild=True
                            #Поиск по rich_text
                            if re.fullmatch(inFilterStr, lRootItem.element_info.rich_text) is not None:
                                lFlagAddChild=True
                            #Поиск по class_name
                            if re.fullmatch(inFilterStr, lRootItem.element_info.class_name) is not None:
                                lFlagAddChild=True
                            #Поиск по friendly_class_name
                            if re.fullmatch(inFilterStr, lRootItem.friendly_class_name()) is not None:
                                lFlagAddChild=True
                            #Поиск по control_type
                            if re.fullmatch(inFilterStr, lRootItem.wrapper_object().element_info.control_type) is not None:
                                lFlagAddChild=True
                        #Строка была найдена - добавляем элемент в результирующий список
                        if lFlagAddChild:
                            lResultList.append(lRootItem.wrapper_object())
                        lChildrenList = [lRootItem.wrapper_object()]
            #Елемент на вход поступил - выполнить его анализ
            else:
                #Получить список элементов
                lParentUIOChildrenList=inParentUIO.children()
                #Циклический обход по детям, на предмет вхождения искомой строки в один из атрибутов
                for lChildrenItem in lParentUIOChildrenList:
                    #Предел по времени превышен - выйти из поиска
                    if time.time()-inTimeStartPoint > inRuntimeLimit: raise RuntimeError("Время Выполнения UIO_Search_UIOList превышено")
                    lFlagAddChild=False
                    #Если тип искомой строки str
                    if inFilterType == "STR":
                        #Поиск по title
                        if inFilterStr == lChildrenItem.element_info.name:
                            lFlagAddChild=True
                        #Поиск по rich_text
                        if inFilterStr == lChildrenItem.element_info.rich_text:
                            lFlagAddChild=True
                        #Поиск по class_name
                        if inFilterStr == lChildrenItem.element_info.class_name:
                            lFlagAddChild=True
                        #Поиск по friendly_class_name
                        if inFilterStr == lChildrenItem.friendly_class_name():
                            lFlagAddChild=True
                        #Поиск по control_type
                        if inFilterStr == lChildrenItem.element_info.control_type:
                            lFlagAddChild=True
                    #Если тип искомой строки wildcard
                    elif inFilterType == "WC":
                        #Поиск по title
                        if fnmatch.fnmatch(lChildrenItem.element_info.name,inFilterStr) == True:
                            lFlagAddChild=True
                        #Поиск по rich_text
                        if fnmatch.fnmatch(lChildrenItem.element_info.rich_text,inFilterStr) == True:
                            lFlagAddChild=True
                        #Поиск по class_name
                        if fnmatch.fnmatch(lChildrenItem.element_info.class_name,inFilterStr) == True:
                            lFlagAddChild=True
                        #Поиск по friendly_class_name
                        if fnmatch.fnmatch(lChildrenItem.friendly_class_name(),inFilterStr) == True:
                            lFlagAddChild=True
                        #Поиск по control_type
                        if fnmatch.fnmatch(lChildrenItem.element_info.control_type,inFilterStr) == True:
                            lFlagAddChild=True
                    #Если тип искомой строки regexp
                    elif inFilterType == "RE":
                        #Поиск по title
                        if re.fullmatch(inFilterStr, lChildrenItem.element_info.name) is not None:
                            lFlagAddChild=True
                        #Поиск по rich_text
                        if re.fullmatch(inFilterStr, lChildrenItem.element_info.rich_text) is not None:
                            lFlagAddChild=True
                        #Поиск по class_name
                        if re.fullmatch(inFilterStr, lChildrenItem.element_info.class_name) is not None:
                            lFlagAddChild=True
                        #Поиск по friendly_class_name
                        if re.fullmatch(inFilterStr, lChildrenItem.friendly_class_name()) is not None:
                            lFlagAddChild=True
                        #Поиск по control_type
                        if re.fullmatch(inFilterStr, lChildrenItem.element_info.control_type) is not None:
                            lFlagAddChild=True
                    #Строка была найдена - добавляем элемент в результирующий список
                    if lFlagAddChild:
                        lResultList.append(lChildrenItem)
                #Циклический поиск по детям от текущего элемента
                for lChildElement in lParentUIOChildrenList:
                    #Предел по времени превышен - выйти из поиска
                    if time.time()-inTimeStartPoint > inRuntimeLimit: raise RuntimeError("Время Выполнения UIO_Search_UIOList превышено")
                    lResultList.extend(UIO_Search_UIOList(inFilterStr, inFilterType, inParentUIOSelector=[lUIOSelector],inParentUIO=lChildElement,inFlagRaiseException=inFlagRaiseException,inRuntimeLimit=inRuntimeLimit, inTimeStartPoint=inTimeStartPoint))
            #Старт циклического поиска при наличии родительского элемента    
            if inParentUIO is None and len(lChildrenList)>0:
                for lChildElement in lChildrenList:
                    lResultList.extend(UIO_Search_UIOList(inFilterStr, inFilterType, inParentUIOSelector=[lUIOSelector],inParentUIO=lChildElement,inFlagRaiseException=inFlagRaiseException, inRuntimeLimit=inRuntimeLimit, inTimeStartPoint=inTimeStartPoint))
        return lResultList
    
    except RuntimeError:#Обработка истечения таймаута
        return lResultList
    except Exception as e:#Общая обработка исключений
        if inFlagRaiseException: raise e
        else: return []

def UIO_GetValue_Str(inUIO):
    """L-,W+: Получить значение UI объекта по методу get_value. Если нет такого метода или ошибка выполнения - вернуть None

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lFilterStr = "1С*"
        lFilterType = "WC"
        UIOList = UIDesktop.UIO_Search_UIOTree(inFilterStr=lFilterStr, inFilterType=lFilterType)
        lValueStr = UIO_GetValue_Str(inUIO)

    :param inUIO: UI объект
    :type inUIO: UIO
    :return: Значение UI объекта
    :rtype: str or None
    """

    try:
        return inUIO.get_value()
    except Exception as e:
        return None

#Поиск списка элементов по заданной строке (в любом из строковых атрибутов элемента) Возвращает структуру свойств UIO
def UIO_Search_UIOTree(inFilterStr, inFilterType, inParentUIOSelector=None, inParentUIOList=None, inBackendStr = mDefaultPywinautoBackend):
    """L-,W+: Получить список UIO объектов по заданной строке. Поиск производится по всем атрибутам UIO объектов строкового типа.

    ОБНОВЛЕНИЕ 1.4.0: Функция обновлена под использование в новой версии студии
    
    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lFilterStr = "1С*"
        lFilterType = "WC"
        UIOList = UIDesktop.UIO_Search_UIOTree(inFilterStr=lFilterStr, inFilterType=lFilterType)

    :param inFilterStr: Строка, по которой производится поиск
    :type inFilterStr: str, обязательный
    :param inFilterType: Тип задаваемой для поиска строки. Доступно: STR (str), RE (regexp) и WC (wildcard)
    :type inFilterType: str, обязательный
    :return: list, список атрибутов на каждом уровне UIO объекта
    """
    lResultList = []
    inTimeStartPoint = time.time()
    # ОПРЕДЕЛЕНИЕ РОДИТЕЛЬСКОГО ОБЪЕКТА (СПИСКА, ТАК КАК РЕЗУЛЬТАТОМ СЕЛЕКТОРА МОЖЕТ БЫТЬ НЕСКОЛЬКО UIO)
    if inParentUIOList==None: 
        if inParentUIOSelector==None: 
            inParentUIOSelector = [{"backend":inBackendStr}]
            inParentUIOList = UIOSelector_Get_UIOList(inParentUIOSelector)
        else: inParentUIOList = UIOSelector_Get_UIOList(inUIOSelector=inParentUIOSelector)
        # ЦИКЛИЧЕСКИЙ ОБХОД КОРНЕВОГО СПИСКА  - ЕСЛИ НА ВХОД НЕ ПОСТУПИЛ СПИСОК РОДИТЕЛЕЙ
        lIndexChildInt = 0
        # ИТЕРАЦИЯ ПО КОРНЮ
        for lChildUIO in inParentUIOList:
            lChildUIOSelector = copy.deepcopy(inParentUIOSelector)
            if "ctrl_index" not in lChildUIOSelector[-1]:
                lChildUIOSelector[-1]["ctrl_index"]=lIndexChildInt
            lRootItem = lChildUIO
            # ПОИСК СООТВЕТСТВИЯ (СТРОКА)
            lFlagAddChild=False
            lUIValueStr = UIO_GetValue_Str(lRootItem)
            #if lUIValueStr!=None: lUIValueStr = ''.join(c for c in lUIValueStr if c.isalnum())
            #Если тип искомой строки str
            if inFilterType == "STR":
                #Поиск по title
                if inFilterStr == lRootItem.element_info.name:
                    lFlagAddChild=True
                #Поиск по rich_text
                if inFilterStr == lRootItem.element_info.rich_text:
                    lFlagAddChild=True
                #Поиск по class_name
                if inFilterStr == lRootItem.element_info.class_name:
                    lFlagAddChild=True
                #Поиск по friendly_class_name
                if inFilterStr == lRootItem.friendly_class_name():
                    lFlagAddChild=True
                #Поиск по control_type
                if inFilterStr == lRootItem.element_info.control_type:
                    lFlagAddChild=True
                #Поиск по get_value
                if lUIValueStr!=None and inFilterStr == lUIValueStr:
                    lFlagAddChild=True
            #Если тип искомой строки wildcard
            elif inFilterType == "WC":
                #Поиск по title
                if fnmatch.fnmatch(lRootItem.element_info.name,inFilterStr) == True:
                    lFlagAddChild=True
                #Поиск по rich_text
                if fnmatch.fnmatch(lRootItem.element_info.rich_text,inFilterStr) == True:
                    lFlagAddChild=True
                #Поиск по class_name
                if fnmatch.fnmatch(lRootItem.element_info.class_name,inFilterStr) == True:
                    lFlagAddChild=True
                #Поиск по friendly_class_name
                if fnmatch.fnmatch(lRootItem.friendly_class_name(),inFilterStr) == True:
                    lFlagAddChild=True
                #Поиск по control_type
                if fnmatch.fnmatch(lRootItem.element_info.control_type,inFilterStr) == True:
                    lFlagAddChild=True
                #Поиск по get_value
                if lUIValueStr!=None and fnmatch.fnmatch(lUIValueStr,inFilterStr) == True:
                    lFlagAddChild=True
            #Если тип искомой строки regexp
            elif inFilterType == "RE":
                #Поиск по title
                if re.fullmatch(inFilterStr, lRootItem.element_info.name) is not None:
                    lFlagAddChild=True
                #Поиск по rich_text
                if re.fullmatch(inFilterStr, lRootItem.element_info.rich_text) is not None:
                    lFlagAddChild=True
                #Поиск по class_name
                if re.fullmatch(inFilterStr, lRootItem.element_info.class_name) is not None:
                    lFlagAddChild=True
                #Поиск по friendly_class_name
                if re.fullmatch(inFilterStr, lRootItem.friendly_class_name()) is not None:
                    lFlagAddChild=True
                #Поиск по control_type
                if re.fullmatch(inFilterStr, lRootItem.wrapper_object().element_info.control_type) is not None:
                    lFlagAddChild=True
                #Поиск по get_value
                if lUIValueStr!=None and re.fullmatch(inFilterStr, lUIValueStr) is not None:
                    lFlagAddChild=True
            # Рекурсивный вызов для вложенных элементов
            lChildChildSearchTree = UIO_Search_UIOTree(inFilterStr=inFilterStr, inFilterType=inFilterType, inParentUIOSelector=lChildUIOSelector, inParentUIOList=[lChildUIO], inBackendStr = inBackendStr)
            if len(lChildChildSearchTree)>0:
                # ПОДГОТОВИТЬ СТРУКТУРУ СВОЙСТВ CHILD
                lChildDict = UIOEI_Convert_UIOInfo(lChildUIO.element_info)
                lChildDict["selector"]=lChildUIOSelector
                lChildDict["ctrl_index"]=lIndexChildInt
                lChildDict["child_list"]=lChildChildSearchTree
                lResultList.append(lChildDict)
            #Строка была найдена - добавляем элемент в результирующий список
            elif lFlagAddChild:
                lChildDict = UIOEI_Convert_UIOInfo(lChildUIO.element_info)
                lChildDict["selector"]=lChildUIOSelector
                lChildDict["ctrl_index"]=lIndexChildInt
                lChildDict["child_list"]=[]
                lResultList.append(lChildDict)
            lIndexChildInt+=1
    else:
        # ЦИКЛИЧЕСКИЙ ОБХОД СПИСКА РОДИТЕЛЕЙ - ЕСЛИ НА ВХОД ПОСТУПИЛ СПИСОК РОДИТЕЛЕЙ
        lIndexInt = 0
        for lParentUIO in inParentUIOList:
            lParentUIOSelector = copy.deepcopy(inParentUIOSelector)
            if "ctrl_index" not in lParentUIOSelector[-1]:
                lParentUIOSelector[-1]["ctrl_index"]=lIndexInt
            lChildrenList = lParentUIO.children()
            lIndexChildInt = 0
            # ИТЕРАЦИЯ ПО ДЕТЯМ
            for lChildUIO in lChildrenList:
                lChildUIOSelector = copy.deepcopy(lParentUIOSelector)
                lChildUIOSelector.append({"ctrl_index":lIndexChildInt})
                lRootItem = lChildUIO
                lUIValueStr = UIO_GetValue_Str(lRootItem)
                #if lUIValueStr!=None: lUIValueStr = ''.join(c for c in lUIValueStr if c.isalnum())
                # ПОИСК СООТВЕТСТВИЯ (СТРОКА)
                lFlagAddChild=False
                #Если тип искомой строки str
                if inFilterType == "STR":
                    #Поиск по title
                    if inFilterStr == lRootItem.element_info.name:
                        lFlagAddChild=True
                    #Поиск по rich_text
                    if inFilterStr == lRootItem.element_info.rich_text:
                        lFlagAddChild=True
                    #Поиск по class_name
                    if inFilterStr == lRootItem.element_info.class_name:
                        lFlagAddChild=True
                    #Поиск по friendly_class_name
                    if inFilterStr == lRootItem.friendly_class_name():
                        lFlagAddChild=True
                    #Поиск по control_type
                    if inFilterStr == lRootItem.element_info.control_type:
                        lFlagAddChild=True
                    #Поиск по get_value
                    if lUIValueStr!=None and inFilterStr == lUIValueStr:
                        lFlagAddChild=True
                #Если тип искомой строки wildcard
                elif inFilterType == "WC":
                    #Поиск по title
                    if fnmatch.fnmatch(lRootItem.element_info.name,inFilterStr) == True:
                        lFlagAddChild=True
                    #Поиск по rich_text
                    if fnmatch.fnmatch(lRootItem.element_info.rich_text,inFilterStr) == True:
                        lFlagAddChild=True
                    #Поиск по class_name
                    if fnmatch.fnmatch(lRootItem.element_info.class_name,inFilterStr) == True:
                        lFlagAddChild=True
                    #Поиск по friendly_class_name
                    if fnmatch.fnmatch(lRootItem.friendly_class_name(),inFilterStr) == True:
                        lFlagAddChild=True
                    #Поиск по control_type
                    if fnmatch.fnmatch(lRootItem.element_info.control_type,inFilterStr) == True:
                        lFlagAddChild=True
                    #Поиск по get_value
                    if lUIValueStr!=None and fnmatch.fnmatch(lUIValueStr,inFilterStr) == True:
                        lFlagAddChild=True
                #Если тип искомой строки regexp
                elif inFilterType == "RE":
                    #Поиск по title
                    if re.fullmatch(inFilterStr, lRootItem.element_info.name) is not None:
                        lFlagAddChild=True
                    #Поиск по rich_text
                    if re.fullmatch(inFilterStr, lRootItem.element_info.rich_text) is not None:
                        lFlagAddChild=True
                    #Поиск по class_name
                    if re.fullmatch(inFilterStr, lRootItem.element_info.class_name) is not None:
                        lFlagAddChild=True
                    #Поиск по friendly_class_name
                    if re.fullmatch(inFilterStr, lRootItem.friendly_class_name()) is not None:
                        lFlagAddChild=True
                    #Поиск по control_type
                    if re.fullmatch(inFilterStr, lRootItem.wrapper_object().element_info.control_type) is not None:
                        lFlagAddChild=True
                    #Поиск по get_value
                    if lUIValueStr!=None and re.fullmatch(inFilterStr, lUIValueStr) is not None:
                        lFlagAddChild=True
                # Рекурсивный вызов для вложенных элементов
                lChildChildSearchTree = UIO_Search_UIOTree(inFilterStr=inFilterStr, inFilterType=inFilterType, inParentUIOSelector=lChildUIOSelector, inParentUIOList=[lChildUIO], inBackendStr = inBackendStr)
                if len(lChildChildSearchTree)>0:
                    # ПОДГОТОВИТЬ СТРУКТУРУ СВОЙСТВ CHILD
                    lChildDict = UIOEI_Convert_UIOInfo(lChildUIO.element_info)
                    lChildDict["selector"]=lChildUIOSelector
                    lChildDict["ctrl_index"]=lIndexChildInt
                    lChildDict["child_list"]=lChildChildSearchTree
                    lResultList.append(lChildDict)
                #Строка была найдена - добавляем элемент в результирующий список
                elif lFlagAddChild:
                    lChildDict = UIOEI_Convert_UIOInfo(lChildUIO.element_info)
                    lChildDict["selector"]=lChildUIOSelector
                    lChildDict["ctrl_index"]=lIndexChildInt
                    lChildDict["child_list"]=[]
                    lResultList.append(lChildDict)
                lIndexChildInt+=1
            lIndexInt+=1
    # ДЛЯ КАЖДОГО ЭЛЕМЕНТА ФОРМИРУЕМ СЕЛЕКТОР
    #Вернуть результат
    return lResultList

#old: - PywinautoExtElementsGetInfo
def UIOSelector_Get_UIOInfoList (inUIOSelector, inElement=None, inFlagRaiseException=True):
    """L+,W+: Техническая функция: Получить список параметров последних уровней UIO селектора по UIO объектам, которые удовлетворяют входящим inUIOSelector, поиск по которым будет производится от уровня inElement.

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIOInfoList = UIDesktop.UIOSelector_Get_UIOInfoList(lDemoBaseUIOSelector) # Получить словарь параметров по UIO селектору.

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет произведено извлечение всех атрибутов на всех уровнях.
    :type inUIOSelector: list, обязательный
    :param inElement: UIO объект, от которого выполнить поиск дочерних UIO объектов по UIO селектору inUIOSelector. По умолчанию None - поиск среди всех приложений.
    :type inElement: UIO объект, необязательный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    :return: dict, пример: {"title":None,"rich_text":None,"process_id":None,"process":None,"handle":None,"class_name":None,"control_type":None,"control_id":None,"rectangle":{"left":None,"top":None,"right":None,"bottom":None}, 'runtime_id':None}
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        #Получить родительский объект если на вход ничего не поступило
        lResultList=UIOSelector_Get_UIOList(inUIOSelector, inElement, inFlagRaiseException)
        lIterator = 0
        for lItem in lResultList:
            lResultList[lIterator]=UIOEI_Convert_UIOInfo(lResultList[lIterator].element_info)
            lIterator = lIterator + 1
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_Get_UIOInfoList",
                            "ArgumentList": [inUIOSelector, inElement],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            lResultList = lPIPEResponseDict["Result"]
    return lResultList

#old: - PywinautoExtTryToRestore
def UIOSelector_TryRestore_Dict(inSpecificationList):
    """L-,W+: Восстановить окно приложения на экране по UIO селектору inSpecificationList, если оно было свернуто. Функция обернута в try .. except - ошибок не возникнет.

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ УЖЕ ИСПОЛЬЗУЕТСЯ В РЯДЕ ДРУГИХ ФУНКЦИЙ ТАК КАК АДРЕССАЦИЯ ПО UIA FRAMEWORK НЕДОСТУПНА, ЕСЛИ ПРИЛОЖЕНИЕ СВЕРНУТО.

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        UIDesktop.UIOSelector_TryRestore_Dict(lDemoBaseUIOSelector) # Попытка восстановления свернутого окна по UIO селектору.

    :param inSpecificationList: UIO селектор, который определяет UIO объект, для которого будет произведено извлечение всех атрибутов на всех уровнях.
    :type inSpecificationList: list, обязательный
    """
    #Конвертация селектора в формат UIO
    inSpecificationList = Selector_Convert_Selector(inSelector=inSpecificationList, inToTypeStr="UIO")
    lResult={}
    try:
        #Подготовка взодного массива
        inControlSpecificationArray=UIOSelector_SearchUIONormalize_UIOSelector(inSpecificationList)
        #Выполнить подключение к объекту. Восстановление необходимо только в бэке win32,
        #так как в uia свернутое окно не распознается
        lRPAApplication = pywinauto.Application(backend="win32")
        lRPAApplication.connect(**inSpecificationList[0])
        lRPAApplication.top_window().restore()
    except Exception:
        True==False
    return lResult

#old: - ElementActionGetList
def UIOSelector_Get_UIOActivityList (inUIOSelector,inFlagRaiseException=True):
    """L+,W+: Получить список доступных действий/функций по UIO селектору inUIOSelector. Описание возможных активностей см. ниже.

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lActivityList = UIDesktop.UIOSelector_Get_UIOActivityList(lDemoBaseUIOSelector) # Получить список активностей по UIO селектору.

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inUIOSelector: list, обязательный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    """
    #Список исключений для отображения
    ignore_list = {
        "ref",
        "root",
        "rectangle",
        "parent",
        "invoke",
        "descendants",
        "appdata",
        "actions",
        "children",
        "element_info",
        "was_maximized",
        "can_select_multiple",
        "capture_as_image",
        "collapse",
        "expand",
        "from_point",
        "get_expand_state",
        "get_selection",
        "is_child",
        "is_collapsed",
        "is_expanded",
        "is_selected",
        "is_selection_required"
    }
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        #Получить объект
        lObject=UIOSelector_Get_UIO(inUIOSelector,inFlagRaiseException=inFlagRaiseException)
        lActionList=dir(lObject)
        lResult=dir(lObject)
        #Выполнить чистку списка от неактуальных методов
        for lActionItem in lActionList:
            #Удалить те, которые начинаются на _
            if lActionItem[0]=='_':
                lResult.remove(lActionItem)
            #Удалить те, которые начинаются с символа верхнего регистра
            elif lActionItem[0].isupper():
                lResult.remove(lActionItem)
            #Удалить те, которые начинаются с iface - extended режим
            elif lActionItem.startswith("iface"):
                lResult.remove(lActionItem)
            #Удалить те, которые начинаются с iter - extended режим
            elif lActionItem.startswith("iter"):
                lResult.remove(lActionItem)
            # Удалить те, которые в ignore списке
            elif lActionItem in ignore_list:
                lResult.remove(lActionItem)
            # Удалить те, которые не начинаются с get / set (для AT-SPI LINUX)
            elif inUIOSelector[0].get("backend", "at-spi")=="at-spi":
                if lActionItem.startswith("get_") or lActionItem.startswith("set_"): pass
                else: lResult.remove(lActionItem)
            
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_Get_UIOActivityList",
                            "ArgumentList": [inUIOSelector],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            lResult = lPIPEResponseDict["Result"]
    return lResult


def UIOSelectorUIOActivity_Get_ArgDict(inUIOSelector, inActionStr):
    """L+,W+: Сформировать преднастроенный список/словарь аргументов, передаваемый в функцию inActionStr, которая будет вызываться у объекта UIO, полученного по inUIOSelector

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lActivityResult = UIDesktop.UIOSelectorUIOActivity_Get_ArgDict(lDemoBaseUIOSelector, "type_keys")
        
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

    l_uio = UIOSelector_Get_UIO(inSpecificationList=inUIOSelector)

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
        try:
            lDefSignature = inspect.signature(lDef)
            for lItemKeyStr in lDefSignature.parameters:
                lItemValue = lDefSignature.parameters[lItemKeyStr]
                if lItemValue.default is inspect._empty:
                    lResultDict["ArgDict"][lItemKeyStr] = None
                    lResultDict["ArgList"].append(f"{lItemValue.name}{':'+lItemValue.annotation if lItemValue.annotation!=inspect._empty else ''}")
                else:
                    lResultDict["ArgDict"][lItemKeyStr] = lItemValue.default
                    lResultDict["ArgList"].append(lItemValue.default)
        except ValueError:
            pass

    return lResultDict

#old: - ElementRunAction
def UIOSelectorUIOActivity_Run_Dict(inUIOSelector, inActionName, inFlagRaiseException=True, inArgumentList=None, inkwArgumentObject=None):
    """L+,W+: Выполнить активность inActionName над UIO объектом, полученным с помощью UIO селектора inUIOSelector. Описание возможных активностей см. ниже.

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lActivityResult = UIDesktop.UIOSelectorUIOActivity_Run_Dict(lDemoBaseUIOSelector, "click") # выполнить действие над UIO объектом с помощью UIO селектора.

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inUIOSelector: list, обязательный
    :param inActionName: наименование активности, которую требуется выполнить над UIO объектом
    :type inActionName: str, обязательный
    :param inFlagRaiseException: True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.
    :type inFlagRaiseException: bool, опциональный
    :param inArgumentList: список передаваемых неименованных аргументов в функцию inActionName
    :type inArgumentList: list, необязательный
    :param inkwArgumentObject: словарь передаваемых именованных аргументов в функцию inActionName
    :type inkwArgumentObject: dict, необязательный
    :return: возвращает результат запускаемой функции с наименованием inActionName над UIO объектом
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    if inArgumentList is None: inArgumentList=[] # 2021 02 22 Minor fix by Ivan Maslov
    if inkwArgumentObject is None: inkwArgumentObject={} # 2021 02 22 Minor fix by Ivan Maslov
    lResult={}
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    #Run activity if SafeOtherProcess is None
    if lSafeOtherProcess is None:
        #Определить объект
        lObject=UIOSelector_Get_UIO(inUIOSelector,inFlagRaiseException=inFlagRaiseException)
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
    else:
        #Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelectorUIOActivity_Run_Dict",
         "ArgumentList": [inUIOSelector, inActionName, inArgumentList, inkwArgumentObject],
         "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            lResult = lPIPEResponseDict["Result"]
    return lResult

#old name - ElementGetInfo
def UIOSelector_Get_UIOInfo(inUIOSelector):
    """L+,W+: Получить свойства UIO объекта (element_info), по заданному UIO селектору. Ниже представлен перечень возвращаемых свойств.

    WINDOWS
    Для backend = win32:
    
    - automation_id (int)
    - class_name (str)
    - control_id (int)
    - control_type (str)
    - full_control_type (str)
    - enabled (bool)
    - handle (int)
    - name (str)
    - parent (object/UIO)
    - process_id (int)
    - rectangle (object/rect)
    - rich_text (str)
    - visible (bool)

    Для backend = uia:

    - automation_id (int)
    - class_name (str)
    - control_id (int)
    - control_type (str)
    - enabled (bool)
    - framework_id (int)
    - handle (int)
    - name (str)
    - parent (object/UIO)
    - process_id (int)
    - rectangle (object/rect)
    - rich_text (str)
    - runtime_id (int)
    - visible (bool)

    LINUX:
    Для backend = at-spi

    "id":
    "name": 
    "caption": 
    "current_value":
    "description": 
    "role_name": 
    "localized_role_name": 
    "child_count":
    "toolkit_name":
    "toolkit_version":
    "path": 
    "alpha":
    "process_id":
    "rectangle":
    "attributes":

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIOElementInfoDict = UIDesktop.UIOSelector_Get_UIOInfo(lDemoBaseUIOSelector) #Получить свойства над UIO объектом с помощью UIO селектора.

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inUIOSelector: list, обязательный
    :return: словарь свойств element_info: Пример {"control_id": ..., "process_id": ...}
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        #Подготовка входного массива
        inUIOSelector=UIOSelector_SearchUIONormalize_UIOSelector(inUIOSelector)
        #Выполнить идентификацию объектов, если передан массив
        lResultList=[]
        if len(inUIOSelector) > 0:
            #Получить объект
            lTempObject=UIOSelector_Get_UIO(inUIOSelector)
            #Получить инфо объект
            lTempObjectInfo = lTempObject.element_info
            #Добавить информацию об обнаруженом объекте
            lResultList.append(UIOEI_Convert_UIOInfo(lTempObjectInfo))
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_Get_UIOInfo",
                            "ArgumentList": [inUIOSelector],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            lResultList = lPIPEResponseDict["Result"]
    return lResultList
#old: - GUISearchElementByRootXY
def UIOXY_SearchChild_ListDict(inRootElement,inX,inY,inHierarchyList=None, inShowRootBool=False):
    """L-,W+: Техническая функция: Получить иерархию вложенности UIO объекта по заданным корневому UIO объекту, координатам X и Y.

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект с помощью UIO селектора
        lUIOHierarchyList = UIDesktop.UIOXY_SearchChild_ListDict(lUIO, 100, 200) # Получить UIO объект с помощью UIO селектора родительского элемента и координат X / Y

    :param inRootElement: родительский UIO объект, полученный ранее с помощью UIO селектора.
    :type inRootElement: object UIO, обязательный
    :param inX: родительский UIO объект, полученный ранее с помощью UIO селектора.
    :type inX: int, обязательный
    :param inY: родительский UIO объект, полученный ранее с помощью UIO селектора.
    :type inY: int, обязательный
    :param inShowRootBool: True - в результирующем списке показывать корневой объект, от которого был инициирован вызов. False - не показывать корневой объект
    :type inShowRootBool: bool, необязательный
    :return: Список словарей - уровней UIO объектов
    """
    if inHierarchyList is None: inHierarchyList = []
    #Инициализация результирующего значения
    lResultElement = None
    lResultElementX1 = None
    lResultElementX2 = None
    lResultElementY1 = None
    lResultElementY2 = None
    lResultHierarchyList=[{'index':None,'element':None}]
    #Получить координаты текущего объекта
    try:
        lRootElementRectX1=inRootElement.element_info.rectangle.left
        lRootElementRectX2=inRootElement.element_info.rectangle.right
        lRootElementRectY1=inRootElement.element_info.rectangle.top
        lRootElementRectY2=inRootElement.element_info.rectangle.bottom
        #Добавить объект в результирующий, если координаты попадают в него
        if inX>=lRootElementRectX1 and inX<=lRootElementRectX2 and inY>=lRootElementRectY1 and inY<=lRootElementRectY2:
            lResultElement = inRootElement
            lResultElementX1 = lRootElementRectX1
            lResultElementX2 = lRootElementRectX2
            lResultElementY1 = lRootElementRectY1
            lResultElementY2 = lRootElementRectY2
            #Сформировать результирующий обьъект
            lParentHierarchy = inHierarchyList
            if len(lParentHierarchy)==0:
                if inShowRootBool==True:
                    lParentHierarchy.append({"index":None,"element":lResultElement})
            else:
                lParentHierarchy[-1]["element"] = lResultElement
            lResultHierarchyList=lParentHierarchy
            #Получить список детей и добавить в карту
            lChildIterator=0
            for lChildElement in inRootElement.children():
                #Сформировать результирующий массив
                lChildFoundedHierarchyList = lParentHierarchy.copy()
                lChildFoundedHierarchyList.append({'index': lChildIterator})
                lChildFoundedHierarchyList = UIOXY_SearchChild_ListDict(lChildElement,inX,inY, lChildFoundedHierarchyList)
                lChildFoundedElement = lChildFoundedHierarchyList[-1]["element"]
                #Установить обнаруженный элемент, если текущий результат пустой
                if lResultElement is None and lChildFoundedElement is not None:
                    lResultElement = lChildFoundedElement
                    lResultElementX1 = lResultElement.element_info.rectangle.left
                    lResultElementX2 = lResultElement.element_info.rectangle.right
                    lResultElementY1 = lResultElement.element_info.rectangle.top
                    lResultElementY2 = lResultElement.element_info.rectangle.bottom
                    lResultHierarchyList = lChildFoundedHierarchyList
                #Выполнить сверку lChildFoundedElement и lResultElement если оба имеются
                elif lResultElement is not None and lChildFoundedElement is not None: 
                    #Правила перезатирания карты, если имеется старый объект
                    #[Накладываемый объект] - НО - ElementNew
                    #[Имеющийся объект] - ИО - ElementOld
                    #3 типа вхождения объектов
                    #тип 1 - [имеющийся объект] полностью входит в [накладываемый объект] (ИО X1 Y1 >= НО X1 Y1; ИО X2 Y2 <= НО X2 Y2) - не вносить НО в bitmap в эти диапазоны
                    #тип 2 - [имеющийся объект] полностью выходит за пределы [накладываемого объекта] (ИО X1 Y1 < НО X1 Y1; ИО X2 Y2 > НО X2 Y2) - вносить НО в bitmap
                    #тип 3 - [имеющийся объект] частично входит в [накладываемый объект] (все остальные случаи)- вносить НО в bitmap
                    #Получить координаты ИО
                    lChildFoundedElementInfo = lChildFoundedElement.element_info
                    #lElementNew = inElement
                    lChildFoundedElementX1 = lChildFoundedElementInfo.rectangle.left
                    lChildFoundedElementX2 = lChildFoundedElementInfo.rectangle.right
                    lChildFoundedElementY1 = lChildFoundedElementInfo.rectangle.top
                    lChildFoundedElementY2 = lChildFoundedElementInfo.rectangle.bottom
                    #Проверка вхождения по типу 1
                    if (lResultElementX1>=lChildFoundedElementX1) and (lResultElementY1>=lChildFoundedElementY1) and (lResultElementX2<=lChildFoundedElementX2) and (lResultElementY2<=lChildFoundedElementY2):
                        False == True
                    #Проверка вхождения по типу 3
                    elif (lResultElementX1<lChildFoundedElementX1) and (lResultElementY1<lChildFoundedElementY1) and (lResultElementX2>lChildFoundedElementX2) and (lResultElementY2>lChildFoundedElementY2):
                        lResultElement = lChildFoundedElement
                        lResultElementX1 = lChildFoundedElementX1
                        lResultElementX2 = lChildFoundedElementX2
                        lResultElementY1 = lChildFoundedElementY1
                        lResultElementY2 = lChildFoundedElementY2
                        lResultHierarchyList = lChildFoundedHierarchyList
                    #Проверка вхождения по типу 2
                    else:
                        lResultElement = lChildFoundedElement
                        lResultElementX1 = lChildFoundedElementX1
                        lResultElementX2 = lChildFoundedElementX2
                        lResultElementY1 = lChildFoundedElementY1
                        lResultElementY2 = lChildFoundedElementY2
                        lResultHierarchyList = lChildFoundedHierarchyList
                lChildIterator=lChildIterator+1
    except Exception as e:
        False == False
    return lResultHierarchyList

def UIOSelector_LevelInfo_List(inUIOSelector, inBackend=mDefaultPywinautoBackend):
    """L+,W+: Получить список свойств всех уровней до UI объекта, обнаруженного с помощью селектора inUIOSelector.
    
    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIOList = UIDesktop.UIOSelector_LevelInfo_List(lDemoBaseUIOSelector) # Получить список свойств каждого уровня

    :param inUIOSelector: Селектор на UIO объект (CSS | XPATH | UIO).
    :type inUIOSelector: list, обязательный
    :param inBackend: вид backend "win32" или "uia". По умолчанию mDefaultPywinautoBackend ("win32")
    :type inBackend: str, необязательный
    :return: список дочерних UIO объектов
    """  
    if inUIOSelector is None: inUIOSelector = []
    else: inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    if len(inUIOSelector)>0 and "backend" in inUIOSelector[0]: inBackend=inUIOSelector[0]["backend"]
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        #Подготовка входного массива
        inUIOSelector=UIOSelector_SearchUIONormalize_UIOSelector(inUIOSelector)
        #Выполнить идентификацию объектов, если передан массив
        lResultList=[]
        if len(inUIOSelector) > 0:
            #Получить объект
            lTempObject = UIOSelector_Get_UIO(inUIOSelector)
            def recursive(item, backend):
                result_list = []
                if CrossOS.IS_WINDOWS_BOOL==True:
                    result_list =[UIOEI_Convert_UIOInfo(item.element_info)]
                else: 
                    result_list = [UIOEI_Convert_UIOInfo(item)]
                if backend=="uia":
                    # Идентифицировать ctrl_index
                    parent = None
                    if CrossOS.IS_WINDOWS_BOOL==True: parent = item.parent()
                    else: parent=item.parent
                    #while parent == None: parent = item.parent() # Фикс на плавующую ошибку , что иногда не возвращается parent
                    parent_children_list = []
                    if CrossOS.IS_WINDOWS_BOOL==True:
                        parent_children_list = parent.children()
                    else:
                        parent_children_list=list(parent)
                    index = 0
                    for i in parent_children_list:
                        if i==item:
                            result_list[0]["ctrl_index"]=index
                        index+=1
                    parent_parent = None
                    if CrossOS.IS_WINDOWS_BOOL==True: parent_parent = parent.parent()
                    else: parent_parent=parent.parent
                    index = 0
                    #while parent_parent == None: parent_parent = parent.parent()
                    if parent_parent != None:
                        result_list=recursive(parent, backend)+result_list
                    else:
                        del result_list[0]["ctrl_index"]
                    return result_list
                else:
                    # Идентифицировать ctrl_index
                    try:
                        parent = None
                        if CrossOS.IS_WINDOWS_BOOL==True: parent = item.parent()
                        else: parent=item.parent
                        #while parent == None: parent = item.parent() # Фикс на плавующую ошибку , что иногда не возвращается parent
                        if parent != None:
                            if CrossOS.IS_WINDOWS_BOOL==False:
                                if (LCompatibility.is_backend_atspi(parent)!=True) or (LCompatibility.is_backend_atspi(parent) and parent.get_name()!="main" and parent.get_role_name()!="desktop frame"):
                                    parent_children_list = []
                                    if CrossOS.IS_WINDOWS_BOOL==True:
                                        parent_children_list = parent.children()
                                    else:
                                        parent_children_list=list(parent)
                                    index = 0
                                    for i in parent_children_list:
                                        if i==item:
                                            result_list[0]["ctrl_index"]=index
                                        index+=1
                                    result_list=recursive(parent, backend)+result_list
                            else:
                                parent_children_list = []
                                if CrossOS.IS_WINDOWS_BOOL==True:
                                    parent_children_list = parent.children()
                                else:
                                    parent_children_list=list(parent)
                                index = 0
                                for i in parent_children_list:
                                    if i==item:
                                        result_list[0]["ctrl_index"]=index
                                    index+=1
                                result_list=recursive(parent, backend)+result_list
                    except Exception as e:
                        pass
                    return result_list

            return recursive(lTempObject, inBackend)
        else:
            lResultList=BackendStr_GetTopLevelList_UIOInfo(inBackend)
            #Установка бэк-енда на первый элемент
            for lItem in lResultList:
                lItem["backend"]=inBackend
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_GetChildList_UIOList",
                            "ArgumentList": [inUIOSelector, inBackend],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            lResultList = lPIPEResponseDict["Result"]
    return lResultList


#old: - ElementGetChildElementList
def UIOSelector_GetChildList_UIOList(inUIOSelector=None, inBackend=mDefaultPywinautoBackend):
    """L+,W+: Получить список дочерних UIO объектов по входящему UIO селектору inUIOSelector.
    
    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIOList = UIDesktop.UIOSelector_GetChildList_UIOList(lDemoBaseUIOSelector) # Получить список дочерних UIO объектов с помощью UIO селектора

    :param inUIOSelector: родительский UIO объект, полученный ранее с помощью UIO селектора.
    :type inUIOSelector: list, обязательный
    :param inBackend: вид backend "win32" или "uia". По умолчанию mDefaultPywinautoBackend ("win32")
    :type inBackend: str, необязательный
    :return: список дочерних UIO объектов
    """
    if inUIOSelector is None: inUIOSelector = []
    else: inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        #Подготовка входного массива
        inUIOSelector=UIOSelector_SearchUIONormalize_UIOSelector(inUIOSelector)
        #Выполнить идентификацию объектов, если передан массив
        lResultList=[]
        if len(inUIOSelector) > 0:
            #Получить объект
            lTempObject = UIOSelector_Get_UIO(inUIOSelector)
            #Получить список дочерних объектов
            lTempChildList = []
            if CrossOS.IS_WINDOWS_BOOL==True:
                lTempChildList = lTempObject.children()
            elif LCompatibility.is_backend_atspi(lTempObject): # UI ОБЪЕКТЫ WNCK НЕ ИТЕРИРУЮТСЯ
                lTempChildList = list(lTempObject)
            lIterator=0
            #Подготовить результирующий объект
            for lChild in lTempChildList:
                lTempObjectInfo={}
                if CrossOS.IS_WINDOWS_BOOL==True:
                    lTempObjectInfo=lChild.element_info
                else:
                    lTempObjectInfo=lChild
                #Добавить информацию об обнаруженом объекте
                lObjectInfoItem=UIOEI_Convert_UIOInfo(lTempObjectInfo)
                #Итератор внутри объекта (для точной идентификации)
                lObjectInfoItem['ctrl_index']=lIterator
                lResultList.append(lObjectInfoItem)
                #Инкремент счетчика
                lIterator=lIterator+1
        else:
            lResultList=BackendStr_GetTopLevelList_UIOInfo(inBackend)
            #Установка бэк-енда на первый элемент
            for lItem in lResultList:
                lItem["backend"]=inBackend
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_GetChildList_UIOList",
                            "ArgumentList": [inUIOSelector, inBackend],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            lResultList = lPIPEResponseDict["Result"]
    return lResultList

#old1: - ElementSpecificationArraySearchPrepare
#old2: - ElementSpecificationListNormalize
def UIOSelector_SearchUIONormalize_UIOSelector (inControlSpecificationArray):
    """L+,W+: Нормализовать UIO селектор для дальнейшего использования в функциях поиск UIO объекта. Если недопустимых атрибутов не присутствует, то оставить как есть.

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelectorDitry = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lDemoBaseUIOSelectorClean = UIDesktop.UIOSelector_SearchUIONormalize_UIOSelector(lDemoBaseUIOSelectorDitry) # Очистить UIO селектор от недопустимых ключей для дальнейшего использования

    :param inControlSpecificationArray: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inControlSpecificationArray: list, обязательный
    :return: нормализованный UIO селектор
    """
    #Конвертация селектора в формат UIO
    inControlSpecificationArray = Selector_Convert_Selector(inSelector=inControlSpecificationArray, inToTypeStr="UIO")
    if CrossOS.IS_WINDOWS_BOOL==True:
        lResult=[]
        #Циклический обход
        for lSpecificationItem in inControlSpecificationArray:
            lSpecificationItemNew=lSpecificationItem.copy()
            #Перебор всех элементов
            for lItemKey,lItemValue in lSpecificationItem.items():
                #Флаг удаления атрибута
                lFlagRemoveAttribute=False
                #############################
                #Если является вложенным словарем - удалить
                if type(lItemValue) is dict:
                    lFlagRemoveAttribute=True
                #Является типом None
                if lItemValue is None:
                    lFlagRemoveAttribute=True
                #Проверка допустимого ключевого слова
                if (
                    lItemKey == "class_name" or
                    lItemKey == "class_name_re" or
                    lItemKey == "parent" or
                    lItemKey == "process" or
                    lItemKey == "title" or
                    lItemKey == "title_re" or
                    lItemKey == "top_level_only" or
                    lItemKey == "visible_only" or
                    lItemKey == "enabled_only" or
                    lItemKey == "best_match" or
                    lItemKey == "handle" or
                    lItemKey == "ctrl_index" or
                    lItemKey == "found_index" or
                    lItemKey == "predicate_func" or
                    lItemKey == "active_only" or
                    lItemKey == "control_id" or
                    lItemKey == "control_type" or
                    lItemKey == "auto_id" or
                    lItemKey == "framework_id" or
                    lItemKey == "backend"):
                    pass
                else:
                    lFlagRemoveAttribute=True

                    
                #############################
                #Конструкция по удалению ключа из словаря
                if lFlagRemoveAttribute:
                    lSpecificationItemNew.pop(lItemKey)
            #Проверит наличие ctrl_index - если он есть, то удалить control_id и control_type из-за того, что они мешают друг другу
            if 'ctrl_index' in lSpecificationItemNew:
                if "control_id" in lSpecificationItemNew:
                    lSpecificationItemNew.pop("control_id")
                if "control_type" in lSpecificationItemNew:
                    lSpecificationItemNew.pop("control_type")
            #Проверить наличие handle - если он есть, то удалить process, control_id и control_type из-за того, что они мешают друг другу
            if 'handle' in lSpecificationItemNew:
                if "control_id" in lSpecificationItemNew:
                    lSpecificationItemNew.pop("control_id")
                if "control_type" in lSpecificationItemNew:
                    lSpecificationItemNew.pop("control_type")
                if "process" in lSpecificationItemNew:
                    lSpecificationItemNew.pop("process")
            #Иначе Проверить наличие process - если он есть, то удалить тк он нужен только при подключении к процессу
            if 'process' in lSpecificationItemNew:
                lSpecificationItemNew.pop("process")
            #Добавить строку в результирующий массив
            lResult.append(lSpecificationItemNew)
        #Вернуть результат
        return lResult
    else:
        return inControlSpecificationArray

#old name 1 - ElementSpecificationArraySearchPrepare
#old name 2 - ElementSpecificationListNormalize
def UIOSelector_SearchProcessNormalize_UIOSelector (inControlSpecificationArray):
    """L-,W+: Нормализовать UIO селектор для дальнейшего использования в функциях поиска процесса, в котором находится искомый UIO объект. Если недопустимых атрибутов не присутствует, то оставить как есть.

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelectorDitry = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lDemoBaseUIOSelectorClean = UIDesktop.UIOSelector_SearchProcessNormalize_UIOSelector(lDemoBaseUIOSelectorDitry) # Очистить UIO селектор от недопустимых ключей для дальнейшего использования

    :param inControlSpecificationArray: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inControlSpecificationArray: list, обязательный
    :return: нормализованный UIO селектор
    """
    #Конвертация селектора в формат UIO
    inControlSpecificationArray = Selector_Convert_Selector(inSelector=inControlSpecificationArray, inToTypeStr="UIO")
    lResult=[]
    #Циклический обход
    for lSpecificationItem in inControlSpecificationArray:
        lSpecificationItemNew=lSpecificationItem.copy()
        #Перебор всех элементов
        for lItemKey,lItemValue in lSpecificationItem.items():
            #Флаг удаления атрибута
            lFlagRemoveAttribute=False
            #############################
            #Если является вложенным словарем - удалить
            if type(lItemValue) is dict:
                lFlagRemoveAttribute=True
            #Является типом None
            if lItemValue is None:
                lFlagRemoveAttribute=True
            #Проверка допустимого ключевого слова
            if (
                lItemKey == "class_name" or
                lItemKey == "class_name_re" or
                lItemKey == "parent" or
                lItemKey == "process" or
                lItemKey == "title" or
                lItemKey == "title_re" or
                lItemKey == "top_level_only" or
                lItemKey == "visible_only" or
                lItemKey == "enabled_only" or
                lItemKey == "best_match" or
                lItemKey == "handle" or
                lItemKey == "ctrl_index" or
                lItemKey == "found_index" or
                lItemKey == "predicate_func" or
                lItemKey == "active_only" or
                lItemKey == "control_id" or
                lItemKey == "control_type" or
                lItemKey == "auto_id" or
                lItemKey == "framework_id" or
                lItemKey == "backend"):
                pass
            else:
                lFlagRemoveAttribute=True

                
            #############################
            #Конструкция по удалению ключа из словаря
            if lFlagRemoveAttribute:
                lSpecificationItemNew.pop(lItemKey)
        #Проверит наличие ctrl_index - если он есть, то удалить control_id и control_type из-за того, что они мешают друг другу
        if 'ctrl_index' in lSpecificationItemNew:
            if "control_id" in lSpecificationItemNew:
                lSpecificationItemNew.pop("control_id")
            if "control_type" in lSpecificationItemNew:
                lSpecificationItemNew.pop("control_type")
        #Проверить наличие handle - если он есть, то удалить process, control_id и control_type из-за того, что они мешают друг другу
        if 'handle' in lSpecificationItemNew:
            if "control_id" in lSpecificationItemNew:
                lSpecificationItemNew.pop("control_id")
            if "control_type" in lSpecificationItemNew:
                lSpecificationItemNew.pop("control_type")
            if "process" in lSpecificationItemNew:
                lSpecificationItemNew.pop("process")
        #Иначе Проверить наличие process - если он есть, то удалить title, control_id и control_type из-за того, что они мешают друг другу
        elif 'process' in lSpecificationItemNew:
            if "control_id" in lSpecificationItemNew:
                lSpecificationItemNew.pop("control_id")
            if "control_type" in lSpecificationItemNew:
                lSpecificationItemNew.pop("control_type")
            if "title" in lSpecificationItemNew:
                lSpecificationItemNew.pop("title")
        #Добавить строку в результирующий массив
        lResult.append(lSpecificationItemNew)
    #Вернуть результат
    return lResult

#old: - ElementInfoExportObject
def UIOEI_Convert_UIOInfo(inElementInfo):
    """L-,W+: Техническая функция: Дообогащение словаря с параметрами UIO объекта по заданному UIO.element_info

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по UIO селектору.
        lUIOProcessInfoDict = UIDesktop.UIOEI_Convert_UIOInfo(lUIO.element_info)

    :param inElementInfo: экземпляр класса UIO.element_info, для которого требуется дообогатить словарь с параметрами (в дальнейшем можно использовать как элемент UIO селектора).
    :type inElementInfo: object, обязательный
    :return: dict, пример: {"title":None,"rich_text":None,"process_id":None,"process":None,"handle":None,"class_name":None,"control_type":None,"control_id":None,"rectangle":{"left":None,"top":None,"right":None,"bottom":None}, 'runtime_id':None}
    """
    #Подготовить выходную структуру данных
    lResult = {"title":None,"rich_text":None,"process_id":None,"process":None,"handle":None,"class_name":None,"control_type":None,"control_id":None,"rectangle":{"left":None,"top":None,"right":None,"bottom":None}, 'runtime_id':None}
    #Проверка name
    try:
        lResult['title']=inElementInfo.name
    except Exception as e:
        True == False
    #Проверка rich_text
    try:
        lResult['rich_text']=inElementInfo.rich_text
    except Exception as e:
        True == False
    #Проверка process_id
    try:
        lResult['process_id']=inElementInfo.process_id
        lResult['process']=inElementInfo.process_id
    except Exception as e:
        True == False
    #Проверка handle
    try:
        lResult['handle']=inElementInfo.handle
    except Exception as e:
        True == False
    #Проверка class_name
    try:
        lResult['class_name']=inElementInfo.class_name
    except Exception as e:
        True == False
    #Проверка control_type
    try:
        lResult['control_type']=inElementInfo.control_type
    except Exception as e:
        True == False
    #Проверка control_id
    try:
        if inElementInfo.control_id!=0:
            lResult['control_id']=inElementInfo.control_id
    except Exception as e:
        True == False
    #Проверка rectangle left
    try:
        lResult['rectangle']['left']=inElementInfo.rectangle.left
    except Exception as e:
        True == False
    #Проверка rectangle right
    try:
        lResult['rectangle']['right']=inElementInfo.rectangle.right
    except Exception as e:
        True == False
    #Проверка rectangle top
    try:
        lResult['rectangle']['top']=inElementInfo.rectangle.top
    except Exception as e:
        True == False
    #Проверка rectangle bottom
    try:
        lResult['rectangle']['bottom']=inElementInfo.rectangle.bottom
    except Exception as e:
        True == False
    #Проверка runtime_id
    try:
        lResult['runtime_id']=inElementInfo.runtime_id
    except Exception as e:
        True == False
    #Вернуть результат
    return lResult

#old: - GetRootElementList
def BackendStr_GetTopLevelList_UIOInfo(inBackend=mDefaultPywinautoBackend):
    """L+,W+: Получить список UIOInfo словарей - процессы, которые запущены в рабочей сессии и готовы для взаимодействия с роботом через backend inBackend

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lAppList = UIDesktop.BackendStr_GetTopLevelList_UIOInfo() # Очистить UIO селектор от недопустимых ключей для дальнейшего использования

    :param inBackend: вид backend, который планируется использовать для взаимодействия с UIO объектами
    :type inBackend: list, обязательный
    :return: список UIOInfo словарей
    """
    #Получить список объектов
    lResultList=pywinauto.findwindows.find_elements(top_level_only=True,backend=inBackend)    
    lResultList2=[]
    for lI in lResultList:
        lTempObjectInfo=lI
        lResultList2.append(UIOEI_Convert_UIOInfo(lI))
    return lResultList2

#old: - ElementDrawOutlineNew
def UIOSelector_Highlight(inUIOSelector):
    """L+,W+: Подсветить на несколько секунд на экране зеленой рамкой UIO объект, который соответствует входящему UIO селектору inUIOSelector

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        UIDesktop.UIOSelector_Highlight(lDemoBaseUIOSelector) # Подсветить UIO объект по UIO селектору

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inUIOSelector: list, обязательный
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        UIO_Highlight(UIOSelector_Get_UIO(inUIOSelector))
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_Highlight",
                            "ArgumentList": [inUIOSelector],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            return lPIPEResponseDict["Result"]
    return True
#old: - ElementDrawOutlineNewFocus
def UIOSelector_FocusHighlight(inUIOSelector):
    """L+,W+: Установить фокус и подсветить на несколько секунд на экране зеленой рамкой UIO объект, который соответствует входящему UIO селектору inUIOSelector

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        UIDesktop.UIOSelector_FocusHighlight(lDemoBaseUIOSelector) # Установить фокус и подсветить UIO объект по UIO селектору

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inUIOSelector: list, обязательный
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        UIO_FocusHighlight(UIOSelector_Get_UIO(inUIOSelector))
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_FocusHighlight",
                            "ArgumentList": [inUIOSelector],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            return lPIPEResponseDict["Result"]
    return True


def UIOSelector_Focus(inUIOSelector):
    """L+,W+: Установить фокус на приложение, в котором находится UIO объект

    !ВНИМАНИЕ! ДАННАЯ ФУНКЦИОНАЛЬНОСТЬ В АВТОМАТИЧЕСКОМ РЕЖИМЕ ПОДДЕРЖИВАЕТ ВСЕ РАЗРЯДНОСТИ ПРИЛОЖЕНИЙ (32|64), КОТОРЫЕ ЗАПУЩЕНЫ В СЕСИИ. PYTHON x64 ИМЕЕТ ВОЗМОЖНОСТЬ ВЗЗАИМОДЕЙСТВИЯ С x32 UIO ОБЪЕКТАМИ, НО МЫ РЕКОМЕНДУЕМ ДОПОЛНИТЕЛЬНО ИСПОЛЬЗОВАТЬ ИНТЕРПРЕТАТОР PYTHON x32 (ПОДРОБНЕЕ СМ. ФУНКЦИЮ Configure())

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        UIDesktop.UIOSelector_Focus(lDemoBaseUIOSelector) # Установить фокус и подсветить UIO объект по UIO селектору

    :param inUIOSelector: UIO селектор, который определяет UIO объект, для которого будет представлен перечень доступных активностей.
    :type inUIOSelector: list, обязательный
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Check the bitness
    lSafeOtherProcess = UIOSelector_SafeOtherGet_Process(inUIOSelector)
    if lSafeOtherProcess is None:
        UIO_Focus(UIOSelector_Get_UIO(inUIOSelector))
    else:
        # Run function from other process with help of PIPE
        lPIPEResuestDict = {"ModuleName": "UIDesktop", "ActivityName": "UIOSelector_FocusHighlight",
                            "ArgumentList": [inUIOSelector],
                            "ArgumentDict": {}}
        # Отправить запрос в дочерний процесс, который отвечает за работу с Windows окнами
        ProcessCommunicator.ProcessChildSendObject(lSafeOtherProcess, lPIPEResuestDict)
        # Get answer from child process
        lPIPEResponseDict = ProcessCommunicator.ProcessChildReadWaitObject(lSafeOtherProcess)
        if lPIPEResponseDict["ErrorFlag"]:
            raise Exception(
                f"Exception was occured in child process (message): {lPIPEResponseDict['ErrorMessage']}, (traceback): {lPIPEResponseDict['ErrorTraceback']}")
        else:
            return lPIPEResponseDict["Result"]
    return True

def UIOSelector_Click(inUIOSelector, inRuleStr="CC", inFocusBool = True):
    """L+,W+: Выполнить клик по UI объекту
        
    !ВНИМАНИЕ! Функция использует мышь. Программные способы инициализации события нажатия мыши см. в перечне активностей объекта UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        UIDesktop.UIOSelector_Click(lDemoBaseUIOSelector) # Выполнить клик по UIO объекту

    :param inUIO: UIO объект, который будет подсвечен
    :type inUIO: object UIO, обязательный
    :param inRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inRuleStr: str, опциональный
    :param inFocusBool: True - выполнить фокусировку на объект перед нажатием, False - Не выполнять фокусировку (ускорение производительности робота)
    :type inFocusBool: bool, опциональный
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    lUIO = UIOSelector_Get_UIO(inUIOSelector)
    if inFocusBool: UIO_Focus(lUIO)
    UIO_Click(lUIO, inRuleStr = inRuleStr)

def UIOSelector_ClickRight(inUIOSelector, inRuleStr="CC", inFocusBool = True):
    """L+,W+: Выполнить правый клик по UI объекту
        
    !ВНИМАНИЕ! Функция использует мышь. Программные способы инициализации события нажатия мыши см. в перечне активностей объекта UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        UIDesktop.UIOSelector_ClickRight(lDemoBaseUIOSelector) # Выполнить правый клик по UIO объекту

    :param inUIO: UIO объект, который будет подсвечен
    :type inUIO: object UIO, обязательный
    :param inRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inRuleStr: str, опциональный
    :param inFocusBool: True - выполнить фокусировку на объект перед нажатием, False - Не выполнять фокусировку (ускорение производительности робота)
    :type inFocusBool: bool, опциональный
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    lUIO = UIOSelector_Get_UIO(inUIOSelector)
    if inFocusBool: UIO_Focus(lUIO)
    UIO_ClickRight(lUIO, inRuleStr = inRuleStr)

def UIOSelector_ClickDouble(inUIOSelector, inRuleStr="CC", inFocusBool = True):
    """L+,W+: Выполнить двойной левый клик по UI объекту
        
    !ВНИМАНИЕ! Функция использует мышь. Программные способы инициализации события нажатия мыши см. в перечне активностей объекта UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        UIDesktop.UIOSelector_ClickDouble(lDemoBaseUIOSelector) # Выполнить двойной левый клик по UIO объекту

    :param inUIO: UIO объект, который будет подсвечен
    :type inUIO: object UIO, обязательный
    :param inRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inRuleStr: str, опциональный
    :param inFocusBool: True - выполнить фокусировку на объект перед нажатием, False - Не выполнять фокусировку (ускорение производительности робота)
    :type inFocusBool: bool, опциональный
    """
    #Конвертация селектора в формат UIO
    inUIOSelector = Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    lUIO = UIOSelector_Get_UIO(inUIOSelector)
    if inFocusBool: UIO_Focus(lUIO)
    UIO_ClickDouble(lUIO, inRuleStr = inRuleStr)

#old: - draw_outline_new
def UIO_Highlight(lWrapperObject,colour='green',thickness=2,fill=None,rect=None,inFlagSetFocus=False, inHighlightCountInt=2):
    """L+,W+: Выполнить подсветку UIO объекта на экране

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по UIO селектору
        UIDesktop.UIO_Highlight(lUIO) # Подсветить UIO объект по UIO селектору зеленым цветом с толщиной подсветки 2 px.

    :param lWrapperObject: UIO объект, который будет подсвечен
    :type lWrapperObject: object UIO, обязательный
    :param colour: цвет подсветки UIO объекта. Варианты: 'red', 'green', 'blue'. По умолчанию 'green'
    :type colour: str, необязательный
    :param thickness: толщина подсветки UIO объекта. По умолчанию 2
    :type thickness: int, необязательный
    :param inFlagSetFocus: признак установки фокуса на UIO объект перед подсветкой. По умолчанию False
    :type inFlagSetFocus: bool, необязательный
    """
    if fill is None: fill = win32defines.BS_NULL
    if lWrapperObject is not None:
        """
        Draw an outline around the window.
        * **colour** can be either an integer or one of 'red', 'green', 'blue'
        (default 'green')
        * **thickness** thickness of rectangle (default 2)
        * **fill** how to fill in the rectangle (default BS_NULL)
        * **rect** the coordinates of the rectangle to draw (defaults to
          the rectangle of the control)
        """
        if inFlagSetFocus:
            #Установить фокус на объект, чтобы было видно выделение
            lWrapperObject.set_focus()
            time.sleep(0.5)
        # don't draw if dialog is not visible
        #if not lWrapperObject.is_visible():
        #    return
        colours = {
            "green": 0x00ff00,
            "blue": 0xff0000,
            "red": 0x0000ff,
        }
        # if it's a known colour
        if colour in colours:
            colour = colours[colour]
        if rect is None:
            rect = lWrapperObject.rectangle()
        # create the pen(outline)
        pen_handle = win32functions.CreatePen(
                win32defines.PS_SOLID, thickness, colour)
        # create the brush (inside)
        brush = win32structures.LOGBRUSH()
        brush.lbStyle = fill
        brush.lbHatch = win32defines.HS_DIAGCROSS
        brush_handle = win32functions.CreateBrushIndirect(ctypes.byref(brush))
        # get the Device Context
        dc = win32functions.CreateDC("DISPLAY", None, None, None )
        # push our objects into it
        win32functions.SelectObject(dc, brush_handle)
        win32functions.SelectObject(dc, pen_handle)
        # draw the rectangle to the DC
        win32functions.Rectangle(
            dc, rect.left, rect.top, rect.right, rect.bottom)
        # Delete the brush and pen we created
        win32functions.DeleteObject(brush_handle)
        win32functions.DeleteObject(pen_handle)
        # delete the Display context that we created
        win32functions.DeleteDC(dc)

#old: - draw_outline_new_focus
def UIO_FocusHighlight(lWrapperObject,colour='green',thickness=2,fill=None,rect=None):
    """L+,W+: Установить фокус и выполнить подсветку UIO объекта на экране

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по UIO селектору
        UIDesktop.UIO_FocusHighlight(lUIO) # Установить фокус и подсветить UIO объект по UIO селектору зеленым цветом с толщиной подсветки 2 px.

    :param lWrapperObject: UIO объект, который будет подсвечен
    :type lWrapperObject: object UIO, обязательный
    :param colour: цвет подсветки UIO объекта. Варианты: 'red', 'green', 'blue'. По умолчанию 'green'
    :type colour: str, необязательный
    :param thickness: толщина подсветки UIO объекта. По умолчанию 2
    :type thickness: int, необязательный
    """
    if fill is None: fill = win32defines.BS_NULL
    UIO_Highlight(lWrapperObject,'green',2,fill,None,True)

def UIO_Focus(lWrapperObject):
    """L+,W+: Установить фокус UIO объекта на экране

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по UIO селектору
        UIDesktop.UIO_Focus(lUIO) # Установить фокус на UIO объект

    :param lWrapperObject: UIO объект, который будет подсвечен
    :type lWrapperObject: object UIO, обязательный
    """
    if lWrapperObject is not None:
        #Установить фокус на объект, чтобы было видно выделение
        lWrapperObject.set_focus()
        time.sleep(0.5)

#Определить разрядность процесса
lProcessBitnessStr = str(struct.calcsize("P") * 8)
Usage.Process(inComponentStr="Robot")
License.ConsoleVerify()

from . import Screen
def UIO_GetPoint(inUIO, inRuleStr="CC"):
    """L+,W+: Получить точку по прямоугольной области UI объекта inUIO с учетом сумвольного указания точки inRuleStr
        
    !ВНИМАНИЕ! Функция использует мышь. Программные способы инициализации события нажатия мыши см. в перечне активностей объекта UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по UIO селектору
        UIDesktop.UIO_Click(lUIO) # Выполнить клик по UIO объекту

    :param inUIO: UIO объект, который будет подсвечен
    :type inUIO: object UIO, обязательный
    :param inRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inRuleStr: str, опциональный
    :return: Точка на экране
    :rtype: Screen.Point

    """
    lPoint = None
    if CrossOS.IS_WINDOWS_BOOL: 
        lBox = Screen.BoxParse(inUIO.element_info.rectangle)
        lPoint = Screen.PointFromBox(inBox = lBox, inRuleStr = inRuleStr)
    else:
        lBox = Screen.BoxParse(LCompatibility.get_rect(inUIO))
        lPoint = Screen.PointFromBox(inBox = lBox, inRuleStr = inRuleStr)
    return lPoint

def UIO_Click(inUIO, inRuleStr="CC"):
    """L+,W+: Выполнить клик по UI объекту
        
    !ВНИМАНИЕ! Функция использует мышь. Программные способы инициализации события нажатия мыши см. в перечне активностей объекта UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по UIO селектору
        UIDesktop.UIO_Click(lUIO) # Выполнить клик по UIO объекту

    :param inUIO: UIO объект, который будет подсвечен
    :type inUIO: object UIO, обязательный
    :param inRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inRuleStr: str, опциональный

    """
    lPoint = UIO_GetPoint(inUIO,inRuleStr)
    Screen.PointClick(lPoint)

def UIO_ClickRight(inUIO, inRuleStr="CC"):
    """L+,W+: Выполнить правый клик по UI объекту
        
    !ВНИМАНИЕ! Функция использует мышь. Программные способы инициализации события нажатия мыши см. в перечне активностей объекта UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по UIO селектору
        UIDesktop.UIO_ClickRight(lUIO) # Выполнить клик по UIO объекту

    :param inUIO: UIO объект, который будет подсвечен
    :type inUIO: object UIO, обязательный
    :param inRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inRuleStr: str, опциональный

    """
    lPoint = UIO_GetPoint(inUIO,inRuleStr)
    Screen.PointClick(lPoint, inButtonStr="right")


def UIO_ClickDouble(inUIO, inRuleStr="CC"):
    """L+,W+: Выполнить двойной клик по UI объекту
        
    !ВНИМАНИЕ! Функция использует мышь. Программные способы инициализации события нажатия мыши см. в перечне активностей объекта UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        # 1С: UIO Селектор выбора базы
        lDemoBaseUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]		
        lUIO = UIDesktop.UIOSelector_Get_UIO(lDemoBaseUIOSelector) # Получить UIO объект по UIO селектору
        UIDesktop.UIO_ClickDouble(lUIO) # Выполнить клик по UIO объекту

    :param inUIO: UIO объект, который будет подсвечен
    :type inUIO: object UIO, обязательный
    :param inRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inRuleStr: str, опциональный

    """
    lPoint = UIO_GetPoint(inUIO,inRuleStr)
    Screen.PointClickDouble(lPoint)

def GetFocused_UIO():
    """L-,W+: Получить UIO объект, на котором установлен фокус

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lUIO = UIDesktop.GetFocused_UIO()

    :return: UIO объект
    """
    result = None
    try:
        list = UIOSelector_Get_UIOList(inSpecificationList=[{"backend":"win32"}])
        for l in list:
            if l.is_active():
                result = l
    except Exception as e:
        pass
    return result

def Selector_Get_Type(inSelector):
    """L+,W+: Техническая функция: Определить тип селектора

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]
        lType = UIDesktop.Selector_Get_Type(inSelector=lSelector) 

    :param inSelector: Селектор, тип которого необходимо определить
    :type inSelector: str или list, обязательный
    :return: Тип селектора (UIO, CSS или XPATH)
    """
    if isinstance(inSelector, list): 
        return "UIO"
    elif isinstance(inSelector, str): 
        try:
            parse_result = json.loads(inSelector)
            if isinstance(parse_result, list): return "UIO"
        except:
            pass
        if "/" in inSelector:return "XPATH"
        else: return "CSS"
    else: return "ERROR"


def Selector_Convert_Selector(inSelector, inToTypeStr):
    """L+,W+: Техническая функция: Перевести селектор в заданный тип. Доступно: UIO, CSS и XPATH

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lToType = "XPATH"
        lUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]
        lXPATHSelector = UIDesktop.Selector_Convert_Selector(inSelector=lUIOSelector, inToTypeStr=lToType) 

    :param inSelector: Селектор, который необходимо преобразовать
    :type inSelector: str или list, обязательный
    :param inToTypeStr: Тип, в который необходимо преобразовать селектор
    :type inToTypeStr: str, обязательный
    :return: Селектор
    """
    #Определяем вид селектора
    lFromTypeStr = Selector_Get_Type(inSelector)
    if lFromTypeStr ==  "ERROR": raise TypeError("Selector type couldn't be determined")

    #При конвертации в UIO
    if inToTypeStr == "UIO":
        try:
            if lFromTypeStr == "XPATH": #Отрабатываем приобразование XPath -> UIO
                lUIOSelector = XPATH_To_UIOSelector(inSelector)
            elif lFromTypeStr == "CSS": #Отрабатываем приобразование CSS -> UIO
                lUIOSelector = CSS_To_UIOSelector(inSelector)
            elif lFromTypeStr == "UIO": lUIOSelector = inSelector
            return lUIOSelector
        except Exception as e: raise e
    
    #При конвертации в XPATH
    if inToTypeStr == "XPATH":
        try:
            if lFromTypeStr == "UIO":#Отрабатываем приобразование UIO -> XPath 
                lXPATHSelector = UIOSelector_To_XPATH(inSelector)
            elif lFromTypeStr == "CSS":#Отрабатываем приобразование CSS -> XPath
                lCSSSelector = CSS_To_UIOSelector(inSelector)
                lXPATHSelector = UIOSelector_To_XPATH(lCSSSelector)
            elif lFromTypeStr == "XPATH": lXPATHSelector = inSelector
            return lXPATHSelector
        except Exception as e: raise e
    
    #При конвертации в CSS
    if inToTypeStr == "CSS":
        try:
            if lFromTypeStr == "UIO": #Отрабатываем приобразование UIO -> CSS
                lCSSSelector = UIOSelector_To_CSS(inSelector)
            elif lFromTypeStr == "XPATH": #Отрабатываем приобразование XPATH -> CSS
                lXPATHSelector = XPATH_To_UIOSelector(inSelector)
                lCSSSelector = UIOSelector_To_CSS(lXPATHSelector)
            elif lFromTypeStr == "CSS": lCSSSelector = inSelector
            return lCSSSelector
        except Exception as e: raise e


def XPATH_To_UIOSelector(inXPATHSelector):
    """L+,W+:Выполнить конвертацию селектора из XPATH в UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lXPATHSelector = "/Запуск 1С:Предприятия[@class_name='V8TopLevelFrameTaxiStarter'][@backend='uia']"
        lUIOSelector = UIDesktop.XPATH_To_UIOSelector(inXPATHSelector=lXPATHSelector)

    :param inUIOSelector: Селектор в формате XPATH
    :type inUIOSelector: str, обязательный
    """
    inUIOSelector = []
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
            if lParam == "*" or lParam == "": pass
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

def UIOSelector_To_XPATH(inUIOSelector):
    """L+,W+:Выполнить конвертацию селектора из UIO в XPATH

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]
        lXPATHSelector = UIDesktop.UIOSelector_To_XPATH(inUIOSelector=lUIOSelector)

    :param inUIOSelector: Селектор в формате UIO
    :type inUIOSelector: list, обязательный
    """
    if isinstance(inUIOSelector, str): inUIOSelector = json.loads(inUIOSelector)
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
            else: lOneLevelAttrStr += f'[@{key}="{lItem[key]}"]'
        #Составление итогового XPath селектора    
        if lTitleFlag: lSelectorTmpStr = lSelectorTmpStr + lDelimiter + lOneLevelAttrStr
        else: lSelectorTmpStr = lSelectorTmpStr + lDelimiter + "*" + lOneLevelAttrStr
    inXPATHSelector = lSelectorTmpStr

    return inXPATHSelector


def CSS_To_UIOSelector(inCSSSelector):
    """L+,W+:Выполнить конвертацию селектора из CSS в UIO

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lCSSSelector = "[title='Запуск 1С:Предприятия'][class_name='V8TopLevelFrameTaxiStarter'][backend='uia']"
        lUIOSelector = UIDesktop.CSS_To_UIOSelector(inCSSSelector=lCSSSelector)

    :param inCSSSelector: Селектор в формате CSS
    :type inCSSSelector: str, обязательный
    """
    lUIOSelector = []
    #Разбиваем селектор по уровням
    lUIOSelectorList = inCSSSelector.split(">")
    for lLevel in lUIOSelectorList:
        lLevel = lLevel.rstrip(" ").lstrip(" ")
        #Обработка пробелов, выступающих разделителями для замены на depth_start, depth_end              
        lTmpLevel = re.search(r"\]\s+\[", lLevel)
        if lTmpLevel is not None:lLevel = lLevel.replace(lTmpLevel.group(0),"]%[")
        lLevel = lLevel.split("%")
        #Обрабатываем возможную замену " " -> depth_start:1, depth_end:99
        if len(lLevel) > 1: lLevel[-1] = "/" + lLevel[-1]
        #Обработка атрибутов внутри одного уровня
        for lItem in lLevel:
            lParams = re.split('[\[\]]', lItem)
            lOneLevelDict = {}
            #Приводим к виду UIOSelector
            for lParam in lParams:
                if lParam == "": pass
                elif "/" in lParam: 
                    lOneLevelDict["depth_start"] = 1
                    lOneLevelDict["depth_end"] = 99
                elif "=" in lParam: 
                    if "'" in lParam: lParam = lParam.replace("'","")
                    elif '"' in lParam: lParam = lParam.replace('"',"")
                    lParamList = lParam.split("=")
                    try: 
                        lParamList[1] = int(lParamList[1])
                        lOneLevelDict[lParamList[0]] = lParamList[1]
                    except: lOneLevelDict[lParamList[0]] = lParamList[1].replace("."," ")
                else:
                    lOneLevelDict["title"] = lParam.replace("."," ")
            if lOneLevelDict != {}:lUIOSelector.append(lOneLevelDict)

    return lUIOSelector

def UIOSelector_To_CSS(inUIOSelector):
    """L+,W+:Выполнить конвертацию селектора из UIO в CSS

    .. code-block:: python

        # UIDesktop: Взаимодействие с UI объектами приложений
        from pyOpenRPA.Robot import UIDesktop
        lUIOSelector = [{"title":"Запуск 1С:Предприятия","class_name":"V8TopLevelFrameTaxiStarter","backend":"uia"}]
        lCSSSelector = UIDesktop.UIOSelector_To_CSS(inUIOSelector=lUIOSelector)

    :param inUIOSelector: Селектор в формате UIO
    :type inUIOSelector: list, обязательный
    """
    if isinstance(inUIOSelector, str): inUIOSelector = json.loads(inUIOSelector)
    lSelectorTmpStr = ""
    lCSSSelector = ""
    lLevelInt=0
    #Цикл по уровням
    for lItem in inUIOSelector:
        lOneLevelAttrStr = ""
        lDelimiter = ">"
        lGoUpFlag = False
        #Цикл по атрибутам внутри уровня
        for key in lItem:
            if key == "depth_end" and lLevelInt>0: lDelimiter = " "
            elif key == "depth_start" and lLevelInt>0:pass
            elif key == "go_up": lGoUpFlag = True
            elif key == "title": lOneLevelAttrStr = lItem[key].replace(" ",".") + lOneLevelAttrStr
            else: 
                try: lOneLevelAttrStr += f'[{key}="{lItem[key]}"]'
                except Exception: lOneLevelAttrStr += f'[{key}="{lItem[key]}"]'
        #Составление итогового CSS селектора
        if lGoUpFlag: raise ValueError("CSS doesn't support the go_up attribute")   
        else: lSelectorTmpStr = lSelectorTmpStr + lDelimiter + lOneLevelAttrStr
        lLevelInt+=1
    lCSSSelector = lSelectorTmpStr[1:]

    return lCSSSelector
if CrossOS.IS_WINDOWS_BOOL == False:
    from .Utils import LCompatibility
else:
    from .Utils import WCompatibility
