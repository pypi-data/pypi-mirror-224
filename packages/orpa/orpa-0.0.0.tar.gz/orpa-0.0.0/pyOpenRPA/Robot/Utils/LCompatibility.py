import copy
import pyatspi
import fnmatch
import re
import tkinter as tk
import threading
import time
from .. import UIDesktop
import subprocess
from ...Tools import CrossOS
import gi
gi.require_version('Wnck', '3.0')
from gi.repository import Wnck
backend_default = "at-spi"

def is_backend_atspi(in_uio=None, in_uio_selector=None):
    return not is_backend_wnck(in_uio=in_uio, in_uio_selector=in_uio_selector)
def is_backend_wnck(in_uio=None, in_uio_selector=None):
    if in_uio_selector!=None and in_uio==None: in_uio=get_list(in_uio_selector=in_uio_selector)[0]
    return type(in_uio) is gi.repository.Wnck.Window

def get_rect_l_r_t_b(in_uio):
    if is_backend_atspi(in_uio):
        attr_dict = get_attr_dict(in_uio)["rectangle"]
        return (attr_dict["x"], attr_dict["x"]+attr_dict["width"], attr_dict["y"], attr_dict["y"]+attr_dict["height"])
    else:
        g = in_uio.get_geometry()
        return (g[0], g[0]+g[2], g[1], g[1]+g[3])
    
def get_rect(in_uio):
    g = get_attr_dict(in_uio) 
    res = None
    if is_backend_wnck(in_uio=in_uio):
        res = g["geometry"]
    else:
        res = g["rectangle"]
    return res

# ATTENTION : NEED xwininfo
def _wnck_get_geometry(in_uio):
    if is_backend_wnck(in_uio=in_uio):
        # Получение вывода команды xwininfo
        try:
            output = subprocess.check_output(["xwininfo", "-id", str(in_uio.get_xid()), "-frame"])
        except Exception as e:
            return {"x":0,"y":0, "width":0, "height":0}
        # Преобразование вывода в строку
        output_str = output.decode()

        # Поиск координат в выводе
        x = int(output_str.split("Absolute upper-left X:")[1].split("\n")[0])
        y = int(output_str.split("Absolute upper-left Y:")[1].split("\n")[0])
        width = int(output_str.split("Width:")[1].split("\n")[0])
        height = int(output_str.split("Height:")[1].split("\n")[0])
        return {"x":x,"y":y, "width":width, "height":height}

def get_attr_dict(in_uio=None, in_uio_selector=None, in_backend=backend_default):
    if in_uio_selector!=None and in_uio==None: in_uio=get_list(in_uio_selector=in_uio_selector)[0]
    if is_backend_wnck(in_uio=in_uio, in_uio_selector=in_uio_selector):
        g = _wnck_get_geometry(in_uio)
        res = {
            "name": in_uio.get_name(),
            "role": in_uio.get_role(),
            "class_group_name": in_uio.get_class_group_name(),
            "class_instance_name": in_uio.get_class_instance_name(),
            "group_leader": in_uio.get_group_leader(),
            "icon_name": in_uio.get_icon_name(),
            "ref_count":in_uio.ref_count,
            "pid":in_uio.get_pid(),
            "xid":in_uio.get_xid(),
            "geometry":g,
            "backend":"wnck"
        }
    else:
        res = {
            "id":in_uio.id,
            "name": in_uio.get_name(),
            "current_value": None,
            "description": in_uio.get_description(),
            "role_name": in_uio.get_role_name(),
            "child_count":in_uio.childCount,
            "toolkit_name":in_uio.get_toolkit_name(),
            "toolkit_version":in_uio.get_toolkit_version(),
            "path": in_uio.path,
            "alpha": in_uio.get_alpha(),
            "process_id":in_uio.get_process_id(),
            "rectangle":{"x":in_uio.get_position(0).x, "y": in_uio.get_position(0).y, "width": in_uio.get_extents(0).width, "height": in_uio.get_extents(0).height},
            "attributes":in_uio.get_attributes(),
            "backend":"at-spi"
        }
        #RECTANGLE PROCESSING
        if res["role_name"]=="application" and res["child_count"]>0:
            res["rectangle"]={"x":in_uio[0].get_position(0).x, "y": in_uio[0].get_position(0).y, "width": in_uio[0].get_extents(0).width, "height": in_uio[0].get_extents(0).height}
        try:  res["current_value"]=in_uio.get_current_value()
        except: pass
    return res


