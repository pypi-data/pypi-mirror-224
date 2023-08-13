$(document).ready(function() {


    ////////////////////////////////////////////////////
    ///////// ORPA BROWSER TABS НАЧАЛО /////////////////
    ////////////////////////////////////////////////////
    orpa_browser_tabs_new = function () {
      var url_str = $("#orpa-browser-driver-tab-url")[0].value
      var callback = function(in_data) {

      }
      orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIWeb.PageNew", [url_str], null)
    }

    orpa_browser_tabs_close = function () {
      var callback = function(in_data) {

      }
      orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIWeb.PageClose", [], null)

    }

    orpa_browser_tabs_open= function() {
      var url_str = $("#orpa-browser-driver-tab-url")[0].value
      var callback = function(in_data) {
        orpa_browser_tree_refresh()
      }
      orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIWeb.PageOpen", [url_str], null)
    }



    ////////////////////////////////////////////////////
    ///////// ORPA BROWSER SELECTOR НАЧАЛО /////////////////
    ////////////////////////////////////////////////////  

    orpa_browser_selector_uio_clear=function(in_selector_uio) {
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



  orpa_browser_selector_range_select = function(in_range) {
      var l_callback=function(in_mode_str) {
          l_range = orpa_range_get("orpa-browser-selector-type", in_mode_str)
          orpa_range_select(l_range)
      }
      orpa_browser_selector.mode_set(in_range.getAttribute("orpa-data-value"), l_callback)
  }

  orpa_browser_selector_search_list = function() {
    var uio_selector = orpa_browser_selector.uio_get()
    var in_callback=function(in_data) {
      for (var i = 0; i< in_data.length;i++) {
        var item_selector = mGlobal.iSysClone(uio_selector, true)
        item_selector[item_selector.length - 1]["ctrl_index"]=i;
        in_data[i].selector=item_selector
      }

      orpa_browser_tree_callback_api(in_data)
    }
    orpa_browser_tree.loader_turn_on()
    orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIWeb.UIOSelectorListAttributeDictGet", [uio_selector], null)
  }

    ////////////////////////////////////////////////////
    ///////// ORPA BROWSER TREE НАЧАЛО /////////////////
    ////////////////////////////////////////////////////
    orpa_browser_tree = new orpa_utils_tree("orpa-browser-tree"); 


    orpa_browser_mouse_search = function(){ 
      orpa_utils_modal_uio_search_mouse_show(); 
      orpa_api_activity_list_execute_async_json(orpa_browser_tree_callback_api, "pyOpenRPA.Robot.UIWeb.MouseSearchChildTree", [3.0], null);
    }

    orpa_browser_tree_to_selector = function(in_item=null) {
      if (in_item==null) {
        // Достать выбранный объект
        in_item = $("#orpa-browser-tree .orpa-utils-list-item-selected")[0].js_dict["selector"]
      } else {
        in_item = in_item["selector"]
      }
      orpa_browser_selector.uio_set(in_item)
  }

  orpa_browser_tree_selected_item = null
  orpa_browser_tree_callback_api = function(in_data) {
    orpa_utils_modal_uio_search_mouse_hide();
    var recursive = function (in_data, parent_item=null) {
      var l_data_list = []
      if (in_data!=null) {
        in_data.forEach((item, index) => {
          //ФОРМИРУЕМ СЕЛЕКТОР
          var selector_dict = [{}]
          if ("selector" in item) {
            selector_dict = mGlobal.iSysClone(item.selector,true);
          } else {
            //selector_dict=orpa_browser_selector_uio_clear([item])
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
          var attr_limit_int = 80
          //ОТПРАВЛЯЕМ В ДЕРЕВО
          var l_title = item.title
          if (item.title==null) {
            l_title = "Нет тэга"
          }
          // ФОРМИРУЕМ DISCRIPTION ОПИСАНИЕ
          var l_description_str = ""
          if ("id" in item) {
            l_description_str+="id: "+item.id+","
          }
          if ("class_list" in item) {
            if (item.class_list.length>0) {
              l_description_str+=" class: ."+item.class_list.join('.')+","  
              if (l_description_str.length > attr_limit_int) {
                l_description_str = l_description_str.substring(0, attr_limit_int) + "...";
              }
            }
                    
          }
          if ("style_dict" in item) {
            var l_len = Object.keys(item.style_dict).length
            if (l_len>0) {
              l_description_str+=" style: "
              for (let i in item.style_dict) { 
                var l_value = item.style_dict[i]
                l_description_str+=i+":"+l_value+","
              }
              if (l_description_str.length > attr_limit_int) {
                l_description_str = l_description_str.substring(0, attr_limit_int) + "...";
              }
            }
  
          }
          var l_data_item = {
            "title_str": l_title,
            "description_str":l_description_str,
            "action_list":[
              {"_title_str":"ПОДСВЕТИТЬ", "icon_str":"lightbulb", "popup_str":"Выделить цветом UI объект", "callback_click":function(in_object, in_item, in_action){orpa_api_activity_list_execute_async_json(function(){}, "pyOpenRPA.Robot.UIWeb.UIOSelectorFocusHighlight", [in_item.selector], null)}},
              {"_title_str":"СЕЛЕКТОР", "icon_str":"i cursor" ,"popup_str":"Сформировать селектор для обращения к UI объекту", "callback_click":function(in_object, in_item, in_action){orpa_browser_tree_to_selector(in_item);}},
              {"_title_str":"РАСКРЫТЬ", "icon_str":"level down alternate", "visible_filter_str": "NO_CHILD", "popup_str":"Отобразить вложенные UI объекты", "callback_click":function(in_object, in_item, in_action){orpa_browser_tree_selected_item=in_item; orpa_api_activity_list_execute_async_json(orpa_browser_tree_callback_api, "pyOpenRPA.Robot.UIWeb.UIOSelectorChildListAttributeDictGet", [in_item.selector], null)}},
              {"_title_str":"СВЕРНУТЬ", "icon_str":"level up alternate", "visible_filter_str": "HAS_CHILD", "popup_str":"Свернуть вложенные UI объекты","callback_click":function(in_object, in_item, in_action){in_item.child_list=[]; orpa_browser_tree.render();}},
            ],
            "callback_selected": function(in_object, in_item) {orpa_browser_level_load_levels(in_object, in_item);},
            "is_unselect_block_bool": true,
            "selector": selector_dict
          }
          
          //ОБРАБОТКА ДЕТЕЙ
          if ("child_list" in item) {
            l_data_item["child_list"] = recursive(item.child_list, item)
          }
          l_data_list.push(l_data_item)

        })
      };
      return l_data_list
    }
    l_data_list = recursive(in_data, orpa_browser_tree_selected_item)
    if (orpa_browser_tree_selected_item!=null) {
      orpa_browser_tree_selected_item['child_list']=l_data_list
      orpa_browser_tree_selected_item = null
    } else {
      orpa_browser_tree.load(l_data_list)
    }
    orpa_browser_tree.render()
    orpa_browser_tree.loader_turn_off();
  }
  orpa_browser_tree_refresh=function() {
    orpa_browser_tree.loader_turn_on();
    orpa_api_activity_list_execute_async_json(orpa_browser_tree_callback_api, "pyOpenRPA.Robot.UIWeb.UIOSelectorListAttributeDictGet", null, null)

  }
  orpa_browser_tree_refresh()

  ////////////////////////////////////////////////////
  ///////// ORPA BROWSER TREE КОНЕЦ /////////////////
  ////////////////////////////////////////////////////

  
    ////////////////////////////////////////////////////
    ///////// ORPA BROWSER LEVEL НАЧАЛО /////////////////
    ////////////////////////////////////////////////////
    // Получить информацию об уровнях по селектору - 1й элемент (UIO/XPATH/CSS). in_callback(in_data)
    orpa_browser_levels=function(in_selector, in_callback) {
      orpa_browser_level.loader_turn_on();
      orpa_browser_property.loader_turn_on();
      orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIWeb.UIOSelectorLevelInfoList", in_arg_list=[in_selector])
    }
    orpa_browser_level = new orpa_utils_tree("orpa-browser-level"); 
    orpa_browser_level.mode_set("LIST")
    orpa_browser_level_load_levels=function(in_object, in_item) {
      var callback=function(in_data) {
        var l_data_list=[]
        in_data.forEach((item, index) => {           
          //selector_dict.ctrl_index = index // СФОРМИРОВАТЬ СЕЛЕКТОР ДЛЯ ДАЛЬНЕЙШЕЙ ОТРАБОТКИ
          var attr_limit_int = 80
          //ОТПРАВЛЯЕМ В ДЕРЕВО
          var l_title = item.title
          if (item.title==null) {
            l_title = "Нет тэга"
          }
          // ФОРМИРУЕМ DISCRIPTION ОПИСАНИЕ
          var l_description_str = ""
          if ("id" in item) {
            l_description_str+="id: "+item.id+","
          }
          if ("class_list" in item) {
            if (item.class_list.length>0) {
              l_description_str+=" class: ."+item.class_list.join('.')+","  
              if (l_description_str.length > attr_limit_int) {
                l_description_str = l_description_str.substring(0, attr_limit_int) + "...";
              }
            }
                    
          }
          if ("style_dict" in item) {
            var l_len = Object.keys(item.style_dict).length
            if (l_len>0) {
              l_description_str+=" style: "
              for (let i in item.style_dict) { 
                var l_value = item.style_dict[i]
                l_description_str+=i+":"+l_value+","
              }
              if (l_description_str.length > attr_limit_int) {
                l_description_str = l_description_str.substring(0, attr_limit_int) + "...";
              }
            }

          }
          //ОТПРАВЛЯЕМ В ДЕРЕВО
          l_data_list.push(
            {
              "icon_str": "dot circle",
              "title_str": "Уровень "+index+": "+l_title,
              "description_str":l_description_str,
              "action_list":[],
              "callback_selected": function(in_object, in_item) {orpa_browser_property_load(in_item);},
              "server_item": item,
              "level_int": index,
              "is_unselect_block_bool": true
            }
          )
        });
        l_data_list.slice(-1)[0].is_selected_bool=true
        orpa_browser_level.load(l_data_list)
        orpa_browser_level.render()
        orpa_browser_level.loader_turn_off();
        orpa_browser_property_load(l_data_list.slice(-1)[0])
      }

      orpa_browser_levels(in_item.selector, callback);
    }

    ////////////////////////////////////////////////////
    ///////// ORPA BROWSER LEVEL КОНЕЦ /////////////////
    ////////////////////////////////////////////////////

    // ORPA DESKTOP MEMORY
    orpa_browser_memory_slot_dict = {}

    orpa_browser_memory_switch=function(in_new_item) {
      key_old_str = orpa_range_value_get("orpa-browser-memory-slot")
      orpa_browser_memory_save(key_old_str)
      orpa_range_select(in_new_item);
      key_new_str = orpa_range_value_get("orpa-browser-memory-slot")
      orpa_browser_memory_restore(key_new_str)
    }

    orpa_browser_memory_save= function(in_slot_key) {
      orpa_browser_memory_slot_dict[in_slot_key]={}
      slot_dict = orpa_browser_memory_slot_dict[in_slot_key]
      slot_dict["tree"]=orpa_browser_tree.data_list
      slot_dict["tree_mode"]=orpa_browser_tree.mode
      slot_dict["level"]=orpa_browser_level.data_list
      slot_dict["property"]=orpa_browser_property.data_list
      slot_dict["selector"]=orpa_browser_selector.uio_get()
      slot_dict["action"]=orpa_browser_action.data_get()
      slot_dict["action-result"]=document.getElementById("orpa-browser-action-result").innerHTML

    }
    orpa_browser_memory_restore = function (in_slot_key) {
      if (in_slot_key in orpa_browser_memory_slot_dict) {
        slot_dict = orpa_browser_memory_slot_dict[in_slot_key]
        orpa_browser_tree.load(slot_dict.tree)
        orpa_browser_tree.mode_set(slot_dict.tree_mode)
        orpa_browser_level.load(slot_dict.level)
        orpa_browser_property.load(slot_dict.property)
        orpa_browser_selector.uio_set(slot_dict["selector"])
        orpa_browser_action.data_load(slot_dict["action"])
        document.getElementById("orpa-browser-action-result").innerHTML=slot_dict["action-result"]
        if (slot_dict["action-result"]!="") {
          document.getElementById("orpa-browser-action-result").classList.remove("orpa-placeholder");
        } else {
          document.getElementById("orpa-browser-action-result").classList.add("orpa-placeholder");
        }
        
      } else {
        orpa_browser_tree_refresh()
        orpa_browser_tree.mode_set("TREE")
        orpa_browser_level.clear()
        orpa_browser_property.clear()
        orpa_browser_selector.clear()
        orpa_browser_action.clear()
        document.getElementById("orpa-browser-action-result").innerHTML=""
        document.getElementById("orpa-browser-action-result").classList.add("orpa-placeholder");
      }
    }
    orpa_browser_memory_clear = function(in_slot_key) {

    }


    ////////////////////////////////////////////////////
    ///////// ORPA BROWSER PROPERTY НАЧАЛО /////////////////
    ////////////////////////////////////////////////////
    var orpa_browser_property_limit_len = 120
    orpa_browser_property = new orpa_utils_tree("orpa-browser-property"); 
    orpa_browser_property.mode_set("LIST")

    orpa_browser_property_load=function(in_item) {
      var l_data_list = []
      var const_ignore={"rectangle":true}
      for (let key in in_item.server_item) {
        if (key in const_ignore) {
          // В списке игнорирования
        } else {
          let str = in_item.server_item[key];
          let str_render = str
          if (typeof str === "string") {
            if (str.length > orpa_browser_property_limit_len) {
              str_render = str.slice(0, orpa_browser_property_limit_len) + "...";
            }
          }
          if (str === "" || str == null) {
            str_render = "Отсутствует"
          }
          l_icon_str = "circle outline"
          if (orpa_browser_selector.attribute_exists(in_item.level_int, key)) {
            l_icon_str = "circle"
          }

          //КЕЙС ФОРМИРОВАНИЯ КЛАССОВ
          var class_child_list = []
          if (key == "class_list" && false == true) {
            for (let class_value in in_item.server_item["class_list"]) {
              class_child_list.push({
                "icon_str": l_icon_str,
                "title_str": class_value+": ",
                "title_right_str": "",
                "description_str":"",
                "action_list":[],
                "callback_selected": function(in_object, in_item) {in_item.icon_str="circle"; orpa_browser_selector.attribute_set(in_item.level_int,key, str); orpa_browser_property.render();},
                "callback_unselected": function(in_object, in_item) {in_item.icon_str="circle outline"; orpa_browser_selector.attribute_remove(in_item.level_int,key); orpa_browser_property.render();},
                "child_list": class_child_list,
                "level_int": in_item.level_int
    
              }) 

            }

          }

          l_data_list.push(
            {
              "icon_str": l_icon_str,
              "title_str": key+": ",
              "title_right_str": String(str_render),
              "description_str":"",
              "action_list":[],
              "callback_selected": function(in_object, in_item) {in_item.icon_str="circle"; orpa_browser_selector.attribute_set(in_item.level_int,key, str); orpa_browser_property.render();},
              "callback_unselected": function(in_object, in_item) {in_item.icon_str="circle outline"; orpa_browser_selector.attribute_remove(in_item.level_int,key); orpa_browser_property.render();},
              "child_list": class_child_list,
              "level_int": in_item.level_int
  
            }
          )
        }
        
      }
      // ДОБАВИТЬ ИНФО ПРО МНОГОУРОВНЕВЫЙ ПОИСК DEPTH
      l_icon_str = "circle outline"
      if (orpa_browser_selector.attribute_exists(in_item.level_int, "depth_end")) {
        l_icon_str = "circle"
      }
      l_data_list.push(
        {
          "icon_str": l_icon_str,
          "title_str": "depth: ",
          "title_right_str": String("Многоуровневый поиск"),
          "description_str":"",
          "action_list":[],
          "callback_selected": function(in_object, in_item) {in_item.icon_str="circle"; orpa_browser_selector.attribute_set(in_item.level_int,"depth_start", 1);orpa_browser_selector.attribute_set(in_item.level_int,"depth_end", 99); orpa_browser_property.render();},
          "callback_unselected": function(in_object, in_item) {in_item.icon_str="circle outline"; orpa_browser_selector.attribute_remove(in_item.level_int,"depth_start");orpa_browser_selector.attribute_remove(in_item.level_int,"depth_end"); orpa_browser_property.render();},

          "level_int": in_item.level_int

        }
      )
      orpa_browser_property.load(l_data_list)
      orpa_browser_property.render()
      orpa_browser_property.loader_turn_off();
    }

    orpa_browser_action = new orpa_utils_action("orpa-browser-action", "orpa-browser-action-result",false);
    orpa_browser_selector = new orpa_utils_selector('orpa-browser-selector-textarea', 'UIO', orpa_browser_action.on_change_uio_selector, "BROWSER");
    
    orpa_api_uiweb_selector_convert = function(in_selector, in_type_str, in_callback, in_type_from_str=null) {
      switch (true) {
        case in_type_from_str=="XPATH" && in_type_str=="UIO":
          orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIWeb.XPATH_To_UIOSelector", [in_selector], null)
          break;
        case in_type_from_str=="UIO" && in_type_str=="XPATH":
          orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIWeb.UIOSelector_To_XPATH", [in_selector], null)
          break;
        case in_type_from_str=="CSS" && in_type_str=="UIO":
          orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIWeb.CSS_To_UIOSelector", [in_selector], null)
          break;
        case in_type_from_str=="UIO" && in_type_str=="CSS":
            orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIWeb.UIOSelector_To_CSS", [in_selector], null)
          break;
        default:
          orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIWeb.SelectorConvert", [in_selector, in_type_str], null)
          break;
      }
    }

    orpa_browser_action.render();
  })