$('#orpa-mouse-function-select')
    .dropdown()
;

$('#orpa-keyboard-function-select')
    .dropdown()
;

$(document).ready(function() {
    
    var l_result_cv2_bool = orpa_api_activity_list_execute_sync("importlib.util.find_spec",["cv2"])
    if (JSON.parse(l_result_cv2_bool) == null) {
        $('#orpa-screen-accuracy-img-locate').prop('disabled', true);
        $('#orpa-screen-accuracy-img-locate').val('1.0');
    }
        var l_response_data = null
        ///Загрузка локации project
        $.ajax({
            type: "POST",
            url: '/api/orpa-screen-img-tree-location-path',
            success: function(in_data)
              {
                  l_response_data = in_data
              },
            async:false,
        });
        $('#orpa-mouse-screen-dir-location').val(l_response_data)
        orpa_screen_dir_render()


    orpa_keyboard_do_variants_update()
})


orpa_before_action_focus = function(in_selector, in_selector_type, in_wait_time) {
    var l_result_list = ""
    if (in_selector != ""){
        if (in_selector_type == "UIO") {
            in_selector = JSON.parse('['+in_selector+']')
        }
        var l_arg_list = in_selector
        var l_activity_name_str = "pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight"
        l_result_list = orpa_api_activity_list_execute_sync(l_activity_name_str, l_arg_list, null)
        // Проверка на возможную ошибку (для ShowModal)
        if (l_result_list.includes("ErrorTraceback")==true) {l_result_list=JSON.parse(l_result_list)}
    }
    var l_arg_list_2 = [parseFloat(in_wait_time)]
    orpa_api_activity_list_execute_sync("time.sleep", l_arg_list_2, null)
    return l_result_list
}

//  РАЗДЕЛ КЛАВИАТУРА & БУФЕР -- ORPA-KEYBOARD -- НАЧАЛО 

orpa_keyboard_do_function = function () {
    //Фокус и ожидание перед выполнение функции
    var l_selector = $('.orpa-before-action-focus-keyboard').val()
    var l_wait_time = parseFloat($('.ui.tag.label.teal.tiny.noselect.keyboard-wait-time').html().substring(0,3))
    var l_selector_type = $('.ui.tag.label.teal.tiny.noselect.keyboard-selector-type').html()
    /// СФОРМИРОВАТЬ ACTIVITY LIST
    var activity_list = []
    if (l_selector != ""){
        if (l_selector_type == "UIO") {
            l_selector = JSON.parse(l_selector)
        }
        activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight", "ArgList":[l_selector], "ArgDict":{}})
    }
    activity_list.push({"Def":"time.sleep", "ArgList":[l_wait_time], "ArgDict":{}})
    //Основная функция (Keyboard.Down/Up/Send/Wait)
    var l_activity_name_str = "pyOpenRPA.Robot.Keyboard."+document.getElementsByName('orpa-keyboard-action')[0].value
    var l_KeyInt = $('#orpa-keyboard-hotkey-symbol').val()
    var l_arg_dict = {"inKeyInt":l_KeyInt}
    activity_list.push({"Def":l_activity_name_str, "ArgList":null, "ArgDict":l_arg_dict})

    var callback = function(response) {

    }
    orpa_api_activity_list_execute_async_json_many(callback, activity_list)
}

orpa_keyboard_do_write_function = function() {
    //Фокус и ожидание перед выполнение функции
    var l_selector = $('.orpa-before-action-focus-keyboard').val()
    var l_wait_time = parseFloat($('.ui.tag.label.teal.tiny.noselect.keyboard-wait-time').html().substring(0,3))
    var l_selector_type = $('.ui.tag.label.teal.tiny.noselect.keyboard-selector-type').html()
    /// СФОРМИРОВАТЬ ACTIVITY LIST
    var activity_list = []
    if (l_selector != ""){
        if (l_selector_type == "UIO") {
            l_selector = JSON.parse(l_selector)
        }
        activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight", "ArgList":[l_selector], "ArgDict":{}})
    }
    activity_list.push({"Def":"time.sleep", "ArgList":[l_wait_time], "ArgDict":{}})
    //Основная функция (Keyboard.Write)
    var l_activity_name_str = "pyOpenRPA.Robot.Keyboard.Write"
    var l_text = $('.orpa-keyboard-write-data').val()
    var l_arg_dict = {"inTextStr":l_text}
    activity_list.push({"Def":l_activity_name_str, "ArgList":null, "ArgDict":l_arg_dict})

    var callback = function(response) {

    }
    orpa_api_activity_list_execute_async_json_many(callback, activity_list)
}

orpa_keyboard_do_function_hotkey = function() {

    //Фокус и ожидание перед выполнение функции
    var l_selector = $('.orpa-before-action-focus-keyboard').val()
    var l_wait_time = parseFloat($('.ui.tag.label.teal.tiny.noselect.keyboard-wait-time').html().substring(0,3))
    var l_selector_type = $('.ui.tag.label.teal.tiny.noselect.keyboard-selector-type').html()
    /// СФОРМИРОВАТЬ ACTIVITY LIST
    var activity_list = []
    if (l_selector != ""){
        if (l_selector_type == "UIO") {
            l_selector = JSON.parse(l_selector)
        }
        activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight", "ArgList":[l_selector], "ArgDict":{}})
    }
    activity_list.push({"Def":"time.sleep", "ArgList":[l_wait_time], "ArgDict":{}})
    //Основная функция (Keyboard.HotkeyCombination)
    var l_activity_name_str = "pyOpenRPA.Robot.Keyboard.HotkeyCombination"
    var l_special_symbol_list = document.getElementsByClassName('ui tag label teal tiny noselect keyboard-hotkey')
    var l_special_symbol_str = ""
    var l_arg_list = []
    for (var j=0;j<l_special_symbol_list.length; j++) {
        l_special_symbol_str = l_special_symbol_list[j].innerHTML
        l_arg_list.push(l_special_symbol_str)
    }
    var l_common_symbol_int = $('#orpa-keyboard-hotkey-symbol').val()
    if (l_common_symbol_int!="") {
        l_arg_list.push(l_common_symbol_int)
    }
    activity_list.push({"Def":l_activity_name_str, "ArgList":l_arg_list, "ArgDict":null})

    var callback = function(response) {

    }
    orpa_api_activity_list_execute_async_json_many(callback, activity_list)
}



