# 1.2.0 - general processor - contains old orchestrator processor + RDPActive processor
import time, copy, threading, uuid, sys, inspect, pyscreeze, traceback

def ActivityItemHelperDefList(inDefQueryStr=None):
    """L+,W+: Получить список синонимов (текстовых ключей), доступных для использования в Активностях (ActivityItem).

    :param inDefStr: Часть текстового ключ (начало / середина / конец)
    :return: Список доступных ключей в формате: ["ActivityItemDefAliasUpdate", "ActivityItemDefAliasCreate", etc...]
    """
    lResultList = []
    if inDefQueryStr is not None: # do search alg
        for lModuleStr in sys.modules:
            lModule = sys.modules[lModuleStr]
            for lDefStr in dir(lModule):
                lNameStr = f"{lModuleStr}.{lDefStr}"
                lNameStr = lNameStr.upper()
                if inDefQueryStr.upper() in lNameStr:
                    lResultList.append(f"{lModuleStr}.{lDefStr}")
    else:
        for lModuleStr in sys.modules:
            lModule = sys.modules[lModuleStr]
            for lDefStr in dir(lModule):
                lResultList.append(f"{lModuleStr}.{lDefStr}")
    return lResultList

def ActivityItemHelperDefAutofill(inDef):
    """L+,W+: Анализ аргументов функции по синониму (текстовому ключу).

    :param inDef: Часть текстового ключ (начало / середина / конец)
    :return: Преднастроенная структура активности (ActivityItem)         
        {
            "Def": None,
            "ArgList": [],
            "ArgDict": {}
        }
    """
    lResultDict = {
        "Def": None,
        "ArgList": [],
        "ArgDict": {}
    }
    lResultDict["Def"] = inDef        
    lSplitList = inDef.split(".")
    lModuleStr = ".".join(lSplitList[:-1])
    lDefStr = lSplitList[-1]
    lModule = sys.modules[lModuleStr]
    lModuleDefList = dir(lModule)
    lDef = None
    if lDefStr in lModuleDefList:
        lItemDef = getattr(lModule,lDefStr)
        if callable(lItemDef): lDef=lItemDef
        else: raise Exception("Def is not callable")
        lDefSignature = inspect.signature(lDef)
        for lItemKeyStr in lDefSignature.parameters:
            lItemValue = lDefSignature.parameters[lItemKeyStr]
            if lItemValue.default is inspect._empty:
                lResultDict["ArgDict"][lItemKeyStr] = None
            else:
                lResultDict["ArgDict"][lItemKeyStr] = lItemValue.default
    return lResultDict
import json
def ActivityListExecute(inActivityList):
    lResultList = [] # init the result list
    for lActivityItem in inActivityList:  # Iterate throught the activity list
        lDef = None  # Def variable
        if callable(lActivityItem["Def"]):  # CHeck if def is callable
            lDef = lActivityItem["Def"]  # Get the def
        else:  # Is not callable - check alias
            # Append Orchestrator def to ProcessorDictAlias
            lSplitList = lActivityItem["Def"].split(".")
            lModuleStr = ".".join(lSplitList[:-1])
            lDefStr = lSplitList[-1]
            lModule = sys.modules[lModuleStr]
            lModuleDefList = dir(lModule)
            if lDefStr in lModuleDefList:
                lItemDef = getattr(lModule,lDefStr)
                if callable(lItemDef): lDef=lItemDef
                else: raise Exception("Def is not callable")
        if lActivityItem.get("ArgList", None) == None: lActivityItem["ArgList"]=[]
        if lActivityItem.get("ArgDict", None) == None: lActivityItem["ArgDict"]={} 
        # Обработка случая - аргумент строка. Актуально для XPATH и CSS селекторов
        if isinstance(lActivityItem["ArgList"], str): 
            try: lActivityItemResult = lDef(lActivityItem["ArgList"])
            except Exception as e: lActivityItemResult={"ErrorHeader":str(e), "ErrorTraceback":traceback.format_exc()}
        else:
            try:lActivityItemResult = lDef(*lActivityItem["ArgList"], **lActivityItem["ArgDict"])
            except Exception as e: lActivityItemResult={"ErrorHeader":str(e), "ErrorTraceback":traceback.format_exc()}
        # ??? при возврате box необходим отличный от обычного подход ???
        try: 
            if isinstance(lActivityItemResult, pyscreeze.Box): 
                lActivityItemResult= {"left":int(lActivityItemResult.left), "top":int(lActivityItemResult.top), "width":int(lActivityItemResult.width), "height":int(lActivityItemResult.height)}   
        except Exception:pass
        # Попытаться конвертировать в JSON - если не конвертируется, то  взять str отображение
        try:
            json.dumps(lActivityItemResult)
            lResultList.append(lActivityItemResult) # return the result
        except Exception as e:
            lResultList.append(str(lActivityItemResult)) # return the result
    return lResultList # return the result list

def __ActivityListVerify__(inActivityList):
    """
    Verify ActivityList variable - raise exception if input list is not list of dict with structure:
        #    "Def":"DefAliasTest", # def link or def alias (look gSettings["Processor"]["AliasDefDict"])
        #    "ArgList":[1,2,3], # Args list
        #    "ArgDict":{"ttt":1,"222":2,"dsd":3}, # Args dictionary

    :param inActivityList:
    :return:
    """
    # CASE LIST
    if type(inActivityList) is list:
        for lItem in inActivityList:
            # CASE LIST item is LIST
            if type(lItem) is list:
                raise Exception(f"pyOpenRPA Processor.__ActivityListVerify__: inActivityList has wrong structure! Details: Your ActivityList item is list too. List of the list :(")
            # CASE Item is not dict
            if type(lItem) is not dict:
                raise Exception(f"pyOpenRPA Processor.__ActivityListVerify__: inActivityList has wrong structure! Details: Your ActivityList item is is not dict")
            # CASE HAS NO "Def"
            if "Def" not in lItem:
                raise Exception(f"pyOpenRPA Processor.__ActivityListVerify__: inActivityList has wrong structure! Details: Activity item has no attribute 'Def'")
    #CASE NOT LIST
    else:
        raise Exception(f"pyOpenRPA Processor.__ActivityListVerify__: inActivityList has wrong structure! Details: Your ActivityList is not a list.")