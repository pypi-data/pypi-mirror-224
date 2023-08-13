from pyOpenRPA.Tools import CrossOS
import itertools
import sys, os
if CrossOS.IS_WINDOWS_BOOL: from keyboard import *
else: 
    from pynput import keyboard as linux_keyboard
    from pynput.keyboard import Key, Controller
    LINUX_KEYBOARD = Controller()
# USER RIGHTS FOR LINUX KEY READ (DIALOUT GROUP)
# https://github.com/Dygmalab/Bazecor/issues/26
if CrossOS.IS_LINUX_BOOL: 
    import pyautogui
    press = LINUX_KEYBOARD.press
    release = LINUX_KEYBOARD.release
    def send(hotkey, do_press=True, do_release=True):
        key = Key2Code(hotkey)
        if do_press and do_release: LINUX_KEYBOARD.press(key); LINUX_KEYBOARD.release(key); return
        if do_press: LINUX_KEYBOARD.press(key)
        if do_release: LINUX_KEYBOARD.release(key)

WIN = CrossOS.IS_WINDOWS_BOOL
LIN = CrossOS.IS_LINUX_BOOL
import time

# Настройки модуля Keyboard
WAIT_AFTER_SEC_FLOAT = 0.4 # Время, которое ожидать после выполнения любой операции модуля Keyboard. Настройка является единой для всех участов кода, использующих модуль Keyboard. Если для некоторой функции требуется изменить данное время ожидания, то в отношении этой функции можно применить соответсвующий аргумент.

# ШЕСТНАДЦАТИРИЧНЫЙ СКАН-КОД В РУССКОЙ РАСКЛАДКЕ (НЕЗАВИСИМО ОТ ВЫБРАННОГО ЯЗЫКА НА КЛАВИАТУРЕ) 
# ОТОБРАЖЕНИЕ СКАН КОДОВ НА КЛАВИАТУРЕ https://snipp.ru/handbk/scan-codes
from ..Utils import __define__
KEY_RUS_LAYOUT = "ru" # NEED FOR LINUX (FOR LAYOUT SWITCH)
KEY_RUS_Ф = 0x1E if WIN else 'a' #A
KEY_RUS_И = 0x30 if WIN else 'b' #B
KEY_RUS_С = 0x2E if WIN else 'c' #C
KEY_RUS_В = 0x20 if WIN else 'd' #D
KEY_RUS_У = 0x12 if WIN else 'e' #E
KEY_RUS_А = 0x21 if WIN else 'f' #F
KEY_RUS_П = 0x22 if WIN else 'g' #G
KEY_RUS_Р = 0x23 if WIN else 'h' #H
KEY_RUS_Ш = 0x17 if WIN else 'i' #I
KEY_RUS_О = 0x24 if WIN else 'j' #J
KEY_RUS_Л = 0x25 if WIN else 'k' #K
KEY_RUS_Д = 0x26 if WIN else 'l' #L
KEY_RUS_Ь = 0x32 if WIN else 'm' #M
KEY_RUS_Т = 0x31 if WIN else 'n' #N
KEY_RUS_Щ = 0x18 if WIN else 'o' #O
KEY_RUS_З = 0x19 if WIN else 'p' #P
KEY_RUS_Й = 0x10 if WIN else 'q' #Q
KEY_RUS_К = 0x13 if WIN else 'r' #R
KEY_RUS_Ы = 0x1F if WIN else 's' #S
KEY_RUS_Е = 0x14 if WIN else 't' #T
KEY_RUS_Г = 0x16 if WIN else 'u' #U
KEY_RUS_М = 0x2F if WIN else 'v' #V
KEY_RUS_Ц = 0x11 if WIN else 'w' #W
KEY_RUS_Ч = 0x2D if WIN else 'x' #X
KEY_RUS_Н = 0x15 if WIN else 'y' #Y
KEY_RUS_Я = 0x2C if WIN else 'z' #Z
KEY_RUS_Ё = 0x29 if WIN else '~' #~
KEY_RUS_Ж = 0x27 if WIN else ':' #:
KEY_RUS_Б = 0x33 if WIN else '<' #<
KEY_RUS_Ю = 0x34 if WIN else '>' #>
KEY_RUS_Х = 0x1A if WIN else '[' #[
KEY_RUS_Ъ = 0x1B if WIN else ']' #]
KEY_RUS_Э = 0x28 if WIN else "'" #'
 
KEY_ENG_LAYOUT = "us" # NEED FOR LINUX (FOR LAYOUT SWITCH)
KEY_ENG_A = 0x1E if WIN else 'a' #A
KEY_ENG_B = 0x30 if WIN else 'b' #B
KEY_ENG_C = 0x2E if WIN else 'c' #C
KEY_ENG_D = 0x20 if WIN else 'd' #D
KEY_ENG_E = 0x12 if WIN else 'e' #E
KEY_ENG_F = 0x21 if WIN else 'f' #F
KEY_ENG_G = 0x22 if WIN else 'g' #G
KEY_ENG_H = 0x23 if WIN else 'h' #H
KEY_ENG_I = 0x17 if WIN else 'i' #I
KEY_ENG_J = 0x24 if WIN else 'j' #J
KEY_ENG_K = 0x25 if WIN else 'k' #K
KEY_ENG_L = 0x26 if WIN else 'l' #L
KEY_ENG_M = 0x32 if WIN else 'm' #M
KEY_ENG_N = 0x31 if WIN else 'n' #N
KEY_ENG_O = 0x18 if WIN else 'o' #O
KEY_ENG_P = 0x19 if WIN else 'p' #P
KEY_ENG_Q = 0x10 if WIN else 'q' #Q
KEY_ENG_R = 0x13 if WIN else 'r' #R
KEY_ENG_S = 0x1F if WIN else 's' #S
KEY_ENG_T = 0x14 if WIN else 't' #T
KEY_ENG_U = 0x16 if WIN else 'u' #U
KEY_ENG_V = 0x2F if WIN else 'v' #V
KEY_ENG_W = 0x11 if WIN else 'w' #W
KEY_ENG_X = 0x2D if WIN else 'x' #X
KEY_ENG_Y = 0x15 if WIN else 'y' #Y
KEY_ENG_Z = 0x2C if WIN else 'z' #Z

