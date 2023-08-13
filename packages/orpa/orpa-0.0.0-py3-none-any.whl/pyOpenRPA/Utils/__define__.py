import time
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
import json
import os
import base64
from pyOpenRPA.Tools import CrossOS
import subprocess
import sys
import pyOpenRPA
import requests
gProgramDataPathStr=""
if CrossOS.IS_WINDOWS_BOOL: gProgramDataPathStr = "C:\\ProgramData"
if CrossOS.IS_LINUX_BOOL: gProgramDataPathStr = os.path.expanduser("~/.config")
gProgramDataPORPathStr = os.path.join(gProgramDataPathStr, "pyOpenRPA")

if not os.path.exists(gProgramDataPORPathStr): os.makedirs(gProgramDataPORPathStr, exist_ok=True)
DEFINE = None
DEFINE_ACCEPTED = False

# ПАКЕТ ДЛЯ ВСТАВКИ В МОДУЛИ
def cert_validate(in_cert_path_str = "orpa.key", in_version_str="1.4.0"):
    l_data = cert_load(in_cert_path_str = in_cert_path_str)
    result = False
    if l_data != None:
      required_fields = ["pc_str", "ver_str", "time_from_float", "time_to_float", "is_ee_bool", "is_online_bool"]
      if all(field in l_data for field in required_fields):
          current_time = time.time()
          if current_time>=l_data["time_from_float"] and current_time<=l_data["time_to_float"] and l_data["ver_str"]==in_version_str and guid()==l_data["pc_str"]:
            result = True
    return result

def version_get():
  l_version_str = pyOpenRPA.__version__
  l_version_str = l_version_str.strip()
  if "v" in l_version_str:
    l_version_str=l_version_str[1:]
    l_version_str = l_version_str.strip()
  return l_version_str

def cert_data_generate(id_path_str="orpa.id"):
    l_version_str = version_get()
    l_data = {
        "pc_str": guid(), 
        "ver_str": l_version_str, 
        "time_from_float": time.time(), 
        "time_to_float": time.time()+32140800, 
        "is_ee_bool": False, 
        "is_online_bool": True
    }
    with open(id_path_str, "w", encoding="utf8") as f: f.write(json.dumps(l_data))
import uuid
import shutil
def cert_install(in_file_path_str="orpa.key"):
  src_file = in_file_path_str
  dst_name_str = str(uuid.uuid4())+".key"
  dst_file = os.path.join(gProgramDataPORPathStr, dst_name_str)
  shutil.copy(src_file, dst_file)