orpa_keyboard_do_variants_update = function () {
    // КЕЙС, если идет прогрузка методов / свойств UI объекта
    var callback=function(in_data) {
        html=""
        for (var j=0;j<in_data.length; j++) {
            value = in_data[j]
            html+="<span style=\"color:blue;cursor:pointer;\" onclick=\"document.getElementById('orpa-keyboard-hotkey-symbol').value = '"+value+"'\">"+value+"</span>"
        }
        document.getElementById("orpa-keyboard-hotkey-symbol-variants").innerHTML=html
    }
    var callback2=function(in_data) {
        input = document.getElementById("orpa-keyboard-hotkey-symbol")
        if (in_data == null) {
            input.style['background-color'] = "#ee2a918a";
        } else {
            input.style['background-color'] = "#2aeead8a";
        }
        document.getElementById("orpa-keyboard-hotkey-symbol-variants").innerHTML=html
    }
    var l_common_symbol_int = $('#orpa-keyboard-hotkey-symbol').val()
    if (l_common_symbol_int != "") {
        orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.Keyboard.KeyVariants", [l_common_symbol_int])
        orpa_api_activity_list_execute_async_json(callback2, "pyOpenRPA.Robot.Keyboard.Key2Code", [l_common_symbol_int])
    } else {
        input = document.getElementById("orpa-keyboard-hotkey-symbol")
        input.style['background-color'] = "";
        document.getElementById("orpa-keyboard-hotkey-symbol-variants").innerHTML=""
    }
}

 
orpa_keyboard_clipboard_get = function() {
    var l_activity_name_str = "pyOpenRPA.Robot.Clipboard.Get"
    var l_result = orpa_api_activity_list_execute_sync(l_activity_name_str, null, null)
    $('#orpa-keyboard-clipboard-textarea').val(l_result.slice(0,-1).substring(1))
}

orpa_keyboard_clipboard_set = function() {
    var l_activity_name_str = "pyOpenRPA.Robot.Clipboard.Set"
    var l_text_area_str = $('#orpa-keyboard-clipboard-textarea').val()
    var l_arg_list = [l_text_area_str]
    orpa_api_activity_list_execute_sync(l_activity_name_str, l_arg_list, null)
}

//  РАЗДЕЛ КЛАВИАТУРА & БУФЕР -- ORPA-KEYBOARD -- КОНЕЦ 

//  РАЗДЕЛ МЫШЬ & ЭКРАН -- ORPA-MOUSE -- НАЧАЛО 
// Функция по отрисовке дерева файлов внутри "Локации"
orpa_screen_dir_render = function() {
    var l_path = $('#orpa-mouse-screen-dir-location').val()
    var l_data_dict = {
        "Path": l_path,
      }
    var l_response_data=null
    ///Загрузка данных
    $.ajax({
      type: "POST",
      url: '/api/orpa-screen-img-tree',
      data: JSON.stringify(l_data_dict),
      success: function(in_data)
        {
            l_response_data = JSON.parse(in_data)
        },
      dataType: "text",
      async:false,
    });
    var l_img_tree = $('.ui.list.img.tree')
    l_img_tree.css({"backgroundColor":"white"})
    var l_html_str = ''
    // Если пришла строка - то ошибка в поиске директории
    if ("ErrorTraceback" in l_response_data == true) {
        mGlobal.ShowModal(l_response_data["ErrorHeader"], l_response_data["ErrorTraceback"])
    }
    // Иначе - отрисовываем содержимое (только файлы)
    else {
        for (var j=0;j<l_response_data.length; j++) {
            l_html_str += `<div class="orpa-screen-img-dir-item-conteiner">
            <div class="img-tree-item-${j}" onclick="orpa_api_snipingtool_screenshot_render($('.img-tree-item-${j}'))">${l_response_data[j]}</div>
            <span class="orpa-screen-img-tree-item-action" onclick="orpa_api_img_tree_item_detect($('.img-tree-item-${j}'))">Распознать</span>&emsp;
            <span class="orpa-screen-img-tree-item-action" onclick="orpa_mouse_image_do_function($('.img-tree-item-${j}'))">Найти</span>&emsp;
            <span class="orpa-screen-img-tree-item-action" onclick="orpa_api_img_tree_item_rename($('.img-tree-item-${j}'))">Переименовать</span>&emsp;
            <span class="orpa-screen-img-tree-item-action" onclick="orpa_api_img_tree_item_delete($('.img-tree-item-${j}'))">Удалить</span></div>`
        } 
    }
    l_img_tree.html(l_html_str)
    var l_date = new Date()
    $('#orpa-mouse-screen-save-location').val(`${l_date.getMonth()}_${l_date.getDate()}__${l_date.getHours()}_${l_date.getMinutes()}_${l_date.getSeconds()}.png`)
}