KEY_ENG_TILDE = 0x29 if WIN else '~' #~
KEY_ENG_COLON = 0x27 if WIN else ':' #:
KEY_ENG_PLUS = 0x0D if WIN else '+' #+
KEY_ENG_MINUS = 0x0C if WIN else '-' #-
KEY_ENG_LESS_THAN = 0x33 if WIN else '<' #< ,
KEY_ENG_GREATER_THAN = 0x34 if WIN else '>' #> .
KEY_ENG_SOLIDUS = 0x35 if WIN else '/' #/ ?
KEY_ENG_SQUARE_BRACKET_LEFT = 0x1A if WIN else '['  #[
KEY_ENG_SQUARE_BRACKET_RIGHT = 0x1B if WIN else ']' #]
KEY_ENG_APOSTROPHE = 0x28 if WIN else "'" #' "
KEY_ENG_VERTICAL_LINE = 0x2B if WIN else '|' #| \

KEY_ENG_NUMPAD_0 = 0x52 if WIN else '0' 
KEY_ENG_NUMPAD_1 = 0x4F if WIN else '1' 
KEY_ENG_NUMPAD_2 = 0x50 if WIN else '2' 
KEY_ENG_NUMPAD_3 = 0x51 if WIN else '3' 
KEY_ENG_NUMPAD_4 = 0x4B if WIN else '4' 
KEY_ENG_NUMPAD_5 = 0x4C if WIN else '5' 
KEY_ENG_NUMPAD_6 = 0x4D if WIN else '6' 
KEY_ENG_NUMPAD_7 = 0x47 if WIN else '7' 
KEY_ENG_NUMPAD_8 = 0x48 if WIN else '8' 
KEY_ENG_NUMPAD_9 = 0x49 if WIN else '9' 
KEY_ENG_NUMPAD_ASTERISK = 0x37 if WIN else '*'  #*
KEY_ENG_NUMPAD_PLUS = 0x4E if WIN else '+' 
KEY_ENG_NUMPAD_MINUS = 0x4A if WIN else '-' 
KEY_ENG_NUMPAD_DELETE = 0x53 if WIN else linux_keyboard.Key.delete
KEY_ENG_NUMPAD_SOLIDUS = 0x35 if WIN else '/' #/ 
KEY_ENG_NUMPAD_ENTER = 0x11c if WIN else linux_keyboard.Key.enter

KEY_ENG_0 = 0xB if WIN else '0' 
KEY_ENG_1 = 0x2 if WIN else '1' 
KEY_ENG_2 = 0x3 if WIN else '2' 
KEY_ENG_3 = 0x4 if WIN else '3' 
KEY_ENG_4 = 0x5 if WIN else '4' 
KEY_ENG_5 = 0x6 if WIN else '5' 
KEY_ENG_6 = 0x7 if WIN else '6' 
KEY_ENG_7 = 0x8 if WIN else '7' 
KEY_ENG_8 = 0x9 if WIN else '8' 
KEY_ENG_9 = 0xA if WIN else '9' 

KEY_HOT_NUMPAD_0 = 0x52 if WIN else '0' 
KEY_HOT_NUMPAD_1 = 0x4F if WIN else '1' 
KEY_HOT_NUMPAD_2 = 0x50 if WIN else '2' 
KEY_HOT_NUMPAD_3 = 0x51 if WIN else '3' 
KEY_HOT_NUMPAD_4 = 0x4B if WIN else '4' 
KEY_HOT_NUMPAD_5 = 0x4C if WIN else '5' 
KEY_HOT_NUMPAD_6 = 0x4D if WIN else '6' 
KEY_HOT_NUMPAD_7 = 0x47 if WIN else '7' 
KEY_HOT_NUMPAD_8 = 0x48 if WIN else '8' 
KEY_HOT_NUMPAD_9 = 0x49 if WIN else '9' 
KEY_HOT_NUMPAD_ASTERISK = 0x37 if WIN else '*'  #*
KEY_HOT_NUMPAD_PLUS = 0x4E if WIN else '+' 
KEY_HOT_NUMPAD_MINUS = 0x4A if WIN else '-' 
KEY_HOT_NUMPAD_DELETE = 0x53 if WIN else linux_keyboard.Key.delete
KEY_HOT_NUMPAD_SOLIDUS = 0x35 if WIN else '/' #/ 
KEY_HOT_NUMPAD_ENTER = 0x11c if WIN else linux_keyboard.Key.enter

KEY_HOT_F1 = 0x3B if WIN else linux_keyboard.Key.f1 
KEY_HOT_F2 = 0x3C if WIN else linux_keyboard.Key.f2 
KEY_HOT_F3 = 0x3D if WIN else linux_keyboard.Key.f3 
KEY_HOT_F4 = 0x3E if WIN else linux_keyboard.Key.f4 
KEY_HOT_F5 = 0x3F if WIN else linux_keyboard.Key.f5 
KEY_HOT_F6 = 0x40 if WIN else linux_keyboard.Key.f6 
KEY_HOT_F7 = 0x41 if WIN else linux_keyboard.Key.f7 
KEY_HOT_F8 = 0x42 if WIN else linux_keyboard.Key.f8  
KEY_HOT_F9 = 0x43 if WIN else linux_keyboard.Key.f9  
KEY_HOT_F10 = 0x44 if WIN else linux_keyboard.Key.f10 
KEY_HOT_F11 = 0x57 if WIN else linux_keyboard.Key.f11
KEY_HOT_F12 = 0x58 if WIN else linux_keyboard.Key.f12
KEY_HOT_F13 = 0x7C if WIN else linux_keyboard.Key.f13
KEY_HOT_F14 = 0x7D if WIN else linux_keyboard.Key.f14
KEY_HOT_F15 = 0x7E if WIN else linux_keyboard.Key.f15
KEY_HOT_F16 = 0x7F if WIN else linux_keyboard.Key.f16
KEY_HOT_F17 = 0x80 if WIN else linux_keyboard.Key.f17
KEY_HOT_F18 = 0x81 if WIN else linux_keyboard.Key.f18
KEY_HOT_F19 = 0x82 if WIN else linux_keyboard.Key.f19
KEY_HOT_F20 = 0x83 if WIN else linux_keyboard.Key.f20
KEY_HOT_F21 = 0x84 if WIN else linux_keyboard.Key.f20 # LINUX DO NOT HAS THIS KEY
KEY_HOT_F22 = 0x85 if WIN else linux_keyboard.Key.f20 # LINUX DO NOT HAS THIS KEY
KEY_HOT_F23 = 0x86 if WIN else linux_keyboard.Key.f20 # LINUX DO NOT HAS THIS KEY
KEY_HOT_F24 = 0x87 if WIN else linux_keyboard.Key.f20 # LINUX DO NOT HAS THIS KEY