def get_top_level_list(in_backend=backend_default):
    result_list = []
    if in_backend=="at-spi":
        # Получаем объект доступности для рабочего стола
        desktop = pyatspi.Registry.getDesktop(0)
        # Получаем количество дочерних объектов доступности на рабочем столе
        childCount = desktop.childCount
        # Получаем список приложений
        result_list = []
        for app in desktop:
            try:
                # Добавляем имя приложения в список (Если не пустой процесс, а имеются окна)
                if app.get_role_name()=="application" and app.childCount==0:
                    pass
                else:
                    result_list.append(app)
            except:
                pass
    elif in_backend=="wnck":
        # Get the screen and window list
        screen = Wnck.Screen.get_default()
        screen.force_update()
        windows = screen.get_windows()
        # Print the name of each window
        for window in windows:
            result_list.append(window)
    return result_list
    
def focus(in_uio):
    wnck_uio = atspi_to_wnck(in_uio=in_uio)
    wnck_uio.activate(time.time())
    
def atspi_to_wnck(in_uio):
    if is_backend_atspi(in_uio=in_uio):
        pid = in_uio.get_process_id()
        uio_list = get_list([{"pid": pid,"backend":"wnck"}])
        if len(uio_list)>0: return uio_list[0]
        else: return None
    else: return in_uio

HIGHLIGHT_ROOT = None
HIGHLIGHT_FRAME = None

def highlight_init():
    global HIGHLIGHT_ROOT, HIGHLIGHT_FRAME
    HIGHLIGHT_ROOT = tk.Tk()
    HIGHLIGHT_FRAME = tk.Frame(HIGHLIGHT_ROOT)
    #frame.root.config(cursor="cross")#Изменение курсора
    HIGHLIGHT_ROOT.attributes('-type','normal') #Установить тип (важно для линукс ред ос)
    HIGHLIGHT_ROOT.attributes('-alpha', 0.7) #Установить прозрачность
    #Определить общее разрешение экрана/ов
    HIGHLIGHT_ROOT.geometry( f"{0}x{0}+{0}+{0}" ) #Установить размеры окна snipingtool

    #Установить безрамочный режим и верхний уровень
    HIGHLIGHT_ROOT.overrideredirect(1)
    HIGHLIGHT_ROOT.attributes('-topmost', True)
    HIGHLIGHT_FRAME.canvas = tk.Canvas(HIGHLIGHT_ROOT, width = 0, height = 0, bg = "green")
    HIGHLIGHT_FRAME.canvas.grid(row=0, column=0, sticky='nsew')
    HIGHLIGHT_ROOT.mainloop()
threading.Thread(target= highlight_init).start()