// Инициация snipingtool (ножницы)
orpa_screen_sniping_tool = function() {
    var l_path = $('#orpa-mouse-screen-dir-location').val() + "\\" + $('#orpa-mouse-screen-save-location').val()
    //Фокус и ожидание перед выполнение функции
    var l_selector = $('.orpa-before-action-focus-screen').val()
    var l_wait_time = parseFloat($('.ui.tag.label.teal.tiny.noselect.screen-wait-time').html().substring(0,3))
    var l_selector_type = $('.ui.tag.label.teal.tiny.noselect.screen-selector-type').html()
    var activity_list=[]
    if (l_selector != ""){
        if (l_selector_type == "UIO") {
            l_selector = JSON.parse('['+l_selector+']')
        }
        activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight","ArgList":[l_selector], "ArgDict":{}})

    }
    var l_arg_dict = {"inPath":l_path}
    var callback=function(){
        orpa_screen_dir_render()
    }
    
    activity_list.push({"Def":"time.sleep","ArgList":[l_wait_time], "ArgDict":{}})
    activity_list.push({"Def":"pyOpenRPA.Robot.Screen.InitSnipingTool", "ArgList":null, "ArgDict":l_arg_dict})
    orpa_api_activity_list_execute_async_json_many(callback, activity_list)
}

// Реализация предпросмотра
orpa_api_snipingtool_screenshot_render = function (in_filename) {
    var l_path = $('#orpa-mouse-screen-dir-location').val() + "\\" + in_filename.html()
    var l_data_dict = {
      "Path": l_path,
    }
    var l_response_data=null
    ///Загрузка данных
    $.ajax({
      type: "POST",
      url: '/api/snipingtool-screenshot-render',
      data: JSON.stringify(l_data_dict),
      success: function()
        {
            var l_rnd = Math.floor(Math.random() * 100)
            if ($('#orpa-mouse-screen-img').length==0) {
                var img = "<img id='orpa-mouse-screen-img' src='http://127.0.0.1:8081/api/snipingtool-screenshot-render' style='height:258px;width:100%;object-fit:contain;'>";
                $('.orpa-placeholder-img-preview').html(img);
                $('#orpa-screen-render-filename').html(`ПРЕДПРОСМОТР - ${in_filename.html()}`)
            }
            else {
                $('#orpa-mouse-screen-img').attr("src",`http://127.0.0.1:8081/api/snipingtool-screenshot-render?${l_rnd}`)
                $('#orpa-screen-render-filename').html(`ПРЕДПРОСМОТР - ${in_filename.html()}`)
            }
        },
      dataType: "text",
      async:false,
    });
    return l_response_data
}

// Распознование текста на картинке
orpa_mouse_image_path_str = null
orpa_api_img_tree_item_detect = function(in_filename){
    var l_path = $('#orpa-mouse-screen-dir-location').val() + "\\" + in_filename.html()
    $('#orpa-screen-teseract-location').val(l_path)
    orpa_mouse_image_path_str = l_path
}

// Удаление файлов из img tree
orpa_api_img_tree_item_delete = function(in_filename){
    var l_path = $('#orpa-mouse-screen-dir-location').val() + "\\" + in_filename.html()
    var l_data_dict = {
      "Path": l_path,
    }
    var l_response_data=null
    ///Загрузка данных
    $.ajax({
      type: "POST",
      url: '/api/orpa-screen-img-tree-item-delete',
      data: JSON.stringify(l_data_dict),
      success: function(in_data)
        {
            l_response_data = JSON.parse(in_data)
        },
      dataType: "text",
      async:false,
    });
    if ( l_response_data==null ) {
        orpa_screen_dir_render()
    }
    // Если пришла строка - то ошибка в поиске директории
    else if ("ErrorTraceback" in l_response_data == true) {
        mGlobal.ShowModal(l_response_data["ErrorHeader"],l_response_data["ErrorTraceback"])
    }
}