KEY_HOT_TILDE = 0x29 if WIN else '~' #~
KEY_HOT_COLON = 0x27 if WIN else ':' #:
KEY_HOT_PLUS = 0x0D if WIN else '+' #+
KEY_HOT_MINUS = 0x0C if WIN else '-' #-
KEY_HOT_LESS_THAN = 0x33 if WIN else '<' #< ,
KEY_HOT_GREATER_THAN = 0x34 if WIN else '>' #> .
KEY_HOT_SOLIDUS = 0x35 if WIN else '/' #/ ?
KEY_HOT_SQUARE_BRACKET_LEFT = 0x1A if WIN else '['  #[
KEY_HOT_SQUARE_BRACKET_RIGHT = 0x1B if WIN else ']' #]
KEY_HOT_APOSTROPHE = 0x28 if WIN else "'" #' "
KEY_HOT_VERTICAL_LINE = 0x2B if WIN else '|' #| \

KEY_HOT_ESC = 0x1 if WIN else linux_keyboard.Key.esc
KEY_HOT_BACKSPACE = 0x0E if WIN else linux_keyboard.Key.backspace
KEY_HOT_TAB = 0x0F if WIN else linux_keyboard.Key.tab
KEY_HOT_ENTER = 0x1C if WIN else linux_keyboard.Key.enter
KEY_HOT_CONTEXT_MENU = 0x15D if WIN else linux_keyboard.Key.menu
KEY_HOT_SHIFT = 0x2A if WIN else linux_keyboard.Key.shift
KEY_HOT_SHIFT_LEFT = 0x2A if WIN else linux_keyboard.Key.shift_l
KEY_HOT_SHIFT_RIGHT = 0x36 if WIN else linux_keyboard.Key.shift_r
KEY_HOT_CTRL = 0x1D if WIN else linux_keyboard.Key.ctrl
KEY_HOT_CTRL_LEFT = 0x1D if WIN else linux_keyboard.Key.ctrl_l
KEY_HOT_CTRL_RIGHT = 0x11D if WIN else linux_keyboard.Key.ctrl_r
KEY_HOT_ALT_LEFT = 0x38  if WIN else linux_keyboard.Key.alt_l
KEY_HOT_ALT_RIGHT = 0x138  if WIN else linux_keyboard.Key.alt_r
KEY_HOT_WIN_LEFT = 57435 if WIN else linux_keyboard.Key.cmd_l #OLD AND DONT WORK 0x5B
KEY_HOT_WIN_RIGHT = 57436  if WIN else linux_keyboard.Key.cmd_r #OLD AND DONT WORK 0x5C
KEY_HOT_CAPS_LOCK = 0x3A  if WIN else linux_keyboard.Key.caps_lock
KEY_HOT_NUM_LOCK = 0x45  if WIN else linux_keyboard.Key.num_lock
KEY_HOT_SCROLL_LOCK = 0x46  if WIN else linux_keyboard.Key.scroll_lock
KEY_HOT_END = 0x4F  if WIN else linux_keyboard.Key.end
KEY_HOT_HOME = 0x47 if WIN else linux_keyboard.Key.home
KEY_HOT_SPACE = 0x39 if WIN else linux_keyboard.Key.space
KEY_HOT_PAGE_UP = 0x49  if WIN else linux_keyboard.Key.page_up
KEY_HOT_PAGE_DOWN = 0x51 if WIN else linux_keyboard.Key.page_down
KEY_HOT_CLEAR = 0x4C if WIN else linux_keyboard.Key.delete
KEY_HOT_LEFT = 0x4B if WIN else linux_keyboard.Key.left
KEY_HOT_UP = 0x48  if WIN else linux_keyboard.Key.up
KEY_HOT_RIGHT = 0x4D  if WIN else linux_keyboard.Key.right
KEY_HOT_DOWN = 0x50  if WIN else linux_keyboard.Key.down
KEY_HOT_PRINT_SCREEN = 0x137  if WIN else linux_keyboard.Key.print_screen
KEY_HOT_INSERT = 0x52 if WIN else linux_keyboard.Key.insert
KEY_HOT_DELETE = 0x53 if WIN else linux_keyboard.Key.delete

KEY_HOT_0 = 0xB if WIN else '0' 
KEY_HOT_1 = 0x2 if WIN else '1' 
KEY_HOT_2 = 0x3 if WIN else '2' 
KEY_HOT_3 = 0x4 if WIN else '3' 
KEY_HOT_4 = 0x5 if WIN else '4' 
KEY_HOT_5 = 0x6 if WIN else '5' 
KEY_HOT_6 = 0x7 if WIN else '6' 
KEY_HOT_7 = 0x8 if WIN else '7' 
KEY_HOT_8 = 0x9 if WIN else '8' 
KEY_HOT_9 = 0xA if WIN else '9' 

MAP_RUS_ENG = { # FOR LINUX PURPOSE
"Ё":"`",
"Й":"q",
"Ц":"w",
"У":"e",
"К":"r",
"Е":"t",
"Н":"y",
"Г":"u",
"Ш":"i",
"Щ":"o",
"З":"p",
"Х":"[",
"Ъ":"]",
"Ф":"a",
"Ы":"s",
"В":"d",
"А":"f",
"П":"g",
"Р":"h",
"О":"j",
"Л":"k",
"Д":"l",
"Ж":";",
"Э":"'",
"Я":"z",
"Ч":"x",
"С":"c",
"М":"v",
"И":"b",
"Т":"n",
"Ь":"m",
"Б":",",
"Ю":"."
}


