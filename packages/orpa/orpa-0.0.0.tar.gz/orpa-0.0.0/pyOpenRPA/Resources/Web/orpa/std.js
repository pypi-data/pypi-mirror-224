// Production steps of ECMA-262, Edition 6, 22.1.2.1
if (!Array.from) {
    Array.from = (function () {
      var toStr = Object.prototype.toString;
      var isCallable = function (fn) {
        return typeof fn === 'function' || toStr.call(fn) === '[object Function]';
      };
      var toInteger = function (value) {
        var number = Number(value);
        if (isNaN(number)) { return 0; }
        if (number === 0 || !isFinite(number)) { return number; }
        return (number > 0 ? 1 : -1) * Math.floor(Math.abs(number));
      };
      var maxSafeInteger = Math.pow(2, 53) - 1;
      var toLength = function (value) {
        var len = toInteger(value);
        return Math.min(Math.max(len, 0), maxSafeInteger);
      };

      // The length property of the from method is 1.
      return function from(arrayLike/*, mapFn, thisArg */) {
        // 1. Let C be the this value.
        var C = this;

        // 2. Let items be ToObject(arrayLike).
        var items = Object(arrayLike);

        // 3. ReturnIfAbrupt(items).
        if (arrayLike == null) {
          throw new TypeError('Array.from requires an array-like object - not null or undefined');
        }

        // 4. If mapfn is undefined, then let mapping be false.
        var mapFn = arguments.length > 1 ? arguments[1] : void undefined;
        var T;
        if (typeof mapFn !== 'undefined') {
          // 5. else
          // 5. a If IsCallable(mapfn) is false, throw a TypeError exception.
          if (!isCallable(mapFn)) {
            throw new TypeError('Array.from: when provided, the second argument must be a function');
          }

          // 5. b. If thisArg was supplied, let T be thisArg; else let T be undefined.
          if (arguments.length > 2) {
            T = arguments[2];
          }
        }

        // 10. Let lenValue be Get(items, "length").
        // 11. Let len be ToLength(lenValue).
        var len = toLength(items.length);

        // 13. If IsConstructor(C) is true, then
        // 13. a. Let A be the result of calling the [[Construct]] internal method 
        // of C with an argument list containing the single item len.
        // 14. a. Else, Let A be ArrayCreate(len).
        var A = isCallable(C) ? Object(new C(len)) : new Array(len);

        // 16. Let k be 0.
        var k = 0;
        // 17. Repeat, while k < len… (also steps a - h)
        var kValue;
        while (k < len) {
          kValue = items[k];
          if (mapFn) {
            A[k] = typeof T === 'undefined' ? mapFn(kValue, k) : mapFn.call(T, kValue, k);
          } else {
            A[k] = kValue;
          }
          k += 1;
        }
        // 18. Let putStatus be Put(A, "length", len, true).
        A.length = len;
        // 20. Return A.
        return A;
      };
    }());
  }
if (!Object.assign) {
    Object.defineProperty(Object, 'assign', {
      enumerable: false,
      configurable: true,
      writable: true,
      value: function(target, firstSource) {
        'use strict';
        if (target === undefined || target === null) {
          throw new TypeError('Cannot convert first argument to object');
        }

        var to = Object(target);
        for (var i = 1; i < arguments.length; i++) {
          var nextSource = arguments[i];
          if (nextSource === undefined || nextSource === null) {
            continue;
          }

          var keysArray = Object.keys(Object(nextSource));
          for (var nextIndex = 0, len = keysArray.length; nextIndex < len; nextIndex++) {
            var nextKey = keysArray[nextIndex];
            var desc = Object.getOwnPropertyDescriptor(nextSource, nextKey);
            if (desc !== undefined && desc.enumerable) {
              to[nextKey] = nextSource[nextKey];
            }
          }
        }
        return to;
      }
    });
  }

function escapeRegExp(string) {
  return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); // $& means the whole matched string
}
function replaceAll(str, match, replacement){
  // howto replaceAll("rtyrytt", 't','1')
    return str.replace(new RegExp(escapeRegExp(match), 'g'), ()=>replacement);
 }
////////////////////////////////////////////
//Связывание html списка объектов с рекурсивным списком вложенных словарей
function orpa_utils_map_html_dict(in_object, in_dict, in_html_list, in_html_list_index_int=0) {
  in_dict.forEach((item, index) => {
    in_html_list[in_html_list_index_int].js_dict = in_dict[index]
    in_html_list[in_html_list_index_int].js_object = in_object
    in_html_list_index_int=in_html_list_index_int+1
    if (in_dict[index].child_list) {
      in_html_list_index_int = orpa_utils_map_html_dict(in_object, in_dict[index].child_list, in_html_list, in_html_list_index_int);
    }
  });
  return in_html_list_index_int
}

orpa_utils_popup_show=function(html_element, text_str) {
  $(html_element)
  .popup({
    content : text_str,
    on: 'manual'
  }).popup("show")
}

class orpa_utils_selector {
    constructor(in_html_id_str, in_mode_value_str, in_callback_new_selector=null, in_module_type="DESKTOP") {
        this.html_id_str = in_html_id_str
        // Установить аттрибут onchange на textarea
        document.getElementById(this.html_id_str).onchange=this.on_change
        this.uio = null
        this.mode_str = in_mode_value_str
        this.error_bool = false
        this.callback_new_selector=in_callback_new_selector
        this.module_type_str = in_module_type // DESKTOP | BROWSER
    }
    code_generate = () =>  {
      var selector_textarea = document.getElementById(this.html_id_str)
      var code_str = "'"+selector_textarea.value+"'"
      if (this.mode_str=="UIO") {
        code_str = selector_textarea.value
      }
      code_str = replaceAll(code_str, "\n", "")
      code_str = orpa_utils_json_2_python(code_str)
      clipboard_set(code_str)
    }

    code_highlight_generate = () =>  {
      if (this.module_type_str=="DESKTOP") {
        var code_str = `#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelector_FocusHighlight(uio_selector)`
        code_str = replaceAll(code_str, "<SELECTOR>", orpa_utils_json_2_python(JSON.stringify(this.uio_get())))
        clipboard_set(code_str)
      } else {
        var page_url_str = document.getElementById("orpa-browser-driver-tab-url").value
        var code_str = `#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIWeb.UIOSelectorFocusHighlight(uio_selector)`
        code_str = replaceAll(code_str, "<SELECTOR>", orpa_utils_json_2_python(JSON.stringify(this.uio_get())))
        code_str = replaceAll(code_str, "<PAGE_URL>", page_url_str)
        clipboard_set(code_str)
      }
    }

    
    code_locate_all_generate = () =>  {
      if (this.module_type_str=="DESKTOP") {
        var code_str = `#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelector_Get_UIOList(uio_selector)`
        code_str = replaceAll(code_str, "<SELECTOR>", orpa_utils_json_2_python(JSON.stringify(this.uio_get())))
        clipboard_set(code_str)
      } else {
        var page_url_str = document.getElementById("orpa-browser-driver-tab-url").value
        var code_str = `#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio_list = UIWeb.UIOSelectorList(uio_selector)`
        code_str = replaceAll(code_str, "<SELECTOR>", orpa_utils_json_2_python(JSON.stringify(this.uio_get())))
        code_str = replaceAll(code_str, "<PAGE_URL>", page_url_str)
        clipboard_set(code_str)
      }
    }

