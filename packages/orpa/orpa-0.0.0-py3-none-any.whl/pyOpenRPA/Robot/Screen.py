from pyautogui import *
import pyautogui
import pyscreeze
import ctypes
import threading
import sys
from pyOpenRPA.Tools import CrossOS
from . import Mouse, Keyboard, UIDesktop
if CrossOS.IS_WINDOWS_BOOL:
    from pywinauto import win32defines, win32structures, win32functions
    import win32api
elif CrossOS.IS_LINUX_BOOL: 
    import tkinter as tk # Python 3
    from Xlib import display
    from PIL import Image
from screeninfo import get_monitors
import tkinter as tk
if CrossOS.IS_WINDOWS_BOOL:
    from desktopmagic.screengrab_win32 import (
    getDisplayRects, saveScreenToBmp, saveRectToBmp, getScreenAsImage,
    getRectAsImage, getDisplaysAsImages)

import subprocess
import time
import copy

IMAGE_WAIT_SEC_FLOAT = 60
IMAGE_WAIT_INTERVAL_SEC_FLOAT = 1.0

class Box:
    def __init__(self, left,top,width,height):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
    
    left = 0
    top = 0
    width = 0
    height = 0

class Point:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    x = 0
    y = 0

def DisplayInfo():
    """L+,W-: Получить информацию об экранах

    .. code-block:: python

        # Screen: Взаимодействие с экраном
        from pyOpenRPA.Robot import Screen
        Screen.DisplayInfo() # RESULT: [{'x': 0, 'y': 0, 'width': 1920, 'height': 1080, 'depth': 24}]

    """
    result_list = []
    display_obj = display.Display()
    screen_count = display_obj.screen_count()

    for i in range(screen_count):
        screen_obj = display_obj.screen(i)
        root_window = screen_obj.root
        geometry = root_window.get_geometry()
        result_list.append({"x":geometry.x, "y":geometry.y, "width":geometry.width, "height": geometry.height, "depth": geometry.depth})
    display_obj.close()
    return result_list
def DisplayBox(inBox):
    """L+,W-: Скорректировать прямоугольную область Box под существующие экраны.

    :param inBox: Прямоугольная область 
    :type inBox: Box, list, dict
    """
    
    inBox=BoxParse(inBox)
    result_box = copy.copy(inBox)
    display_list = DisplayInfo()
    flag_display_overlay = False
    for display in display_list:
        display_box = BoxParse(display)
        if BoxOverlay(inBox, display_box):
            flag_display_overlay=True
            if result_box.left<display_box.left: result_box.left = display_box.left
            if result_box.top<display_box.top: result_box.top = display_box.top
            if result_box.left+result_box.width>display_box.left+display_box.width: result_box.width = display_box.left+display_box.width
            if result_box.top+result_box.height>display_box.top+display_box.height: result_box.height = display_box.top+display_box.height
            break
    if flag_display_overlay==False: return BoxParse([0,0,0,0])
    return result_box

def BoxToDict(inBox):
    """L+,W+: Конвертировать объект Box в {"x":0, "y":0, "width":100, "height":100}

    :param inBox: Прямоугольная область 
    :type inBox: Box, list, dict
    """
    inBox=BoxParse(inBox)
    return {"x":inBox.left, "y":inBox.top, "width":inBox.width, "height":inBox.height}

def PointIsInBox(inPoint, inBox): 
    """L+,W+: Проверить вхождение точки Point в прямоугольную область Box

    .. code-block:: python

        # Screen: Взаимодействие с экраном
        from pyOpenRPA.Robot import Screen
        # Поддерживает форматы
        Screen.PointIsInBox([1,1], [10,10,200,200])
        Screen.PointIsInBox((1,1), (1,1,200,200))
        Screen.PointIsInBox({"x":1,"y":1}, {"x":1,"y":1, "w":200,"h":200})

    """
    lPoint = PointParse(inPoint)
    lBox = BoxParse(inBox)
    return (lPoint.x>=lBox.left and lPoint.x<=lBox.width+lBox.left and lPoint.y>=lBox.top and lPoint.y<=lBox.top+lBox.height)

def PointParse(*args, **kwargs):
    """L+,W+: Создать экземпляр точки.

    .. code-block:: python

        # Screen: Взаимодействие с экраном
        from pyOpenRPA.Robot import Screen
        # Поддерживает форматы
        Screen.PointParse(x=1,y=1)
        Screen.PointParse(1,1)
        Screen.PointParse(x=1,y=1)
        Screen.PointParse(l=1,t=1)
        Screen.PointParse([1,1])
        Screen.PointParse((1,1))
        Screen.PointParse({"x":1,"y":1})

    """
    lTopInt=0; lLeftInt=0;

    if len(args)==2: # xywh
        lLeftInt=args[0];lTopInt=args[1];
    elif len(args)==1:
        var = args[0]
        if type(var) is pyscreeze.Point: return Point(x=var.x, y=var.y) #Передан корректный объект - конвертация не требуется
        if (type(var) is tuple) or (type(var) is list):
            lLeftInt=var[0];lTopInt=var[1];
        elif (type(var) is dict):
            for char in ["x","X","l","L","left","LEFT","Left"]: 
                if char in var: lLeftInt=var[char]; break;
            for char in ["y","Y","T","t","top","TOP","Top"]: 
                if char in var: lTopInt=var[char]; break;
            for char in ["w","W","width","WIDTH","Width"]: 
                if char in var: lLeftInt=var[char]; break;
            for char in ["h","H","height","HEIGHT","Height"]: 
                if char in var: lTopInt=var[char]; break;
            for char in ["r","R","right","RIGHT","Right"]: 
                if char in var: lLeftInt=var[char]; break;
            for char in ["b","B","bottom","BOTTOM","Bottom"]: 
                if char in var: lTopInt=var[char]; break;
        else:
            attr_list = dir(var)
            for char in ["x","X","l","L","left","LEFT","Left"]: 
                if char in attr_list: lLeftInt=getattr(var,char); break;
            for char in ["y","Y","T","t","top","TOP","Top"]: 
                if char in attr_list: lTopInt=getattr(var,char); break;
            for char in ["w","W","width","WIDTH","Width"]: 
                if char in attr_list: lLeftInt=getattr(var,char); break;
            for char in ["h","H","height","HEIGHT","Height"]: 
                if char in attr_list: lTopInt=getattr(var,char); break;
            for char in ["r","R","right","RIGHT","Right"]: 
                if char in attr_list: lLeftInt=getattr(var,char); break;
            for char in ["b","B","bottom","BOTTOM","Bottom"]: 
                if char in attr_list: lTopInt=getattr(var,char); break;

    if len(kwargs)>0:
        for char in ["x","X","l","L","left","LEFT","Left"]: 
            if char in kwargs: lLeftInt=kwargs[char]; break;
        for char in ["y","Y","T","t","top","TOP","Top"]: 
            if char in kwargs: lTopInt=kwargs[char]; break;
        for char in ["w","W","width","WIDTH","Width"]: 
            if char in kwargs: lLeftInt=kwargs[char]; break;
        for char in ["h","H","height","HEIGHT","Height"]: 
            if char in kwargs: lTopInt=kwargs[char]; break;
        for char in ["r","R","right","RIGHT","Right"]: 
            if char in kwargs: lLeftInt=kwargs[char]; break;
        for char in ["b","B","bottom","BOTTOM","Bottom"]: 
            if char in kwargs: lTopInt=kwargs[char]; break;
    # СОЗДАТЬ ОБЪЕКТ BOX
    return PointCreate(inXInt=lLeftInt, inYInt=lTopInt )