def Write(inTextStr:str, inDelayFloat:float=0, inRestoreStateAfterBool:bool=True, inExactBool:bool=None, inWaitAfterSecFloat:float=WAIT_AFTER_SEC_FLOAT):
    """L+,W+: Печатает текст, который был передан в переменной inTextStr (поддерживает передачу в одной строке символов разного языка). Не зависит от текущей раскладки клавиатуры! Посылает искусственные клавишные события в ОС, моделируя печать данного текста. Знаки, не доступные на клавиатуре, напечатаны как явный unicode знаки, использующие определенную для ОС функциональность, такие как alt+codepoint.
    Чтобы гарантировать текстовую целостность, все в настоящее время нажатые ключи выпущены прежде текст напечатан, и модификаторы восстановлены впоследствии.

    ВНИМАНИЕ! ПЕЧАТАЕТ ЛЮБУЮ СТРОКУ, ДАЖЕ В СОЧЕТАНИИ НЕСКОЛЬКИХ ЯЗЫКОВ ОДНОВРЕМЕННО. ДЛЯ РАБОТЫ С ГОРЯЧИМИ КЛАВИШАМИ ИСПОЛЬЗУЙ ФУНКЦИЮ Send, Up, Down, HotkeyCombination

    ВНИМАНИЕ! В LINUX НЕ ДЕЙСТВУЮТ СЛЕДУЮЩИЕ ПАРАМЕТРЫ: inRestoreStateAfterBool, inExactBool

    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.Write("Привет мой милый мир! Hello my dear world!")

    :param inTextStr: Текст, отправляемый на печать. Не зависит от текущей раскладки клавиатуры! 
    :type inTextStr: str
    :param inDelayFloat: Число секунд, которое ожидать между нажатиями. По умолчанию 0
    :type inDelayFloat: float, опциональный
    :param inRestoreStateAfterBool: Может использоваться, чтобы восстановить регистр нажатых ключей после того, как текст напечатан, т.е. нажимает ключи, которые были выпущены в начало.
    :type inRestoreStateAfterBool: bool, опциональный
    :param inExactBool: Печатает все знаки как явный unicode. Необязательный параметр
    :type inExactBool: bool, опциональный
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    if CrossOS.IS_WINDOWS_BOOL:
        write(text=inTextStr, delay=inDelayFloat, restore_state_after=inRestoreStateAfterBool, exact=inExactBool)
    elif CrossOS.IS_LINUX_BOOL:
        _WriteLinux(inTextStr=inTextStr, inDelayFloat=inDelayFloat)
    time.sleep(inWaitAfterSecFloat)

def _WriteLinux(inTextStr, inDelayFloat=0.01):
    lModuleKeyboard = sys.modules[__name__]
    lVarList = dir(lModuleKeyboard)
    lLayoutStr = None
    for lCharStr in inTextStr:
        # Check rus (ru)
        lVarNameStr = f"KEY_RUS_{lCharStr.upper()}"
        lFoundBool = False
        lShiftBool = False
        if lVarNameStr in lVarList: 
            lNewLayoutStr=getattr(lModuleKeyboard, "KEY_RUS_LAYOUT")
            lCapBool = lCharStr.isupper()
            lCharStr = MAP_RUS_ENG[lCharStr.upper()]
            #if lCapBool == True: lCharStr=lCharStr.upper()
            if lCapBool == True: lShiftBool=True            
            lFoundBool=True
        # Check eng (us)
        lVarNameStr = f"KEY_ENG_{lCharStr.upper()}"
        if lVarNameStr in lVarList and lFoundBool == False: 
            lNewLayoutStr=getattr(lModuleKeyboard, "KEY_ENG_LAYOUT")
            lFoundBool=True
        if lFoundBool == False: lNewLayoutStr=getattr(lModuleKeyboard, "KEY_ENG_LAYOUT")
        # CHECK LAST LAYOUT
        if lNewLayoutStr != lLayoutStr: 
            #print(f"setxkbmap -layout {lNewLayoutStr}")
            os.system(f"setxkbmap -layout {lNewLayoutStr}")
            lLayoutStr = lNewLayoutStr
        if lShiftBool == True: pyautogui.keyDown('shift')  # hold down the shift key
        pyautogui.write(lCharStr, interval = inDelayFloat)
        if lShiftBool == True: pyautogui.keyUp('shift')  # hold down the shift key
    
    # Set 2 layout with alt+shift switch
    os.system(f"setxkbmap -layout {getattr(lModuleKeyboard, 'KEY_ENG_LAYOUT')},{getattr(lModuleKeyboard, 'KEY_RUS_LAYOUT')} -option grp:alt_shift_toggle")

def Hotkeys(*inKeyList, inDelaySecFloat = 0.3,inWaitAfterSecFloat:float=WAIT_AFTER_SEC_FLOAT):
    """L+,W+: Синоним функции HotkeyCombination
        .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.Hotkeys(Keyboard.KEY_HOT_CTRL_LEFT,Keyboard.KEY_ENG_A) # Ctrl + a
        Keyboard.Hotkeys(Keyboard.KEY_HOT_CTRL_LEFT,Keyboard.KEY_ENG_C) # Ctrl + c
        Keyboard.Hotkeys("ctrl","a") #Ctrl+A
        Keyboard.Hotkeys("ctrl", "x") #Ctrl+X
        Keyboard.Hotkeys(Keyboard.KEY_HOT_ALT_LEFT,Keyboard.KEY_HOT_TAB, Keyboard.KEY_HOT_TAB)
    """
    HotkeyCombination(*inKeyList, inDelaySecFloat = inDelaySecFloat,inWaitAfterSecFloat=inWaitAfterSecFloat)

def HotkeyCombination(*inKeyList, inDelaySecFloat = 0.3,inWaitAfterSecFloat:float=WAIT_AFTER_SEC_FLOAT):
    """L+,W+: Получает перечень клавиш для одновременного нажатия. Между нажатиями программа ожидания время inDelaySecFloat
    ВНИМАНИЕ! НЕ ЗАВИСИТ ОТ ТЕКУЩЕЙ РАСКЛАДКИ КЛАВИАТУРЫ

    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.HotkeyCombination(Keyboard.KEY_HOT_CTRL_LEFT,Keyboard.KEY_ENG_A) # Ctrl + a
        Keyboard.HotkeyCombination(Keyboard.KEY_HOT_CTRL_LEFT,Keyboard.KEY_ENG_C) # Ctrl + c
        Keyboard.HotkeyCombination(Keyboard.KEY_HOT_CTRL_LEFT,Keyboard.KEY_ENG_A)
        Keyboard.HotkeyCombination("ctrl", "x") #Ctrl+X
        Keyboard.HotkeyCombination(Keyboard.KEY_HOT_ALT_LEFT,Keyboard.KEY_HOT_TAB, Keyboard.KEY_HOT_TAB)
    
    :param inKeyList: Список клавиш для одновременного нажатия. Перечень клавиш см. в разделе "Коды клавиш". Пример: KEY_HOT_CTRL_LEFT,KEY_ENG_A
    :param inDelaySecFloat: Интервал между нажатиями. Необходим в связи с тем, что операционной системе требуется время на реакцию на нажатие клавиш, по умолчанию: 0.3
    :type inDelaySecFloat: float, опциональный
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    for l_key_item in inKeyList:
        l_key_item = Key2Code(inKeyStr=l_key_item)
        if l_key_item == inKeyList[-1]:
            send(l_key_item)
        else:
            press(l_key_item)
        time.sleep(inDelaySecFloat)
    lRevKeyList = list(reversed(inKeyList))
    for l_key_item in lRevKeyList:
        l_key_item = Key2Code(inKeyStr=l_key_item)
        if l_key_item == lRevKeyList[0]:
            pass
        else:
            release(l_key_item)
        time.sleep(inDelaySecFloat)
    time.sleep(inWaitAfterSecFloat)

