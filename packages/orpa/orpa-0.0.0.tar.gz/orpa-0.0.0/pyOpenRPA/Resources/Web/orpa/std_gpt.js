

orpa_gpt_translate = function() {
    var data_dict = {"message_str":"", "to_lang_str":"", "provider_str":"", "orpa_key_str":""}
    data_dict["message_str"] = $('.orpa-gpt-message').val()
    data_dict["to_lang_str"] = $('#orpa-gpt-translate-to-lang').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html()
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    var func_data = JSON.stringify(data_dict)
    $('#orpa-gpt-history').append(`<div class="ui message warning" style="margin-left:20%; width:80%;margin-bottom: 5px;">
                                        <div class="header">ПОЛЬЗОВАТЕЛЬ (ПЕРЕВОД) <i style="margin-left:10px;display:inline-block"class="code icon teal" onclick='orpa_gpt_translate_history_copy(${func_data}); orpa_utils_popup_show(this, "Код Python скопирован в буфер обмена! Для вставки используйте комбинацию клавиш Ctrl+V");'></i></div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>Переведи следующий текст на ${$('#orpa-gpt-translate-to-lang').val()} язык: <br>${$('.orpa-gpt-message').val()}</p>
                                        </div></div>`)
    $.ajax({
        url: '/api/orpa-gpt-text-translate',         
        method: 'post',  
        data: JSON.stringify(data_dict),          
        dataType: 'html',              
        success: function(data){ 
            response = JSON.parse(data)
            if (response['status_str'] == 'OK_RESPONSE') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (ПЕРЕВОД)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>Ответ на ваш запрос: <br>${response['response']}</p>
                                        <p style="font-style:italic;">ЗАПРОС: ${response['billing_dict']['token_cost_last_request_int']}Т, ОТВЕТ: ${response['billing_dict']['token_cost_last_response_int']}Т, ВРЕМЯ ОТВЕТА: ${response['timing_ai_sec_float']} СЕК.</p>
                                        </div></div>`)
            }
            else if (response['status_str'] == 'NOT_AVAILABLE_TOKEN_WRONG') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (ПЕРЕВОД)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>${response['response']}</p>
                                        </div></div>`)
            
            }
            orpa_history_dump()
        }
    });
}

orpa_gpt_name_modify_ru = function() {
    var data_dict = {"name_str":"", "case_str":"", "provider_str":"", "orpa_key_str":""}
    data_dict["name_str"] = $('.orpa-gpt-message').val()
    data_dict["case_str"] = $('#orpa-gpt-to-modify').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html()
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    var func_data = JSON.stringify(data_dict)
    $('#orpa-gpt-history').append(`<div class="ui message warning" style="margin-left:20%; width:80%;margin-bottom: 5px;">
                                        <div class="header">ПОЛЬЗОВАТЕЛЬ (СКЛОНЕНИЕ) <i style="margin-left:10px;display:inline-block"class="code icon teal" onclick='orpa_gpt_name_modify_ru_history_copy(${func_data}); orpa_utils_popup_show(this, "Код Python скопирован в буфер обмена! Для вставки используйте комбинацию клавиш Ctrl+V");'></i></div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>Поставь <b>${$('.orpa-gpt-message').val()}</b> в ${$('#orpa-gpt-to-modify').val()} падеж</p>
                                        </div></div>`)
    $.ajax({
        url: '/api/orpa-gpt-name-modify-ru',         
        method: 'post',  
        data: JSON.stringify(data_dict),          
        dataType: 'html',              
        success: function(data){ 
            response = JSON.parse(data)
            if (response['status_str'] == 'OK_RESPONSE') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (СКЛОНЕНИЕ)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>Ответ на ваш запрос: <br>${response['response']}</p>
                                        <p style="font-style:italic;">ЗАПРОС: ${response['billing_dict']['token_cost_last_request_int']}Т, ОТВЕТ: ${response['billing_dict']['token_cost_last_response_int']}Т, ВРЕМЯ ОТВЕТА: ${response['timing_ai_sec_float']} СЕК.</p>
                                        </div></div>`)
            } 
            else if (response['status_str'] == 'NOT_AVAILABLE_TOKEN_WRONG') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (СКЛОНЕНИЕ)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>${response['response']}</p>
                                        </div></div>`)
            
            }
            orpa_history_dump()
        }
      });
}