def highlight(in_uio, in_count_int = 4):
    count = in_count_int
    iterator = 0
    global HIGHLIGHT_ROOT, HIGHLIGHT_FRAME
    storage={"flag_sync_stop":False, "rect": get_rect(in_uio)}
    def toggle_color(iterator,count, storage):
        global HIGHLIGHT_ROOT, HIGHLIGHT_FRAME
        interval = 500
        if HIGHLIGHT_FRAME.canvas.cget("bg") == "green":
            HIGHLIGHT_FRAME.canvas.config(bg="black")
            #HIGHLIGHT_FRAME.canvas.config(width=0,height=0)
            HIGHLIGHT_ROOT.geometry( f"{0}x{0}+{storage['rect']['x']}+{storage['rect']['y']}" ) #Установить размеры окна snipingtool
        else:
            #frame.canvas.config(bg="green")
            HIGHLIGHT_FRAME.canvas.config(bg="green")
            HIGHLIGHT_FRAME.canvas.config(width=storage['rect']['width'],height=storage['rect']['height'])
            HIGHLIGHT_ROOT.geometry( f"{storage['rect']['width']}x{storage['rect']['height']}+{storage['rect']['x']}+{storage['rect']['y']}" ) #Установить размеры окна snipingtool
            #frame.canvas.config(width = width, height = height)
            #frame.canvas = tk.Canvas(root, width = width, height = height, bg = "green")
            #frame.canvas.grid(row=0, column=0, sticky='nsew')
        if iterator>count:
            #HIGHLIGHT_ROOT.destroy()
            HIGHLIGHT_ROOT.geometry( f"{0}x{0}+{storage['rect']['x']}+{storage['rect']['y']}" ) #Установить размеры окна snipingtool
            storage["flag_sync_stop"] = True
        else:
            HIGHLIGHT_FRAME.canvas.after(interval, toggle_color, iterator+1,count, storage)
    if storage["rect"]["width"] > 0 and storage["rect"]["height"] >0:
        storage["rect"]=Screen.BoxToDict(Screen.DisplayBox(storage["rect"]))
        toggle_color(iterator,count, storage)
        while not storage["flag_sync_stop"]: time.sleep(0.3) # СОЗДАНИЕ СИНХРОННОСТИ
        return True
    else:
        return False


def get_child_list(in_uio_selector,in_flag_raise_exception=True):
    uio_parent_list = get_list(in_uio_selector=in_uio_selector, in_flag_raise_exception=in_flag_raise_exception)
    result_list = []
    for item in uio_parent_list:
        result_list = result_list + list(item)
    return result_list