def cert_load(in_cert_path_str = "orpa.key"):
    log = b"LS0tLS1CRUdJTiBSU0EgUFJJVkFURSBLRVktLS0tLQpNSUlFb2dJQkFBS0NBUUVBd1Q0a3ZzcWxtM2xSRFZibyt2SVdWQkk2MkNENXNXZDVQSjF6V3lHRlBMTzVNSlEwCitxOXMzK0VYWGd1NWEvODBNZnJlaGlka1JDQThtbWhtbW51b1BWeERUb3ZvbUhhdWoxVDdrYVRUYXFwd3pHV0MKY29DeHdKaVd2MUMxQWU0T1VDaWNZZ05YRXBLVlA4RmpmZzAxQTI1a3FTVFVZWlRXV01CNlZGL3ZDS29oUXNNRApZVXpHcWo4TWtoTHZYWTl4UmdEOXIyOVNXdWU4Z3ZYTDFOaXdacU1pUVZxRGpVQS9IVzk4MHV4MnBxdGhGRVFNClNKTXdnZmROcWZVak1ZVVlCalg1UDRkT0tCT2RVWEU0K2pBYlpOQUVaU0FaN0JTNkRQT3hpeC9UODdyVnFHYjIKM2FlK0prOXhBS2pZeWFrOEFxY3hScTlmSThCbFZBOUpsdG1WM1FJREFRQUJBb0lCQUNKb1F6aXBjbVZGYTVZWgpkSEJDTEpHWmtWcXNQR2xIQ0VJdnNydDJNM2dFZENQZkw3TzNDb2F1V0cvSlhLR0xGaXNVQlEwVDlIbGcyQW1TCkx6cXdhOXRKRXo3b0VHa2RNS1dhdHhST3Fjb2pRT1JUNnE4aWxRTzY1NVIyOVZPN3BGYkhkRmpMU1hTb0h1VDAKTlJmYm1DWGRRUlVRMXJQdFFXRWFIRzNyaXU4YXM5c0c5UUpib3ZtQ0gvTFRha2p3K3FPcy9ZS1lBRHU2VjRqbgp2bjVnQWpoVXR5RWRUWk8yZUxmSFFVcFBDSnhOL21RVk96eVlLcVB0Y3NFTWZNVmlaR2g0T3dnOFdnZC9vdWMrCnp3b1hUcGl5OVVHWWU2eFNhWkxienZYdjM0K2Nmb2pmZjR2QlNHVkg0bHdjS0cwVXB3ZmVXb0s3YURsck53L0cKV2lmMmFZRUNnWUVBd3JWazNJTHQ4YURHc2dlRm9IUE1uV2hrbWxDVkpuRHFlZHlsbnlLMUdOOUt5dzFUcHlFcwp0ODB3K0JrTmVRK3ZnRWNMZ3FMT0FybWJSYS9FL3lRWnlBUU1jSDdvYXFTU2g3V0VmVEQ0OXdjMUM4cmdaNUpwCnR1b3lxem9wNlh0cDVkV2YyRHE0WnpFdlZFdERiMCtoNjNzOWk5TWhScWVVdW80bWg1b1ZjVDBDZ1lFQS9oS2cKUzZjTXBMUVB2YlJGWHB6K0Y3VDlMVGFyODNOS0lJSUs4ekZJaTVDVkpOdXhhdDVKY2FIOHo2MXN3ajBoOHJPbQpIUU1XYnd3clcwK0YvWEdLODgzWXo4SE1BcVhOS0lBdHkvcVJ3VG0rNkVTbWoyMnlLcDU2aExXWWxDZEdOS2lBCmJMdGJMNVpwTW5NaGIxUTZFK2JLNzJIVW9QZlQvWXdTQU93RHdTRUNnWUJCYXZhWFMvb3IrNnVtZHZhRGdVU1gKQWxNQ3NkNWF5d2RNcUVDUkpmVVloVFU0NGFKZ2ZibnJpeXBQd1FNUTBKOVRod3NyK2cwalJ6OE8rODVCTnR6ZQpvZFdZR2x0Mk1STDJPNXRuQUlRMVl4dUVlY1pKcGh5VWt6MHc0RnJpa2s5ekpBSVBnVE1ob0puWlJXeER3c3FSCk5wZm9HYWlOZDVKMTEzckVocFY3dFFLQmdDSnVBYnpld1U3Y2U3bVlZVUltQWlUU1NQREVsTjZqdytyTjFKQUsKSUt1UkJ6VDhkSGxuOEFudkNxUlYrd1FEWnNOTjV2Zk5nRS9DRldvRlI4SUZqZS9sK0RpSEtZOCtTcVB2WXNWZQppanZtQ0dIUFU4Ymg5Wi9pNC9WeDZtQkJSamxDa0V5cnd2cWE1bHlJejRJWHB0c2xqbUNNSUZWRDREMWVxdDNuCkhjY2hBb0dBRmpCUFlnSkNRc3dwdmsxUi9SN2h0NS9nckVYRGd2eWdoRFRCeDd1anozZkdiZG1GblIyLytpSmgKa3NWZ3QwaUNLaCt0SjFtN1NPVUZGWVpzRllYS1pCcVBqMDVQUjR2Rk5xLzh5MVAyeGlJVzVIdy9MdG4zOXRIdwpDMFNXdGZJOXBmSjcyT3dUNUNvN1pRajdTYk1BSWIyT05EcGY5d1IwSlNYY1FqZHE1ZTQ9Ci0tLS0tRU5EIFJTQSBQUklWQVRFIEtFWS0tLS0t"
    decipher = PKCS1_OAEP.new(RSA.importKey(base64.b64decode(log)))
    message = None
    try:
      with open(in_cert_path_str, "rb") as f: message = f.read()
      return json.loads(decipher.decrypt(message).decode())
    except: return None
    