// Нахождение картинки из img tree
orpa_mouse_image_do_function = function(in_filename) {
    var l_path = $('#orpa-mouse-screen-dir-location').val() + "\\" + in_filename.html()
    orpa_mouse_image_path_str = l_path
    //Фокус и ожидание перед выполнение функции
    var l_selector = $('.orpa-before-action-focus-screen').val() 
    var l_wait_time = parseFloat($('.ui.tag.label.teal.tiny.noselect.screen-wait-time').html().substring(0,3))
    var l_selector_type = $('.ui.tag.label.teal.tiny.noselect.screen-selector-type').html()
    var activity_list=[]
    if (l_selector != ""){
        if (l_selector_type == "UIO") {
            l_selector = JSON.parse('['+l_selector+']')
        }
        activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight","ArgList":[l_selector], "ArgDict":{}})
    }
    var l_arg_dict = {"inPath":l_path}
    var callback=function(response){
        var l_result = response[response.length-1]
        // Отрисовка результата
        var l_html_str = ""
        var l_sut_str = $('#orpa-screen-sut-img-locate').val()
        if (l_sut_str.length != 2) {mGlobal.ShowModal("Неверно задано символьное указание точки (СУТ)","")}
        else {
            if (l_result.length>0) {
                $(".orpa-placeholder-locate-result").css({"backgroundColor":"white"})
            }
            for (var j=0;j<l_result.length; j++) {
                l_render_data = l_result[j]
                l_html_str += `<div class="orpa-screen-locate-result-conteiner" onclick="orpa_screen_location_args_fill($('.orpa-screen-locate-result-coord-x-${j}').attr('value'),$('.orpa-screen-locate-result-coord-y-${j}').attr('value'))">
                <div class="orpa-screen-locate-result-${j}" style="font-size: 14px"><b>Область ${j}</b></div>
                <span class="orpa-screen-locate-result-coord-x-${j}" value="${l_render_data.left}" style="font-size: 12px">X: ${l_render_data.left}</span>&emsp;
                <span class="orpa-screen-locate-result-coord-y-${j}" value="${l_render_data.top}" style="font-size: 12px">Y: ${l_render_data.top}</span>&emsp;
                <span class="orpa-screen-locate-result-coord-w-${j}" value="${l_render_data.width}" style="font-size: 12px">W: ${l_render_data.width}</span>&emsp;
                <span class="orpa-screen-locate-result-coord-h-${j}" value="${l_render_data.height}" style="font-size: 12px">H: ${l_render_data.height}</span>&emsp;
                <i style="margin-left:10px;display:inline-block"class="code icon teal" onclick="orpa_mouse_detect_point_copy(${j});orpa_utils_popup_show(this, 'Код Python скопирован в буфер обмена! Для вставки используйте комбинацию клавиш Ctrl+V');"></i></div>`
            }
        }
        $(".orpa-placeholder-locate-result").html(l_html_str)
    }
    activity_list.push({"Def":"time.sleep","ArgList":[l_wait_time], "ArgDict":{}})
    // Учет точности, если установлен cv2
    if ($('#orpa-screen-accuracy-img-locate').is(':disabled') == true) {
        var l_arg_dict = {"inImgPathStr":l_path}
    }
    else {
        var l_confidence_float = parseFloat($('#orpa-screen-accuracy-img-locate').val())
        var l_arg_dict = {"inImgPathStr":l_path, "inConfidenceFloat":l_confidence_float}
    }
    activity_list.push({"Def":"pyOpenRPA.Robot.Screen.ImageLocateAllInfo", "ArgList":null, "ArgDict":l_arg_dict})
    if (l_selector!="") {activity_list.push({"Def":"pyOpenRPA.Robot.Keyboard.HotkeyCombination", "ArgList":["ALT", "TAB"], "ArgDict":null})}
    
    orpa_api_activity_list_execute_async_json_many(callback, activity_list)
}

// Переименовка из img tree
orpa_api_img_tree_item_rename = function(in_filename) {
    var l_path = $('#orpa-mouse-screen-dir-location').val() + "\\" + in_filename.html()
    var l_new_filename = prompt("Введите новое имя файла", '')
    if (l_new_filename==null) {l_new_filename=in_filename.html()}
    var l_new_path = $('#orpa-mouse-screen-dir-location').val() + "\\" + l_new_filename
    var l_data_dict = {
        "Path": l_path,
        "NewPath": l_new_path
      }
    var l_response_data=null
    ///Загрузка данных
    $.ajax({
      type: "POST",
      url: '/api/orpa-screen-img-tree-item-rename',
      data: JSON.stringify(l_data_dict),
      success: function(in_data)
        {
            l_response_data = JSON.parse(in_data)
        },
      dataType: "text",
      async:false,
    });
    if ( l_response_data==null ) {
        orpa_screen_dir_render()
    }
    else if ("ErrorTraceback" in l_response_data == true) {
        mGlobal.ShowModal(l_response_data["ErrorHeader"],l_response_data["ErrorTraceback"])
    }
}

// Вывод результатов LocateAll
orpa_screen_location_args_fill = function(x,y) {
    var l_arg_list = `[${x},${y}]`
    $('#mouse-argument-dataset').val(l_arg_list)
}

// Инициация функций модуля Mouse
orpa_mouse_do_function = function() {
    //Фокус и ожидание перед выполнение функции
    var l_selector = $('.orpa-before-action-focus-screen').val()
    var l_wait_time = $('.ui.tag.label.teal.tiny.noselect.screen-wait-time').html().substring(0,3)
    var l_selector_type = $('.ui.tag.label.teal.tiny.noselect.screen-selector-type').html()
    var l_result_activity = orpa_before_action_focus(l_selector, l_selector_type, l_wait_time)
    // Mouse function
    if (typeof(l_result_activity)=="object") {
        mGlobal.ShowModal(l_result_activity["ErrorHeader"],l_result_activity["ErrorTraceback"])
    }
    else {
        var l_activity_name_str = "pyOpenRPA.Robot.Mouse."+document.getElementsByName('orpa-mouse-action')[0].value
        var l_arg_type_list = $('.ui.tag.label.teal.tiny.noselect.mouse-arg-type')
        var l_arg_type_str = ""
        if (l_arg_type_list.html() == "СПИСОК") {l_arg_type_str = "list"}
        else {l_arg_type_str = "dict"}
    
        if (l_arg_type_str == "list") {
            var l_arg_list = $('#mouse-argument-dataset').val().replace("[","").replace("]","").split(",")
            for (var j=0;j<l_arg_list.length; j++) {
                l_arg_list[j] = parseInt(l_arg_list[j])
            } 
            orpa_api_activity_list_execute_async(null,l_activity_name_str, l_arg_list, null)
        }
        else if (l_arg_type_str == "dict") {
            var l_arg_dict = JSON.parse($('#mouse-argument-dataset').val())
            orpa_api_activity_list_execute_async(null,l_activity_name_str, null, l_arg_dict)
        }
    }
}