def get_list (in_uio_selector=None,in_parent_uio=None,in_flag_raise_exception=True, in_backend=backend_default):
    if in_uio_selector!=None and len(in_uio_selector)>0: in_backend=in_uio_selector[0].get("backend", backend_default)
    result_list=[]
    children_list=[]
    filter_ignore_attr_set = {"depth_start", "depth_end", "shift", "go_up" , "ctrl_index", "backend"}
    # ВЕТКА ПУСТОЙ СПЕЦИФИКАЦИИ
    if in_uio_selector==None: in_uio_selector=[]
    if in_uio_selector==[]:
        #Получить список объектов    
        return get_top_level_list(in_backend=in_backend)
    #КОНВЕРТАЦИЯ СЕЛЕКТОРА В ФОРМАТ UIO
    #in_uio_selector = Selector_Convert_Selector(inSelector=in_uio_selector, inToTypeStr="UIO")
    #Создать копию входного листа, чтобы не менять массив в других верхнеуровневых функциях
    in_uio_selector=copy.deepcopy(in_uio_selector)
    try:

        selector_lvl_0_dict = in_uio_selector[0]
        #Обработка якоря go_up по необходимости
        if 'go_up' in selector_lvl_0_dict and in_parent_uio!=None:
            try:
                #Поднимаемся по уровням наверх
                for i in range(int(selector_lvl_0_dict['go_up'])):
                    in_parent_uio = in_parent_uio.parent
                #Обработка случая наличия go_up (отключение дальнешей проверки на этом уровне)
                uio_children_list = []
                if in_parent_uio is None: raise AttributeError("Nonetype error")
                children_list.append(in_parent_uio)
            except AttributeError: 
                if in_flag_raise_exception: raise Exception('Value of the "go_up" attribute is too large')
                else: return []
        #Обработка якоря shift по необходимости
        elif 'shift' in selector_lvl_0_dict and in_parent_uio!=None:
            try:
                #Поднимаемся на один уровень 
                inElementParentChildrenList = list(in_parent_uio.parent)
                for index, lNewChildren in enumerate(inElementParentChildrenList): #Ищем индекс текущего элемента внутри списка всех детей от родителя
                    if in_parent_uio == lNewChildren: #По нахождению делаем необходимый переход
                        if int(selector_lvl_0_dict['shift']) > 0: in_parent_uio = inElementParentChildrenList[index+int(selector_lvl_0_dict['shift'])]
                        else: 
                            if index-abs(int(selector_lvl_0_dict['shift'])) < 0: raise IndexError("Bad value error")
                            in_parent_uio = inElementParentChildrenList[index-abs(int(selector_lvl_0_dict['shift']))]
                        break
                #Обработка случая наличия shift (отключение дальнешей проверки на этом уровне)
                uio_children_list = []
                children_list.append(in_parent_uio)
            except IndexError: 
                if in_flag_raise_exception: raise Exception('Value of the "shift" attribute is too large')
                else: return []
        else: # если нет атрибута go_up и/или shift
            #Получить список элементов
            if in_parent_uio is None:
                uio_children_list=get_top_level_list(in_backend=in_backend)
            else:
                uio_children_list=list(in_parent_uio)
            #Если нет точного обозначения элемента
            lFlagGoCheck=True
        #Учесть поле depth_start (если указано)
        if 'depth_start' in selector_lvl_0_dict:
            if selector_lvl_0_dict["depth_start"]>1:
                lFlagGoCheck=False

        #Циклический обход по детям, на предмет соответствия всем условиям
        lFilterList = []
        for index, uio_children_item in enumerate(uio_children_list):
            #Обработка глубины depth (рекурсивный вызов для всех детей с занижением индекса глубины)
            #По умолчанию значение глубины 1
            if 'depth_end' in selector_lvl_0_dict:
                if selector_lvl_0_dict['depth_end']>1:
                    #Подготовка новой версии спецификации
                    uio_selector_children=in_uio_selector.copy()
                    uio_selector_children[0]=uio_selector_children[0].copy()
                    uio_selector_children[0]["depth_end"]=uio_selector_children[0]["depth_end"]-1
                    if 'depth_start' in uio_selector_children[0]:
                        uio_selector_children[0]["depth_start"]=uio_selector_children[0]["depth_start"]-1
                    #Циклический вызов для всех детей со скорректированной спецификацией
                    result_list.extend(get_list(uio_selector_children,uio_children_item,in_flag_raise_exception))
            #Фильтрация
            if lFlagGoCheck:
                # НОВЫЙ ДВИЖОК ФИЛЬТРАЦИИ УНИВЕРСАЛЬНЫЙ
                uio_attr_dict = get_attr_dict(uio_children_item)
                flag_add_child=True
                for selector_attr in selector_lvl_0_dict:
                    selector_attr_value = selector_lvl_0_dict[selector_attr]
                    # ПЕРЕЙТИ К ФИЛЬТРАЦИИ ЕСЛИ НЕ ВХОДИТ В МНОЖЕСТВО КЛЮЧЕВЫХ СЛОВ
                    if selector_attr not in filter_ignore_attr_set:
                        # ВИД ПРОВЕРКИ (РАВЕНСТВО / WC / RE)
                        selector_attr_name = selector_attr.lower()
                        if "_re" in selector_attr_name: # RE MATCH
                            selector_attr_name = selector_attr_name.replace("_re", "")
                            if selector_attr_name in uio_attr_dict: # ПРОВЕРИТЬ НАЛИЧИЕ АТРИБУТА СО СТОРОНЫ UI ОБЪЕКТА
                                if re.fullmatch(selector_attr_value,uio_attr_dict[selector_attr_name]) is None: flag_add_child=False
                            else: flag_add_child=False
                        elif "_wc" in selector_attr_name: # WC MATCH
                            selector_attr_name = selector_attr_name.replace("_wc", "")
                            if selector_attr_name in uio_attr_dict: # ПРОВЕРИТЬ НАЛИЧИЕ АТРИБУТА СО СТОРОНЫ UI ОБЪЕКТА
                                if fnmatch.fnmatch(uio_attr_dict[selector_attr_name], selector_attr_value) == False: flag_add_child=False
                            else: flag_add_child=False
                        else: # EQUAL MATCH
                            if selector_attr_name in uio_attr_dict: # ПРОВЕРИТЬ НАЛИЧИЕ АТРИБУТА СО СТОРОНЫ UI ОБЪЕКТА
                                if selector_attr_value!=uio_attr_dict[selector_attr_name]:flag_add_child=False
                            else: flag_add_child=False
                #Все проверки пройдены - флаг добавления
                if flag_add_child:
                    lFilterList.append(uio_children_item)
        if "ctrl_index" in in_uio_selector[0]:
            lIndexInt = in_uio_selector[0]["ctrl_index"]
            if lIndexInt<len(lFilterList):
                children_list.append(lFilterList[lIndexInt])
        else:
            children_list.extend(lFilterList)                
        #Выполнить рекурсивный вызов (уменьшение количества спецификаций), если спецификация больше одного элемента
        #????????Зачем в условии ниже is not None ???????????
        if len(in_uio_selector)>1 and len(children_list)>0:
            #Вызвать рекурсивно функцию получения следующего объекта, если в спецификации есть следующий объект
            for child_item in children_list:
                result_list.extend(get_list(in_uio_selector[1:],child_item,in_flag_raise_exception))
        else:
            result_list.extend(children_list)
        #Условие, если результирующий список пустой и установлен флаг создания ошибки (и in_parent_uio is None - не следствие рекурсивного вызова)
        if in_parent_uio is None and len(result_list)==0 and in_flag_raise_exception:
            raise Exception("There are no UI elements by selector (UIO / XPATH / CSS)")
        #if __define__.DEFINE_ACCEPTED==True: return result_list
        #else: return []
        return result_list
    except Exception as e:
        if in_flag_raise_exception: raise e
        else: return []