def cert_find_load(in_folder_path_str=None):
  orpa_ver_str = version_get()
  if in_folder_path_str is None: in_folder_path_str = gProgramDataPORPathStr
  file_list = os.listdir(os.path.abspath(in_folder_path_str))
  for file_item in file_list:
     file_path_str = os.path.join(in_folder_path_str, file_item)
     if file_path_str.endswith(".key"):
        if cert_validate(file_path_str, orpa_ver_str):
           return cert_load(file_path_str)
  return {
        "pc_str": guid(), 
        "ver_str": orpa_ver_str, 
        "time_from_float": time.time(), 
        "time_to_float": time.time()+32140800, 
        "is_ee_bool": False, 
        "is_online_bool": True
    }

def cert_check():
  global DEFINE
  global DEFINE_ACCEPTED
  DEFINE = cert_find_load()
  DEFINE_ACCEPTED = False
  if DEFINE["is_online_bool"]==True and is_online(): DEFINE_ACCEPTED=True
  if DEFINE["is_online_bool"]==False: DEFINE_ACCEPTED=True
  if CrossOS.IS_WINDOWS_BOOL:
    from pyOpenRPA.Robot import Window
    if DEFINE_ACCEPTED==False: Window.DialogYesNo(inTitle="pyOpenRPA | ORPA лицензирование", inBody="Уважаемый пользователь! Платформа ORPA была запущена в режиме CE (Community Edition), в базовом случае для неё требуется доступ в сеть интернет. Если Вы хотите использовать ORPA CE или EE версии без доступа в интернет, пожалуйста обратитесь в центр поддержки пользователей ООО ОПЕН РПА. \n\nКонтакты: \nтелеграм: @pyOpenRPA_Support, \nпочта: Support@pyOpenRPA.ru, \nтелефон: +7 995 233 45 31. \n\nПопробуйте повторить попытку при наличии соединения с сетью интернет.")
  else:
    if DEFINE_ACCEPTED==False: 
      print("pyOpenRPA | ORPA лицензирование")
      print("Уважаемый пользователь!")
      print("Платформа ORPA была запущена в режиме CE (Community Edition)")
      print("В базовом случае для неё требуется доступ в сеть интернет. Если Вы хотите использовать ORPA CE или EE версии без доступа в интернет, пожалуйста обратитесь в центр поддержки пользователей ООО ОПЕН РПА. \n\nКонтакты: \nтелеграм: @pyOpenRPA_Support, \nпочта: Support@pyOpenRPA.ru, \nтелефон: +7 995 233 45 31. \n\nПопробуйте повторить попытку при наличии соединения с сетью интернет.")

def is_online():
    try:
      ret = requests.get("https://pyopenrpa.ru", verify=True)
      if ret.status_code==200: return True
      else: return False
    except Exception as e:
      return False

def run(cmd):
  try:
    return subprocess.run(cmd, shell=True, capture_output=True, check=True, encoding="utf-8") \
                     .stdout \
                     .strip()
  except:
    return None

def guid():
  if sys.platform == 'darwin':
    return run(
      "ioreg -d2 -c IOPlatformExpertDevice | awk -F\\\" '/IOPlatformUUID/{print $(NF-1)}'",
    )
  if sys.platform == 'win32' or sys.platform == 'cygwin' or sys.platform == 'msys':
    return run('wmic csproduct get uuid').split('\n')[2] \
                                         .strip()
  if sys.platform.startswith('linux'):
    return run('cat /var/lib/dbus/machine-id') or \
           run('cat /etc/machine-id')
  if sys.platform.startswith('openbsd') or sys.platform.startswith('freebsd'):
    return run('cat /etc/hostid') or \
           run('kenv -q smbios.system.uuid')
cert_check()