    //Стрелочная функция для того, чтобы объект this не переопределялся из за html onchange объекта, а оставался экземпляром класса
    on_change = () =>  {
        // проверить и вернуть true или false
        var selector_textarea = document.getElementById(this.html_id_str)
        var selector_str = selector_textarea.value
        if (selector_str==="") {
          this.uio_set()
        } else {
          var l_mode_to_str = {"UIO":"XPATH","CSS":"UIO","XPATH":"UIO"}[this.mode_str]
          var callback = (in_data) => {
              this.error_bool = true
              try {
                  if (in_data.indexOf("ErrorHeader")!=-1) {
                      this.error_bool = false
                      selector_textarea.style['border-color'] = "red";
                  } else {
                      selector_textarea.style['border-color'] = "";
                      if (this.mode_str=="UIO") {
                          this.uio=JSON.parse(selector_str)
                      } else {
                          this.uio=in_data
                      }
                      if (this.callback_new_selector!=null) this.callback_new_selector(this.uio)
                  }
              } catch (error) {
                  // Обработка ошибки
                  selector_textarea.style['border-color'] = "";
                  if (this.mode_str=="UIO") {
                      this.uio=JSON.parse(selector_str)
                  } else {
                      this.uio=in_data
                  }
                  if (this.callback_new_selector!=null) this.callback_new_selector(this.uio)
              }
              
          }
          if (this.module_type_str=="DESKTOP") {
            orpa_api_uidesktop_selector_convert(selector_str, l_mode_to_str, callback, this.mode_str)
          } else {
            orpa_api_uiweb_selector_convert(selector_str, l_mode_to_str, callback, this.mode_str)
          }

        }
        
    }
    //in_callback(in_mode_str)
    mode_set = function (in_mode_to_str, in_callback=null) {
        // проверить и вернуть true или false
        var selector_textarea = document.getElementById(this.html_id_str)
        var selector_str = selector_textarea.value
        this.mode_to_str = in_mode_to_str
        var callback = (in_data) => {
            this.error_bool = true
            var selector_textarea = document.getElementById(this.html_id_str)
            try {
                if ("ErrorHeader" in in_data) {
                    this.error_bool = false
                    selector_textarea.style['border-color'] = "red";
                } else {
                    selector_textarea.style['border-color'] = "";
                    this.mode_str=this.mode_to_str
                    if (this.mode_to_str=="UIO") {
                        selector_textarea.value=JSON.stringify(in_data, null, 4)
                    } else {
                        selector_textarea.value=in_data
                    }
                }
            } catch (error) {
                // Обработка ошибки
                selector_textarea.style['border-color'] = "";
                this.mode_str=this.mode_to_str
                if (this.mode_to_str=="UIO") {
                    selector_textarea.value=JSON.stringify(in_data, null, 4)
                } else {
                    selector_textarea.value=in_data
                }
            }
            this.mode_to_str = null
            if (in_callback!=null) {
                in_callback(this.mode_str)
            }
        }
        if (this.module_type_str=="DESKTOP") {
          orpa_api_uidesktop_selector_convert(selector_str, in_mode_to_str, callback, this.mode_str)
        } else {
          orpa_api_uiweb_selector_convert(selector_str, in_mode_to_str, callback, this.mode_str)
        }
    }
    uio_set=function(in_uio=null) {
        if (in_uio!=null) {
          this.uio=in_uio  
        }
        if (in_uio===[]) {
          this.uio=in_uio  
        } else {
          // проверить и вернуть true или false
          var selector_textarea = document.getElementById(this.html_id_str)
          var l_mode_to_str = this.mode_str
          var callback = (in_data) => {
              this.error_bool = true
              try {
                  if ("ErrorHeader" in in_data) {
                      this.error_bool = false
                      selector_textarea.style['border-color'] = "red";
                  } else {
                      selector_textarea.style['border-color'] = "";
                      if (this.mode_str=="UIO") {
                          selector_textarea.value=JSON.stringify(this.uio, null, 4)
                      } else {
                          selector_textarea.value=in_data
                      }
                      if (this.callback_new_selector!=null) this.callback_new_selector(this.uio)
                  }
              } catch (error) {
                  // Обработка ошибки
                  selector_textarea.style['border-color'] = "";
                  if (this.mode_str=="UIO") {
                      selector_textarea.value=JSON.stringify(this.uio, null, 4)
                  } else {
                      selector_textarea.value=in_data
                  }
                  if (this.callback_new_selector!=null) this.callback_new_selector(this.uio)
              }
              
          }
          if (this.module_type_str=="DESKTOP") {
            orpa_api_uidesktop_selector_convert(this.uio, l_mode_to_str, callback, "UIO")
          } else {
            orpa_api_uiweb_selector_convert(this.uio, l_mode_to_str, callback, "UIO")
          }
        }
        
        
    }
    uio_get=function() {
      var uio = []
      if (this.uio != null) {
        uio = this.uio
      }
      return uio
    }
    attribute_set=function(in_uio_level_int, in_attribute_name_str, in_attribute_value) {
        this.uio[in_uio_level_int][in_attribute_name_str]=in_attribute_value
        this.uio_set()
    }
    attribute_remove=function(in_uio_level_int, in_attribute_name_str) {
      delete this.uio[in_uio_level_int][in_attribute_name_str]
      this.uio_set()
    }
    attribute_exists=function(in_uio_level_int, in_attribute_name_str) {
        try {
            if (in_attribute_name_str in this.uio[in_uio_level_int]) {
                return true
            } else {
                return false
            }
        } catch (error) {
            return false
        }
    }
    ui_highlight=function() {
      var l_action_str = ""
      if (this.uio != null) {
        if (this.module_type_str=="DESKTOP") {
          l_action_str="pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight" 
        } else {
          l_action_str="pyOpenRPA.Robot.UIWeb.UIOSelectorFocusHighlight" 
        }
        orpa_api_activity_list_execute_async(function(){}, l_action_str, [this.uio]);

      } else {

        orpa_helper_info('orpa_desktop_selector_empty');
      }

      
    }
    clear=function() {
      this.uio=null
      var selector_textarea = document.getElementById(this.html_id_str)
      selector_textarea.value=""
    }
}
orpa_utils_json_2_python = function(in_str) {
  var code_str = in_str
  code_str = replaceAll(code_str,"null","None")
  code_str = replaceAll(code_str,"undefined","None")
  code_str = replaceAll(code_str,"true","True")
  code_str = replaceAll(code_str,"false","False")
  return code_str
}