// Реализация просмотра tesseract
orpa_api_tesseract_render = function () {
    var l_path = $('#orpa-screen-teseract-location').val()
    var l_data_dict = {
      "Path": l_path,
    }
    var l_response_data=null
    ///Загрузка данных
    $.ajax({
      type: "POST",
      url: '/api/orpa-screen-tesseract-run',
      data: JSON.stringify(l_data_dict),
      success: function(in_data)
        {
            l_response_data = JSON.parse(in_data)
        },
      dataType: "text",
      async:false,
    });
    if ("ErrorTraceback" in l_response_data == true) {
        mGlobal.ShowModal(l_response_data["ErrorHeader"],l_response_data["ErrorTraceback"])
    }
    else {
        var l_html_str = `<div class="orpa-screen-tesseract-result">${l_response_data[0]}</div>`
        $('.orpa-placeholder-tesseract-result').css({"backgroundColor":"white"});
        $('.orpa-placeholder-tesseract-result').html(l_html_str);
    }

}

// Парсер символьного указания точки
orpa_sut_parse = function(in_sut_str, in_box_list) {
    var l_x_int = null
    var l_y_int = null
    // Вычисление координаты x
    if (in_sut_str[0].toUpperCase() == "C") {l_x_int = parseInt(in_box_list['left']) + parseInt(parseInt(in_box_list['width'])/2)}
    else if (in_sut_str[0].toUpperCase() == "L") {l_x_int = parseInt(in_box_list['left'])}
    else if (in_sut_str[0].toUpperCase() == "R") {l_x_int = parseInt(in_box_list['left']) + parseInt(in_box_list['width'])}
    // Вычисление координаты y
    if (in_sut_str[1].toUpperCase() == "C") {l_y_int = parseInt(in_box_list['top']) + parseInt(parseInt(in_box_list['height'])/2)}
    else if (in_sut_str[1].toUpperCase() == "U") {l_y_int = parseInt(in_box_list['top'])}
    else if (in_sut_str[1].toUpperCase() == "D") {l_y_int = parseInt(in_box_list['top']) + parseInt(in_box_list['height'])}
    return [l_x_int, l_y_int]
}