def BoxParse(*args, **kwargs):
    """L+,W+: Создать экземпляр прямоугольной области.

    .. code-block:: python

        # Screen: Взаимодействие с экраном
        from pyOpenRPA.Robot import Screen
        # Поддерживает форматы
        Screen.BoxParse(x=1,y=1,w=900, h=90)
        Screen.BoxParse(1,1,900, 90)
        Screen.BoxParse(x=1,y=1,r=901, b=91)
        Screen.BoxParse(x=1,y=1,r=901, bottom=91)
        Screen.BoxParse([1,1,900, 90])
        Screen.BoxParse((1,1,900, 90))
        Screen.BoxParse({"x":1,"y":1,"w":900, "h":90})

    """
    lTopInt=0; lLeftInt=0; lHeightInt=0; lWidthInt=0

    if len(args)==4: # xywh
        lLeftInt=args[0];lTopInt=args[1];lWidthInt=args[2];lHeightInt=args[3]
    elif len(args)==2: # wh == rb
        lWidthInt=args[0];lHeightInt=args[1]
    elif len(args)==1:
        var = args[0]
        if type(var) is pyscreeze.Box: return Box(left=var.left, top=var.top, width=var.width, height=var.height) #Передан корректный объект - конвертация не требуется
        if (type(var) is tuple) or (type(var) is list):
            lLeftInt=var[0];lTopInt=var[1];lWidthInt=var[2];lHeightInt=var[3]
        elif (type(var) is dict):
            for char in ["x","X","l","L","left","LEFT","Left"]: 
                if char in var: lLeftInt=var[char]; break;
            for char in ["y","Y","T","t","top","TOP","Top"]: 
                if char in var: lTopInt=var[char]; break;
            for char in ["w","W","width","WIDTH","Width"]: 
                if char in var: lWidthInt=var[char]; break;
            for char in ["h","H","height","HEIGHT","Height"]: 
                if char in var: lHeightInt=var[char]; break;
            for char in ["r","R","right","RIGHT","Right"]: 
                if char in var: lWidthInt=var[char]-lLeftInt; break;
            for char in ["b","B","bottom","BOTTOM","Bottom"]: 
                if char in var: lHeightInt=var[char]-lTopInt; break;
        else:
            attr_list = dir(var)
            for char in ["x","X","l","L","left","LEFT","Left"]: 
                if char in attr_list: lLeftInt=getattr(var,char); break;
            for char in ["y","Y","T","t","top","TOP","Top"]: 
                if char in attr_list: lTopInt=getattr(var,char); break;
            for char in ["w","W","width","WIDTH","Width"]: 
                if char in attr_list: lWidthInt=getattr(var,char); break;
            for char in ["h","H","height","HEIGHT","Height"]: 
                if char in attr_list: lHeightInt=getattr(var,char); break;
            for char in ["r","R","right","RIGHT","Right"]: 
                if char in attr_list: lWidthInt=getattr(var,char)-lLeftInt; break;
            for char in ["b","B","bottom","BOTTOM","Bottom"]: 
                if char in attr_list: lHeightInt=getattr(var,char)-lTopInt; break;

    if len(kwargs)>0:
        for char in ["x","X","l","L","left","LEFT","Left"]: 
            if char in kwargs: lLeftInt=kwargs[char]; break;
        for char in ["y","Y","T","t","top","TOP","Top"]: 
            if char in kwargs: lTopInt=kwargs[char]; break;
        for char in ["w","W","width","WIDTH","Width"]: 
            if char in kwargs: lWidthInt=kwargs[char]; break;
        for char in ["h","H","height","HEIGHT","Height"]: 
            if char in kwargs: lHeightInt=kwargs[char]; break;
        for char in ["r","R","right","RIGHT","Right"]: 
            if char in kwargs: lWidthInt=kwargs[char]-lLeftInt; break;
        for char in ["b","B","bottom","BOTTOM","Bottom"]: 
            if char in kwargs: lHeightInt=kwargs[char]-lTopInt; break;
    # СОЗДАТЬ ОБЪЕКТ BOX
    return BoxCreate(inTopInt=lTopInt, inLeftInt= lLeftInt, inHeightInt= lHeightInt, inWidthInt=lWidthInt)

def BoxCreate(inTopInt:int, inLeftInt:int, inHeightInt:int, inWidthInt:int) -> Box:
    """L+,W+: Создать экземпляр прямоугольной области.

    !ВНИМАНИЕ! Координаты inTopInt, inLeftInt определяют верхний левый край прямоугольной области.

    :param inTopInt: Координата левой верхней точки в пикселях по оси X (горизонталь)
    :type inTopInt: int
    :param inLeftInt: Координата левой верхней точки в пикселях по оси Y (вертикаль)
    :type inLeftInt: int
    :param inHeightInt: Расстояние вниз от левой верхней точки в пикселях
    :type inHeightInt: int
    :param inWidthInt: Расстояние вправо от левой верхней точки в пикселях
    :type inWidthInt: int
    """
    return Box(top = inTopInt, left = inLeftInt, height = inHeightInt, width = inWidthInt)

def BoxNormalize(*inArgList, **inAgrDict) -> list:
    pass

def BoxMoveTo(inBox, inDXInt=None, inDYInt=None):
    """L+,W+: Переместить прямоугольную область (сохранить длину/ширину).

    !ВНИМАНИЕ! ПОДДЕРЖИВАЕТ ПАКЕТНУЮ ОБРАТКУ ПРИ ПЕРЕДАЧЕ СПИСКА ЭКЗЕМПЛЯРОВ BOX

    .. code-block:: python

        # Screen: Взаимодействие с экраном
        from pyOpenRPA.Robot import Screen
        # Вариант изменения 1-го элемента
        # Создать пробную прямоугольную область
        lBox = Screen.BoxCreate(inTopInt=10, inLeftInt=10, inHeightInt=10, inWidthInt=10)
        # Переместить пробную прямоугольную область
        lBox = Screen.BoxMoveTo(lBox, inDXInt=100, inDYInt=200)
        
    :param inBox: Экземпляр класса прямоугольной области Box
    :type inBox: Box
    :param inDXInt: Смещение левой верхней координаты по оси X в пикселях (горизонтальная ось). 
    :type inDXInt: int, опциональный
    :param inDYInt: Смещение левой верхней координаты по оси Y в пикселях (вертикальная ось). 
    :type inDYInt: int, опциональный
    :return: Экземпляр класса прямоугольной области Box
    :rtype: Box
    """
    if type(inBox) is list:
        lResult = []
        for lBox in inBox:
            lResult.append(BoxMoveTo(lBox, inDXInt=inDXInt, inDYInt=inDYInt))
        return lResult
    else:
        lTopInt = inBox.top
        lLeftInt = inBox.left
        if inDXInt: lLeftInt = inBox.left + inDXInt
        if inDYInt: lTopInt = inBox.top + inDYInt
        return BoxCreate(inTopInt=lTopInt, inLeftInt=lLeftInt,
            inHeightInt=inBox.height, inWidthInt=inBox.width)