orpa_gpt_classify_emotions = function() {
    var data_dict = {"message_str":"", "provider_str":"", "orpa_key_str":""}
    data_dict["message_str"] = $('.orpa-gpt-message').val()
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html()
    var func_data = JSON.stringify(data_dict)
    $('#orpa-gpt-history').append(`<div class="ui message warning" style="margin-left:20%; width:80%;margin-bottom: 5px;">
                                        <div class="header">ПОЛЬЗОВАТЕЛЬ (АНАЛИЗ ЭМОЦИЙ) <i style="margin-left:10px;display:inline-block"class="code icon teal" onclick='orpa_gpt_classify_emotions_history_copy(${func_data}); orpa_utils_popup_show(this, "Код Python скопирован в буфер обмена! Для вставки используйте комбинацию клавиш Ctrl+V");'></i></div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>Проведи анализ эмоций следующего текста:<br>${$('.orpa-gpt-message').val()}</p>
                                        </div></div>`)
    $.ajax({
        url: '/api/orpa-gpt-text-classify-emotions',         
        method: 'post',  
        data: JSON.stringify(data_dict),          
        dataType: 'html',              
        success: function(data){ 
            response = JSON.parse(data)
            if (response['status_str'] == 'OK_RESPONSE') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (АНАЛИЗ ЭМОЦИЙ)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>Ответ на ваш запрос: <br>Интерес: ${response['response']['interest']}<br>Безразличие: ${response['response']['indifference']}
                                        <br>Удивление: ${response['response']['surprise']}<br>Тревожность: ${response['response']['anxiety']}
                                        <br>Надежда: ${response['response']['hope']}<br>Опасение: ${response['response']['fear']}
                                        <br>Благодарность: ${response['response']['gratitude']}<br>Гнев: ${response['response']['disappointment']}
                                        <br>Удовлетворение: ${response['response']['satisfaction']}<br>Разочарование: ${response['response']['fear']}</p>
                                        <p style="font-style:italic;">ЗАПРОС: ${response['billing_dict']['token_cost_last_request_int']}Т, ОТВЕТ: ${response['billing_dict']['token_cost_last_response_int']}Т, ВРЕМЯ ОТВЕТА: ${response['timing_ai_sec_float']} СЕК.</p>
                                        </div></div>`)
            }
            else if (response['status_str'] == 'NOT_AVAILABLE_TOKEN_WRONG') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (АНАЛИЗ ЭМОЦИЙ)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>${response['response']}</p>
                                        </div></div>`)
            
            }
            orpa_history_dump()
        }
      });
}

orpa_gpt_extract = function() {
    var data_dict = {"message_str":"", "extract_list":[], "provider_str":"", "orpa_key_str":""}
    data_dict["message_str"] = $('.orpa-gpt-message').val()
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html()
    for (let i=0; i < document.getElementsByClassName('orpa-arg-param-variable').length; i++) {
        if (document.getElementsByClassName('orpa-arg-param-variable')[i].value != "") {
            data_dict['extract_list'].push({'subject_str':document.getElementsByClassName('orpa-arg-param-point')[i].value, 'var_str': document.getElementsByClassName('orpa-arg-param-variable')[i].value})
        }
        
    }
    var func_data = JSON.stringify(data_dict)
    $('#orpa-gpt-history').append(`<div class="ui message warning" style="margin-left:20%; width:80%;margin-bottom: 5px;">
                                        <div class="header">ПОЛЬЗОВАТЕЛЬ (ИЗВЛЕЧЕНИЕ АТРИБУТОВ) <i style="margin-left:10px;display:inline-block"class="code icon teal" onclick='orpa_gpt_extract_history_copy(${func_data}); orpa_utils_popup_show(this, "Код Python скопирован в буфер обмена! Для вставки используйте комбинацию клавиш Ctrl+V");'></i></div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>Извлеки атрибуты из следующего текста: <br>${$('.orpa-gpt-message').val()}</p>
                                        </div></div>`)
    $.ajax({
        url: '/api/orpa-gpt-text-extract',         
        method: 'post',  
        data: JSON.stringify(data_dict),          
        dataType: 'html',              
        success: function(data){ 
            response = JSON.parse(data)
            if (response['status_str'] == 'OK_RESPONSE') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (ИЗВЛЕЧЕНИЕ АТРИБУТОВ)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>Ответ на ваш запрос: <br>${response['response']}</p>
                                        <p style="font-style:italic;">ЗАПРОС: ${response['billing_dict']['token_cost_last_request_int']}Т, ОТВЕТ: ${response['billing_dict']['token_cost_last_response_int']}Т, ВРЕМЯ ОТВЕТА: ${response['timing_ai_sec_float']} СЕК.</p>
                                        </div></div>`)
            }
            else if (response['status_str'] == 'NOT_AVAILABLE_TOKEN_WRONG') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (ИЗВЛЕЧЕНИЕ АТРИБУТОВ)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>${response['response']}</p>
                                        </div></div>`)
            
            }
            orpa_history_dump()
        }
      });
}