def HotkeyCtrlV(inWaitAfterSecFloat:float=0.4) -> None:
    """L+,W+: Выполнить вставку текста из буфера обмена
    ВНИМАНИЕ! НЕ ЗАВИСИТ ОТ ТЕКУЩЕЙ РАСКЛАДКИ КЛАВИАТУРЫ
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.HotkeyCtrlV()
    
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    HotkeyCombination(KEY_HOT_CTRL_LEFT,KEY_ENG_V) # Ctrl + v
    time.sleep(inWaitAfterSecFloat)

def HotkeyCtrlZ(inWaitAfterSecFloat:float=0.4) -> None:
    """L+,W+: Отменить последнее действие
    ВНИМАНИЕ! НЕ ЗАВИСИТ ОТ ТЕКУЩЕЙ РАСКЛАДКИ КЛАВИАТУРЫ
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.HotkeyCtrlZ()
    
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    HotkeyCombination(KEY_HOT_CTRL_LEFT,KEY_ENG_Z) # Ctrl + z
    time.sleep(inWaitAfterSecFloat)

def HotkeyCtrlA_CtrlC(inWaitAfterSecFloat:float=0.4) -> None:
    """L+,W+: Выполнить выделение текста, после чего скопировать его в буфер обмена
    ВНИМАНИЕ! НЕ ЗАВИСИТ ОТ ТЕКУЩЕЙ РАСКЛАДКИ КЛАВИАТУРЫ
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.HotkeyCtrlA_CtrlC() # Отправить команды: выделить все, скопировать в буфер обмена
    
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    HotkeyCombination(KEY_HOT_CTRL_LEFT,KEY_ENG_A) # Ctrl + a
    HotkeyCombination(KEY_HOT_CTRL_LEFT,KEY_ENG_C) # Ctrl + c
    time.sleep(inWaitAfterSecFloat)


def HotkeyCtrlA_CtrlX(inWaitAfterSecFloat:float=0.4) -> None:
    """L+,W+: Выполнить выделение текста, после чего вырезать его в буфер обмена
    ВНИМАНИЕ! НЕ ЗАВИСИТ ОТ ТЕКУЩЕЙ РАСКЛАДКИ КЛАВИАТУРЫ
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.HotkeyCtrlA_CtrlX() # Отправить команды: выделить все, скопировать в буфер обмена
    
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    HotkeyCombination(KEY_HOT_CTRL_LEFT,KEY_ENG_A) # Ctrl + a
    HotkeyCombination(KEY_HOT_CTRL_LEFT,KEY_ENG_X) # Ctrl + X
    time.sleep(inWaitAfterSecFloat)

def Send(inKeyInt:int, inDoPressBool:bool=True, inDoReleaseBool:bool=True,inWaitAfterSecFloat:float=WAIT_AFTER_SEC_FLOAT) -> None:
    """L+,W+: Имитация нажатия/отпускания любой физической клавиши. Посылает событие в операционную систему, которые выполняет нажатие и отпускание данной клавиши
    
    ВНИМАНИЕ! ПРИ ПОПЫТКЕ ПЕЧАТИ ТЕКСТА БУДЕТ УЧИТЫВАТЬ ТЕКУЩУЮ РАСКЛАДКУ КЛАВИАТУРЫ. ДЛЯ ПЕЧАТИ ТЕКСТА ИСПОЛЬЗУЙ Write!

    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.Send(Keyboard.KEY_ENG_A) # Нажать клавишу A. Если будет активна русская раскладка, то будет выведена буква ф.

    :param inKeyInt: Перечень клавиш см. в разделе "Коды клавиш". Пример: KEY_HOT_CTRL_LEFT,KEY_ENG_A
    :type inKeyInt: int
    :param inDoPressBool: Выполнить событие нажатия клавиши, По умолчанию True
    :type inDoPressBool: bool, опциональный
    :param inDoReleaseBool: Выполнить событие отпускания клавиши, По умолчанию True
    :type inDoReleaseBool: bool, опциональный
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    inKeyInt = Key2Code(inKeyStr=inKeyInt)
    send(hotkey=inKeyInt, do_press=inDoPressBool, do_release=inDoReleaseBool)
    time.sleep(inWaitAfterSecFloat)
    
def Up(inKeyInt:int, inWaitAfterSecFloat:float=WAIT_AFTER_SEC_FLOAT) -> None:
    """L+,W+: Отпустить (поднять) клавишу. Если клавиша уже была поднята, то ничего не произойдет.
    
    ВНИМАНИЕ! ПРИ ПОПЫТКЕ ПЕЧАТИ ТЕКСТА БУДЕТ УЧИТЫВАТЬ ТЕКУЩУЮ РАСКЛАДКУ КЛАВИАТУРЫ. ДЛЯ ПЕЧАТИ ТЕКСТА ИСПОЛЬЗУЙ Write!

    ВНИМАНИЕ! ФУНКЦИЯ МОЖЕТ ОТРАБОТАТЬ НЕКОРРЕКТНО В ТОМ СЛУЧАЕ, ЕСЛИ ДЕЙСТВИЕ ПРОИСХОДИТ СРАЗУ ПОСЛЕ НАЖАТИЯ КЛАВИШИ ENTER (ИСПОЛЬЗУЙТЕ SLEEP)
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.Up(Keyboard.KEY_ENG_A) # Отпустить клавишу A.

    :param inKeyInt: Перечень клавиш см. в разделе "Коды клавиш". Пример: KEY_HOT_CTRL_LEFT, KEY_ENG_A
    :type inKeyInt: int
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    inKeyInt = Key2Code(inKeyStr=inKeyInt)
    if CrossOS.IS_LINUX_BOOL:
        LINUX_KEYBOARD.release(inKeyInt)
    else:
        send(hotkey=inKeyInt, do_press=False, do_release=True)
    time.sleep(inWaitAfterSecFloat)
    
