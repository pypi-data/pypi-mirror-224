from email import utils
import os
import shutil
from . import CrossOS

def TemplateFolder(inDstPathStr):
    """L+,W+: Сформировать папку (набор папок), если ранее эти папки не существовали

    .. code-block:: python

        from pyOpenRPA.Utils import Disk
        Disk.TemplateFolder(inDstPathStr="path\\to\\folder")

    :param inDstPathStr: Путь к папке, которая должна существовать
    :type inDstPathStr: str
    """
    # проверка наличия всех файлов/каталогов
    if not os.path.exists(os.path.abspath(inDstPathStr)):
        os.makedirs(inDstPathStr, exist_ok=True)

def TemplateFile(inDstPathStr, inTmplPathStr):
    """L+,W+: Сформировать файл (копировать из шаблона), если ранее этот файл не существовал

    .. code-block:: python

        from pyOpenRPA.Utils import Disk
        Disk.TemplateFile(inDstPathStr="path\\to\\destination\\file.txt", inTmplPathStr="path\\to\\template.txt")

    :param inDstPathStr: Путь к файлу, который должен существовать. Если не существует - скопировать из шаблона inTmplPathStr
    :type inDstPathStr: str
    :param inTmplPathStr: Путь к файлу шаблона, который потребуется копировать, если файл inDstPathStr не будет обнаружен
    :type inTmplPathStr: str
    """
    TemplateFolder(inDstPathStr=CrossOS.PathJoinList(inList=CrossOS.PathSplitList(inPathStr=inDstPathStr)[:-1]))
    if os.path.exists(inDstPathStr) == False:
        shutil.copy(inTmplPathStr, inDstPathStr)

CheckFolder = TemplateFolder
CheckFile = TemplateFile