from .. import Screen
#old: - GUISearchElementByRootXY
def get_list_by_x_y(in_uio,in_x,in_y,in_show_root_bool=False, in_flag_stop_first=False, in_uio_index_int = None, in_level_limit_int = 30, in_level_iterator = 0):
    """L+,W+: Техническая функция: Получить иерархию вложенности UIO объекта по заданным корневому UIO объекту, координатам X и Y.

    """
    #Инициализация результирующего значения
    result_level = [{'index':in_uio_index_int,'element':in_uio}]
    result =[]
    #Получить координаты текущего объекта
    uio_box = Screen.BoxParse(get_rect(in_uio))
    point = Screen.PointParse(in_x,in_y)
    #Добавить объект в результирующий, если координаты попадают в него
    if Screen.PointIsInBox(point, uio_box):
        # ТОЧКА ВНУТРИ - ПРОДОЛЖИТЬ ПОИСК
        # РЕКУРСИВНЫЙ ВЫЗОВ ПО ДЕТЯМ - ВОЗМОЖНО ЕСТЬ УРОВЕНЬ ГЛУБЖЕ
        child_index=0
        flag_first_branch_found=False
        if in_level_iterator<in_level_limit_int:
            list_uio=[]
            try:
                list_uio = list(in_uio)
            except Exception as e:
                pass
            for child_uio in list_uio:
                if in_flag_stop_first==True and flag_first_branch_found==True: break;
                child_result = get_list_by_x_y(child_uio,in_x,in_y, in_show_root_bool=True,in_flag_stop_first=in_flag_stop_first, in_uio_index_int=child_index, in_level_limit_int = in_level_limit_int, in_level_iterator = in_level_iterator+1)
                for item in child_result:
                    if in_show_root_bool==True: result.append(result_level+item)
                    else: result.append(item)
                    flag_first_branch_found = True
                    if in_flag_stop_first==True and flag_first_branch_found==True: break;
                child_index=child_index+1
        if in_show_root_bool==True and len(result)==0:
            result.append(result_level)
    return result


