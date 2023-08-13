import time
from pyOpenRPA.Utils import License
from pyOpenRPA.Utils import __define__
import datetime
def Welcome():
    lText="""
###########################################
###########################################
###################    #####   ############
###################    #####   ############
###########   #####    #####   ############
###########   #####    #####   ############
###########   #####    #####   ######   ###
###########   #####    #####   ###    #####
###########   #####    #####       ########
###   #####   #####    #####    ###########
#####    ##   #####    ##    ##############
#######       #####        ################
##########    #####    ####################
############    ###    ####################
##############         ####################
#################      ####################
#########                        ##########
###########################################
###########################################
    """
    print(lText)
    time.sleep(1)
    lText="""
(RUS LANGUAGE) 
**********************************************************************************************
Добро пожаловать в модуль администрирования pyOpenRPA | ORPA!
**********************************************************************************************

pyOpenRPA | ORPA - это открытое и гибридное программное обеспечение класса RPA, которое разработано и зарегистрировано на территории Российской Федерации (Автор Иван Маслов, 2019г.). Все исходные коды доступны неограниченному кругу лиц для просмотра.
Данное ПО позволяет решить любые задачи, относящиеся к классу программной роботизации RPA.

Получить или проверить сертификат, а также ознакомиться с текстом лицензионного соглашения Вы можете по адресу: 
https://pyopenrpa.ru/verification
Операция формирования сертификата является автоматизированной и занимает несколько секунд.

По всем вопросам Вы можете обратиться к правообладателю, контакты см. по адресу: 
https://pyopenrpa.ru/Index/pyOpenRPA_product_service.pdf
Используя ПО pyOpenRPA Вы осознаете свою ответственность в случаях нарушения лицензионного законодательства и совершения неправомерных действий.

ВНИМАНИЕ! НЕЗНАНИЕ ЗАКОНА НЕ ОСВОБОЖДАЕТ ОТ ОТВЕТСТВЕННОСТИ."""
    print(lText)
    time.sleep(1)
    lText=""

def Status():
    print(f":СТАТУС АКТИВАЦИИ:")

    print(f"СЕРТИФИКАТ")
    print(f"Номер: {License.CertificateKeyGet()}")
    print(f"-------------------------------------")
    print(f"ЛИЦЕНЗИЯ")
    print(f"Действует с: {str(datetime.datetime.fromtimestamp(__define__.DEFINE['time_from_float']))}")
    print(f"Действует до: {str(datetime.datetime.fromtimestamp(__define__.DEFINE['time_to_float']))}")
    print(f"Версия pyOpenRPA | ORPA: {__define__.DEFINE['ver_str']}")
    print(f"Онлайн версия: {__define__.DEFINE['is_online_bool']}")
    print(f"Enterprise версия: {__define__.DEFINE['is_ee_bool']}")
    print(f"Техническая информация: {__define__.DEFINE}")
    if __define__.DEFINE['is_online_bool'] == True and __define__.DEFINE['is_ee_bool']:
        print(f"--------------------------------------------------------------------------------------")
        print(f"ВНИМАНИЕ: ТЕКУЩАЯ ВЕРСИЯ PYOPENRPA | ORPA МОЖЕТ ИСПОЛЬЗОВАТЬСЯ ТОЛЬКО В НЕКОММЕРЧЕСКИХ ЦЕЛЯХ")
        print(f"--------------------------------------------------------------------------------------")
        time.sleep(2)
    print()

def CertificateSet():
    print(f":УСТАНОВКА СЕРТИФИКАТА:")
    lCertificateKeyStr = input("Укажите код сертификата:")
    License.CertificateKeySet(inCertificateKeyStr=lCertificateKeyStr)
    print()
    Status()
import os
def LicenseIdFileSave():
    print(f":ЭКСПОРТ ЛИЦЕНЗИИ:")
    lPath = os.path.join(os.path.expanduser("~"), "orpa.id")
    lPathStr = input(f"Укажите путь для сохранения файла идентификатора (по-умолчанию: {lPath}):")
    if lPathStr=="": lPathStr = lPath
    __define__.cert_data_generate(lPathStr)
    print(f"Файл идентификатора сохранен по адресу: {lPathStr}\n Для получения ключа активации необходимо отправить файл идентификатора в центр поддержки клиентов ОПЕН РПА (EMail, Telegram).")
    print("")

def LicenseKeyFileInstall():
    print(f":УСТАНОВКА ЛИЦЕНЗИИ:")
    lPath = os.path.join(os.path.expanduser("~"), "orpa.key")
    lPathStr = input(f"Укажите путь к файлу лицензии (по-умолчанию: {lPath}):")
    if lPathStr=="": lPathStr = lPath
    __define__.cert_install(lPathStr)
    print(f"Файл лицензии успешно установлен.")
    __define__.cert_check()
    Status()
    print(f"Файл лицензии будет подгружен в компоненты pyOpenRPA | ORPA после перезапуска.")
    print("")

def Help():
    print(f":СПИСОК КОМАНД:")
    print(f"0 - Подсказка команд")
    print(f"1 - Статус активации платформы")
    print(f"2 - Сертификат, установить")
    print(f"3 - Лицензия, сформировать идентификатор (файл .id)")
    print(f"4 - Лицензия, установить (файл .key)")
    print()

if __name__ == "__main__":
    mode_str = "1"
    Welcome()
    Help()
    while mode_str!="":
        print("Для справки нажать 0")
        print("Для выхода нажать Enter")
        mode_str = input("Выбрать команду (номер): ")
        print("\n")
        if mode_str == "1": Status()
        elif mode_str == "0": Help()
        elif mode_str == "2": CertificateSet()
        elif mode_str == "3": LicenseIdFileSave()
        elif mode_str == "4": LicenseKeyFileInstall()
        else: Help()