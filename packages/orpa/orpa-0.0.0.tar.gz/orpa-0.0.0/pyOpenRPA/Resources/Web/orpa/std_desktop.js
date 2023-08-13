$(document)
  .ready(function() {
    ////////////////////////////////////////////////////
    ///////// ORPA DESKTOP SELECTOR НАЧАЛО /////////////////
    ////////////////////////////////////////////////////  

    orpa_desktop_selector_uio_clear=function(in_selector_uio) {
    ///Создать урезанную версию селектора
    lTextAreaSpecificationArray=mGlobal.iSysClone(in_selector_uio,true);
    for (var i = 0; i< lTextAreaSpecificationArray.length; i++) {
        ///Очистить ненужные ключи для выборки
        delete lTextAreaSpecificationArray[i]['rich_text']
        delete lTextAreaSpecificationArray[i]['process_id']
        delete lTextAreaSpecificationArray[i]['rectangle']
        delete lTextAreaSpecificationArray[i]['control_id']
        delete lTextAreaSpecificationArray[i]['process']
        delete lTextAreaSpecificationArray[i]['name']
        delete lTextAreaSpecificationArray[i]['handle']
        delete lTextAreaSpecificationArray[i]['control_type']
        delete lTextAreaSpecificationArray[i]['runtime_id']
        delete lTextAreaSpecificationArray[i]['selector']
        delete lTextAreaSpecificationArray[i]['child_list']
        if (i!=0) {
            delete lTextAreaSpecificationArray[i]['title']
            delete lTextAreaSpecificationArray[i]['class_name']
        }
    }
    return lTextAreaSpecificationArray
    }



    orpa_desktop_selector_range_select = function(in_range) {
    var l_callback=function(in_mode_str) {
        l_range = orpa_range_get("orpa-desktop-selector-type", in_mode_str)
        orpa_range_select(l_range)
    }
    orpa_desktop_selector.mode_set(in_range.getAttribute("orpa-data-value"), l_callback)
    }




    ////////////////////////////////////////////////////
    ///////// ORPA DESKTOP TREE НАЧАЛО /////////////////
    ////////////////////////////////////////////////////
    orpa_desktop_tree = new orpa_utils_tree("orpa-desktop-tree"); 

    orpa_desktop_tree_to_selector = function(in_item=null) {
    if (in_item==null) {
        // Достать выбранный объект
        in_item = $("#orpa-desktop-tree .orpa-utils-list-item-selected")[0].js_dict["selector"]
    } else {
        in_item = in_item["selector"]
    }
    orpa_desktop_selector.uio_set(in_item)
    }

    orpa_desktop_tree_selected_item = null
    orpa_desktop_tree_callback_api = function(in_data) {
    orpa_utils_modal_uio_search_mouse_hide();
    var recursive = function (in_data, parent_item=null) {
    var l_data_list = []
    in_data.forEach((item, index) => {
        //ФОРМИРУЕМ СЕЛЕКТОР
        if ("selector" in item) {
        selector_dict = mGlobal.iSysClone(item.selector,true);
        } else {
        selector_dict=orpa_desktop_selector_uio_clear([item])
        // ЕСЛИ ЕСТЬ РОДИТЕЛЬ
        if (parent_item!=null) {
            selector_dict = mGlobal.iSysClone(parent_item.selector,true);
            if ("ctrl_index" in item) {
            selector_dict.push({"ctrl_index":item.ctrl_index})
            } else {
            selector_dict.push({"ctrl_index":index})
            } 
        }
        item.selector = selector_dict
        }
        //selector_dict.ctrl_index = index // СФОРМИРОВАТЬ СЕЛЕКТОР ДЛЯ ДАЛЬНЕЙШЕЙ ОТРАБОТКИ

        //ОТПРАВЛЯЕМ В ДЕРЕВО
        l_title = item.title
        if (item.title=="") {
        l_title = "Нет заголовка"
        }
        var l_data_item = {
        "title_str": l_title,
        "description_str":`process_id: ${item.process_id}; handle: ${item.handle}; class_name: ${item.class_name}; RECT: L${item.rectangle.left} T${item.rectangle.top} R${item.rectangle.right} B${item.rectangle.bottom}`,
        "action_list":[
            {"_title_str":"ПОДСВЕТИТЬ", "icon_str":"lightbulb", "popup_str":"Выделить цветом UI объект", "callback_click":function(in_object, in_item, in_action){orpa_api_activity_list_execute_async(function(){}, "pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight", [in_item.selector]);}},
            {"_title_str":"ПОИСК МЫШИ", "icon_str":"mouse pointer", "popup_str":"Выполнить поиск вложенного UI объекта с помощью мыши", "callback_click":function(in_object, in_item, in_action){orpa_desktop_tree_selected_item=in_item; orpa_utils_modal_uio_search_mouse_show(); orpa_api_activity_list_execute_async_json(orpa_desktop_tree_callback_api, "pyOpenRPA.Robot.UIDesktop.UIOSelector_SearchChildByMouse_UIOTree", [in_item.selector, 3.0], null)}},
            {"_title_str":"СЕЛЕКТОР", "icon_str":"i cursor" ,"popup_str":"Сформировать селектор для обращения к UI объекту", "callback_click":function(in_object, in_item, in_action){orpa_desktop_tree_to_selector(in_item);}},
            {"_title_str":"РАСКРЫТЬ", "icon_str":"level down alternate", "visible_filter_str": "NO_CHILD", "popup_str":"Отобразить вложенные UI объекты", "callback_click":function(in_object, in_item, in_action){orpa_desktop_tree_selected_item=in_item; orpa_api_activity_list_execute_async_json(orpa_desktop_tree_callback_api, "pyOpenRPA.Robot.UIDesktop.UIOSelector_GetChildList_UIOList", [in_item.selector], null)}},
            {"_title_str":"СВЕРНУТЬ", "icon_str":"level up alternate", "visible_filter_str": "HAS_CHILD", "popup_str":"Свернуть вложенные UI объекты","callback_click":function(in_object, in_item, in_action){in_item.child_list=[]; orpa_desktop_tree.render();}},
        ],
        "callback_selected": function(in_object, in_item) {orpa_desktop_level_load_levels(in_object, in_item);},
        "is_unselect_block_bool": true,
        "selector": selector_dict
        }
        
        //ОБРАБОТКА ДЕТЕЙ
        if ("child_list" in item) {
        l_data_item["child_list"] = recursive(item.child_list, item)
        }
        l_data_list.push(l_data_item)
    });
    return l_data_list
    }
    l_data_list = recursive(in_data, orpa_desktop_tree_selected_item)
    if (orpa_desktop_tree_selected_item!=null) {
    orpa_desktop_tree_selected_item['child_list']=l_data_list
    orpa_desktop_tree_selected_item = null
    } else {
    orpa_desktop_tree.load(l_data_list)
    }
    orpa_desktop_tree.render()
    orpa_desktop_tree.loader_turn_off();
    }
    orpa_desktop_tree_refresh=function() {
    backend_str = orpa_range_value_get("orpa-desktop-framework")
    orpa_desktop_tree.loader_turn_on();
    orpa_api_activity_list_execute_async_json(orpa_desktop_tree_callback_api, "pyOpenRPA.Robot.UIDesktop.UIOSelector_GetChildList_UIOList", null, {inBackend: backend_str})

    }
    orpa_desktop_tree_refresh()
    orpa_desktop_tree_search=function() {
    var search_value_str = document.getElementById("orpa-desktop-tree-search-value").value
    var search_type_str = orpa_range_value_get("orpa-desktop-tree-search")
    var backend_str = orpa_range_value_get("orpa-desktop-framework")
    orpa_desktop_tree.loader_turn_on();
    orpa_api_activity_list_execute_async_json(orpa_desktop_tree_callback_api, "pyOpenRPA.Robot.UIDesktop.UIO_Search_UIOTree", [search_value_str, search_type_str, null, null, backend_str], null)
    }
    ////////////////////////////////////////////////////
    ///////// ORPA DESKTOP TREE КОНЕЦ /////////////////
    ////////////////////////////////////////////////////

    ////////////////////////////////////////////////////
    ///////// ORPA DESKTOP LEVEL НАЧАЛО /////////////////
    ////////////////////////////////////////////////////
    orpa_desktop_level = new orpa_utils_tree("orpa-desktop-level"); 
    orpa_desktop_level.mode_set("LIST")
    orpa_desktop_level_load_levels=function(in_object, in_item) {
    var callback=function(in_data) {
    var l_data_list=[]
    in_data.forEach((item, index) => {           
        //selector_dict.ctrl_index = index // СФОРМИРОВАТЬ СЕЛЕКТОР ДЛЯ ДАЛЬНЕЙШЕЙ ОТРАБОТКИ
        //ОТПРАВЛЯЕМ В ДЕРЕВО
        l_data_list.push(
        {
            "icon_str": "dot circle",
            "title_str": "Уровень "+index+": "+item.title,
            "description_str":`process_id: ${item.process_id}; handle: ${item.handle}; class_name: ${item.class_name}; RECT: L${item.rectangle.left} T${item.rectangle.top} R${item.rectangle.right} B${item.rectangle.bottom}`,
            "action_list":[],
            "callback_selected": function(in_object, in_item) {orpa_desktop_property_load(in_item);},
            "server_item": item,
            "level_int": index,
            "is_unselect_block_bool": true
        }
        )
    });
    l_data_list.slice(-1)[0].is_selected_bool=true
    orpa_desktop_level.load(l_data_list)
    orpa_desktop_level.render()
    orpa_desktop_level.loader_turn_off();
    orpa_desktop_property_load(l_data_list.slice(-1)[0])
    }

    orpa_desktop_levels(in_item.selector, callback);
    }

    ////////////////////////////////////////////////////
    ///////// ORPA DESKTOP LEVEL КОНЕЦ /////////////////
    ////////////////////////////////////////////////////

    ////////////////////////////////////////////////////
    ///////// ORPA DESKTOP PROPERTY НАЧАЛО /////////////////
    ////////////////////////////////////////////////////
    var orpa_desktop_property_limit_len = 120
    orpa_desktop_property = new orpa_utils_tree("orpa-desktop-property"); 
    orpa_desktop_property.mode_set("LIST")

    orpa_desktop_property_load=function(in_item) {
    var l_data_list = []
    var const_ignore={"rectangle":true}
    for (let key in in_item.server_item) {
    if (key in const_ignore) {
        // В списке игнорирования
    } else {
        let str = in_item.server_item[key];
        let str_render = str
        if (typeof str === "string") {
        if (str.length > orpa_desktop_property_limit_len) {
            str_render = str.slice(0, orpa_desktop_property_limit_len) + "...";
        }
        }
        if (str === "" || str == null) {
        str_render = "Отсутствует"
        }
        l_icon_str = "circle outline"
        if (orpa_desktop_selector.attribute_exists(in_item.level_int, key)) {
        l_icon_str = "circle"
        }
        l_data_list.push(
        {
            "icon_str": l_icon_str,
            "title_str": key+": ",
            "title_right_str": String(str_render),
            "description_str":"",
            "action_list":[],
            "callback_selected": function(in_object, in_item) {in_item.icon_str="circle"; orpa_desktop_selector.attribute_set(in_item.level_int,key, str); orpa_desktop_property.render();},
            "callback_unselected": function(in_object, in_item) {in_item.icon_str="circle outline"; orpa_desktop_selector.attribute_remove(in_item.level_int,key); orpa_desktop_property.render();},

            "level_int": in_item.level_int

        }
        )
    }

    }
    // ДОБАВИТЬ ИНФО ПРО МНОГОУРОВНЕВЫЙ ПОИСК DEPTH
    l_icon_str = "circle outline"
    if (orpa_desktop_selector.attribute_exists(in_item.level_int, "depth_end")) {
    l_icon_str = "circle"
    }
    l_data_list.push(
    {
        "icon_str": l_icon_str,
        "title_str": "depth: ",
        "title_right_str": String("Многоуровневый поиск"),
        "description_str":"",
        "action_list":[],
        "callback_selected": function(in_object, in_item) {in_item.icon_str="circle"; orpa_desktop_selector.attribute_set(in_item.level_int,"depth_start", 1);orpa_desktop_selector.attribute_set(in_item.level_int,"depth_end", 99); orpa_desktop_property.render();},
        "callback_unselected": function(in_object, in_item) {in_item.icon_str="circle outline"; orpa_desktop_selector.attribute_remove(in_item.level_int,"depth_start");orpa_desktop_selector.attribute_remove(in_item.level_int,"depth_end"); orpa_desktop_property.render();},

        "level_int": in_item.level_int

    }
    )
    orpa_desktop_property.load(l_data_list)
    orpa_desktop_property.render()
    orpa_desktop_property.loader_turn_off();
    }

    // ORPA DESKTOP ACTION



    ///Выполнить действие
    orpa_desktop_action_load_by_selector = function (in_selector_uio) {

    var action_type_str = orpa_range_value_get("orpa-desktop-action-type")
    if (action_type_str=="OBJECT") {
    //Установить свойство disabled на textarea
    document.getElementById("orpa-desktop-action-arg-textarea").removeAttribute("disabled")
    document.getElementById("orpa-desktop-action-args-title").style.removeProperty('display');
    document.getElementById("orpa-desktop-action-help-title").style.setProperty("display","none")
    document.getElementById("orpa-desktop-action-arg-textarea").style.setProperty("height","93px")
    document.getElementById("orpa-desktop-action-button-focus-run").style.removeProperty("display")
    document.getElementById("orpa-desktop-action-button-run").style.removeProperty("display")
    // КЕЙС, если идет прогрузка методов / свойств UI объекта
    var callback=function(in_data) {
        var lDataKeyList=in_data
        var lValueList=[]
        for (var i = 0; i< lDataKeyList.length;i++) {
            if (lDataKeyList[i].length>0)
                if (lDataKeyList[i][0]!="_")
                    lValueList.push({'name':lDataKeyList[i],'value':lDataKeyList[i]})
        }
        ///Установка значений в dropdown
        $('.ui.dropdown.gui-action')
        .dropdown({
            values: lValueList,
            onChange: orpa_desktop_action_helper_load
        })
        ;
    }
    orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIDesktop.UIOSelector_Get_UIOActivityList", [in_selector_uio])

    } else {
    // КЕЙС, если ВЫБРАН МОДУЛЬ UI Desktop

    //Установить свойство disabled на textarea
    document.getElementById("orpa-desktop-action-arg-textarea").setAttribute("disabled","")
    document.getElementById("orpa-desktop-action-help-title").style.removeProperty('display');
    document.getElementById("orpa-desktop-action-args-title").style.setProperty("display","none")
    document.getElementById("orpa-desktop-action-arg-textarea").style.setProperty("height","101px")
    document.getElementById("orpa-desktop-action-button-focus-run").style.setProperty("display","none")
    document.getElementById("orpa-desktop-action-button-run").style.setProperty("display","none")
    var lValueList=[]
    for (let key in orpa_desktop_action_dict) {
        var item = orpa_desktop_action_dict[key]
        lValueList.push({'name':key,'value':key})
    }
    ///Установка значений в dropdown
    $('.ui.dropdown.gui-action')
        .dropdown({
        values: lValueList,
        onChange: orpa_desktop_action_module_code_generator
        })
    ;
    }
    }

    orpa_desktop_action_args_render=function() {
    var arg_type_str = orpa_range_value_get("orpa-desktop-action-arg-type")
    var arg_textarea = document.getElementById("orpa-desktop-action-arg-textarea")
    if (arg_type_str=="LIST") {
    arg_textarea.setAttribute("placeholder", "[\"Привет\", \"Мир\"]")
    if (orpa_desktop_action_helper_list_str!=null) {
        orpa_desktop_action_helper_render_function()
        arg_textarea.value=orpa_desktop_action_helper_list_str
    } else {
        orpa_desktop_action_helper_render_property()
        arg_textarea.value="Выбранное наименование является свойством. Нажмите 'Выполнить', чтобы просмотреть его содержимое"
    }
    } else {
    arg_textarea.setAttribute("placeholder", "{\"key1\":\"Привет\", \"key2\":\"Мир\"}")
    if (orpa_desktop_action_helper_dict_str!=null) {
        orpa_desktop_action_helper_render_function()
        arg_textarea.value=orpa_desktop_action_helper_dict_str
    } else {
        orpa_desktop_action_helper_render_property()
        arg_textarea.value="Выбранное наименование является свойством. Нажмите 'Выполнить', чтобы просмотреть его содержимое"
    }
    }
    }
    orpa_desktop_action_helper_save=function() {
    var arg_type_str = orpa_range_value_get("orpa-desktop-action-arg-type")
    var arg_textarea = document.getElementById("orpa-desktop-action-arg-textarea")
    if (arg_type_str=="LIST") {
    orpa_desktop_action_helper_list_str=arg_textarea.value
    } else {
    orpa_desktop_action_helper_dict_str=arg_textarea.value
    }
    }
    orpa_desktop_action_helper_render_function = function() {
    orpa_desktop_action_helper_is_function = true
    //Установить свойство disabled на textarea
    document.getElementById("orpa-desktop-action-arg-textarea").removeAttribute("disabled")
    document.getElementById("orpa-desktop-action-args-title").style.removeProperty('display');
    document.getElementById("orpa-desktop-action-help-title").style.setProperty("display","none")
    document.getElementById("orpa-desktop-action-arg-textarea").style.setProperty("height","93px")
    document.getElementById("orpa-desktop-action-button-focus-run").style.removeProperty("display")
    }

    orpa_desktop_action_helper_render_property = function () {
    orpa_desktop_action_helper_is_function = false
    //Установить свойство disabled на textarea
    document.getElementById("orpa-desktop-action-arg-textarea").setAttribute("disabled","")
    document.getElementById("orpa-desktop-action-help-title").style.removeProperty('display');
    document.getElementById("orpa-desktop-action-args-title").style.setProperty("display","none")
    document.getElementById("orpa-desktop-action-arg-textarea").style.setProperty("height","101px")
    document.getElementById("orpa-desktop-action-button-focus-run").style.setProperty("display","none")
    }

    orpa_desktop_action_helper_dict_str = null
    orpa_desktop_action_helper_list_str = null
    orpa_desktop_action_helper_is_function = null
    orpa_desktop_action_helper_load=function(in_value) {
    var callback=function(in_data) {
        var arg_type_str = orpa_range_value_get("orpa-desktop-action-arg-type")
        var arg_textarea = document.getElementById("orpa-desktop-action-arg-textarea")
        if (arg_type_str=="LIST") {
        orpa_desktop_action_helper_dict_str = null
        if (in_data["ArgList"]==null) {
            orpa_desktop_action_helper_list_str=null
        } else {
            orpa_desktop_action_helper_list_str=JSON.stringify(in_data["ArgList"])
        }
        } else {
        orpa_desktop_action_helper_list_str = null
        if (in_data["ArgDict"]==null) {
            orpa_desktop_action_helper_dict_str=null
        } else {
            orpa_desktop_action_helper_dict_str=JSON.stringify(in_data["ArgDict"])
        }
        }
        orpa_desktop_action_args_render()
    }
    orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIDesktop.UIOSelectorUIOActivity_Get_ArgDict", [orpa_desktop_selector.uio_get(), in_value])

    }

    orpa_desktop_action_module_code_generator=function(in_value) {
    if (in_value!="") {
    var code_str = orpa_desktop_action_dict[in_value].code_str
    var help_str = orpa_desktop_action_dict[in_value].help_str
    document.getElementById("orpa-desktop-action-arg-textarea").value=help_str
    code_str = code_str.replace("<SELECTOR>", JSON.stringify(orpa_desktop_selector.uio_get()));
    clipboard_set(code_str)
    }

    }

    orpa_desktop_action_run=function(in_ui_focus_bool=true) {
    var callback=function(in_data) {
    var result_textarea = document.getElementById("orpa-desktop-action-result")
    var data = in_data[in_data.length - 1]
    if (data==null) {
        result_textarea.innerHTML="Значение null / None"
    } else {
        result_textarea.innerHTML=JSON.stringify(data)
    }
    result_textarea.classList.remove("orpa-placeholder");
    }
    var arg_type_str = orpa_range_value_get("orpa-desktop-action-arg-type")
    var arg_textarea = document.getElementById("orpa-desktop-action-arg-textarea")
    var uio = orpa_desktop_selector.uio_get()
    var action_str = $("#orpa-desktop-action-def-input").dropdown("get value")
    var activity_list = []
    var textarea_value = arg_textarea.value
    if (orpa_desktop_action_helper_is_function==true) {
    if (textarea_value!="" && textarea_value!=null) {
        textarea_value=JSON.parse(textarea_value)
    } else {
        if (arg_type_str=="LIST") {
        textarea_value=[]
        } else {
        textarea_value={}
        }
    }
    } else {
    textarea_value=""
    }
    if (in_ui_focus_bool==true) {
    activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight", "ArgList":[uio], "ArgDict":{}})
    }
    if (arg_type_str=="LIST") {
    activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelectorUIOActivity_Run_Dict", "ArgList":[uio, action_str, true, textarea_value], "ArgDict":{}})
    } else {
    activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelectorUIOActivity_Run_Dict", "ArgList":[uio, action_str, true, null, textarea_value], "ArgDict":{}})
    }

    orpa_api_activity_list_execute_async_json_many(callback, activity_list)
    }




    ////////////////////////////////////////////////////
    ///////// ORPA DESKTOP PROPERTY КОНЕЦ /////////////////
    ////////////////////////////////////////////////////
    // ORPA DESKTOP MEMORY
    orpa_desktop_memory_slot_dict = {}

    orpa_desktop_memory_switch=function(in_new_item) {
    key_old_str = orpa_range_value_get("orpa-desktop-memory-slot")
    orpa_desktop_memory_save(key_old_str)
    orpa_range_select(in_new_item);
    key_new_str = orpa_range_value_get("orpa-desktop-memory-slot")
    orpa_desktop_memory_restore(key_new_str)
    }

    orpa_desktop_memory_save= function(in_slot_key) {
    orpa_desktop_memory_slot_dict[in_slot_key]={}
    slot_dict = orpa_desktop_memory_slot_dict[in_slot_key]
    slot_dict["tree"]=orpa_desktop_tree.data_list
    slot_dict["tree_mode"]=orpa_desktop_tree.mode
    slot_dict["level"]=orpa_desktop_level.data_list
    slot_dict["property"]=orpa_desktop_property.data_list
    slot_dict["selector"]=orpa_desktop_selector.uio_get()
    slot_dict["action"]=orpa_desktop_action.data_get()
    slot_dict["action-result"]=document.getElementById("orpa-desktop-action-result").innerHTML

    }
    orpa_desktop_memory_restore = function (in_slot_key) {
    if (in_slot_key in orpa_desktop_memory_slot_dict) {
    slot_dict = orpa_desktop_memory_slot_dict[in_slot_key]
    orpa_desktop_tree.load(slot_dict.tree)
    orpa_desktop_tree.mode_set(slot_dict.tree_mode)
    orpa_desktop_level.load(slot_dict.level)
    orpa_desktop_property.load(slot_dict.property)
    orpa_desktop_selector.uio_set(slot_dict["selector"])
    orpa_desktop_action.data_load(slot_dict["action"])
    document.getElementById("orpa-desktop-action-result").innerHTML=slot_dict["action-result"]
    if (slot_dict["action-result"]!="") {
        document.getElementById("orpa-desktop-action-result").classList.remove("orpa-placeholder");
    } else {
        document.getElementById("orpa-desktop-action-result").classList.add("orpa-placeholder");
    }

    } else {
    orpa_desktop_tree_refresh()
    orpa_desktop_tree.mode_set("TREE")
    orpa_desktop_level.clear()
    orpa_desktop_property.clear()
    orpa_desktop_selector.clear()
    orpa_desktop_action.clear()
    document.getElementById("orpa-desktop-action-result").innerHTML=""
    document.getElementById("orpa-desktop-action-result").classList.add("orpa-placeholder");
    }
    }
    orpa_desktop_memory_clear = function(in_slot_key) {

    }
    orpa_desktop_selector_search_list = function() {
        var uio_selector = orpa_desktop_selector.uio_get()
        if (uio_selector != null) {
            var in_callback=function(in_data) {
                for (var i = 0; i< in_data.length;i++) {
                var item_selector = mGlobal.iSysClone(uio_selector, true)
                item_selector[item_selector.length - 1]["ctrl_index"]=i;
                in_data[i].selector=item_selector
                }

                orpa_desktop_tree_callback_api(in_data)
            }
            orpa_desktop_tree.loader_turn_on()
            orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIDesktop.UIOSelector_Get_UIOInfoList", [uio_selector], null)
        } else {
            orpa_helper_info('orpa_desktop_selector_empty');
        }

    }

    orpa_desktop_action = new orpa_utils_action("orpa-desktop-action", "orpa-desktop-action-result",true);
    orpa_desktop_selector = new orpa_utils_selector('orpa-desktop-selector-textarea', 'UIO', orpa_desktop_action.on_change_uio_selector, "DESKTOP")

    orpa_desktop_action.render();

    // Загрузить список
    // Сформировать подходящую структуру
    //orpa_desktop_tree.load()
})