# ТЕХ ФУНКЦИЯ В LINUX
def _DownLinuxThread(inKeyInt, inIntervalSecFloat=0.5):
    LINUX_PRESSED_KEY_SET.add(inKeyInt)
    while inKeyInt in LINUX_PRESSED_KEY_SET:
        LINUX_KEYBOARD.press(inKeyInt)
        time.sleep(inIntervalSecFloat)

import threading

def Down(inKeyInt:int, inWaitAfterSecFloat:float=WAIT_AFTER_SEC_FLOAT, inLinuxCharIntervalSecFloat:float = 0.5) -> None:
    """L+,W+: Нажать (опустить) клавишу. Если клавиша уже была опущена, то ничего не произойдет.
    
    ВНИМАНИЕ! ПРИ ПОПЫТКЕ ПЕЧАТИ ТЕКСТА БУДЕТ УЧИТЫВАТЬ ТЕКУЩУЮ РАСКЛАДКУ КЛАВИАТУРЫ. ДЛЯ ПЕЧАТИ ТЕКСТА ИСПОЛЬЗУЙ Write!

    ВНИМАНИЕ! ФУНКЦИЯ МОЖЕТ ОТРАБОТАТЬ НЕКОРРЕКТНО В ТОМ СЛУЧАЕ, ЕСЛИ ДЕЙСТВИЕ ПРОИСХОДИТ СРАЗУ ПОСЛЕ НАЖАТИЯ КЛАВИШИ ENTER (ИСПОЛЬЗУЙТЕ SLEEP)
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.Down(Keyboard.KEY_ENG_A) # Отпустить клавишу A.

    :param inKeyInt: Перечень клавиш см. в разделе "Коды клавиш". Пример: KEY_HOT_CTRL_LEFT, KEY_ENG_A
    :type inKeyInt: int
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    :param inLinuxCharIntervalSecFloat: Интервал отправки символа (не горячих клавиш) на период зажатой кнопки. По умолчанию 0.5 сек.
    :type inLinuxCharIntervalSecFloat: float, опциональный
    """
    inKeyInt = Key2Code(inKeyStr=inKeyInt)
    if CrossOS.IS_LINUX_BOOL:

        if type(inKeyInt) is Key:
            #print(inKeyInt)
            with LINUX_KEYBOARD.pressed(inKeyInt): # БЕЗ ЭТОЙ КОНСТРУКЦИИ НЕ РАБОТАЕТ НАЖАТИЕ ГОРЯЧИХ КЛАВИШ (СВОЕГО РОДА АКТИВАЦИЯ)
                pass
            LINUX_KEYBOARD.press(inKeyInt)
        else:
            thread = threading.Thread(target=_DownLinuxThread, kwargs={"inKeyInt":inKeyInt, "inIntervalSecFloat":inLinuxCharIntervalSecFloat})
            thread.start()
    else:
        send(hotkey=inKeyInt, do_press=True, do_release=False)
    time.sleep(inWaitAfterSecFloat)

def IsDown(inKeyInt:int) -> bool:
    """L+,W+: Проверить, опущена ли клавиша. Вернет True если опущена; False если поднята.
    
    ВНИМАНИЕ! ПРИ ПОПЫТКЕ ПЕЧАТИ ТЕКСТА БУДЕТ УЧИТЫВАТЬ ТЕКУЩУЮ РАСКЛАДКУ КЛАВИАТУРЫ. ДЛЯ ПЕЧАТИ ТЕКСТА ИСПОЛЬЗУЙ Write!

    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        lKeyAIsPressedBool = Keyboard.IsDown(Keyboard.KEY_ENG_A) # Проверить, опущена ли клавиша A.

    :param inKeyInt: Перечень клавиш см. в разделе "Коды клавиш". Пример: KEY_HOT_CTRL_LEFT, KEY_ENG_A
    :type inKeyInt: int
    """
    global LINUX_PRESSED_KEY_SET
    inKeyInt = Key2Code(inKeyStr=inKeyInt)
    if CrossOS.IS_WINDOWS_BOOL:
        return is_pressed(inKeyInt)
    else:
        return inKeyInt in LINUX_PRESSED_KEY_SET

def Wait(inKeyInt:int,inWaitAfterSecFloat:float=WAIT_AFTER_SEC_FLOAT):
    """L+,W+: Блокирует выполнение программы, пока данная обозначенная клавиша не будет нажата.
    ВНИМАНИЕ! НЕ ЗАВИСИТ ОТ ТЕКУЩЕЙ РАСКЛАДКИ КЛАВИАТУРЫ. ОЖИДАЕТ НАЖАТИЕ СООТВЕТСВУЮЩЕЙ ФИЗИЧЕСКОЙ КЛАВИШИ
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.Wait(Keyboard.KEY_ENG_A) # Ждать нажатие клавиши A.

    :param inKeyInt: Перечень клавиш см. в разделе "Коды клавиш". Пример: KEY_HOT_CTRL_LEFT,KEY_ENG_A
    :type inKeyInt: int
    :param inWaitAfterSecFloat: Количество секунд, которые ожидать после выполнения операции. По умолчанию установлено в настройках модуля Keyboard (базовое значение 0.4)
    :type inWaitAfterSecFloat: float, опциональный
    """
    inKeyInt = Key2Code(inKeyStr=inKeyInt)
    if CrossOS.IS_WINDOWS_BOOL: wait(hotkey=inKeyInt)
    else:
        while not IsDown(inKeyInt): time.sleep(0.4) 
    time.sleep(inWaitAfterSecFloat)

if CrossOS.IS_WINDOWS_BOOL: key_to_scan_codes("win") # 2022 06 10 Люблю смотреть скан код клавиши Виндовс :)