//////////////////////////////////////
////////////////////////////////////
/////////////////////////////////////
////////////////////////////////////
//////////////////////////////////////
//////////////////////////////////////
/////////////////////////////////////
// Панель действий
//Режим (DESKTOP | BROWSER) Тип атрибута: Модуль, объект. Методы получить/загрузить
class orpa_utils_action {
  constructor(in_html_id_str, in_html_id_result_str, is_tab_desktop_bool=true) {
    this.html_id_str = in_html_id_str
    this.html_id_result_str = in_html_id_result_str
    this.data = {
      "is_tab_desktop_bool": is_tab_desktop_bool, 
      "is_module_bool":true,
      "is_function_bool":true, 
      "function_str":null, 
      "function_list":[],
      "args_is_dict":true, 
      "args_value_list_str": "",
      "args_value_dict_str": "",
      "uio_selector":null
    }
    this.__();
  }
  clear = function() {
    this.data = {
      "is_tab_desktop_bool": this.data.is_tab_desktop_bool, 
      "is_module_bool":true,
      "is_function_bool":true, 
      "function_str":null, 
      "function_list":[],
      "args_is_dict":true, 
      "args_value_list_str": "",
      "args_value_dict_str": "",
      "uio_selector":null
    }
    this.__();
    this.render();
  }
  __=function() {
    // IN CODE REPLACE THE <SELECTOR> STR to the selector
    if (this.data["is_tab_desktop_bool"]) {
      this.help_function_list=[
        "Exists",
        "Highlight",
        "Focus",
        "FocusHighlight",
        "WaitAppear",
        "WaitAppearList",
        "WaitDisappear",
        "WaitDisappearList",
        "Click",
        "ClickRight",
        "ClickDouble",
        "TryRestore",
        "GetActivityList",
        "GetLevelList"
      ]
      this.help_code_generator_dict ={
        "Exists":{"help_str": "Код Python скопирован в буфер обмена.\nФункция проверяет наличие UI объекта по UIO селектору.","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio_exists_bool = UIDesktop.UIOSelector_Exist_Bool(uio_selector)`},
        "Highlight":{"help_str": "Код Python скопирован в буфер обмена.\nФункция выполняет посвечивание обнаруженного UI объекта по UIO селектору","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelector_Highlight(uio_selector)`},
        "Focus":{"help_str": "Код Python скопирован в буфер обмена.\nФункция выполняет фокусировку на объект по UIO селектору","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelector_Focus(uio_selector)`},
        "FocusHighlight":{"help_str": "Код Python скопирован в буфер обмена.\nФункция выполняет фокусировку на объект и посвечивание обнаруженного UI объекта по UIO селектору","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelector_FocusHighlight(uio_selector)`},
        "WaitAppear":{"help_str": "Код Python скопирован в буфер обмена.\nФункция ожидает появления хотя бы обного UI объекта по UIO селектору.\n\n:параметр inWaitSecs: Количество секунд, которые отвести на ожидание UIO объекта. По умолчанию 24 часа (86400 секунд)\n:параметр inFlagRaiseException (опционально): True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelectorSecs_WaitAppear_Bool (uio_selector,inWaitSecs=60, inFlagRaiseException=True)`},
        "WaitAppearList":{"help_str": "Код Python скопирован в буфер обмена.\nФункция ожидает появления хотя бы обного UI объекта из списка UIO селекторов.\n\n:параметр inWaitSecs: Количество секунд, которые отвести на ожидание UIO объекта. По умолчанию 24 часа (86400 секунд)\n:параметр inFlagWaitAllInMoment: True - Ожидать до того момента, пока не исчезнут все запрашиваемые UIO объекты на рабочей области\n:параметр inFlagRaiseException (опционально): True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio_selector_list = [uio_selector]\nappeared_index_list = UIDesktop.UIOSelectorsSecs_WaitAppear_List(uio_selector_list,inWaitSecs=60,inFlagWaitAllInMoment=True, inFlagRaiseException=True)`},
        "WaitDisappear":{"help_str": "Код Python скопирован в буфер обмена.\nФункция ожидает момента, когда на экране не будет доступно ни одного UI объекта по UIO селектору.\n\n:параметр inWaitSecs: Количество секунд, которые отвести на ожидание UIO объекта. По умолчанию 24 часа (86400 секунд)\n:параметр inFlagRaiseException (опционально): True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelectorSecs_WaitDisappear_Bool (uio_selector,inWaitSecs=60, inFlagRaiseException=True)`},
        "WaitDisappearList":{"help_str": "Код Python скопирован в буфер обмена.\nФункция ожидает момента, когда на экране не будет доступно ни одного UI объекта из списка UIO селекторов.\n\n:параметр inWaitSecs: Количество секунд, которые отвести на ожидание UIO объекта. По умолчанию 24 часа (86400 секунд)\n:параметр inFlagRaiseException (опционально): True - формировать ошибку exception, если платформа не обнаружина ни одного UIO объекта по заданному UIO селектору. False - обратный случай (может привести к ошибочным результатам). По умолчанию True.","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio_selector_list = [uio_selector]\ndisappeared_index_list = UIDesktop.UIOSelectorsSecs_WaitDisappear_List(uio_selector_list,inWaitSecs=60,inFlagWaitAllInMoment=True, inFlagRaiseException=True)`},
        "TryRestore":{"help_str": "Код Python скопирован в буфер обмена.\nФункция пытается восстановить окно приложения, если оно было свернуто. Окно идентифицируется по установленному UIO селектору","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelector_TryRestore_Dict(uio_selector)`},
        "Click":{"help_str": "Код Python скопирован в буфер обмена.\nФункция пытается восстановить окно приложения, если оно было свернуто. Окно идентифицируется по установленному UIO селектору","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelector_Click(uio_selector, inRuleStr = "CC", inFocusBool = True)`},
        "ClickRight":{"help_str": "Код Python скопирован в буфер обмена.\nФункция пытается восстановить окно приложения, если оно было свернуто. Окно идентифицируется по установленному UIO селектору","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelector_ClickRight(uio_selector, inRuleStr = "CC", inFocusBool = True)`},
        "ClickDouble":{"help_str": "Код Python скопирован в буфер обмена.\nФункция пытается восстановить окно приложения, если оно было свернуто. Окно идентифицируется по установленному UIO селектору","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIDesktop.UIOSelector_ClickDouble(uio_selector, inRuleStr = "CC", inFocusBool = True)`},
        "GetActivityList":{"help_str": "Код Python скопирован в буфер обмена.\nФункция возвращает список функций / свойств, доступных для UI объекта по установленному UIO селектору","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nactivity_list = UIDesktop.UIOSelector_Get_UIOActivityList(uio_selector)\n#UIOSelectorUIOActivity_Run_Dict(uio_selector, inActionName="click_input")`},
        "GetLevelList":{"help_str": "Код Python скопирован в буфер обмена.\nФункция возвращает список атрибутов, обнаруженных на всех родительских уровнях до UI объекта по UIO селектору","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIDesktop\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nlevel_info_list = UIDesktop.UIOSelector_LevelInfo_List(uio_selector)`},
      }
    } else {
      this.help_function_list=[
        "UIOAttributeDictGet",
        "UIOSelectorChildListAttributeDictGet",
        "UIOSelectorListAttributeDictGet",
        "UIOSelectorLevelInfoList",
        "UIOSelectorActivityListGet",
        "UIOTextGet",
        "UIOAttributeGet",
        "UIOAttributeStyleGet",
        "UIOAttributeSet",
        "UIOAttributeRemove",
        "UIOAttributeStyleSet",
        "UIOAttributeStyleRemove",
        "UIOClick",
        "UIOSelectorHighlight",
        "UIOSelectorClick",
        "UIOSelectorSetValue",
        "UIOSelectorWaitAppear",
        "UIOSelectorWaitDisappear"
      ]
      this.help_code_generator_dict ={
        "UIOAttributeDictGet":{"help_str": "Код Python скопирован в буфер обмена.\nФункция получает словарь атрибутов по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio=UIWeb.UIOSelectorFirst(uio_selector)\nuio_attr_dict = UIWeb.UIOAttributeDictGet(uio)`},
        "UIOSelectorChildListAttributeDictGet":{"help_str": "Код Python скопирован в буфер обмена.\nФункция получает словарь атрибутов по детям первого UI объекта, определенного по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio_child_attr_dict = UIWeb.UIOSelectorChildListAttributeDictGet(uio_selector)`},
        "UIOSelectorListAttributeDictGet":{"help_str": "Код Python скопирован в буфер обмена.\nФункция получает список словарей атрибутов по UI объектам, которые удовлетворяют селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio_attr_list = UIWeb.UIOSelectorListAttributeDictGet(uio_selector)`},
        "UIOSelectorLevelInfoList":{"help_str": "Код Python скопирован в буфер обмена.\nФункция получает список словарей атрибутов по уровням первого UI объекта, который удовлетворяет селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio_level_list = UIWeb.UIOSelectorLevelInfoList(uio_selector)`},
        "UIOSelectorActivityListGet":{"help_str": "Код Python скопирован в буфер обмена.\nФункция получает список доступных активностей по UI объекту, определенного по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio_activity_list = UIWeb.UIOSelectorActivityListGet(uio_selector)`},
        "UIOTextGet":{"help_str": "Код Python скопирован в буфер обмена.\nФункция получает текст UI объекта, определенного по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio=UIWeb.UIOSelectorFirst(uio_selector)\nuio_text_str = UIWeb.UIOTextGet(uio)`},
        "UIOAttributeGet":{"help_str": "Код Python скопирован в буфер обмена.\nФункция получает значение атрибута по селектору (UIO / XPATH / CSS) и наименованию аттрибута.","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio=UIWeb.UIOSelectorFirst(uio_selector)\nuio_attr_str = UIWeb.UIOAttributeGet(uio, "TYPE ATTRIBUTE NAME HERE")`},
        "UIOAttributeStyleGet":{"help_str": "Код Python скопирован в буфер обмена.\nФункция получает значение стилевого атрибута по селектору (UIO / XPATH / CSS) и наименованию аттрибута.","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio=UIWeb.UIOSelectorFirst(uio_selector)\nuio_attr_style_str = UIWeb.UIOAttributeStyleGet(uio, "TYPE STYLE ATTRIBUTE NAME HERE")`},
        "UIOAttributeSet":{"help_str": "Код Python скопирован в буфер обмена.\nФункция устанавливает атрибут у UI объекта по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio=UIWeb.UIOSelectorFirst(uio_selector)\nUIWeb.UIOAttributeSet(uio, "TYPE ATTRIBUTE NAME", "TYPE ATTRIBUTE VALUE")`},
        "UIOAttributeStyleSet":{"help_str": "Код Python скопирован в буфер обмена.\nФункция устанавливает стилевой атрибут у UI объекта по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio=UIWeb.UIOSelectorFirst(uio_selector)\nUIWeb.UIOAttributeStyleSet(uio, "TYPE STYLE ATTRIBUTE NAME", "TYPE STYLE ATTRIBUTE VALUE")`},
        "UIOAttributeRemove":{"help_str": "Код Python скопирован в буфер обмена.\nФункция удаляет атрибут у UI объекта по селектору (UIO / XPATH / CSS) и наименованию аттрибута.","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio=UIWeb.UIOSelectorFirst(uio_selector)\nUIWeb.UIOAttributeRemove(uio, "TYPE ATTRIBUTE NAME HERE")`},
        "UIOAttributeStyleRemove":{"help_str": "Код Python скопирован в буфер обмена.\nФункция удаляет атрибут у UI объекта по селектору (UIO / XPATH / CSS) и наименованию аттрибута.","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio=UIWeb.UIOSelectorFirst(uio_selector)\nUIWeb.UIOAttributeStyleRemove(uio, "TYPE STYLE ATTRIBUTE NAME HERE")`},
        "UIOClick":{"help_str": "Код Python скопирован в буфер обмена.\nФункция инициирует внутреннее событие нажатия по UI объекту, определенного по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nuio=UIWeb.UIOSelectorFirst(uio_selector)\nUIWeb.UIOClick(uio)`},
        "UIOSelectorHighlight":{"help_str": "Код Python скопирован в буфер обмена.\nФункция подсвечивает (выделяет зеленой линией на 3 сек.) UI объект, определенный по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIWeb.UIOSelectorHighlight(uio_selector)`},
        "UIOSelectorClick":{"help_str": "Код Python скопирован в буфер обмена.\nФункция инициирует внутреннее событие нажатия по UI объекту, определенного по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIWeb.UIOSelectorClick(uio_selector)`},
        "UIOSelectorSetValue":{"help_str": "Код Python скопирован в буфер обмена.\nФункция устанавливает значение UI объекта, определенного по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIWeb.UIOSelectorSetValue(uio_selector, "Текст для установки")`},
        "UIOSelectorWaitAppear":{"help_str": "Код Python скопирован в буфер обмена.\nФункция ожидает появление UI объекта на странице по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIWeb.UIOSelectorWaitAppear(uio_selector) #Полный перечень параметров см. в документации`},
        "UIOSelectorWaitDisappear":{"help_str": "Код Python скопирован в буфер обмена.\nФункция ожидает пропажу UI объекта на странице по селектору (UIO / XPATH / CSS).","code_str":`#Импорт библиотеки\nfrom pyOpenRPA.Robot import UIWeb\nUIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт\nUIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта\n#Установить селектор и вызвать функцию\nuio_selector = <SELECTOR>\nUIWeb.UIOSelectorWaitDisappear(uio_selector) #Полный перечень параметров см. в документации`},
      }
    }
  }
  code_run_generate = (is_focus_bool=false) =>  {
    if (this.data.is_tab_desktop_bool==true) {
      if (this.data.is_module_bool) {
        var in_value = this.data.function_str
        if (in_value!="") {
          var code_str = this.help_code_generator_dict[in_value].code_str
          code_str = replaceAll(code_str, "<SELECTOR>", orpa_utils_json_2_python(JSON.stringify(this.data["uio_selector"])))
          clipboard_set(code_str)
        } 
      } else {
        `
        from pyOpenRPA.Robot import UIDesktop #Импорт (удалить, если импортировано ранее)
        # Установить селектор, получить UI объект, выполнить действие
        uio_selector = []
        uio = UIDesktop.UIOSelector_Get_UIO(uio_selector)
        uio.set_focus()
        result = uio.<FUNC>(*<JSON_LIST>)
        result = uio.<FUNC>(**<JSON_DICT>)
        `
        var code_str = `from pyOpenRPA.Robot import UIDesktop #Импорт (удалить, если импортировано ранее)
# Установить селектор, получить UI объект, выполнить действие`
        code_str += `\nuio_selector = `+orpa_utils_json_2_python(JSON.stringify(this.data["uio_selector"]))
        code_str += `\nuio = UIDesktop.UIOSelector_Get_UIO(uio_selector)`
        if (is_focus_bool==true) {code_str += `\nuio.set_focus()`}
        if (this.data["is_function_bool"]) {
          if (this.data["args_is_dict"]==true) {
            code_str += `\nresult = uio.`+this.data["function_str"]+"(**"+orpa_utils_json_2_python(this.data["args_value_dict_str"])+")"
          } else {
            code_str += `\nresult = uio.`+this.data["function_str"]+"(*"+orpa_utils_json_2_python(this.data["args_value_list_str"])+")"
          }
        } else {
          code_str += `\nresult = uio.`+this.data["function_str"]
        }
        clipboard_set(code_str)
      }
    } else {
      if (this.data.is_module_bool) {
        var in_value = this.data.function_str
        if (in_value!="") {
          var page_url_str = document.getElementById("orpa-browser-driver-tab-url").value
          var code_str = this.help_code_generator_dict[in_value].code_str
          code_str = replaceAll(code_str, "<SELECTOR>", orpa_utils_json_2_python(JSON.stringify(this.data["uio_selector"])))
          code_str = replaceAll(code_str, "<PAGE_URL>", page_url_str)
          clipboard_set(code_str)
        } 
      } else {
        `
        from pyOpenRPA.Robot import UIWeb #Импорт (удалить, если импортировано ранее)
        # Установить селектор, получить UI объект, выполнить действие
        uio_selector = []
        uio = UIWeb.UIOSelectorFirst(uio_selector)
        UIWeb.BrowserFocus()
        result = uio.<FUNC>(*<JSON_LIST>)
        result = uio.<FUNC>(**<JSON_DICT>)
        `
        var page_url_str = document.getElementById("orpa-browser-driver-tab-url").value
        var code_str = `from pyOpenRPA.Robot import UIWeb #Импорт (удалить, если импортировано ранее)
UIWeb.BrowserChromeStart() #!Удалить, если браузер уже открыт
UIWeb.PageOpen("<PAGE_URL>")#!Удалить, если страница уже открыта
# Установить селектор, получить UI объект, выполнить действие`
        code_str += `\nuio_selector = `+orpa_utils_json_2_python(JSON.stringify(this.data["uio_selector"]))
        code_str += `\nuio = UIWeb.UIOSelectorFirst(uio_selector)`
        if (is_focus_bool==true) {code_str += `\nUIWeb.BrowserFocus()`}
        if (this.data["is_function_bool"]) {
          if (this.data["args_is_dict"]==true) {
            code_str += `\nresult = uio.`+this.data["function_str"]+"(**"+orpa_utils_json_2_python(this.data["args_value_dict_str"])+")"
          } else {
            code_str += `\nresult = uio.`+this.data["function_str"]+"(*"+orpa_utils_json_2_python(this.data["args_value_list_str"])+")"
          }
        } else {
          code_str += `\nresult = uio.`+this.data["function_str"]
        }
        code_str = replaceAll(code_str, "<PAGE_URL>", page_url_str)
        clipboard_set(code_str)
      }
    }
    
  } 

  function_list_load = function (in_function_list, in_function_str=null) {
    this.data["function_list"]=in_function_list
    if (in_function_str!=null) this.data["function_str"]=in_function_str
    this.render()
  }
  mode_is_module_set=function(in_is_module_bool) {
    this.data["is_module_bool"]=in_is_module_bool
    var in_uio_selector = this.data["uio_selector"]
    if (in_is_module_bool==false && this.data["uio_selector"]!=null) {
      var callback= (in_data) =>  {
        this.data["function_list"]=in_data
        this.render()

      }
      if (this.data["is_tab_desktop_bool"]) {
        orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIDesktop.UIOSelector_Get_UIOActivityList", [in_uio_selector])
      } else {
        orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIWeb.UIOSelectorActivityListGet", [in_uio_selector])
      }
    } else {
      this.data["function_list"]=[]
      this.render()
    }
    
  }
  mode_is_tab_desktop_set = function(in_is_tab_desktop_bool) {
    this.data["is_tab_desktop_bool"]=in_is_tab_desktop_bool
    this.render()
  }
  mode_is_dict_set = function (in_is_dict) {
    this.data["args_is_dict"]=in_is_dict
    this.render()
  }
  mode_is_function_set = function (in_is_function_bool) {
    this.data["is_function_bool"]=in_is_function_bool
    this.render()
  }
  on_change_uio_selector = (in_uio_selector) =>  {
    this.data["uio_selector"]=in_uio_selector
    if (this.data["is_module_bool"]) {

    } else {
      // КЕЙС, если идет прогрузка методов / свойств UI объекта
      var callback= (in_data) =>  {
        this.data["function_list"]=in_data
        this.render()

      }
      if (this.data["is_tab_desktop_bool"]) {
        orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIDesktop.UIOSelector_Get_UIOActivityList", [in_uio_selector])
      } else {
        orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIWeb.UIOSelectorActivityListGet", [in_uio_selector])
      }
    }
  }

  on_change_function = (in_function_str) =>  {
    if (in_function_str!="" && in_function_str!=this.data["function_str"]) {
      this.data["function_str"]=in_function_str
      var callback = (in_data) =>  {
        if (in_data["ArgList"]==null && in_data["ArgDict"]==null) {
          this.data["is_function_bool"]=false
        } else {
          this.data["is_function_bool"]=true
          this.data["args_value_list_str"] = JSON.stringify(in_data["ArgList"])
          this.data["args_value_dict_str"] = JSON.stringify(in_data["ArgDict"])
        }
        this.render(); 
      }
      if (this.data.is_module_bool==false) {
        if (this.data["is_tab_desktop_bool"]==false) {
          orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIWeb.UIOSelectorActivityArgGet", [this.data["uio_selector"], this.data["function_str"]])
        } else {
          orpa_api_activity_list_execute_async_json(callback, "pyOpenRPA.Robot.UIDesktop.UIOSelectorUIOActivity_Get_ArgDict", [this.data["uio_selector"], this.data["function_str"]])
        }
      } else {
        this.code_run_generate();
        this.render(); 
      }

    }

  }

  focus_run = (in_ui_focus_bool=true) =>  {
    var callback= (in_data) =>  {
      var result_textarea = document.getElementById(this.html_id_result_str)
      var data = in_data[in_data.length - 1]
      if (data==null) {
        result_textarea.innerHTML="Значение null / None"
      } else {
        result_textarea.innerHTML=JSON.stringify(data)
      }
      result_textarea.classList.remove("orpa-placeholder");
    }
    var uio = this.data["uio_selector"]
    var action_str = this.data["function_str"]
    var activity_list = []
    var textarea_value = null
    if (this.data["is_function_bool"]) {
        if (this.data["args_is_dict"]==false) {
          textarea_value=JSON.parse(this.data["args_value_list_str"])
        } else {
          textarea_value=JSON.parse(this.data["args_value_dict_str"])
        }
    } else {
      textarea_value=""
    }
    
    if (this.data["is_tab_desktop_bool"]) {
      if (in_ui_focus_bool==true) {
        activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelector_FocusHighlight", "ArgList":[uio], "ArgDict":{}})
      }
      if (this.data["args_is_dict"]==false) {
        activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelectorUIOActivity_Run_Dict", "ArgList":[uio, action_str, true, textarea_value], "ArgDict":{}})
      } else {
        activity_list.push({"Def":"pyOpenRPA.Robot.UIDesktop.UIOSelectorUIOActivity_Run_Dict", "ArgList":[uio, action_str, true, null, textarea_value], "ArgDict":{}})
      }
    } else {
      if (in_ui_focus_bool==true) {
        activity_list.push({"Def":"pyOpenRPA.Robot.UIWeb.UIOSelectorFocusHighlight", "ArgList":[uio], "ArgDict":{}})
      }
      if (this.data["args_is_dict"]==false) {
        activity_list.push({"Def":"pyOpenRPA.Robot.UIWeb.UIOSelectorActivityRun", "ArgList":[uio, action_str, textarea_value], "ArgDict":{}})
      } else {
        activity_list.push({"Def":"pyOpenRPA.Robot.UIWeb.UIOSelectorActivityRun", "ArgList":[uio, action_str, null, textarea_value], "ArgDict":{}})
      }
    }
    orpa_api_activity_list_execute_async_json_many(callback, activity_list)
  }

  run = function() {
    this.focus_run(false)
  }

  on_change_dropdown = function(in_value) {

  }
  data_get = function() {
    return this.data

  }
  data_load = function(in_data) {
    this.data=in_data
    this.render()
  }
  args_value_save = () =>  {
    var arg_textarea = $("#"+this.html_id_str+" .orpa-arg-textarea")[0]
    if (this.data["args_is_dict"]) {
      this.data["args_value_dict_str"]=arg_textarea.value
    } else {
      this.data["args_value_list_str"]=arg_textarea.value
    }
  }

  render = function() {
    var arg_textarea = $("#"+this.html_id_str+" .orpa-arg-textarea")[0]
    if (this.data["args_is_dict"]) {
      arg_textarea.setAttribute("placeholder", "{\"key1\":\"Привет\", \"key2\":\"Мир\"}")
      arg_textarea.value=this.data["args_value_dict_str"]
    } else {
      arg_textarea.setAttribute("placeholder", "[\"key1\",\"key2\"]")
      arg_textarea.value=this.data["args_value_list_str"]
    }
    
    // МОДУЛЬ ИЛИ ОБЪЕКТ
    if (this.data["is_module_bool"]) {
      this.data["function_list"]=this.help_function_list
      orpa_range_select($("#"+this.html_id_str+" .orpa-module")[0])
      // РЕНДЕРИНГ ПОД СВОЙСТВО
      $("#"+this.html_id_str+" .orpa-args-title")[0].style.setProperty("display","none")
      $("#"+this.html_id_str+" .orpa-help-title")[0].style.removeProperty('display');
      
      arg_textarea.setAttribute("disabled","")
      arg_textarea.style.setProperty("height","101px")
      $("#"+this.html_id_str+" .orpa-button-focus-run")[0].style.setProperty("display","none")
      $("#"+this.html_id_str+" .orpa-code-focus-run")[0].style.setProperty("display","none")
      $("#"+this.html_id_str+" .orpa-button-run")[0].style.setProperty("display","none")
      $("#"+this.html_id_str+" .orpa-code-run")[0].style.setProperty("display","none")
      arg_textarea.value = "Выбрать функцию модуля из списка выше. Код Python будет сгенерирован и скопирован в буфер обмена автоматически. Описание функции будет доступно для просмотра в этом окне после выбора функции."
      var in_value = this.data.function_str
      if (in_value!="" && in_value!=null) {
        if (in_value in this.help_code_generator_dict) {
          var help_str = this.help_code_generator_dict[in_value].help_str
          arg_textarea.value = help_str
        }
      }
      

    } else {
      orpa_range_select($("#"+this.html_id_str+" .orpa-object")[0])
      if (this.data["is_function_bool"]) {
        // РЕНДЕРИНГ ПОД ФУНКЦИЮ
        //Установить свойство disabled на textarea
        $("#"+this.html_id_str+" .orpa-args-title")[0].style.removeProperty('display');
        $("#"+this.html_id_str+" .orpa-help-title")[0].style.setProperty("display","none")
        var arg_textarea = $("#"+this.html_id_str+" .orpa-arg-textarea")[0]
        arg_textarea.removeAttribute("disabled")
        arg_textarea.style.setProperty("height","93px")
        $("#"+this.html_id_str+" .orpa-button-focus-run")[0].style.removeProperty("display")
        $("#"+this.html_id_str+" .orpa-code-focus-run")[0].style.removeProperty("display")
        $("#"+this.html_id_str+" .orpa-button-run")[0].style.removeProperty("display")
        $("#"+this.html_id_str+" .orpa-code-run")[0].style.removeProperty("display")
      } else {
        // РЕНДЕРИНГ ПОД СВОЙСТВО
        $("#"+this.html_id_str+" .orpa-args-title")[0].style.setProperty("display","none")
        $("#"+this.html_id_str+" .orpa-help-title")[0].style.removeProperty('display');
        var arg_textarea = $("#"+this.html_id_str+" .orpa-arg-textarea")[0]
        arg_textarea.setAttribute("disabled","")
        arg_textarea.style.setProperty("height","101px")
        $("#"+this.html_id_str+" .orpa-button-focus-run")[0].style.setProperty("display","none")
        $("#"+this.html_id_str+" .orpa-code-focus-run")[0].style.setProperty("display","none")
        $("#"+this.html_id_str+" .orpa-button-run")[0].style.removeProperty("display")
        $("#"+this.html_id_str+" .orpa-code-run")[0].style.removeProperty("display")
        arg_textarea.value="Выбранное наименование является свойством. Нажмите 'Выполнить', чтобы просмотреть его содержимое"

  
      }
      //Активация тэга вида аргументов (список или словарь)
      if (this.data["args_is_dict"]) {
        orpa_range_select($("#"+this.html_id_str+" .orpa-dict")[0])
      } else {
        orpa_range_select($("#"+this.html_id_str+" .orpa-list")[0])
      }


    }
    //Подгрузка списка
    var lValueList=[]
    ///Установка значений в dropdown
    var lFunctionList = this.data["function_list"]
    for (var i=0; i<lFunctionList.length; i++) {
      var value = lFunctionList[i]
      if (value==this.data["function_str"]) {
        lValueList.push({'name':value,'value':value, "selected":true})
      } else {
        lValueList.push({'name':value,'value':value})
      }
    }
    $("#"+this.html_id_str+" .orpa-dropdown")
      .dropdown({
        values: lValueList,
        onChange: this.on_change_function
      })
    ;


  }

}



class orpa_utils_tree {
  // Должна быть структура списка в HTML дереве с ID: orpa_utils_list_html_template
  constructor(in_html_id_str) {
    this.html_id_str = in_html_id_str
    this.items = [];
    this.item_selected_dict = null
    this.mode = 'TREE'; // 'LIST' or 'TREE'
    this.data_list = []
    /*
    [
      {
        "is_selected_bool":False,
        "title_str":"",
        "description_str":"",
        "action_list":[
          {"title_str":"", "callback_click":""}
        ],
        "callback_selected": null,
        "child_list": [
          ...
        ]
      }
    ]

    */
    this.source = document.getElementById('orpa_utils_list_html_template').innerHTML;
    Handlebars.registerPartial('orpa_utils_list_html_template', this.source);
    Handlebars.registerHelper('check_length', function (v1, v2, options) {
      'use strict';
      if (v1 != null) {
        if (v1.length>v2) {
          return options.fn(this);
       }
      }
        return options.inverse(this);
      });
    Handlebars.registerHelper('if_equals', function(arg1, arg2, options) {
        return (arg1 == arg2) ? options.fn(this) : options.inverse(this);
    });
    Handlebars.registerHelper('has_child_display', function(arg1, options) {
      return (arg1 == "HAS_CHILD" || arg1==null) ? options.fn(this) : options.inverse(this);
  });
  Handlebars.registerHelper('no_child_display', function(arg1, options) {
    return (arg1 == "NO_CHILD" || arg1==null) ? options.fn(this) : options.inverse(this);
});
    this.template = Handlebars.compile(this.source);

  }
  workspace_get() {
    return $("#"+this.html_id_str+" .orpa-utils-tree-workspace")[0]

  }
  loader_turn_on() {
    $("#"+this.html_id_str+" .dimmer")[0].classList.add("active");
  }

  loader_turn_off() {
      $("#"+this.html_id_str+" .dimmer")[0].classList.remove("active");
  }

  select(in_item) {
    // Очистить предыдущий выбор
    function clean_is_selected(in_dict) {
      in_dict.forEach((item, index) => {
        in_dict[index].is_selected_bool=false
        if (item.child_list) {
          clean_is_selected(item.child_list);
        }
      });
    }
    clean_is_selected(this.data_list);
    // Установить новый
    in_item.is_selected_bool=true
    this.render() //Рендеринг
  }
  unselect() {
    // Очистить предыдущий выбор
    function clean_is_selected(in_dict) {
      in_dict.forEach((item, index) => {
        in_dict[index].is_selected_bool=false
        if (item.child_list) {
          clean_is_selected(item.child_list);
        }
      });
    }
    clean_is_selected(this.data_list);
    this.render() //Рендеринг
  }

  render() {
    //Сформировать ограниченный список, если есть потомки
    var new_data_list = []
    if (this.mode == 'LIST') {
      var def_recursive = function (in_list, new_data_list) {
        in_list.forEach((item, index) => {
          if (item.child_list==null || item.child_list.length == 0) {
            new_data_list.push(item) 
          } else {
            if (Array.isArray(item.child_list)) {
              def_recursive(item.child_list, new_data_list)
            }
            
          }
        })
      }
      def_recursive(this.data_list, new_data_list)
    } else {
      new_data_list = this.data_list
    }

    // JavaScript код
    var context = {
      data_list: new_data_list
    };
    var html = this.template(context);
    var l_tree = this.workspace_get();
    if (new_data_list.length==0) {
      l_tree.style['background-color'] = "#e8e8e8"
    } else {
      l_tree.style['background-color'] = ""
    }

    l_tree.innerHTML = html;
    var item_list = $("#"+this.html_id_str+" .item")
    orpa_utils_map_html_dict(this, new_data_list, item_list) // Связывание HTML с JS рекурсивным списком
    $('.orpa-utils-tree-popup').popup();
  }

  hide() {
    this.items.forEach(item => item.style.display = 'none');
  }

  show() {
    this.items.forEach(item => item.style.display = 'block');
  }

  clear() {
    this.data_list=[]
    this.render()
  }

  load(in_data_list) {
    this.data_list = in_data_list
    this.render()
  }
  /// УСТАНОВИТЬ РЕЖИМ ОТОБРАЖЕНИЯ ('LIST' || 'TREE'), ПОСЛЕ ЧЕГО ВЫПОЛНИТЬ ПЕРЕРИСОВЫВАНИЕ
  mode_set(in_mode_str) {
    this.mode = in_mode_str;
    this.render();
  }
}
mGlobal={}
$(document)
  .ready(function() {
        // Инициировать поиск объекта по мыши (UIO/XPATH/CSS) in_callback(in_data)
        orpa_desktop_search_mouse=function(in_selector, in_callback) {
          orpa_api_activity_list_execute_async(in_callback, "pyOpenRPA.Robot.UIDesktop.UIOSelector_SearchChildByMouse_UIOTree", in_arg_list=[in_selector])
        }
        // Получить потомков по селектору (UIO/XPATH/CSS). in_callback(in_data)
        orpa_desktop_childs=function(in_selector, in_callback) {
          orpa_api_activity_list_execute_async(in_callback, "pyOpenRPA.Robot.UIDesktop.UIOSelector_GetChildList_UIOList", in_arg_list=[in_selector])
        }
      // Получить информацию об уровнях по селектору - 1й элемент (UIO/XPATH/CSS). in_callback(in_data)
      orpa_desktop_levels=function(in_selector, in_callback) {
        orpa_desktop_level.loader_turn_on();
        orpa_desktop_property.loader_turn_on();
        orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIDesktop.UIOSelector_LevelInfo_List", in_arg_list=[in_selector])
      }


          orpa_api_activity_list_execute_sync_json = function (in_activity_name_str, in_arg_list=null, in_arg_dict=null) {
            return JSON.parse(orpa_api_activity_list_execute_sync(in_activity_name_str, in_arg_list, in_arg_dict))
          }
          orpa_api_activity_list_execute_sync = function (in_activity_name_str, in_arg_list=null, in_arg_dict=null) {
            if (in_arg_list==null) { in_arg_list=[] }
            if (in_arg_dict==null) { in_arg_dict={} }
            var l_data_dict = {
              "Def": in_activity_name_str,
              "ArgList": in_arg_list,
              "ArgDict": in_arg_dict
            }
            var l_response_data=null
            ///Загрузка данных
            $.ajax({
              type: "POST",
              url: '/api/activity-list-execute',
              data: JSON.stringify(l_data_dict),
              success: function(in_data)
                {
                    l_response_data=in_data
                },
              dataType: "text",
              async:false
            });
            try {

              data_json = JSON.parse(l_response_data)
              if ("ErrorHeader" in data_json) {
                if (data_json["ErrorTraceback"].indexOf("There are no UI elements by selector (UIO / XPATH / CSS)")!=-1) {
                  orpa_utils_modal_uio_no_elements();
                } else {
                  
                  orpa_workspace_modal_show("GUI Error",data_json.ErrorHeader+" \nTraceback: "+data_json.ErrorTraceback);
                  throw new Error('Со стороны сервера поступила ошибка - прервать обработку JS');
                }

              }
              
            }
            catch(e) {

            }

            return l_response_data
        }

        
        orpa_api_activity_list_execute_async_json = function (in_success_callback, in_activity_name_str, in_arg_list=null, in_arg_dict=null) {
          orpa_api_activity_list_execute_async(function(in_data) {in_success_callback(JSON.parse(in_data))},in_activity_name_str, in_arg_list=in_arg_list, in_arg_dict=in_arg_dict)
        }
          orpa_api_activity_list_execute_async_json_many = function(in_success_callback, in_activity_list) {
            //in_activity_list [{"Def":"", "ArgList":[], "ArgDict":{}}]
          orpa_api_activity_list_execute_async_many(function(in_data) {in_success_callback(JSON.parse(in_data))},in_activity_list)
        }
        orpa_api_activity_list_execute_async_many = function(in_success_callback, in_activity_list) {
          // in_activity_list: [{"Def":"", "ArgList":[], "ArgDict":{}}]
          var l_response_data=null
          ///Загрузка данных
          $.ajax({
            type: "POST",
            url: '/api/activity-list-execute',
            data: JSON.stringify(in_activity_list),
            success: function(in_data){
                data_json = JSON.parse(in_data)
                data_json.forEach(element => {
                  try {
                    if ("ErrorHeader" in element) {
                      if (element["ErrorTraceback"].indexOf("There are no UI elements by selector (UIO / XPATH / CSS)")!=-1) {
                        orpa_utils_modal_uio_no_elements();
                      } else {
                        
                        orpa_workspace_modal_show("GUI Error",element.ErrorHeader+" \nTraceback: "+element.ErrorTraceback);
                        throw new Error('Со стороны сервера поступила ошибка - прервать обработку JS');
                      }
      
                    }
                  }
                  catch(e) {
      
                  }
              });
              in_success_callback(in_data)},
            dataType: "text"
          });
          return l_response_data
        }
        orpa_api_activity_list_execute_async = function (in_success_callback, in_activity_name_str, in_arg_list=null, in_arg_dict=null) {
          if (in_arg_list==null) { in_arg_list=[] }
          if (in_arg_dict==null) { in_arg_dict={} }
          var l_data_dict = {
            "Def": in_activity_name_str,
            "ArgList": in_arg_list,
            "ArgDict": in_arg_dict
          }
          var l_response_data=null
          ///Загрузка данных
          $.ajax({
            type: "POST",
            url: '/api/activity-list-execute',
            data: JSON.stringify(l_data_dict),
            success: function(in_data){
              try {

                data_json = JSON.parse(in_data)
                if ("ErrorHeader" in data_json) {
                  if (data_json["ErrorTraceback"].indexOf("There are no UI elements by selector (UIO / XPATH / CSS)")!=-1) {
                    orpa_utils_modal_uio_no_elements();
                  } else {
                    
                    orpa_workspace_modal_show("GUI Error",data_json.ErrorHeader+" \nTraceback: "+data_json.ErrorTraceback);
                    throw new Error('Со стороны сервера поступила ошибка - прервать обработку JS');
                  }
  
                }
                
              }
              catch(e) {
  
              }
              in_success_callback(in_data)},
            dataType: "text"
          });
          return l_response_data
      }


      /////////////////////////////////////////////////////////////////
      ///ПАРАМЕТРЫ
      /////////////////////////////////////////////////////////////////
      mGlobal.GenerateUniqueID=function(inPrefix) {
          return inPrefix+Math.round(Math.random()*1000)+"-"+Math.round(Math.random()*10000)+"-"+Math.round(Math.random()*1000)
      }

      jump = function (h){
        //var top = document.getElementById(h).offsetTop; //Getting Y of target element
        //window.scrollTo(0, top);                        //Go there directly or some transition
        $(h)[0].scrollIntoView();
        window.scrollTo(0, window.scrollY-20);
      };


      
      
      clipboard_set=function(lText) {
          //const el = document.createElement('textarea');
          //el.value = lText;
          //document.body.appendChild(el);
          //el.select();
          navigator.clipboard.writeText(lText)
          //document.body.removeChild(el);
      };
      ///////////////////////////
      ///Функция нормализации текстовой строки для HTML
      ///////////////////////////

      oldHTMLNormalizeStr=function(inString)
      {
          lResult=inString;
          lResult=lResult.replace(/&/g,"&amp;");
          lResult=lResult.replace(/</g,"&lt;");
          lResult=lResult.replace(/>/g,"&gt;");
          lResult=lResult.replace(/"/g,"&quot;");
          lResult=lResult.replace(/'/g,"&#39;");
          return lResult;
      }
      ///Функция перезапуска студии
      oldfRestartStudioServer= function()
      {
          ///Загрузка данных
          $.ajax({
            type: "POST",
            url: 'RestartStudio',
            data: '',
            success: 
              function(lData,l2,l3)
              {
                  var lResponseJSON=JSON.parse(lData);
              },
            dataType: "text"
          });
      }
      
      ///Функция клонирования объекта
      mGlobal.iSysClone=function(obj,lIsCloneSubProperty,lSubItemCallback) {
          ///Выполнить инициализацию переменной, если она не была передана
          if (typeof(lIsCloneSubProperty)=="undefined") {
              lIsCloneSubProperty=true;
          }
          ///Вернуть значение, если передан простой тип данных
          if (null == obj || "object" != typeof obj) return obj;
          ///Выполнить инициализацию новой переменной
          var copy = obj.constructor();
          ///Циклический обход по всем свойствам объекта
          for (var attr in obj) {
              ///Исключить присваивание тех свойств, которые унаследованы от прототипа
              if (obj.hasOwnProperty(attr)) {
                  ///Проверить, является ли вложенное свойство объектом
                  if (typeof(obj[attr])=="object" && lIsCloneSubProperty) {
                      ///Рекурсивный вызов клонирования дочернего элемента
                      copy[attr] = mGlobal.iSysClone(obj[attr],lIsCloneSubProperty);
                  } else {
                      ///Клонируемое свойство не является объектом - выполнить копирование
                      copy[attr] = obj[attr];
                  }
                  ///Вызов callback функции в которую передается текущий атрибут
                  if (typeof(lSubItemCallback)!="undefined") {
                      lSubItemCallback(copy[attr]);
                  }
              }
          }
          ///Вернуть результат функции клонирования
          return copy;
      }
    
      

    // fix main menu to page on passing
    $('.main.menu').visibility({
      type: 'fixed'
    });
    $('.overlay').visibility({
      type: 'fixed',
      offset: 80
    });

    // lazy load images
    $('.image').visibility({
      type: 'image',
      transition: 'vertical flip in',
      duration: 500
    });

    // show dropdown on hover
    $('.main.menu  .ui.dropdown').dropdown({
      on: 'hover'
    });

      orpa_workspace_modal_show=function(inHeaderText,inMessageText)
      {
          //Установка заголовка
          $('#orpa-utils-modal-template.ui.modal div.header').html(inHeaderText);
          //Установка текста
          $('#orpa-utils-modal-template.ui.modal div.content p').html(inMessageText);
          //Активация модального окна
          $('#orpa-utils-modal-template.ui.modal').modal('show');
      }
      orpa_workspace_expand=function(){
          $("#orpa-desktop")[0].style.setProperty('width', "inherit", "important")
          $("#orpa-project")[0].style.setProperty('width', "inherit", "important")
          $("#orpa-browser")[0].style.setProperty('width', "inherit", "important")
          $("#orpa-keyboard")[0].style.setProperty('width', "inherit", "important")
          $("#orpa-mouse")[0].style.setProperty('width', "inherit", "important")
          $("#orpa-gpt")[0].style.setProperty('width', "inherit", "important")
          $("#orpa-workspace-expand")[0].style.setProperty('display', "none")
          $("#orpa-workspace-compress")[0].style.setProperty('display', "")
      }
      orpa_workspace_compress=function(){
          $("#orpa-desktop")[0].style.setProperty('width', "")
          $("#orpa-project")[0].style.setProperty('width', "")
          $("#orpa-browser")[0].style.setProperty('width', "")
          $("#orpa-keyboard")[0].style.setProperty('width', "")
          $("#orpa-mouse")[0].style.setProperty('width', "")
          $("#orpa-gpt")[0].style.setProperty('width', "")
          $("#orpa-tabs")[0].style.setProperty('width', "")
          $("#orpa-workspace-expand")[0].style.setProperty('display', "")
          $("#orpa-workspace-compress")[0].style.setProperty('display', "none")
      }

      orpa_keyboard_workspace_proportion_set = function (in_col_1, in_col_2, in_col_3) {
        l_class_list = ["one","two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "elewen", "twelve", "thirdteen", "fourteen", "fifthteen", "sixteen"]
        l_object_list = [$("#orpa-keyboard-col-1")[0], $("#orpa-keyboard-col-2")[0], $("#orpa-keyboard-col-3")[0]] 
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
      orpa_desktop_workspace_proportion_set = function (in_col_1, in_col_2, in_col_3) {
        l_class_list = ["one","two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "elewen", "twelve", "thirdteen", "fourteen", "fifthteen", "sixteen"]
        l_object_list = [$("#orpa-desktop-col-1")[0], $("#orpa-desktop-col-2")[0], $("#orpa-desktop-col-3")[0]] 
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

      orpa_range_toogle=function(in_css_selector_or_object){
        if (orpa_range_is_selected(in_css_selector_or_object)==true) {
            orpa_range_unselect(in_css_selector_or_object)
        } else {
            orpa_range_select(in_css_selector_or_object)
        }
    }
    orpa_range_is_selected=function(in_css_selector_or_object) {
        var l_object = in_css_selector_or_object
        if (typeof(in_selector_or_object) == "string") {
            l_object = $(in_css_selector_or_object)[0]
        }
        return l_object.classList.contains("teal")
    }
    orpa_range_select=function(in_css_selector_or_object, in_only_this_bool = false) {
        var l_object = in_css_selector_or_object
        if (typeof(in_selector_or_object) == "string") {
            l_object = $(in_css_selector_or_object)[0]
        }
        //ПРОВЕРИТЬ НАЛИЧИЕ ОСТАЛЬНЫХ ЭЛЕМЕНТОВ ГРУППЫ
        if (in_only_this_bool==false) {
            l_orpa_data_key_str = l_object.getAttribute("orpa-data-key")
            l_group = $("[orpa-data-key='"+l_orpa_data_key_str+"']")
            for (var i=0;i<l_group.length; i++) {
                if (l_group[i]!=l_object) {
                    //UNSELECT
                    orpa_range_unselect(l_group[i], true) 
                }

            }
        
        }
        // УСТАНОВИТЬ СВОЙСТВО ПО ТЕКУЩЕМУ ОБЪЕКТУ
        l_object.classList.add("teal")
    }
    orpa_range_value_get=function(in_orpa_data_key, in_default=null) {
      //ПРОВЕРИТЬ НАЛИЧИЕ ОСТАЛЬНЫХ ЭЛЕМЕНТОВ ГРУППЫ
        l_group = $(".teal[orpa-data-key='"+in_orpa_data_key+"']")
        if (l_group.length>0) {
          return l_group[0].getAttribute("orpa-data-value")
        } else {
          return in_default
        }
  }

  orpa_range_value_set=function(in_orpa_data_key, in_orpa_data_value,  in_default=null) {
    //ПРОВЕРИТЬ НАЛИЧИЕ ОСТАЛЬНЫХ ЭЛЕМЕНТОВ ГРУППЫ
      l_group = $("[orpa-data-key='"+in_orpa_data_key+"'][orpa-data-value='"+in_orpa_data_value+"']")
      if (l_group.length>0) {
        orpa_range_select(l_group[0])
        return l_group[0]
      } else {
        return in_default
      }
}


  orpa_range_get=function(in_orpa_data_key, in_orpa_data_value) {
    //ПРОВЕРИТЬ НАЛИЧИЕ ОСТАЛЬНЫХ ЭЛЕМЕНТОВ ГРУППЫ
      l_group = $("[orpa-data-key='"+in_orpa_data_key+"'][orpa-data-value='"+in_orpa_data_value+"']")
      if (l_group.length>0) {
          return l_group[0]
      } else {
        return null
      }
}
    orpa_range_unselect=function(in_css_selector_or_object, in_only_this_bool = false) {
        var l_object = in_css_selector_or_object
        if (typeof(in_selector_or_object) == "string") {
            l_object = $(in_css_selector_or_object)[0]
        }
        //ПРОВЕРИТЬ НАЛИЧИЕ ОСТАЛЬНЫХ ЭЛЕМЕНТОВ ГРУППЫ
        if (in_only_this_bool==false) {
            l_orpa_data_key_str = l_object.getAttribute("orpa-data-key")
            l_group = $("[orpa-data-key='"+l_orpa_data_key_str+"']")
            for (var i=0;i<l_group.length; i++) {
                if (l_group[i]!=l_object) {
                    //UNSELECT
                    orpa_range_unselect(l_group[i], true) 
                }

            }
        
        }
        // УСТАНОВИТЬ СВОЙСТВО ПО ТЕКУЩЕМУ ОБЪЕКТУ
        l_object.classList.remove("teal")
    }

    
    orpa_project_jupyter_refresh = function() {
      iframe = document.getElementById("orpa-project-iframe");
      iframe.src = iframe.src;
    }
    orpa_project_jupyter_fullscreen = function() {
      document.getElementById("orpa-project-iframe").requestFullscreen();
    }

    orpa_project_jupyter_set_path=function() {
      $.ajax({
        type: "POST",
        url: '/api/orpa-lab-set-path',
        data: "",
        dataType: "text"
      });
    }

    orpa_project_jupyter_open_path=function() {
      $.ajax({
        type: "POST",
        url: '/api/orpa-lab-open-path',
        data: "",
        dataType: "text"
      });
    }

    ////////////////////////////////////////////////////
    ///////// ORPA API НАЧАЛО /////////////////
    ////////////////////////////////////////////////////
    // UIO, CSS, XPATH
    orpa_api_uidesktop_selector_convert = function(in_selector, in_type_str, in_callback, in_type_from_str=null) {
      switch (true) {
        case in_type_from_str=="XPATH" && in_type_str=="UIO":
          orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIDesktop.XPATH_To_UIOSelector", [in_selector], null)
          break;
        case in_type_from_str=="UIO" && in_type_str=="XPATH":
          orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIDesktop.UIOSelector_To_XPATH", [in_selector], null)
          break;
        case in_type_from_str=="CSS" && in_type_str=="UIO":
          orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIDesktop.CSS_To_UIOSelector", [in_selector], null)
          break;
        case in_type_from_str=="UIO" && in_type_str=="CSS":
            orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIDesktop.UIOSelector_To_CSS", [in_selector], null)
          break;
        default:
          orpa_api_activity_list_execute_async_json(in_callback, "pyOpenRPA.Robot.UIDesktop.Selector_Convert_Selector", [in_selector, in_type_str], null)
          break;
      }
    }

    orpa_api_helper_def_autofill_merge=function(inTargetDict, inLastDict) {
      // Merge 2 dict (get values from Last dict if key exists in new dict
      for (const [lKeyStr, lValue] of Object.entries(inTargetDict)) {
        //Check if key exists in LastDict
        if (lKeyStr in inLastDict) {
          inTargetDict[lKeyStr] = inLastDict[lKeyStr]
        }
      }
      return inTargetDict
    }
    // Debugging onchange def autofill init
    orpa_api_helper_def_autofill = function(in_def_name_str){
      lValueStr = in_def_name_str
      $.ajax({
              type: "GET",
              url: '/orpa/api/helper-def-autofill/'+lValueStr,
              data: null,
              success:
              function(lData,l2,l3)
              {
                  var lResponseJSON=JSON.parse(lData)
                  //ArgDict merge
                  var lArgDictTargetDict = lResponseJSON["ArgDict"]
                  if (lArgDictStr !="" && lArgDictStr !=null) {
                    lArgDictLastDict = JSON.parse(lArgDictStr)
                    lArgDictTargetDict = orpa_api_helper_def_autofill(lArgDictTargetDict, lArgDictLastDict)
                    return lResponseJSON
                  }

        
              },
              dataType: "text"
          });
    }


    orpa_utils_modal_uio_no_elements = function() {
      $("#orpa-utils-modal-uio-no-elements").modal("show")
    }

    orpa_utils_modal_uio_search_mouse_show = function() {
      $("#orpa-utils-modal-uio-search-mouse").modal({closable:false}).modal("show")
    }
    orpa_utils_modal_uio_search_mouse_hide = function() {
      $("#orpa-utils-modal-uio-search-mouse").modal("hide")
    }
    

    ////////////////////////////////////////////////////
    ///////// ORPA API КОНЕЦ /////////////////
    ////////////////////////////////////////////////////



    // ОБНОВИТЬ СОСТОЯНИЕ ВКЛАДОК
    orpa_tabs_render=function() {
      l_group = $(".orpa-tab.ui.tag.label")
      for (var i=0;i<l_group.length; i++) {
        l_workspace_id = l_group[i].getAttribute("orpa-data-value")
        l_workspace = $("#"+l_workspace_id)[0]
        if (l_workspace!=null) {
          l_workspace.style.setProperty('display', "none") 
        }
        
      }
      css_selector_str = ".orpa-tab.teal.ui.tag.label"
      l_workspace_id = $(css_selector_str)[0].getAttribute("orpa-data-value")
      $("#"+l_workspace_id)[0].style.setProperty('display', "")
    }

      $('.tabular.menu .item').tab();
      orpa_tabs_render()
  })
;