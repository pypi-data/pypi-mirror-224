import ctypes
####################################
#Info:L+,W+: Window module of the Robot app (OpenRPA - Robot)
####################################
# WIndow Module - Show information dialog messages to user by the modal windows

################
###DialogYesNo
################

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
from ..Utils import CrossOS

#return 1 - Yes; 2 - No
def DialogYesNo(inTitle,inBody):
    if CrossOS.IS_WINDOWS_BOOL:
        lResult = ctypes.windll.user32.MessageBoxW(0, inBody, inTitle, 1)
        return lResult
    else:
        root = tk.Tk()
        root.wm_attributes('-topmost', 1)
        root.withdraw()
        answer = messagebox.askyesno(inTitle, inBody)
        root.destroy()
        return answer


def DialogFileSelect(inPathStr="", inTitleStr="Выбрать файл", inFileTypeList=[]):
    """_summary_

    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    :param inPathStr: _description_, defaults to ""
    :type inPathStr: str, optional
    :param inTitleStr: _description_, defaults to "Выбрать файл"
    :type inTitleStr: str, optional
    :param inFileTypeList: _description_, defaults to []
    :type inFileTypeList: list, optional
    :return: _description_
    :rtype: _type_
    """
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    file_path = filedialog.askopenfilename(initialdir=os.path.abspath(inPathStr), title=inTitleStr, filetypes=inFileTypeList)
    root.destroy()
    return CrossOS.PathStr(file_path)

def DialogFolderSelect(inPathStr="", inTitleStr="Выбрать папку"):
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    folder_path = filedialog.askdirectory(initialdir=os.path.abspath(inPathStr), title=inTitleStr)
    root.destroy()
    return CrossOS.PathStr(folder_path)

def DialogInfo(inTitle,inBody):    
    root = tk.Tk()
    root.wm_attributes('-topmost', 1)
    root.withdraw()
    messagebox.showinfo(inTitle, inBody)
    root.destroy()
    return None