def BoxModify(inBox, inDWidthInt=None, inDHeightInt=None, inPointRuleStr="CC"):
    """L+,W+: Изменить ширину / высоту прямоугольной области.

    !ВНИМАНИЕ! ПОДДЕРЖИВАЕТ ПАКЕТНУЮ ОБРАТКУ ПРИ ПЕРЕДАЧЕ СПИСКА ЭКЗЕМПЛЯРОВ BOX

    !ВНИМАНИЕ! ЕСЛИ СМЕЩЕНИЕ ПРИВЕДЕТ К ОБРАЗОВАНИЮ ДРОБНОГО ЧИСЛА, БУДЕТ ВЫПОЛНЕНО ОКРУГЛЕНИЕ ПО МАТЕМАТИЧЕСКИМ ПРАВИЛАМ

    .. code-block:: python

        # Screen: Взаимодействие с экраном
        from pyOpenRPA.Robot import Screen
        # Вариант изменения 1-го элемента
        # Создать пробную прямоугольную область
        lBox = Screen.BoxCreate(inTopInt=10, inLeftInt=10, inHeightInt=10, inWidthInt=10)
        # Скорректировать пробную прямоугольную область
        lBox2 = Screen.BoxModify(lBox,10,10,"CC"); print(lBox2)
        lBox2 = Screen.BoxModify(lBox,10,10,"LU"); print(lBox2)
        lBox2 = Screen.BoxModify(lBox,10,10,"LD"); print(lBox2)
        lBox2 = Screen.BoxModify(lBox,10,10,"RU"); print(lBox2)
        lBox2 = Screen.BoxModify(lBox,10,10,"RD"); print(lBox2)
        
    :param inBox: Экземпляр класса прямоугольной области Box
    :type inBox: Box
    :param inDXInt: Смещение левой верхней координаты по оси X в пикселях (горизонтальная ось). 
    :type inDXInt: int, опциональный
    :param inDYInt: Смещение левой верхней координаты по оси Y в пикселях (вертикальная ось). 
    :type inDYInt: int, опциональный
    :param inPointRuleStr: Символьное указание точки (подробнее см. выше), относительно которой выполнить изменение прямоугольной области. Допустимые значения: "CC" (по умолчанию), "LU", "LD", "RD", "RU"
    :type inPointRuleStr: str, опциональный
    :return: Экземпляр класса прямоугольной области Box
    :rtype: Box
    """
    if type(inBox) is list:
        lResult = []
        for lBox in inBox:
            lResult.append(BoxModify(lBox, inDWidthInt=inDWidthInt, inDHeightInt=inDHeightInt, inPointRuleStr=inPointRuleStr))
        return lResult
    else:
        lTopInt = inBox.top
        lLeftInt = inBox.left
        lWidthInt = inBox.width + inDWidthInt
        lHeightInt = inBox.height + inDHeightInt
        inPointRuleStr = inPointRuleStr.upper() # ВЕРХНИЙ РЕГИСТР
        if inDWidthInt: # Изменения по ширине
            if "C" in inPointRuleStr:
                lLeftInt = round(lLeftInt - inDWidthInt / 2)
            elif "R" in inPointRuleStr:
                lLeftInt = lLeftInt - inDWidthInt
        if inDHeightInt: # Изменения по высоте
            if "C" in inPointRuleStr:
                lTopInt = round(lTopInt - inDHeightInt / 2)
            elif "D" in inPointRuleStr:
                lTopInt = lTopInt - inDHeightInt
        return BoxCreate(inTopInt=lTopInt, inLeftInt=lLeftInt,
            inHeightInt=lHeightInt, inWidthInt=lWidthInt)


def BoxDraw(inBox, inColorStr='green',inThicknessInt = 2):
    """L+,W+: Выполнить подсветку прямоугольной области inBox на экране

    !ВНИМАНИЕ! ЦВЕТ inColorStr ПОДДЕРЖИВАЕТСЯ ТОЛЬКО НА ОС WINDOWS

    !ВНИМАНИЕ! ПОДДЕРЖИВАЕТ ПАКЕТНУЮ ОБРАТКУ ПРИ ПЕРЕДАЧЕ СПИСКА ЭКЗЕМПЛЯРОВ BOX

    .. code-block:: python

        # Screen: Взаимодействие с экраном
        from pyOpenRPA.Robot import Screen
        # ВАРИАНТ ОТРИСОВКИ 1ГО ЭЛЕМЕНТА
        # Создать пробную прямоугольную область
        lBox = Screen.BoxCreate(inTopInt=10, inLeftInt=10, inHeightInt=10, inWidthInt=10)
        Screen.BoxDraw(lBox)

        # ВАРИАНТ ПАКЕТНОЙ ОТРИСОВКИ
        # Создать пробную прямоугольную область
        lBox = Screen.BoxCreate(inTopInt=10, inLeftInt=10, inHeightInt=100, inWidthInt=100)
        lBox2 = Screen.BoxCreate(inTopInt=60, inLeftInt=60, inHeightInt=100, inWidthInt=100)
        Screen.BoxDraw([lBox, lBox2])

    :param inBox: Экземпляр класса прямоугольной области Box
    :type inBox: Box
    :param inColorStr: цвет подсветки прямоугольной области. Варианты: 'red', 'green', 'blue'. По умолчанию 'green'
    :type inColorStr: str, необязательный
    :param inThicknessInt: толщина подсветки прямоугольной области. По умолчанию 2
    :type inThicknessInt: int, необязательный
    """
    if type(inBox) is list:
        for lBox in inBox:
            BoxDraw(inBox=lBox, inColorStr=inColorStr,inThicknessInt = inThicknessInt)
    else:
        # Windows case
        if CrossOS.IS_WINDOWS_BOOL:
            fill = win32defines.BS_NULL
            if inBox is not None:
                """
                Draw an outline around the window.
                * **inColorStr** can be either an integer or one of 'red', 'green', 'blue'
                (default 'green')
                * **inThicknessInt** inThicknessInt of rectangle (default 2)
                * **fill** how to fill in the rectangle (default BS_NULL)
                """
                # don't draw if dialog is not visible
                #if not lWrapperObject.is_visible():
                #    return
                colours = {
                    "green": 0x00ff00,
                    "blue": 0xff0000,
                    "red": 0x0000ff,
                }
                # if it's a known colour
                if inColorStr in colours:
                    inColorStr = colours[inColorStr]
                # create the pen(outline)
                pen_handle = win32functions.CreatePen(
                        win32defines.PS_SOLID, inThicknessInt, inColorStr)
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
                    dc, inBox.left, inBox.top, inBox.left+inBox.width, inBox.top+inBox.height)
                # Delete the brush and pen we created
                win32functions.DeleteObject(brush_handle)
                win32functions.DeleteObject(pen_handle)
                # delete the Display context that we created
                win32functions.DeleteDC(dc)
        elif CrossOS.IS_LINUX_BOOL:
            if inBox is not None:
                root = tk.Tk()
                # The image must be stored to Tk or it will be garbage collected.
                label = tk.Label(root, bg='red')
                root.overrideredirect(True)
                root.geometry(f"{inBox.width}x{inBox.height}+{inBox.left}+{inBox.top}") # WxH+X+Y
                root.lift()
                root.wm_attributes("-topmost", True)
                #root.wm_attributes("-disabled", True)
                root.wm_attributes("-alpha", 0.85)
                root.wait_visibility(root)
                # Create a canvas widget
                #canvas=tk.Canvas(root, width=500, height=300)
                #canvas.pack()
                # Add a line in canvas widget
                #canvas.create_line(100,200,500,350, fill="green", width=5)
                #label.pack()
                #label.mainloop()
                #root.mainloop()
                time.sleep(1)
                root.destroy()