#old: - GUISearchElementByRootXY
def __UIOXY_SearchChild_ListDict(inRootElement,inX,inY,inHierarchyList=None, inShowRootBool=False, inFlagSearchAll=False):
    result = get_list_by_x_y(in_uio=inRootElement,in_x=inX,in_y=inY, in_show_root_bool=inShowRootBool, in_flag_stop_first=(not inFlagSearchAll))
    if len(result)==0: return [] 
    else: return result

#old: - GUISearchElementByRootXY
UIDesktop.UIOXY_SearchChild_ListDict = __UIOXY_SearchChild_ListDict

#ALIASES
def __UIOSelector_Get_UIOList(inSpecificationList,inElement=None,inFlagRaiseException=True,inBackend=None):
    if inBackend==None:
        return get_list (in_uio_selector=inSpecificationList,in_parent_uio=inElement,in_flag_raise_exception=inFlagRaiseException)
    else: return get_list (in_uio_selector=inSpecificationList,in_parent_uio=inElement,in_flag_raise_exception=inFlagRaiseException, in_backend=inBackend)
UIDesktop.UIOSelector_Get_UIOList = __UIOSelector_Get_UIOList

def __UIOEI_Convert_UIOInfo(inElementInfo):
    return get_attr_dict (in_uio=inElementInfo)
UIDesktop.UIOEI_Convert_UIOInfo = __UIOEI_Convert_UIOInfo

def __UIOSelector_Get_UIOInfoList (inUIOSelector, inElement=None, inFlagRaiseException=True):
    #Конвертация селектора в формат UIO
    inUIOSelector = UIDesktop.Selector_Convert_Selector(inSelector=inUIOSelector, inToTypeStr="UIO")
    #Получить родительский объект если на вход ничего не поступило
    lResultList=UIDesktop.UIOSelector_Get_UIOList(inUIOSelector, inElement, inFlagRaiseException)
    lIterator = 0
    for lItem in lResultList:
        lResultList[lIterator]=UIDesktop.UIOEI_Convert_UIOInfo(lResultList[lIterator])
        lIterator = lIterator + 1
    return lResultList
UIDesktop.UIOSelector_Get_UIOInfoList = __UIOSelector_Get_UIOInfoList

#old: - GetRootElementList
def __BackendStr_GetTopLevelList_UIOInfo(inBackend="at-spi"):
    #Получить родительский объект если на вход ничего не поступило
    lResultList=UIDesktop.UIOSelector_Get_UIOList(None, inBackend=inBackend)
    lIterator = 0
    for lItem in lResultList:
        lResultList[lIterator]=UIDesktop.UIOEI_Convert_UIOInfo(lResultList[lIterator])
        lIterator = lIterator + 1
    return lResultList
UIDesktop.BackendStr_GetTopLevelList_UIOInfo = __BackendStr_GetTopLevelList_UIOInfo
def __UIOSelector_Get_UIOInfo(inUIOSelector):
    return get_attr_dict (in_uio_selector=inUIOSelector)
UIDesktop.UIOSelector_Get_UIOInfo = __UIOSelector_Get_UIOInfo

#old: - draw_outline_new
def __UIO_Highlight(lWrapperObject,colour='green',thickness=2,fill=None,rect=None,inFlagSetFocus=False, inHighlightCountInt = 3):
    highlight(lWrapperObject, in_count_int = inHighlightCountInt)
UIDesktop.UIO_Highlight = __UIO_Highlight

def __UIO_Focus(lWrapperObject):
    return focus(in_uio=lWrapperObject)
UIDesktop.UIO_Focus = __UIO_Focus

def __UIO_FocusHighlight(lWrapperObject,colour='green',thickness=2,fill=None,rect=None,inFlagSetFocus=False):
    focus(in_uio=lWrapperObject)
    highlight(lWrapperObject)
    return None
UIDesktop.UIO_FocusHighlight = __UIO_FocusHighlight