def KeyIsValid(inKeyStr):
    """L+,W+: Проверка на корректный ввод наименования символа / кнопки в активной операционной системой

    Поддерживает разделители " " "_" "-", допускает произвольную расстановку слов (ctrl left или left ctrl), а также понимает сокращения (ctrl l, ctrl r)

    ВНИМАНИЕ! НЕ ЗАВИСИТ ОТ ТЕКУЩЕЙ РАСКЛАДКИ КЛАВИАТУРЫ. ОЖИДАЕТ НАЖАТИЕ СООТВЕТСВУЮЩЕЙ ФИЗИЧЕСКОЙ КЛАВИШИ
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        lResultBool = Keyboard.KeyIsValid("left ctrl") # RESULT IS: True

    :param inKeyStr: Текстовое обозначение клавиши
    :type inKeyStr: str
    """
    try:
        Key2Code(inKeyStr=inKeyStr, inFlagExceptionBool=True)
        return True
    except Exception as e:
        return False


def KeyVariants(inKeyStr):
    """L+,W+: Предлагает список вариантов наименований с активной операционной системой

    Поддерживает разделители " " "_" "-", допускает произвольную расстановку слов (ctrl left или left ctrl), а также понимает сокращения (ctrl l, ctrl r)

    ВНИМАНИЕ! НЕ ЗАВИСИТ ОТ ТЕКУЩЕЙ РАСКЛАДКИ КЛАВИАТУРЫ. ОЖИДАЕТ НАЖАТИЕ СООТВЕТСВУЮЩЕЙ ФИЗИЧЕСКОЙ КЛАВИШИ
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.KeyVariants("+") # RESULT IS: ['KEY_ENG_NUMPAD_PLUS', 'KEY_ENG_PLUS', 'KEY_HOT_NUMPAD_PLUS', 'KEY_HOT_PLUS']
        Keyboard.KeyVariants("ctrl") # RESULT IS: ['KEY_HOT_CTRL', 'KEY_HOT_CTRL_LEFT', 'KEY_HOT_CTRL_RIGHT']
    
    :param inKeyStr: Текстовое обозначение клавиши
    :type inKeyStr: str
    """
    inKeyStr = inKeyStr.strip()
    variant_list = []
    if type(inKeyStr) is str:
        kbd = sys.modules[__name__]
        map_alias_word = {
        "NUM":"NUMPAD",
        "+":"PLUS",
        "-":"MINUS",
        "~": "TILDE",
        ":":"COLON",
        "<":"LESS",
        ">":"GREATER",
        "/":"SOLID",
        "[":"BRACKET",
        "]":"BRACKET",
        "'":"APOSTROPHE",
        "|": "LINE",
        "*": "ASTERISK",
        "CMD":"WIN"
        }
        # ЗАМЕНА СИМВОЛОВ - и пробела на _
        inKeyStr = inKeyStr.replace(" ",  "_")
        inKeyStr = inKeyStr.replace("-",  "_")
        inKeyStr = inKeyStr.upper()
        # MODULE ATTR LIST
        module_attr_list = dir(kbd)
        # Разбиваем строку на слова
        words = list(inKeyStr.split("_"))
        # ЗАМЕНА ПО СЛОВАМ СИНОНИМАМ, ЕСЛИ ЕСТЬ
        words_new = []
        for item in words:
            if item in map_alias_word: words_new.append(map_alias_word[item])
            else: words_new.append(item)
        words = words_new
        if len(words)>1 and "L" in words: words[words.index("L")]="LEFT"
        if len(words)>1 and "R" in words: words[words.index("R")]="RIGHT"
        # Получаем все возможные комбинации слов заданной длины
        key_list = ["_".join(list(item)).upper() for item in itertools.permutations(words)]
        key_list.append(inKeyStr)
        # Добавить комбинацию - все слова без разделителя
        key_list.append(inKeyStr)
        for KeyStr in key_list:
            # ПЕРЕБОР АТРИБУТОВ МОДУЛЯ
            for attr in module_attr_list:
                if KeyStr in attr and attr not in variant_list and attr.startswith("KEY_"): variant_list.append(attr)
    return variant_list