def BoxAnchorRuleCheck(inBox, inAnchorBox=None, inAnchorRuleStr=None) -> bool:
    """L+,W+: Выполнить проверку соответствия всем условиям вхождения inBox в inAnchorBox с учетом правил inAnchorRule
    
    .. code-block:: python

        # Screen: Взаимодействие с экраном
        from pyOpenRPA.Robot import Screen
        lBox1 = Screen.BoxCreate(inTopInt=265, inLeftInt=62, inHeightInt=100, inWidthInt=90)
        lBox2 = Screen.BoxCreate(inTopInt=160, inLeftInt=160, inHeightInt=100, inWidthInt=100)
        lBox3 = Screen.BoxCreate(inTopInt=460, inLeftInt=60, inHeightInt=100, inWidthInt=100)

        l = Screen.BoxAnchorRuleCheck(inBox=lBox1, inAnchorBox=[lBox2,lBox3], inAnchorRuleStr=["LD","CUS"])
        Screen.BoxDraw([lBox1,lBox2,lBox3])

    :param inBox: Экземпляр класса прямоугольной области Box
    :type inBox: Box
    :param inAnchorBox: Экземпляр класса прямоугольной области Box
    :type inAnchorBox: Box или list из Box
    :param inAnchorRuleStr: Символьное указание области проверки соответствия. Может принимать единственное значение (единый формат для всех inAnchorBox), или список форматов для каждого inAnchorBox (если inAnchorBox является списком Box)
    :type inAnchorRuleStr: str или list из str
    :return: True - соответствует всем правилам
    :rtype: bool
    """
    # Формирование стартовых переменных
    if inAnchorBox is None: inAnchorBox = []
    if type(inAnchorBox) is not list:
        inAnchorBox = [inAnchorBox]
    lAnchorRuleStr = "CC,S"
    if inAnchorRuleStr is None or inAnchorRuleStr=="": inAnchorRuleStr = [lAnchorRuleStr]
    if type(inAnchorRuleStr) is not list:
        inAnchorRuleStr = [inAnchorRuleStr]

    lResult = True

    # Дополнение списка правил до длины якорей, если они расходятся и список правил равен длине 1 или 0 (по умолчанию CC,S)
    if len(inAnchorRuleStr)==1 and len(inAnchorBox)==1:
        if inAnchorRuleStr[0]=="" or inAnchorRuleStr[0] is None: 
            inAnchorRuleStr = [lAnchorRuleStr]
    elif len(inAnchorRuleStr)==1 and len(inAnchorBox)!=1:
        if inAnchorRuleStr[0]!="" and inAnchorRuleStr[0] is not None: 
            lAnchorRuleStr = inAnchorRuleStr[0]
    
    if len(inAnchorRuleStr) != len(inAnchorBox):
        inAnchorRuleStr = []
        for lItem in inAnchorBox:
            inAnchorRuleStr.append(lAnchorRuleStr)

    for lIndexInt, lItemBox in enumerate(inAnchorBox): # Остановиться, если итог False
        lItemRuleStr = inAnchorRuleStr[lIndexInt].upper()
        #print(lItemRuleStr)
        # Подготовка вспомогательных областей
        lScreenWidthPXInt = 9999
        lScreenHeightPXInt = 5555
        lAnchorLUBox = BoxCreate(inTopInt=0, inLeftInt=0, inHeightInt=lItemBox.top, inWidthInt=lItemBox.left)
        lAnchorRUBox = BoxCreate(inTopInt=0, inLeftInt=lItemBox.left+lItemBox.width, inHeightInt=lItemBox.top, inWidthInt=lScreenWidthPXInt)
        lAnchorCUBox = BoxCreate(inTopInt=0, inLeftInt=lItemBox.left, inHeightInt=lItemBox.top, inWidthInt=lItemBox.width)
        lAnchorLCBox = BoxCreate(inTopInt=lItemBox.top, inLeftInt=0, inHeightInt=lItemBox.height, inWidthInt=lItemBox.left)
        lAnchorRCBox = BoxCreate(inTopInt=lItemBox.top, inLeftInt=lItemBox.left+lItemBox.width, inHeightInt=lItemBox.height, inWidthInt=lScreenWidthPXInt)
        lAnchorLDBox = BoxCreate(inTopInt=lItemBox.top+lItemBox.height, inLeftInt=0, inHeightInt=lScreenHeightPXInt, inWidthInt=lItemBox.left)
        lAnchorRDBox = BoxCreate(inTopInt=lItemBox.top+lItemBox.height, inLeftInt=lItemBox.left+lItemBox.width, inHeightInt=lScreenHeightPXInt, inWidthInt=lScreenWidthPXInt)
        lAnchorCDBox = BoxCreate(inTopInt=lItemBox.top+lItemBox.height, inLeftInt=lItemBox.left, inHeightInt=lScreenHeightPXInt, inWidthInt=lItemBox.width)
        #import pdb
        #pdb.set_trace()
        if "S" not in lItemRuleStr: # Проверка без S - Strict
            lResult = False
            # Алгоритм проверки соответствия хотя бы на одно вхождение
            if ("CC" in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lItemBox)==True: lResult = True
            elif ("LU" in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorLUBox)==True: lResult = True
            elif ("RU" in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorRUBox)==True: lResult = True
            elif ("CU" in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorCUBox)==True: lResult = True
            elif ("LC" in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorLCBox)==True: lResult = True
            elif ("RC" in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorRCBox)==True: lResult = True
            elif ("LD" in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorLDBox)==True: lResult = True
            elif ("RD" in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorRDBox)==True: lResult = True
            elif ("CD" in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorCDBox)==True: lResult = True
            if lResult == False: break # Остановиться, если итог False
        else: # Проверка с S - Strict
            lResult = True
            # Алгоритм проверки соответствия хотя бы на одно вхождение для того сегмента, который недоступен
            if ("CC" not in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lItemBox)==True: lResult = False
            elif ("LU" not in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorLUBox)==True: lResult = False
            elif ("RU" not in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorRUBox)==True: lResult = False
            elif ("CU" not in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorCUBox)==True: lResult = False
            elif ("LC" not in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorLCBox)==True: lResult = False
            elif ("RC" not in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorRCBox)==True: lResult = False
            elif ("LD" not in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorLDBox)==True: lResult = False
            elif ("RD" not in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorRDBox)==True: lResult = False
            elif ("CD" not in lItemRuleStr) and BoxOverlay(inBox1=inBox, inBox2=lAnchorCDBox)==True: lResult = False
            if lResult == False: break # Остановиться, если итог False

    return lResult

def BoxOverlay(inBox1, inBox2) -> bool:
    """L+,W+:Проверить наложение 2-х прямоугольных областей друг на друга.
    
    .. code-block:: python

        # Screen: Взаимодействие с экраном
        from pyOpenRPA.Robot import Screen
        lBox1 = Screen.BoxCreate(inTopInt=10, inLeftInt=10, inHeightInt=100, inWidthInt=1000)
        lBox2 = Screen.BoxCreate(inTopInt=160, inLeftInt=160, inHeightInt=100, inWidthInt=100)
        Screen.BoxDraw([lBox1, lBox2])
        Screen.BoxOverlay(lBox1,lBox2)

    :param inBox1: Экземпляр класса прямоугольной области Box
    :type inBox1: Box
    :param inBox2: Экземпляр класса прямоугольной области Box
    :type inBox2: Box
    :return: True - inBox1 наложен на inBox2
    :rtype: bool
    """
    return not ((inBox1.left>inBox2.left + inBox2.width or inBox2.left>inBox1.left + inBox1.width) or (inBox1.top>inBox2.top + inBox2.height or inBox2.top>inBox1.top + inBox1.height))

import re
def BoxGetPoint(inBox, inPointRuleStr="CC") -> Point:
    """L+,W+:Получить точку Point по заданной прямоугольной области Box и строковому параметру расположения inPointRuleStr.

    .. code-block:: python

        # Screen: Взаимодействие с мышью объектами экрана
        from pyOpenRPA.Robot import Screen
        lBox1 = Screen.BoxCreate(inTopInt=10, inLeftInt=10, inHeightInt=100, inWidthInt=1000)
        lPoint = Screen.BoxGetPoint(inBox=lBox1, inPointRuleStr="LC")

    :param inBox: Прямоугольная область на экране
    :type inBox: Box, обязательный
    :param inPointRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inPointRuleStr: str, опциональный
    :return: Точка на экране
    :rtype: Screen.Point
    """
    inBox= BoxParse(inBox) #Конвертация из разных типов (если необходимо)
    lPoint = None
    inPointRuleStr = inPointRuleStr.upper()
    if "CC" in inPointRuleStr: lPoint = Point(x=inBox.left + inBox.width/2,y=inBox.top + inBox.height/2)
    elif "LU" in inPointRuleStr: lPoint = Point(x=inBox.left,y=inBox.top)
    elif "RU" in inPointRuleStr: lPoint = Point(x=inBox.left + inBox.width,y=inBox.top)
    elif "CU" in inPointRuleStr: lPoint = Point(x=inBox.left + inBox.width/2,y=inBox.top)
    elif "LC" in inPointRuleStr: lPoint = Point(x=inBox.left,y=inBox.top + inBox.height/2)
    elif "RC" in inPointRuleStr: lPoint = Point(x=inBox.left + inBox.width,y=inBox.top + inBox.height/2)
    elif "LD" in inPointRuleStr: lPoint = Point(x=inBox.left,y=inBox.top + inBox.height)
    elif "CD" in inPointRuleStr: lPoint = Point(x=inBox.left + inBox.width/2,y=inBox.top + inBox.height)
    elif "RD" in inPointRuleStr: lPoint = Point(x=inBox.left + inBox.width,y=inBox.top + inBox.height)
    # Корректировка при необходимости
    lDXInt=0
    lDYInt=0
    lMatchY = re.search(r'.*Y([-+]?\d*).*', inPointRuleStr)
    if lMatchY is not None: lDYInt=int(lMatchY.group(1))
    lMatchX = re.search(r'.*X([-+]?\d*).*', inPointRuleStr)
    if lMatchX is not None: lDXInt=int(lMatchX.group(1))
    lPoint = PointModify(inPoint=lPoint,inDXInt=lDXInt,inDYInt=lDYInt)
    return lPoint