orpa_gpt_send = function() {
    var data_dict = {"message_list":[], "context_list":[], "provider_str":"", "orpa_key_str":""}
    data_dict["message_list"].push($('.orpa-gpt-message').val())
    data_dict["context_list"].push($('.orpa-gpt-context').val())
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html()
    var func_data = JSON.stringify(data_dict)
    $('#orpa-gpt-history').append(`<div class="ui message warning" style="margin-left:20%; width:80%;margin-bottom: 5px;">
                                        <div class="header">ПОЛЬЗОВАТЕЛЬ (ПРЯМОЙ ЗАПРОС) <i style="margin-left:10px;display:inline-block"class="code icon teal" onclick='orpa_gpt_send_history_copy(${func_data}); orpa_utils_popup_show(this, "Код Python скопирован в буфер обмена! Для вставки используйте комбинацию клавиш Ctrl+V");'></i></div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>${$('.orpa-gpt-message').val()}</p>
                                        </div></div>`)
    $.ajax({
        url: '/api/orpa-gpt-send',         
        method: 'post',  
        data: JSON.stringify(data_dict),          
        dataType: 'html',              
        success: function(data){ 
            response = JSON.parse(data)
            if (response['status_str'] == 'OK_RESPONSE') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (ПРЯМОЙ ЗАПРОС)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>Ответ на ваш запрос: <br>${response['response']}</p>
                                        <p style="font-style:italic;">ЗАПРОС: ${response['billing_dict']['token_cost_last_request_int']}Т, ОТВЕТ: ${response['billing_dict']['token_cost_last_response_int']}Т, ВРЕМЯ ОТВЕТА: ${response['timing_ai_sec_float']} СЕК.</p>
                                        </div></div>`)
            }
            else if (response['status_str'] == 'NOT_AVAILABLE_TOKEN_WRONG') {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">ORPA GPT (ПРЯМОЙ ЗАПРОС)
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        <p>${response['response']}</p>
                                        </div></div>`)
            
            }
            orpa_history_dump()
        }
      });
}