def Key2Code(inKeyStr, inFlagExceptionBool=False):
    """L+,W+: Переводит текстовое обозначение кнопки в код в соответствии с активной операционной системой

    Поддерживает разделители " " "_" "-", допускает произвольную расстановку слов (ctrl left или left ctrl), а также понимает сокращения (ctrl l, ctrl r)

    ВНИМАНИЕ! НЕ ЗАВИСИТ ОТ ТЕКУЩЕЙ РАСКЛАДКИ КЛАВИАТУРЫ. ОЖИДАЕТ НАЖАТИЕ СООТВЕТСВУЮЩЕЙ ФИЗИЧЕСКОЙ КЛАВИШИ
    
    .. code-block:: python

        # Keyboard: Взаимодействие с клавиатурой
        from pyOpenRPA.Robot import Keyboard
        Keyboard.Key2Code("ctrl  left")

    :param inKeyStr: Текстовое обозначение клавиши
    :type inKeyStr: str
    :param inFlagExceptionBool: True - генерация исключения, если не удалось идентифицировать код, False - вернуть входящий аргумент
    """
    if type(inKeyStr) is str:
        if CrossOS.IS_LINUX_BOOL and len(inKeyStr)==1: return inKeyStr # ONE SIZE CHAR - FOR LINUX IS GOOD RESULT
        kbd = sys.modules[__name__]
        map_const_word = {
        "WIN":KEY_HOT_WIN_LEFT,
        "CMD":KEY_HOT_WIN_LEFT,
        "ALT":KEY_HOT_ALT_LEFT,
        "CTRL":KEY_HOT_CTRL_LEFT,
        "~": KEY_HOT_TILDE,
        ":":KEY_HOT_COLON,
        "+":KEY_HOT_PLUS,
        "-":KEY_HOT_MINUS,
        "<":KEY_HOT_LESS_THAN,
        ">":KEY_HOT_GREATER_THAN,
        "/":KEY_HOT_SOLIDUS,
        "[":KEY_HOT_SQUARE_BRACKET_LEFT,
        "]":KEY_HOT_SQUARE_BRACKET_RIGHT,
        "'":KEY_HOT_APOSTROPHE,
        "|": KEY_HOT_VERTICAL_LINE,
        "*": KEY_HOT_NUMPAD_ASTERISK
        }
        map_alias_word = {
        "NUM":"NUMPAD",
        "+":"PLUS",
        "-":"MINUS",
        "CMD": "WIN"
        }
        inKeyStr = inKeyStr.strip()
        # ЗАМЕНА СИМВОЛОВ - и пробела на _
        inKeyStr = inKeyStr.replace(" ",  "_")
        inKeyStr = inKeyStr.replace("-",  "_")
        inKeyStr = inKeyStr.upper()
        # ПРОВЕРКА ПО КОНСТАНТНОМУ СЛОВАРЮ
        if inKeyStr in map_const_word:
            return map_const_word[inKeyStr]
        # Разбиваем строку на слова
        words = list(inKeyStr.split("_"))
        # ЗАМЕНА ПО СЛОВАМ СИНОНИМАМ, ЕСЛИ ЕСТЬ
        words_new = []
        for item in words:
            if item in map_alias_word: words_new.append(map_alias_word[item])
            else: words_new.append(item)
        words = words_new
        if len(words)>1 and "L" in words: words[words.index("L")]="LEFT"
        if len(words)>1 and "R" in words: words[words.index("R")]="RIGHT"
        # Получаем все возможные комбинации слов заданной длины
        key_list = ["_".join(list(item)).upper() for item in itertools.permutations(words)]
        key_list.append(inKeyStr)
        # Добавить комбинацию - все слова без разделителя
        key_list.append(inKeyStr)
        for KeyStr in key_list:
            # ПРОВЕРКА HOT
            key_name_str = f"KEY_HOT_{KeyStr.upper()}"
            if hasattr(kbd, key_name_str): return getattr(kbd, key_name_str)
            # ПРОВЕРКА ENG
            key_name_str = f"KEY_ENG_{KeyStr.upper()}"
            if hasattr(kbd, key_name_str): return getattr(kbd, key_name_str)
            # ПРОВЕРКА RUS
            key_name_str = f"KEY_RUS_{KeyStr.upper()}"
            if hasattr(kbd, key_name_str): return getattr(kbd, key_name_str)
            # ПРОВЕРКА HOT
            key_name_str = f"KEY_{KeyStr.upper()}"
            if hasattr(kbd, key_name_str): return getattr(kbd, key_name_str)
            # ПРОВЕРКА ENG
            key_name_str = f"KEY_{KeyStr.upper()}"
            if hasattr(kbd, key_name_str): return getattr(kbd, key_name_str)
            # ПРОВЕРКА RUS
            key_name_str = f"KEY_{KeyStr.upper()}"
            if hasattr(kbd, key_name_str): return getattr(kbd, key_name_str)
            # ПРОВЕРКА HOT
            key_name_str = f"{KeyStr.upper()}"
            if hasattr(kbd, key_name_str): return getattr(kbd, key_name_str)
            # ПРОВЕРКА ENG
            key_name_str = f"{KeyStr.upper()}"
            if hasattr(kbd, key_name_str): return getattr(kbd, key_name_str)
            # ПРОВЕРКА RUS
            key_name_str = f"{KeyStr.upper()}"
            if hasattr(kbd, key_name_str): return getattr(kbd, key_name_str)
        # КЛАВИША НЕ БЫЛА НАЙДЕНА
        if inFlagExceptionBool==True:
            raise Exception(f"Can't detect Key code by the Key value: {inKeyStr}")
    else:
        return inKeyStr


# МОДУЛЬ ФИКСАЦИИ НАЖАТЫХ КНОПОК
LINUX_PRESSED_KEY_SET=set()

def _OnPressLinux(key):
    global LINUX_PRESSED_KEY_SET
    key_name = None 
    try:
        if key.vk == 65032: key_name = Key2Code("alt")
        else: key_name = Key2Code(key.char)
        #print(f"press char: {key.char}, vk: {key.vk}")
        #print('alphanumeric key {0} pressed'.format(
        #    key_name))
    except AttributeError:
        key_name = Key2Code(key.name)
        #print(f"press {key.name}")
        #print('special key {0} pressed'.format(
        #    key_name))
    LINUX_PRESSED_KEY_SET.add(key_name)
    
def _OnReleaseLinux(key):
    global LINUX_PRESSED_KEY_SET
    key_name = None
    try:
        if key.vk == 65032: # SPECIAL CASE FOR SHIFT IN LINUX (pynput do not detect left or right shift release)
            try:
                key_name = Key2Code("shift r")
                #print(f"release {key_name}")
                if key_name in LINUX_PRESSED_KEY_SET: LINUX_PRESSED_KEY_SET.remove(key_name)

                key_name = Key2Code("shift")
                #print(f"release {key_name}")
                if key_name in LINUX_PRESSED_KEY_SET: LINUX_PRESSED_KEY_SET.remove(key_name)
                key_name = Key2Code("shift l")
                #print(f"release {key_name}")
                if key_name in LINUX_PRESSED_KEY_SET: LINUX_PRESSED_KEY_SET.remove(key_name)
                key_name = Key2Code("alt")
                #print(f"release {key_name}")
                if key_name in LINUX_PRESSED_KEY_SET: LINUX_PRESSED_KEY_SET.remove(key_name)
                key_name = Key2Code("alt r")
                #print(f"release {key_name}")
                if key_name in LINUX_PRESSED_KEY_SET: LINUX_PRESSED_KEY_SET.remove(key_name)
            except: pass
            key_name = Key2Code("shift l")
        else:
            key_name = Key2Code(key.char)
            #print('alphanumeric key {0} released, value {1}'.format(
            #    key_name, key.value))
    except AttributeError:
        key_name = Key2Code(key.name)
        #print('special key {0} released'.format(
        #    key_name))
    try:
        #print(f"release {key_name}")
        if key_name in LINUX_PRESSED_KEY_SET: LINUX_PRESSED_KEY_SET.remove(key_name)
    except: pass

#ОБРАБОТЧИК КНОПОК ДЛЯ LINUX ( ТАК КАК В LINUX НЕТ ПОДСИСТЕМЫ ХРАНЕНИЯ СОСТОЯНИЙ КНОПОК
if CrossOS.IS_LINUX_BOOL:
    # ...or, in a non-blocking fashion:
    listener = linux_keyboard.Listener(
        on_press=_OnPressLinux,
        on_release=_OnReleaseLinux)
    listener.start()