def PointModify(inPoint, inDXInt, inDYInt) -> Point:
    """L+,W+:Скорректировать точку Point.

    .. code-block:: python

        # Screen: Взаимодействие с мышью объектами экрана
        from pyOpenRPA.Robot import Screen
        lPoint = Screen.PointCreate(inXInt=10, inYInt=10)
        lPoint = Screen.PointModify(inPoint=lPoint, inDXInt=90, inDYInt=10)

    :param inPoint: Точка на экране, по которой выполнить нажатие мыши
    :type inPoint: Point, обязательный
    :param inDXInt: Смещение указателя мыши по оси X (горизонтальная ось). 
    :type inDXInt: int, опциональный
    :param inDYInt: Смещение указателя мыши по оси Y (вертикальная ось). 
    :type inDYInt: int, опциональный
    :return: Точка на экране
    :rtype: Screen.Point
    """
    return PointCreate(inXInt=inPoint.x+inDXInt, inYInt=inPoint.y+inDYInt)


def PointFromBox(inBox, inRuleStr):
    """L+,W+:Создать точку Point на основании прямоугольной области и символьного указания точки (см функцию BoxGetPoint).

    .. code-block:: python

        # Screen: Взаимодействие с мышью объектами экрана
        from pyOpenRPA.Robot import Screen
        lBox1 = Screen.PointFromBox(inTopInt=10, inLeftInt=10, inHeightInt=100, inWidthInt=1000)
        lPoint = Screen.PointFromBox(inBox=lBox1, inPointRuleStr="LC")

    :param inBox: Прямоугольная область на экране
    :type inBox: Box, обязательный
    :param inRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inRuleStr: str, опциональный
    :return: Точка на экране
    :rtype: Screen.Point
    """
    return BoxGetPoint(inBox=inBox, inPointRuleStr=inRuleStr)

def PointCreate(inXInt, inYInt):
    """L+,W+:Создать точку Point.

    .. code-block:: python

        # Screen: Взаимодействие с мышью объектами экрана
        from pyOpenRPA.Robot import Screen
        lPoint = Screen.PointCreate(inXInt=10, inYInt=10)

    :param inXInt: Смещение указателя мыши по оси X (горизонтальная ось). 
    :type inXInt: int, опциональный
    :param inYInt: Смещение указателя мыши по оси Y (вертикальная ось). 
    :type inYInt: int, опциональный
    :return: Точка на экране
    :rtype: Screen.Point
    """
    return Point(x=inXInt,y=inYInt)