orpa_mouse_workspace_proportion_set = function (in_col_1, in_col_2, in_col_3) {
    l_class_list = ["one","two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "elewen", "twelve", "thirdteen", "fourteen", "fifthteen", "sixteen"]
    l_object_list = [$("#orpa-mouse-col-1")[0], $("#orpa-mouse-col-2")[0], $("#orpa-mouse-col-3")[0]] 
    l_object_col_list =[in_col_1, in_col_2, in_col_3]
    for (var j=0;j<l_object_list.length; j++) {
      for (var i=0;i<l_class_list.length; i++) {
        l_class = l_class_list[i]
        
        if (l_object_list[j].classList.contains(l_class)) {
          l_object_list[j].classList.remove(l_class)
          l_object_list[j].classList.remove("wide")
          l_object_list[j].classList.remove("column")
        }
      }
      l_object_list[j].classList.add(l_object_col_list[j])
      l_object_list[j].classList.add("wide")
      l_object_list[j].classList.add("column")
    }
  }

  //  РАЗДЕЛ МЫШЬ & ЭКРАН -- ORPA-MOUSE -- КОНЕЦ 
  
//   !!! Функции по копированию кода !!!
// Копирование функций блока СИМВОЛ
orpa_keyboard_do_function_copy = function() {
    var l_func_name_str = document.getElementsByName('orpa-keyboard-action')[0].value
    if (l_func_name_str == "") {l_func_name_str="Send"}
    var l_common_symbol_int = $('#orpa-keyboard-hotkey-symbol').val()
    if (l_common_symbol_int == "") {
        l_common_symbol_int = "A"
    }
    var l_text_area_str = `from pyOpenRPA.Robot import Keyboard\nKeyboard.${l_func_name_str}("`+l_common_symbol_int+`")`
    clipboard_set(l_text_area_str)
}

orpa_keyboard_symbol_function_copy = function() {
    var l_text_area_str = '"'+document.getElementById('orpa-keyboard-hotkey-symbol').value+'"'
    clipboard_set(l_text_area_str)
}

// Копирование функций блока ГОРЯЧИЕ КЛАВИШИ
orpa_keyboard_do_function_hotkey_copy = function() {
    var l_func_name_str = "HotkeyCombination"
    var l_special_symbol_list = document.getElementsByClassName('ui tag label teal tiny noselect keyboard-hotkey')
    var key_list_str = ""
    for (var j=0;j<l_special_symbol_list.length; j++) {
        if (key_list_str.length>0) {key_list_str+=", "}
        var l_special_symbol_str = l_special_symbol_list[j].innerHTML
        key_list_str+="\""+l_special_symbol_str+"\""
    }
    var l_common_symbol_int = $('#orpa-keyboard-hotkey-symbol').val()
    if (l_common_symbol_int != "") {
        if (key_list_str.length>0) {key_list_str+=", "}
        key_list_str+="\""+l_common_symbol_int+"\""
    }
    
    var l_text_area_str = `from pyOpenRPA.Robot import Keyboard\nKeyboard.${l_func_name_str}(`+key_list_str+`)`
    clipboard_set(l_text_area_str)
}

// Копирование функций блока ТЕКСТ
orpa_keyboard_do_write_function_copy = function() {
    var l_func_name_str = "Write"
    var l_text = $('.orpa-keyboard-write-data').val()
    if (l_text == "") {l_text = "Hello World!"}
    var l_text_area_str = `from pyOpenRPA.Robot import Keyboard\nKeyboard.${l_func_name_str}('${l_text}')`
    clipboard_set(l_text_area_str)
}

// Копирование функции Clipboard.Get
orpa_keyboard_clipboard_get_copy = function() {
    var l_func_name_str = "Get"
    var l_text_area_str = `from pyOpenRPA.Robot import Clipboard\nlClipStr = Clipboard.${l_func_name_str}()`
    clipboard_set(l_text_area_str)
}

// Копирование функции Clipboard.Set
orpa_keyboard_clipboard_set_copy = function() {
    var l_func_name_str = "Set"
    var l_copy_body_str = $('#orpa-keyboard-clipboard-textarea').val()
    if (l_copy_body_str == ""){l_copy_body_str="Hello World!"}
    var l_text_area_str = `from pyOpenRPA.Robot import Clipboard\nlClipStr = Clipboard.${l_func_name_str}('${l_copy_body_str}')`
    clipboard_set(l_text_area_str)
}

// Копирование функции InitSnipingTool
orpa_screen_sniping_tool_copy = function() {
    var l_func_name_str = "InitSnipingTool"
    var l_path = $('#orpa-mouse-screen-dir-location').val().replaceAll("\\","\\\\") + "\\\\" + $('#orpa-mouse-screen-save-location').val().replaceAll("\\","\\\\")
    var l_text_area_str = `from pyOpenRPA.Robot import Screen\nScreen.${l_func_name_str}('${l_path}')`
    clipboard_set(l_text_area_str)
}

// Копирование функций модуля Mouse
orpa_mouse_detect_copy = function() {
    if (orpa_range_value_get("orpa-mouse-source")=="file") {
        var l_text_area_str = `# __________  БЛОК ВЗАИМОДЕЙСТВИЯ С ИЗОБРАЖЕНИЕМ\n`
        l_text_area_str += `from pyOpenRPA.Robot import Screen\n`
        l_text_area_str += `BoxList = Screen.ImageLocateAll(r"`+orpa_mouse_image_path_str+`")\n`
        l_text_area_str += `if len(BoxList) > 0: #ОБЛАСТИ НА ЭКРАНЕ ОБНАРУЖЕНЫ - ПЕРЕЙТИ К ДЕЙСТВИЮ\n`
        l_text_area_str += `    for Box in BoxList:\n`
        l_text_area_str += `        #СФОРМИРОВАТЬ ТОЧКУ (Point)\n`
        l_text_area_str += `        RuleStr = "CC+10+10"\n`
        l_text_area_str += `        Point = Screen.PointFromBox(Box, RuleStr)\n`
        l_text_area_str += `        #РАСКОММЕНТИРОВАТЬ ТРЕБУЕМОЕ ДЕЙСТВИЕ\n`
        l_text_area_str += `        #Screen.PointClick(inPoint = Point, inClickCountInt=1, inIntervalSecFloat=0.0, inButtonStr='left') # Клик кнопки мыши\n`
        l_text_area_str += `        #Screen.PointMoveTo(inPoint = Point, inWaitAfterSecFloat=0.0) # Переместить курсор мыши\n`
        l_text_area_str += `        #Screen.PointDown(inPoint = Point, inButtonStr='left', inWaitAfterSecFloat=0.0) # Опустить кнопку мыши\n`
        l_text_area_str += `        #Screen.PointUp(inPoint = Point, inButtonStr='left', inWaitAfterSecFloat=0.0) # Поднять кнопку мыши\n`
        l_text_area_str += `else: #ОБЛАСТИ ИЗОБРАЖЕНИЯ НА ЭКРАНЕ НЕ ОБНАРУЖЕНЫ - ВЫПОЛНИТЬ АЛЬТЕРНАТИВНЫЙ АЛГОРИТМ\n`
        l_text_area_str += `    print("Изображение не обнаружено")\n`
        clipboard_set(l_text_area_str)
    
    } else {
        // ВЕТКА ЗАГРУЗКИ КАРТИНКИ В BASE64 СТРОКУ
        var l_arg_dict = {"inImgPathStr": orpa_mouse_image_path_str, "inLimitBytesInt": 50000}
        var activity_list = []
        activity_list.push({"Def":"pyOpenRPA.Robot.Screen.ImageToBase64", "ArgList":null, "ArgDict":l_arg_dict})

        var callback = function(response) {
            var l_image_base64_str = response[0]
            var l_text_area_str = `# __________  БЛОК ВЗАИМОДЕЙСТВИЯ С ИЗОБРАЖЕНИЕМ\n`
            l_text_area_str += `from pyOpenRPA.Robot import Screen\n`
            l_text_area_str += `ImgBase64Str = r"`+l_image_base64_str+`"\n`
            l_text_area_str += `BoxList = Screen.ImageLocateAll(ImgBase64Str)\n`
            l_text_area_str += `if len(BoxList) > 0: #ОБЛАСТИ НА ЭКРАНЕ ОБНАРУЖЕНЫ - ПЕРЕЙТИ К ДЕЙСТВИЮ\n`
            l_text_area_str += `    for Box in BoxList:\n`
            l_text_area_str += `        #СФОРМИРОВАТЬ ТОЧКУ (Point)\n`
            l_text_area_str += `        RuleStr = "CC+10+10"\n`
            l_text_area_str += `        Point = Screen.PointFromBox(Box, RuleStr)\n`
            l_text_area_str += `        #РАСКОММЕНТИРОВАТЬ ТРЕБУЕМОЕ ДЕЙСТВИЕ\n`
            l_text_area_str += `        #Screen.PointClick(inPoint = Point, inClickCountInt=1, inIntervalSecFloat=0.0, inButtonStr='left') # Клик кнопки мыши\n`
            l_text_area_str += `        #Screen.PointMoveTo(inPoint = Point, inWaitAfterSecFloat=0.0) # Переместить курсор мыши\n`
            l_text_area_str += `        #Screen.PointDown(inPoint = Point, inButtonStr='left', inWaitAfterSecFloat=0.0) # Опустить кнопку мыши\n`
            l_text_area_str += `        #Screen.PointUp(inPoint = Point, inButtonStr='left', inWaitAfterSecFloat=0.0) # Поднять кнопку мыши\n`
            l_text_area_str += `else: #ОБЛАСТИ ИЗОБРАЖЕНИЯ НА ЭКРАНЕ НЕ ОБНАРУЖЕНЫ - ВЫПОЛНИТЬ АЛЬТЕРНАТИВНЫЙ АЛГОРИТМ\n`
            l_text_area_str += `    print("Изображение не обнаружено")\n`
            clipboard_set(l_text_area_str)
        }
        orpa_api_activity_list_execute_async_json_many(callback, activity_list)
    }
}

// Генерация кода распознавания
orpa_mouse_recognize_copy = function() {
    var file_path_str = document.getElementById("orpa-screen-teseract-location").value
    if (orpa_range_value_get("orpa-mouse-source")=="file") {
        var l_text_area_str = `# __________  БЛОК РАСПОЗНАВАНИЯ ИЗОБРАЖЕНИЯ\n`
        l_text_area_str += `import pytesseract\n`
        l_text_area_str += `#pytesseract.pytesseract.tesseract_cmd = r'C:\\path\\to\\tesseract.exe'\n`
        l_text_area_str += `#ДЛЯ WINDOWS СМ. ФАЙЛ ORPA\\Resources\\WTesseract64-400\\tesseract.exe\n`
        l_text_area_str += `lRecognizedStr = Screen.ImageRecognize(r"`+file_path_str+`", inLangStr='rus+eng')\n`
        clipboard_set(l_text_area_str)
    
    } else {
        // ВЕТКА ЗАГРУЗКИ КАРТИНКИ В BASE64 СТРОКУ
        var l_arg_dict = {"inImgPathStr": file_path_str, "inLimitBytesInt": 50000}
        var activity_list = []
        activity_list.push({"Def":"pyOpenRPA.Robot.Screen.ImageToBase64", "ArgList":null, "ArgDict":l_arg_dict})

        var callback = function(response) {
            var l_image_base64_str = response[0]
            var l_text_area_str = `# __________  БЛОК РАСПОЗНАВАНИЯ ИЗОБРАЖЕНИЯ\n`
            l_text_area_str += `from pyOpenRPA.Robot import Screen\n`
            l_text_area_str += `#pytesseract.pytesseract.tesseract_cmd = r'C:\\path\\to\\tesseract.exe'\n`
            l_text_area_str += `#ДЛЯ WINDOWS СМ. ФАЙЛ ORPA\\Resources\\WTesseract64-400\\tesseract.exe\n`
            l_text_area_str += `ImgBase64Str = r"`+l_image_base64_str+`"\n`
            l_text_area_str += `lRecognizedStr = Screen.ImageRecognize(ImgBase64Str, inLangStr='rus+eng')\n`
            clipboard_set(l_text_area_str)
        }
        orpa_api_activity_list_execute_async_json_many(callback, activity_list)
    }
}

orpa_mouse_detect_point_copy = function(index=null) {
    if (orpa_range_value_get("orpa-mouse-source")=="file") {
        var l_text_area_str = `# __________  БЛОК ВЗАИМОДЕЙСТВИЯ С ИЗОБРАЖЕНИЕМ\n`
        l_text_area_str += `from pyOpenRPA.Robot import Screen\n`
        l_text_area_str += `BoxList = Screen.ImageLocateAll(r"`+orpa_mouse_image_path_str+`")\n`
        l_text_area_str += `if len(BoxList) > 0: #ОБЛАСТИ НА ЭКРАНЕ ОБНАРУЖЕНЫ - ПЕРЕЙТИ К ДЕЙСТВИЮ\n`
        l_text_area_str += `    for Box in BoxList:\n`
        l_text_area_str += `        #СФОРМИРОВАТЬ ТОЧКУ (Point)\n`
        l_text_area_str += `        RuleStr = "CC+10+10"\n`
        l_text_area_str += `        Point = Screen.PointFromBox(Box, RuleStr)\n`
        l_text_area_str += `        #РАСКОММЕНТИРОВАТЬ ТРЕБУЕМОЕ ДЕЙСТВИЕ\n`
        l_text_area_str += `        #Screen.PointClick(inPoint = Point, inClickCountInt=1, inIntervalSecFloat=0.0, inButtonStr='left') # Клик кнопки мыши\n`
        l_text_area_str += `        #Screen.PointMoveTo(inPoint = Point, inWaitAfterSecFloat=0.0) # Переместить курсор мыши\n`
        l_text_area_str += `        #Screen.PointDown(inPoint = Point, inButtonStr='left', inWaitAfterSecFloat=0.0) # Опустить кнопку мыши\n`
        l_text_area_str += `        #Screen.PointUp(inPoint = Point, inButtonStr='left', inWaitAfterSecFloat=0.0) # Поднять кнопку мыши\n`
        l_text_area_str += `else: #ОБЛАСТИ ИЗОБРАЖЕНИЯ НА ЭКРАНЕ НЕ ОБНАРУЖЕНЫ - ВЫПОЛНИТЬ АЛЬТЕРНАТИВНЫЙ АЛГОРИТМ\n`
        l_text_area_str += `    print("Изображение не обнаружено")\n`
        clipboard_set(l_text_area_str)
    
    } else {
        // ВЕТКА ЗАГРУЗКИ КАРТИНКИ В BASE64 СТРОКУ
        var l_arg_dict = {"inImgPathStr": orpa_mouse_image_path_str, "inLimitBytesInt": 50000}
        var activity_list = []
        activity_list.push({"Def":"pyOpenRPA.Robot.Screen.ImageToBase64", "ArgList":null, "ArgDict":l_arg_dict})

        var callback = function(response) {
            var l_image_base64_str = response[0]
            var l_text_area_str = `# __________  БЛОК ВЗАИМОДЕЙСТВИЯ С ИЗОБРАЖЕНИЕМ\n`
            l_text_area_str += `from pyOpenRPA.Robot import Screen\n`
            l_text_area_str += `ImgBase64Str = r"`+l_image_base64_str+`"\n`
            l_text_area_str += `BoxList = Screen.ImageLocateAll(ImgBase64Str)\n`
            l_text_area_str += `if len(BoxList) > 0: #ОБЛАСТИ НА ЭКРАНЕ ОБНАРУЖЕНЫ - ПЕРЕЙТИ К ДЕЙСТВИЮ\n`
            l_text_area_str += `    Box = BoxList[`+index+`]\n`
            l_text_area_str += `    #СФОРМИРОВАТЬ ТОЧКУ (Point)\n`
            l_text_area_str += `    RuleStr = "CC+10+10"\n`
            l_text_area_str += `    Point = Screen.PointFromBox(Box, RuleStr)\n`
            l_text_area_str += `    #РАСКОММЕНТИРОВАТЬ ТРЕБУЕМОЕ ДЕЙСТВИЕ\n`
            l_text_area_str += `    #Screen.PointClick(inPoint = Point, inClickCountInt=1, inIntervalSecFloat=0.0, inButtonStr='left') # Клик кнопки мыши\n`
            l_text_area_str += `    #Screen.PointMoveTo(inPoint = Point, inWaitAfterSecFloat=0.0) # Переместить курсор мыши\n`
            l_text_area_str += `    #Screen.PointDown(inPoint = Point, inButtonStr='left', inWaitAfterSecFloat=0.0) # Опустить кнопку мыши\n`
            l_text_area_str += `    #Screen.PointUp(inPoint = Point, inButtonStr='left', inWaitAfterSecFloat=0.0) # Поднять кнопку мыши\n`
            l_text_area_str += `else: #ОБЛАСТИ ИЗОБРАЖЕНИЯ НА ЭКРАНЕ НЕ ОБНАРУЖЕНЫ - ВЫПОЛНИТЬ АЛЬТЕРНАТИВНЫЙ АЛГОРИТМ\n`
            l_text_area_str += `    print("Изображение не обнаружено")\n`
            clipboard_set(l_text_area_str)
        }
        orpa_api_activity_list_execute_async_json_many(callback, activity_list)

    }
}

orpa_mouse_do_function_copy = function() {
    var l_activity_name_str = "pyOpenRPA.Robot.Clipboard.Set"
    var l_func_name_str = document.getElementsByName('orpa-mouse-action')[0].value
    if (l_func_name_str == "") {l_func_name_str="MoveTo"}
    var l_arg_type_list = $('.ui.tag.label.teal.tiny.noselect.mouse-arg-type')
    var l_arg_type_str = ""
    if (l_arg_type_list.html() == "СПИСОК") {l_arg_type_str = "list"}
    else {l_arg_type_str = "dict"}
    if (l_arg_type_str == "list") {
        var l_tmp_arg_list = $('#mouse-argument-dataset').val().replace("[","").replace("]","")
        if (l_tmp_arg_list == "") {
            if (l_func_name_str == "ScrollHorizontal" | l_func_name_str == "ScrollVertical") {l_tmp_arg_list = "250"}
            else {l_tmp_arg_list = "100,100"}
        }
        l_tmp_arg_list = l_tmp_arg_list.split(",")
        for (var j=0;j<l_tmp_arg_list.length; j++) {
            l_tmp_arg_list[j] = parseInt(l_tmp_arg_list[j])
        } 
        var l_text_area_str = `from pyOpenRPA.Robot import Mouse\nMouse.${l_func_name_str}(${l_tmp_arg_list})`
    }
    else if (l_arg_type_str == "dict") {
        var l_tmp_arg_str = $('#mouse-argument-dataset').val().replace(/[{}"]/g, '').replace(/:/g, '=').replace(/,/g, ', ')
        if (l_tmp_arg_str == "") {
            if (l_func_name_str == "ScrollHorizontal" | l_func_name_str == "ScrollVertical") {l_tmp_arg_str = "inScrollClickCountInt=250"}
            else {l_tmp_arg_str = "inXInt=100, inYInt=100"}
        }
        var l_text_area_str = `from pyOpenRPA.Robot import Mouse\nMouse.${l_func_name_str}(${l_tmp_arg_str})`
    }
    var l_arg_list = [l_text_area_str]
    orpa_api_activity_list_execute_sync(l_activity_name_str, l_arg_list, null)
}