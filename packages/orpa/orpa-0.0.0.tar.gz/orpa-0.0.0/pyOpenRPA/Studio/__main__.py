#Import parent folder to import current / other packages
#########################################################
import sys
lFolderPath = "\\".join(__file__.split("\\")[:-3])
sys.path.insert(0, lFolderPath)
#########################################################
from pyOpenRPA.Robot import Keyboard
from pyOpenRPA.Robot import Clipboard
from pyOpenRPA.Robot import Mouse
from pyOpenRPA.Robot import Screen

from pyOpenRPA.Studio import Studio