def PointClick(inPoint:Point, inClickCountInt:int=1, inIntervalSecFloat:float=0.0, inButtonStr:str='left', inMoveDurationSecFloat:float=0.0, inWaitAfterSecFloat:float=None):
    """L+,W+:Нажатие (вниз) кнопки мыши и затем немедленно выпуск (вверх) её. Допускается следующая параметризация.

    .. code-block:: python

        # Screen: Взаимодействие с мышью объектами экрана
        from pyOpenRPA.Robot import Screen
        lPoint = Screen.PointCreate(100,150)
        Screen.PointClick(lPoint) #Выполнить нажатие левой клавиши мыши

    :param inPoint: Точка на экране, по которой выполнить нажатие мыши
    :type inPoint: Point, обязательный
    :param inClickCountInt: Количество нажатий (вниз и вверх) кнопкой мыши, По умолчанию 1
    :type inClickCountInt: int, опциональный
    :param inIntervalSecFloat: Интервал ожидания в секундах между нажатиями, По умолчанию 0.0
    :type inIntervalSecFloat: float, опциональный 
    :param inButtonStr: Номер кнопки, которую требуется нажать. Возможные варианты: 'left', 'middle', 'right' или 1, 2, 3. В остальных случаях инициирует исключение ValueError. По умолчанию 'left'
    :type inButtonStr: str, опциональный
    :param inMoveDurationSecFloat: Время перемещения указателя мыши, По умолчанию 0.0 (моментальное перемещение)
    :type inMoveDurationSecFloat: float, опциональный
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Mouse (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    Mouse.Click(inXInt=inPoint.x, inYInt=inPoint.y, inClickCountInt=inClickCountInt, inIntervalSecFloat=inIntervalSecFloat, inButtonStr=inButtonStr, inMoveDurationSecFloat=inMoveDurationSecFloat, inWaitAfterSecFloat=inWaitAfterSecFloat)


def PointClickDouble(inPoint:Point, inWaitAfterSecFloat:float=None):
    """L+,W+:Двойное нажатие левой клавиши мыши. Данное действие аналогично вызову функции (см. ниже).

    .. code-block:: python

        # Screen: Взаимодействие с мышью объектами экрана
        from pyOpenRPA.Robot import Screen
        lPoint = Screen.PointCreate(100,150)
        Screen.PointClickDouble(lPoint) #Выполнить двойное нажатие левой клавиши мыши

    :param inPoint: Точка на экране, по которой выполнить нажатие мыши
    :type inPoint: Point, обязательный
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Mouse (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    Mouse.ClickDouble(inXInt=inPoint.x, inYInt=inPoint.y, inWaitAfterSecFloat=inWaitAfterSecFloat)


def PointDown(inPoint:Point, inButtonStr:str='left', inWaitAfterSecFloat:float=None):
    """L+,W+:Переместить указатель по координатам inPoint, после чего нажать (вниз) клавишу мыши и не отпускать до выполнения соответсвующей команды (см. Up). 

    .. code-block:: python

        # Screen: Взаимодействие с мышью объектами экрана
        from pyOpenRPA.Robot import Screen
        lPoint = Screen.PointCreate(100,150)
        Screen.PointDown(lPoint)

    :param inPoint: Точка на экране, по которой выполнить нажатие мыши
    :type inPoint: Point, обязательный
    :param inButtonStr: Номер кнопки, которую требуется нажать. Возможные варианты: 'left', 'middle', 'right' или 1, 2, 3. В остальных случаях инициирует исключение ValueError. По умолчанию 'left'
    :type inButtonStr: str, опциональный
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Mouse (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    Mouse.Down(inXInt=inPoint.x, inYInt=inPoint.y,inButtonStr=inButtonStr, inWaitAfterSecFloat=inWaitAfterSecFloat)

def PointUp(inPoint:Point, inButtonStr:str='left', inWaitAfterSecFloat:float=None):
    """L+,W+:Отпустить (вверх) клавишу мыши.

    .. code-block:: python

        # Screen: Взаимодействие с мышью объектами экрана
        from pyOpenRPA.Robot import Screen
        lPoint = Screen.PointCreate(100,150)
        Screen.PointUp(lPoint)

    :param inPoint: Точка на экране, по которой выполнить нажатие мыши
    :type inPoint: Point, обязательный
    :param inButtonStr: Номер кнопки, которую требуется поднять. Возможные варианты: 'left', 'middle', 'right' или 1, 2, 3. В остальных случаях инициирует исключение ValueError. По умолчанию 'left'
    :type inButtonStr: str, опциональный
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Mouse (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    Mouse.Up(inXInt=inPoint.x, inYInt=inPoint.y,inButtonStr=inButtonStr, inWaitAfterSecFloat=inWaitAfterSecFloat)

def PointMoveTo(inPoint:Point, inWaitAfterSecFloat:float=None):
    """L+,W+:Переместить указатель мыши на позицию inXInt, inYInt за время inMoveDurationSecFloat.

    !ВНИМАНИЕ! Отсчет координат inXInt, inYInt начинается с левого верхнего края рабочей области (экрана).

    .. code-block:: python

        # Screen: Взаимодействие с мышью объектами экрана
        from pyOpenRPA.Robot import Screen
        lPoint = Screen.PointCreate(100,150)
        Screen.PointMoveTo(inXInt=100, inYInt=200)

    :param inPoint: Точка на экране, по которой выполнить нажатие мыши
    :type inPoint: Point, обязательный
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Mouse (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    Mouse.MoveTo(inXInt=inPoint.x, inYInt=inPoint.y, inWaitAfterSecFloat=inWaitAfterSecFloat)


def is_base64(s):
    s=CrossOS.PathStr(s) # FIX 2023 07 12
    if os.path.exists(s): return False
    try:
        # декодируем строку base64
        base64.decodebytes(s.encode())
        # если декодирование прошло успешно, то строка является форматом base64
        return True
    except:
        # если декодирование не удалось, то строка не является форматом base64
        return False
from io import BytesIO
from PIL import Image
import pytesseract

def ImageRecognize(inImgPathStr:str, inLangStr = "rus+eng"):
    """L+,W+: Выполнить распознавание текста на изображении

    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        RecognizedStr = Screen.ImageRecognize(inImgPathStr="Button.png")

    :param inImgPathStr: Путь к изображению / Строка Base64 / Список bytes, которое требуется искать на экране.
    :type inImgPathStr: str, относительный или абсолютный
    :param inLangStr: Языки, используемые для распознавания. По умолчанию rus+eng
    :type inLangStr: str, опционально
    :return: Список из Box
    :rtype: list
    """
    # ЕСЛИ ПОСТУПИЛ BASE 64
    if is_base64(inImgPathStr):
        imgdata = base64.b64decode(inImgPathStr)
        return pytesseract.image_to_string(Image.open(BytesIO(imgdata)), lang = inLangStr)
    else:
        inImgPathStr = CrossOS.PathStr(inImgPathStr)
        return pytesseract.image_to_string(Image.open(inImgPathStr), lang = inLangStr)
    
def ImageLocateAll(inImgPathStr:str, inIsGrayModeBool:bool=False, inConfidenceFloat:float=None) -> list:
    """L+,W+: Искать на экране графические объекты, которые похожи на inImgPathStr. Вернуть список прямоугольных областей на экране (Box)

    !ВНИМАНИЕ! Для использования параметра точности inConfidenceFloat необходим пакет Python opencv-python (python -m pip install opencv-python)

    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        Screen.ImageLocateAll(inImgPathStr="Button.png",inConfidenceFloat=0.9)

    :param inImgPathStr: Путь к изображению / Строка Base64 / Список bytes, которое требуется искать на экране.
    :type inImgPathStr: str, относительный или абсолютный
    :param inIsGrayModeBool: True - выполнить поиск изображения в режиме серых оттенков (ускоряет производительность, если допускается искажение цвета). По умолчанию False
    :type inIsGrayModeBool: bool, опционально
    :param inConfidenceFloat: Показатель точности. 1.0 - идентичное соответствие, 0.0 - полное несоответствие. По умолчанию 1.0 (None)
    :type inConfidenceFloat: float, опционально
    :return: Список из Box
    :rtype: list
    """
    lResult = []
    # ЕСЛИ ПОСТУПИЛ BASE 64
    if is_base64(inImgPathStr):
            imgdata = base64.b64decode(inImgPathStr)
            img = Image.open(BytesIO(imgdata))
            if inConfidenceFloat is None or inConfidenceFloat==1: lLocateList = pyautogui.locateAllOnScreen(image = img, grayscale = inIsGrayModeBool)
            else: lLocateList = pyautogui.locateAllOnScreen(image = img, grayscale = inIsGrayModeBool, confidence = inConfidenceFloat)
            for lItem in lLocateList:
                lResult.append(lItem)
            img.close()
            if __define__.DEFINE_ACCEPTED==True: return lResult
            else: []
    # ЕСЛИ ПОСТУПИЛ BYTES
    elif type(inImgPathStr) is bytes:
            img = Image.open(BytesIO(inImgPathStr))
            if inConfidenceFloat is None or inConfidenceFloat==1: lLocateList = pyautogui.locateAllOnScreen(image = img, grayscale = inIsGrayModeBool)
            else: lLocateList = pyautogui.locateAllOnScreen(image = img, grayscale = inIsGrayModeBool, confidence = inConfidenceFloat)
            for lItem in lLocateList:
                lResult.append(lItem)
            img.close()
            if __define__.DEFINE_ACCEPTED==True: return lResult
            else: []
    else:
        inImgPathStr = CrossOS.PathStr(inImgPathStr)
        if inConfidenceFloat is None or inConfidenceFloat==1: lLocateList = pyautogui.locateAllOnScreen(image = inImgPathStr, grayscale = inIsGrayModeBool)
        else: lLocateList = pyautogui.locateAllOnScreen(image = inImgPathStr, grayscale = inIsGrayModeBool, confidence = inConfidenceFloat)
        for lItem in lLocateList:
            lResult.append(lItem)
        if __define__.DEFINE_ACCEPTED==True: return lResult
        else: []
from ..Utils import __define__
def ImageLocateAllInfo(inImgPathStr:str, inIsGrayModeBool:bool=False, inConfidenceFloat:float=None) -> list:
    """L+W+: Искать на экране графические объекты, которые похожи на inImgPathStr. Вернуть список прямоугольных областей на экране (Box)

    !ВНИМАНИЕ! Для использования параметра точности inConfidenceFloat необходим пакет Python opencv-python (python -m pip install opencv-python)

    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        Screen.ImageLocateAll(inImgPathStr="Button.png",inConfidenceFloat=0.9)

    :param inImgPathStr: Путь к изображению, которое требуется искать на экране
    :type inImgPathStr: str, относительный или абсолютный
    :param inIsGrayModeBool: True - выполнить поиск изображения в режиме серых оттенков (ускоряет производительность, если допускается искажение цвета). По умолчанию False
    :type inIsGrayModeBool: bool, опционально
    :param inConfidenceFloat: Показатель точности. 1.0 - идентичное соответствие, 0.0 - полное несоответствие. По умолчанию 1.0 (None)
    :type inConfidenceFloat: float, опционально
    :return: Список из { left: 777, top: 497, width: 264, height: 52 }
    :rtype: list
    """
    lLocateList = ImageLocateAll(inImgPathStr=inImgPathStr, inIsGrayModeBool=inIsGrayModeBool, inConfidenceFloat=inConfidenceFloat)   
    lResult=[]
    for lItem in lLocateList:
        lResult.append({"left": int(lItem.left), "top": int(lItem.top), "width": int(lItem.width), "height": int(lItem.height)})
    return lResult


def ImageExists(inImgPathStr:str, inIsGrayModeBool:bool=False, inConfidenceFloat:float=None) -> list:
    """L+,W+:Проверить, имеется ли на экране хотя бы один подходящий объект. Вернуть булево значение

    !ВНИМАНИЕ! Для использования параметра точности inConfidenceFloat необходим пакет Python opencv-python (python -m pip install opencv-python)


    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        lResult = Screen.ImageExists(inImgPathStr="Button.png",inConfidenceFloat=0.9)

    :param inImgPathStr: Путь к изображению, которое требуется искать на экране
    :type inImgPathStr: str, относительный или абсолютный
    :param inIsGrayModeBool: True - выполнить поиск изображения в режиме серых оттенков (ускоряет производительность, если допускается искажение цвета). По умолчанию False
    :type inIsGrayModeBool: bool, опционально
    :param inConfidenceFloat: Показатель точности. 1.0 - идентичное соответствие, 0.0 - полное несоответствие. По умолчанию 1.0 (None)
    :type inConfidenceFloat: float, опционально
    :return: Список из Box
    :rtype: list
    """
    lLocateList = ImageLocateAll(inImgPathStr=inImgPathStr,inIsGrayModeBool=inIsGrayModeBool, inConfidenceFloat=inConfidenceFloat)
    return len(lLocateList)>0


def ImageWaitAppear(inImgPathStr:str, inWaitSecFloat:float=IMAGE_WAIT_SEC_FLOAT, inWaitIntervalSecFloat:float = IMAGE_WAIT_INTERVAL_SEC_FLOAT, inIsGrayModeBool:bool=False, inConfidenceFloat:float=None) -> list:
    """L+,W+:Ожидать появление изображения на протяжении inWaitSecFloat секунд. Проверять с периодичностью inWaitIntervalSecFloat. Вернуть список прямоугольных областей, которые удовлетворяют условию

    !ВНИМАНИЕ! Для использования параметра точности inConfidenceFloat необходим пакет Python opencv-python (python -m pip install opencv-python)


    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        lBoxList = Screen.ImageWaitAppear(inImgPathStr="Button.png",inConfidenceFloat=0.9)

    :param inImgPathStr: Путь к изображению, которое требуется искать на экране
    :type inImgPathStr: str, относительный или абсолютный
    :param inWaitSecFloat: Время ожидания появления изображения в сек. По умолчанию IMAGE_WAIT_SEC_FLOAT (60)
    :type inWaitSecFloat: float, опциональный
    :param inWaitIntervalSecFloat: Интервал повторной проверки наличия изображения. По умолчанию IMAGE_WAIT_INTERVAL_SEC_FLOAT (1)
    :type inWaitIntervalSecFloat: float, опциональный
    :param inIsGrayModeBool: True - выполнить поиск изображения в режиме серых оттенков (ускоряет производительность, если допускается искажение цвета). По умолчанию False
    :type inIsGrayModeBool: bool, опционально
    :param inConfidenceFloat: Показатель точности. 1.0 - идентичное соответствие, 0.0 - полное несоответствие. По умолчанию 1.0 (None)
    :type inConfidenceFloat: float, опционально
    :return: Список из Box или [] если прошло время ожидания.
    :rtype: list
    """
    lStartSecFloat = time.time()
    lResultList=[]
    while time.time() - lStartSecFloat < inWaitSecFloat:
        lResultList = ImageLocateAll(inImgPathStr=inImgPathStr,inIsGrayModeBool=inIsGrayModeBool, inConfidenceFloat=inConfidenceFloat)
        if len(lResultList)>0: break
        time.sleep(inWaitIntervalSecFloat)
    return lResultList


def ImageWaitDisappear(inImgPathStr:str, inWaitSecFloat:float=IMAGE_WAIT_SEC_FLOAT, inWaitIntervalSecFloat:float = IMAGE_WAIT_INTERVAL_SEC_FLOAT, inIsGrayModeBool:bool=False, inConfidenceFloat:float=None):
    """L+,W+:Ожидать исчезновение изображения на протяжении inWaitSecFloat секунд. Проверять с периодичностью inWaitIntervalSecFloat.

    !ВНИМАНИЕ! Для использования параметра точности inConfidenceFloat необходим пакет Python opencv-python (python -m pip install opencv-python)


    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        Screen.ImageWaitDisappear(inImgPathStr="Button.png",inConfidenceFloat=0.9)

    :param inImgPathStr: Путь к изображению, которое требуется искать на экране
    :type inImgPathStr: str, относительный или абсолютный
    :param inWaitSecFloat: Время ожидания появления изображения в сек. По умолчанию IMAGE_WAIT_SEC_FLOAT (60)
    :type inWaitSecFloat: float, опциональный
    :param inWaitIntervalSecFloat: Интервал повторной проверки наличия изображения. По умолчанию IMAGE_WAIT_INTERVAL_SEC_FLOAT (1)
    :type inWaitIntervalSecFloat: float, опциональный
    :param inIsGrayModeBool: True - выполнить поиск изображения в режиме серых оттенков (ускоряет производительность, если допускается искажение цвета). По умолчанию False
    :type inIsGrayModeBool: bool, опционально
    :param inConfidenceFloat: Показатель точности. 1.0 - идентичное соответствие, 0.0 - полное несоответствие. По умолчанию 1.0 (None)
    :type inConfidenceFloat: float, опционально
    """
    lStartSecFloat = time.time()
    lResultList=[]
    while time.time() - lStartSecFloat < inWaitSecFloat:
        lResultList = ImageLocateAll(inImgPathStr=inImgPathStr,inIsGrayModeBool=inIsGrayModeBool, inConfidenceFloat=inConfidenceFloat)
        if len(lResultList)==0: break
        time.sleep(inWaitIntervalSecFloat)
    return lResultList
import os
import base64
def ImageToBase64(inImgPathStr:str, inLimitBytesInt:int=30000) -> str:
    """L+,W+: Открыть файл и преобразовать содержимое изображения в формат base64 (в виде строки). Вернуть None, если файл не существует или превышает допустимый размер

    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        ImageBase64Str = Screen.ImageToBase64(inImgPathStr="Button.png")
        ImageBytes = base64.b64decode(ImageBase64Str.encode())

    """
    inImgPathStr = CrossOS.PathStr(inImgPathStr)
    str = None
    if os.path.exists(inImgPathStr):
        log = b""
        with open(inImgPathStr, "rb") as f:
            log = f.read()
        if len(log) < inLimitBytesInt:
            str = base64.b64encode(log).decode()
    return str
    

def ImageClick(inImgPathStr:str,inBoxIndexInt:int = 0, inPointRuleStr:str="CC",  inIsGrayModeBool:bool=False, inConfidenceFloat:float=None, inWaitSecFloat:float=0, inWaitIntervalSecFloat:float = 0):
    """L+,W+:Выполнить поиск прямоугольной области по изображению.

    !ВНИМАНИЕ! Для использования параметра точности inConfidenceFloat необходим пакет Python opencv-python (python -m pip install opencv-python)


    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        Screen.ImageClick(inImgPathStr="Button.png",inConfidenceFloat=0.9)

    :param inImgPathStr: Путь к изображению, которое требуется искать на экране
    :type inImgPathStr: str, относительный или абсолютный
    :param inBoxIndexInt: Индекс прямоугольной области, по которой выполнить клик (если обнаружено несколько областей Box), По умолчанию 0
    :type inBoxIndexInt: int, опционально
    :param inPointRuleStr: Правило идентификации точки на прямоугольной области (правила формирования см. выше). Варианты: "LU","CU","RU","LC","CC","RC","LD","CD","RD".  По умолчанию "CC"
    :type inPointRuleStr: str, опциональный
    :param inIsGrayModeBool: True - выполнить поиск изображения в режиме серых оттенков (ускоряет производительность, если допускается искажение цвета). По умолчанию False
    :type inIsGrayModeBool: bool, опционально
    :param inConfidenceFloat: Показатель точности. 1.0 - идентичное соответствие, 0.0 - полное несоответствие. По умолчанию 1.0 (None)
    :type inConfidenceFloat: float, опционально
    :param inWaitSecFloat: Время ожидания появления изображения в сек. По умолчанию 0
    :type inWaitSecFloat: float, опциональный
    :param inWaitIntervalSecFloat: Интервал повторной проверки наличия изображения. По умолчанию 0
    :type inWaitIntervalSecFloat: float, опциональный
    """
    if inWaitSecFloat > 0:
        lBoxList = ImageWaitAppear(inImgPathStr=inImgPathStr,inWaitSecFloat=inWaitSecFloat,inWaitIntervalSecFloat=inWaitIntervalSecFloat,inIsGrayModeBool=inIsGrayModeBool,inConfidenceFloat=inConfidenceFloat)
        if len(lBoxList)>0: PointClick(inPoint=BoxGetPoint(lBoxList[inBoxIndexInt],inPointRuleStr=inPointRuleStr))
    else:
        PointClick(BoxGetPoint(inBox=ImageLocateAll(inImgPathStr=inImgPathStr,inIsGrayModeBool=inIsGrayModeBool,inConfidenceFloat=inConfidenceFloat)[inBoxIndexInt],inPointRuleStr=inPointRuleStr))

def ResolutionsGet():
    """L-,W+:Получить разрешение всех используемых экранов.

    !ВНИМАНИЕ! Данная функция возвращает разрешения с учетом scale factor (масштабирование в настройках Windows)

    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        Screen.ImageClick(inImgPathStr="Button.png",inConfidenceFloat=0.9)

    :return: Список с разрешением в формате [ширина, высота].
    :rtype: list
    """
    lResult = []
    for lMonitor in win32api.EnumDisplayMonitors():
        # Определение hadle у монитора
        lHandle = lMonitor[0].Detach()
        # Подгрузка shcore
        lShcore = ctypes.WinDLL('shcore')
        # Множитель мастшабирования монитора
        lScaleFactor = ctypes.c_uint()
        lShcore.GetScaleFactorForMonitor(lHandle, ctypes.byref(lScaleFactor))
        # Разрешение
        lResult.append([int((lMonitor[2][2]-lMonitor[2][0])*lScaleFactor.value/100),int((lMonitor[2][3]-lMonitor[2][1])*lScaleFactor.value/100)])
    return lResult


class SnipingTool(tk.Frame):
    def __init__(self, parent, path):
        """L+,W+: Инициализация экземпляра класса SnipingTool

        ВНИМАНИЕ В LINUX ПРИ ВЫРЕЗАНИИ ЧАСТИ ЭКРАНА НЕ ПРОИСХОДИТ ЗАТЕМНЕНИЯ - СВЯЗАНО С ОСОБЕННОСТЯМИ ГРАФИЧЕСКИХ ОКОН В LINUX

        .. code-block:: python
            from pyOpenRPA.Robot import Screen
            lRoot = tk.Tk()
            app = Screen.SnipingTool(parent=lRoot, path=inPath)

        :param parent: Верхнеуровневый виджет
        :type parent: экземпляр класса Tk
        :param path: Путь, по которому будет сохранена выделенная область
        :type path: str, относительный или абсолютный
        """
        self.path = CrossOS.PathStr(path) 
        if CrossOS.IS_WINDOWS_BOOL:
            tk.Frame.__init__(self, parent)
            self.root = parent
            self.root.config(cursor="cross")#Изменение курсора
            self.root.attributes('-alpha', 0.2) #Установить прозрачность
            #Определить общее разрешение экрана/ов
            self.width, self.height = self.getMonitorsResolution()
            self.root.geometry( f"{self.width}x{self.height}" ) #Установить размеры окна snipingtool
            
            #Установить безрамочный режим и верхний уровень
            self.root.overrideredirect(1)
            self.root.attributes('-topmost', True)
            self._createVariables(parent)
            self._createCanvas()
            self._createCanvasBinding()

    def getMonitorsResolution(self):
        """L+,W+: Определение разрешения всей области экрана (охватывает все подключенные мониторы)

        .. code-block:: python
            from pyOpenRPA.Robot import Screen
            lRoot = tk.Tk()
            app = Screen.SnipingTool(parent=lRoot, path=inPath)
            lResolution = app.getMonitorsResolution()
        """
        mHeight = 0
        mWidth = 0
        if CrossOS.IS_WINDOWS_BOOL:
            for mMonitor in win32api.EnumDisplayMonitors():
                # Определение hadle у монитора
                mHandle = mMonitor[0].Detach()
                # Подгрузка shcore
                shcore = ctypes.WinDLL('shcore')
                # Множитель мастшабирования монитора
                mScaleFactor = ctypes.c_uint()
                shcore.GetScaleFactorForMonitor(mHandle, ctypes.byref(mScaleFactor))
                # Разрешение
                if mHeight < (mMonitor[2][3] - mMonitor[2][1])*(mScaleFactor.value/100): mHeight = int((mMonitor[2][3] - mMonitor[2][1])*(mScaleFactor.value/100))
                mWidth += int((mMonitor[2][2] - mMonitor[2][0])*(mScaleFactor.value/100))
        else:
            for i in range(display.Display().screen_count()):
                screen = display.Display().screen(i)
                loc_width = screen.root.get_geometry().width
                loc_height = screen.root.get_geometry().height
                # Разрешение
                if mHeight < (loc_height): mHeight = int(loc_height)
                mWidth += int(loc_width)
        return mWidth, mHeight

    def _createVariables(self, parent):
        self.parent = parent
        self.rectx0 = 0
        self.recty0 = 0
        self.rectx1 = 0
        self.recty1 = 0
        self.rectid = None

    def _createCanvas(self):
        self.canvas = tk.Canvas(self.parent, width = self.width, height = self.height, bg = "white")
        self.canvas.grid(row=0, column=0, sticky='nsew')

    def _createCanvasBinding(self):
        self.canvas.bind( "<Button-1>", self.startRect )
        self.canvas.bind( "<ButtonRelease-1>", self.stopRect )
        self.canvas.bind( "<B1-Motion>", self.movingRect )
        
    def startRect(self, event):
        """L-,W+: Начало построения выделяемой прямоугольной области

        :param event: Нажатие клавиши мыши
        :type event: событие
        """
        self.canvas.delete("all")
        #Определение начальных координат выделяемой области
        self.rectx0 = self.canvas.canvasx(event.x)
        self.recty0 = self.canvas.canvasy(event.y) 
        #Создание прямоугольной области
        self.rectid = self.canvas.create_rectangle( self.rectx0, self.recty0, self.rectx0, self.recty0, fill="#4eccde")

    def movingRect(self, event):
        """L-,W+: Построения выделяемой прямоугольной области

        :param event: Перемешение мыши
        :type event: событие
        """
        #Определение координат выделяемой области при перемещении мыши
        self.rectx1 = self.canvas.canvasx(event.x)
        self.recty1 = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rectid, self.rectx0, self.recty0, self.rectx1, self.recty1)

    def stopRect(self, event):
        """L-,W+: Завершение построения выделяемой прямоугольной области

        :param event: Поднятие клавиши мыши
        :type event: событие
        """
        #Определение конечных координат выделяемой области
        self.rectx1 = self.canvas.canvasx(event.x)
        self.recty1 = self.canvas.canvasy(event.y)
        self.canvas.delete("all")
        self.parent.attributes('-alpha', 0.0)
        self.root.destroy()
        #Сохранение прямоугольной области как изображение  
        if CrossOS.IS_WINDOWS_BOOL:
            mImg = getRectAsImage(
                (
                    int(self.rectx0 if self.rectx0 <= self.rectx1 else self.rectx1), 
                    int(self.recty0 if self.recty0 <= self.recty1 else self.recty1), 
                    int(self.rectx1 if self.rectx0 <= self.rectx1 else self.rectx0), 
                    int(self.recty1 if self.recty0 <= self.recty1 else self.recty0)
                )
            )
            mImg.save(self.path)
        else:
            #print(" ".join(['scrot', '-s', f'{self.rectx0},{self.rectx1},{self.recty0},{self.recty1}', self.path]))
            subprocess.run(['scrot', self.path], capture_output=True, text=True)
            mImg = Image.open(self.path)
            mImg = mImg.crop((self.rectx0,self.recty0,self.rectx1,self.recty1))
            mImg.save(self.path)

gThreadStopFlag = False
# Функция для minimize/maximize окна tkintera
def WindowMinimize(inRoot):
    lSelector = [{"title":"tk","class_name":"TkTopLevel","backend":"win32"}]
    lFlag = False
    global gThreadStopFlag
    while True:
        if gThreadStopFlag:break
        if Keyboard.IsDown(Keyboard.KEY_HOT_CTRL_LEFT) and lFlag == False:
            lFlag = True
            lActivityResult = UIDesktop.UIOSelectorUIOActivity_Run_Dict(lSelector, "minimize")
        elif Keyboard.IsDown(Keyboard.KEY_HOT_CTRL_LEFT) == False and lFlag == True:
            lFlag = False
            lActivityResult = UIDesktop.UIOSelectorUIOActivity_Run_Dict(lSelector, "maximize")
            break
        time.sleep(0.05)


def InitSnipingTool(inPath):
    """L-,W+:Выполнить выделение прямоугольной области на экране и сохраненить его как изображение.

    !ВНИМАНИЕ! Для того, чтобы временно свернуть окно, нажмите кнопку CTRL, чтобы раскрыть - отпустите кнопку CTRL

    .. code-block:: python

        # Screen: Взаимодействие с объектами экрана
        from pyOpenRPA.Robot import Screen
        Screen.InitSnipingTool(inPath="Screenshot.png")

    :param inPath: Путь, по которому будет сохранена выделенная область
    :type inPath: str, относительный или абсолютный
    """
    if CrossOS.IS_WINDOWS_BOOL:
        global gThreadStopFlag
        lRoot = tk.Tk()
        def quit(l) -> None:
            lRoot.destroy()  
        lRoot.bind("<Escape>",quit) #Установить esc как кнопку выхода
        app = SnipingTool(lRoot,inPath)
        #Инициализация потока для сворачивания окна (Зажать кнопку CTRL)
        lThread = threading.Thread(target=WindowMinimize, args=(lRoot,), daemon=True)
        lThread.start()
        lRoot.mainloop()
        gThreadStopFlag = True #Посылаем сигнал для остановки потока
        lThread.join()
    else:
        inPath = CrossOS.PathStr(inPath)
        subprocess.run(['scrot', '-s',inPath], capture_output=True, text=True)
