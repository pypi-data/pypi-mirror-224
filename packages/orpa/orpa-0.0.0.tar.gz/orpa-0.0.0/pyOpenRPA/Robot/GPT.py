import requests




def Translate(inMessageStr:str, inToLangStr:str, inOrpaKeyStr:str="", inProviderStr:str=""):
    """L+,W+: Отправка запроса на перевод текста

    .. code-block:: python

        # GPT: Взаимодействие с ИИ
        from pyOpenRPA.Robot import GPT
        lResult = GPT.Translate(inMessageStr="Hello world!", inToLangStr="Русский", inProviderStr="openai", inOrpaKeyStr="abcd-efhj-klmn")`
        print(lResult)

    :param inMessageStr: Текст, который необходимо перевести
    :type inMessageStr: str
    :param inToLangStr: Язык перевода текста
    :type inToLangStr: str
    :param inProviderStr: Наименование провайдера
    :type inProviderStr: str
    :param inOrpaKeyStr: Токен для использования ИИ
    :type inOrpaKeyStr: str
    :return: Словарь с ответом от ИИ и дополнительными параметрами (билинг, статус ответа и т.д)
    :rtype: dict
    """
    lData = {"message_str":inMessageStr, "to_lang_str":inToLangStr,"provider_str":inProviderStr, "orpa_key_str":inOrpaKeyStr}
    lResponse = requests.post("https://pyopenrpa.ru/AI/translate", json=lData)
    lResultJson = lResponse.json()
    return lResultJson


def NameModify(inNameStr:str, inCaseStr:str, inOrpaKeyStr:str="", inProviderStr:str=""):
    """L+,W+: Отправка запроса на склонение текста

    .. code-block:: python

        # GPT: Взаимодействие с ИИ
        from pyOpenRPA.Robot import GPT
        lResult = GPT.NameModify(inNameStr="Иванов Иван Иванович", inCaseStr="Родительный", inProviderStr="openai", inOrpaKeyStr="abcd-efhj-klmn")`
        print(lResult)

    :param inNameStr: Имя/Фамилия/Отчество, которое необходимо просклонять
    :type inNameStr: str
    :param inCaseStr: Падеж, в который необходимо просклонять текст из сообщения 
    :type inCaseStr: str
    :param inProviderStr: Наименование провайдера
    :type inProviderStr: str
    :param inOrpaKeyStr: Токен для использования ИИ
    :type inOrpaKeyStr: str
    :return: Словарь с ответом от ИИ и дополнительными параметрами (билинг, статус ответа и т.д)
    :rtype: dict
    """
    lData = {"name_str":inNameStr, "case_str":inCaseStr,"provider_str":inProviderStr, "orpa_key_str":inOrpaKeyStr}
    lResponse = requests.post("https://pyopenrpa.ru/AI/name_modify_ru", json=lData)
    lResultJson = lResponse.json()
    return lResultJson


def ClassifyEmotions(inMessageStr:str, inOrpaKeyStr:str="", inProviderStr:str=""):
    """L+,W+: Отправка запроса на анализ текста по эмоциям

    .. code-block:: python

        # GPT: Взаимодействие с ИИ
        from pyOpenRPA.Robot import GPT
        lResult = GPT.ClassifyEmotions(inMessageList="Привет, как твои дела?", inProviderStr="openai", inOrpaKeyStr="abcd-efhj-klmn")\n`
        print(lResult)

    :param inMessageStr: Текст сообщения, отправляемый в виде запроса к ИИ, который необходимо проанализировать
    :type inMessageStr: str
    :param inProviderStr: Наименование провайдера
    :type inProviderStr: str
    :param inOrpaKeyStr: Токен для использования ИИ
    :type inOrpaKeyStr: str
    :return: Словарь с ответом от ИИ и дополнительными параметрами (билинг, статус ответа и т.д)
    :rtype: dict
    """
    lData = {"message_str":inMessageStr, "provider_str":inProviderStr, "orpa_key_str":inOrpaKeyStr}
    lResponse = requests.post("https://pyopenrpa.ru/AI/classify_emotions", json=lData)
    lResultJson = lResponse.json()
    return lResultJson

def Extract(inMessageStr:str, inExtractList:list, inOrpaKeyStr:str="", inProviderStr:str=""):
    """L+,W+: Отправка запроса на извлечение атрибутов из текста отправляемого сообщения

    .. code-block:: python

        # GPT: Взаимодействие с ИИ
        from pyOpenRPA.Robot import GPT
        lResult = GPT.Extract(inMessageStr="Мне необходимо запустить 10 программных роботов", inExtractList=[{"subject_str":"Количество роботов", "var_str":"robotCount"}], inProviderStr="openai", inOrpaKeyStr="abcd-efhj-klmn")`
        print(lResult)

    :param inMessageStr: Текст сообщения, отправляемый в виде запроса к ИИ
    :type inMessageStr: str
    :param inExtractList: Список атрибутов, которые необходимо извлечь  из сообщения
    :type inExtractList: list
    :param inProviderStr: Наименование провайдера
    :type inProviderStr: str
    :param inOrpaKeyStr: Токен для использования ИИ
    :type inOrpaKeyStr: str
    :return: Словарь с ответом от ИИ и дополнительными параметрами (билинг, статус ответа и т.д)
    :rtype: dict
    """
    # На запрос по извлечению количества мешков из фразы мне нужно 10 мешков всегда разный ответ. Как по типам данных, так и по наполнению одних и тех же типов.
    lData = {"message_str":inMessageStr, "extract_list":inExtractList, "provider_str":inProviderStr, "orpa_key_str":inOrpaKeyStr}
    lResponse = requests.post("https://pyopenrpa.ru/AI/extract", json=lData)
    lResultJson = lResponse.json()
    return lResultJson


def Send(inMessageList:list, inContextList:list, inOrpaKeyStr:str="", inProviderStr:str=""):
    """L+,W+: Отправка прямого запроса к выбранному провайдеру ИИ

    .. code-block:: python

        # GPT: Взаимодействие с ИИ
        from pyOpenRPA.Robot import GPT
        lResult = GPT.Send(inMessageList=["Что такое RPA?"], inContextList=[""], inProviderStr="openai", inOrpaKeyStr="abcd-efhj-klmn")`
        print(lResult)

    :param inMessageList: Текст сообщения, отправляемый в виде запроса к ИИ
    :type inMessageList: list
    :param inContextList: Текст контекста, отправляемый вмсте с сообщением при запросе к ИИ
    :type inContextList: list
    :param inProviderStr: Наименование провайдера
    :type inProviderStr: str
    :param inOrpaKeyStr: Токен для использования ИИ
    :type inOrpaKeyStr: str
    :return: Словарь с ответом от ИИ и дополнительными параметрами (билинг, статус ответа и т.д)
    :rtype: dict
    """
    lData = {"message_list":inMessageList, "context_list":inContextList, "provider_str":inProviderStr, "orpa_key_str":inOrpaKeyStr}
    lResponse = requests.post("https://pyopenrpa.ru/AI/send", json=lData)
    lResultJson = lResponse.json()
    return lResultJson


# sdfjSHGAGFASJsfsadfDsaf