// НАБОР ФУНКЦИЯ ПО КОПИРОВАНИЮ КОДА
orpa_gpt_send_history_copy = function(data_dict) {
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.Send(inMessageList=["${data_dict['message_list']}"], inContextList=["${data_dict['context_list']}"], inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}
orpa_gpt_send_copy = function() {
    var data_dict = {"message_list":[], "context_list":[], "provider_str":"", "orpa_key_str":""}
    data_dict["message_list"].push($('.orpa-gpt-message').val())
    data_dict["context_list"].push($('.orpa-gpt-context').val())
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html()
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.Send(inMessageList=["${data_dict['message_list']}"], inContextList=["${data_dict['context_list']}"], inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}


orpa_gpt_classify_emotions_history_copy = function(data_dict) {
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.ClassifyEmotions(inMessageStr="${data_dict['message_str']}", inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}
orpa_gpt_classify_emotions_copy = function() {
    var data_dict = {"message_str":"", "provider_str":"", "orpa_key_str":""}
    data_dict["message_str"] = $('.orpa-gpt-message').val()
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html() 
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.ClassifyEmotions(inMessageStr="${data_dict['message_str']}", inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}


orpa_gpt_extract_history_copy = function(data_dict) {
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.Extract(inMessageStr="${data_dict['message_str']}", inExtractList=${JSON.stringify(data_dict['extract_list'])}, inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}
orpa_gpt_extract_copy = function() {
    var data_dict = {"message_str":"", "extract_list":[], "provider_str":"", "orpa_key_str":""}
    data_dict["message_str"] = $('.orpa-gpt-message').val()
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html()
    for (let i=0; i < document.getElementsByClassName('orpa-arg-param-variable').length; i++) {
        if (document.getElementsByClassName('orpa-arg-param-variable')[i].value != "") {
            data_dict['extract_list'].push({'subject_str':document.getElementsByClassName('orpa-arg-param-point')[i].value, 'var_str': document.getElementsByClassName('orpa-arg-param-variable')[i].value})
        }
        
    }
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.Extract(inMessageStr="${data_dict['message_str']}", inExtractList=${JSON.stringify(data_dict['extract_list'])}, inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}


orpa_gpt_name_modify_ru_history_copy = function(data_dict) {
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.NameModify(inNameStr="${data_dict['name_str']}", inCaseStr="${data_dict['case_str']}", inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}
orpa_gpt_name_modify_ru_copy = function() {
    var data_dict = {"name_str":"", "case_str":"", "provider_str":"", "orpa_key_str":""}
    data_dict["name_str"] = $('.orpa-gpt-message').val()
    data_dict["case_str"] = $('#orpa-gpt-to-modify').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html()
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.NameModify(inNameStr="${data_dict['name_str']}", inCaseStr="${data_dict['case_str']}", inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}


orpa_gpt_translate_history_copy = function(data_dict) {
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.Translate(inMessageStr="${data_dict['message_str']}", inToLangStr="${data_dict['to_lang_str']}", inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}
orpa_gpt_translate_copy = function() {
    var data_dict = {"message_str":"", "to_lang_str":"", "provider_str":"", "orpa_key_str":""}
    data_dict["message_str"] = $('.orpa-gpt-message').val()
    data_dict["to_lang_str"] = $('#orpa-gpt-translate-to-lang').val()
    data_dict["provider_str"] = $('.ui.tag.label.teal.tiny.noselect[orpa-data-key="orpa-gpt-provider"]').html()
    data_dict["orpa_key_str"] = $('#orpa-gpt-token-init').val()
    var l_text_area_str = `from pyOpenRPA.Robot import GPT\n`
    l_text_area_str += `lResult = GPT.Translate(inMessageStr="${data_dict['message_str']}", inToLangStr="${data_dict['to_lang_str']}", inProviderStr="${data_dict['provider_str'].toLowerCase()}", inOrpaKeyStr="${data_dict['orpa_key_str']}")\n`
    l_text_area_str += `print(lResult)`
    clipboard_set(l_text_area_str)
}







orpa_add_atr_params = function() {
    let i = parseInt(document.getElementsByClassName('orpa-atr-params-subcontainer')[document.getElementsByClassName('orpa-atr-params-subcontainer').length - 1].id) + 1
    $('.orpa-atr-params-container').append(`<div class="orpa-atr-params-subcontainer" id="${i}"><div class="ui input mini" style="width:40%; margin-right: 25px; margin-bottom: 10px;">
                                                <input class="orpa-arg-param-point" type="text" placeholder="Суть">
                                            </div>
                                            <div class="ui input mini" style="width:40%">
                                                <input class="orpa-arg-param-variable" type="text" placeholder="Имя">
                                            </div>
                                            <i style="display:inline-block" class="minus icon teal" onclick="orpa_delete_atr_params('${i}')"></i></div>`)
}

orpa_delete_atr_params = function(element_id_str) {
    if (element_id_str == "1") {
        $(`.orpa-atr-params-subcontainer[id="${element_id_str}"]`).html(`<div class="ui input mini" style="width:40%; margin-right: 25px; margin-bottom: 10px;">
                                                                            <input class="orpa-arg-param-point" type="text" placeholder="Суть">
                                                                        </div>
                                                                        <div class="ui input mini" style="width:40%">
                                                                            <input class="orpa-arg-param-variable" type="text" placeholder="Имя">
                                                                        </div>
                                                                        <i style="display:inline-block" class="minus icon teal" onclick="orpa_delete_atr_params('1')"></i>`)
    }
    else{$(`.orpa-atr-params-subcontainer[id="${element_id_str}"]`).remove()}
}

orpa_history_dump = function() {
    var mes_history_dict = {"gpt":{"header":[],"body":[]},"user":{"header":[],"body":[]}}
    for (let i=0;i<$('.ui.message.info').length; i++) {
        mes_history_dict['gpt']['header'].push($('.ui.message.info').eq(i).children('.header').html())
        mes_history_dict['gpt']['body'].push($('.ui.message.info').eq(i).children('.orpa-gpt-history-message-body').html())
    }
    for (let i=0;i<$('.ui.message.warning').length; i++) {
        mes_history_dict['user']['header'].push($('.ui.message.warning').eq(i).children('.header').html())
        mes_history_dict['user']['body'].push($('.ui.message.warning').eq(i).children('.orpa-gpt-history-message-body').html())
    }
    $.ajax({
        url: '/api/orpa-gpt-history-dump',         
        method: 'post',  
        data: JSON.stringify(mes_history_dict),          
        dataType: 'html',              
        success: function(data){ 
        }
      });
}

orpa_history_load = function() {
    $.ajax({
        url: '/api/orpa-gpt-history-load',         
        method: 'get',           
        dataType: 'html',              
        success: function(data){ 
            response = JSON.parse(data)
            if (response["gpt"]['header'].length > 2) {
                let error_html = `<button style="margin-bottom: 20px; width:15%; margin-top:10px;"  
                                class="ui button icon" onclick="orpa_utils_popup_show(this, 'Превышен размер хранимых данных. Рекомендуется очистить историю запросов.');">
						        <i style="display:inline-block; font-size:18px; cursor: pointer; margin-left:10px;" data="" class="exclamation triangle icon red"></i></button> `
                $('#orpa-gpt-history-clean-button').append(error_html)
            }
            $('#orpa-gpt-history').html('')
            for (let i=0; i<response['gpt']['header'].length;i++) {
                $('#orpa-gpt-history').append(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                        <div class="header">${response['gpt']['header'][i]}
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        ${response['gpt']['body'][i]}
                                        </div></div>`)
                if (response['user']['header'].length > i) {
                    $('#orpa-gpt-history').append(`<div class="ui message warning" style="margin-left:20%; width:80%;margin-bottom: 5px;">
                                        <div class="header">${response['user']['header'][i]}
                                        </div>
                                        <div class="orpa-gpt-history-message-body">
                                        ${response['user']['body'][i]}
                                        </div></div>`)
                }
            }

        }
      });
}
orpa_history_load()

orpa_check_token = function() {
    if ($('#orpa-gpt-token-init').val().length == 0) {
        $('#orpa-gpt-classify-emotions').prop('disabled',true)
        $('#orpa-gpt-history-clean').prop('disabled',true)
        $('#orpa-gpt-translate-run').prop('disabled',true)
        $('#orpa-gpt-name-modify-ru').prop('disabled',true)
        $('#orpa-gpt-extract').prop('disabled',true)
        $('#orpa-gpt-send').prop('disabled',true)
    }
    else {
        $('#orpa-gpt-classify-emotions').prop('disabled',false)
        $('#orpa-gpt-history-clean').prop('disabled',false)
        $('#orpa-gpt-translate-run').prop('disabled',false)
        $('#orpa-gpt-name-modify-ru').prop('disabled',false)
        $('#orpa-gpt-extract').prop('disabled',false)
        $('#orpa-gpt-send').prop('disabled',false)
    }
}
orpa_check_token()
orpa_gpt_history_clean = function(param) {
    $('#orpa-gpt-history').html(`<div class="ui message info" style="width:80%;margin-bottom: 5px;">
                                <div class="header">ORPA GPT (ПРИВЕТСТВИЕ)
                                </div>
                                <div class="orpa-gpt-history-message-body">
                                <p>Добро пожаловать на вкладку "ИНТЕЛЛЕКТ" от ОПЕН РПА. .... Здесь про генератор кода. Где-то сделать примеры запросов...</p>
                                </div></div>`)
    if (param == 1) {orpa_history_dump()}
}
orpa_gpt_history_clean(0)