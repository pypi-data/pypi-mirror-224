def get_rect(in_uio):
    r = in_uio.element_info.rectangle
    rect_dict = {"x": r.left, "y": r.top, "width": r.right-r.left, "height": r.bottom-r.top}     
    return rect_dict

from .. import UIDesktop
from .. import Screen
#old: - GUISearchElementByRootXY
def get_list_by_x_y(in_uio,in_x,in_y,in_show_root_bool=False, in_flag_stop_first=False, in_uio_index_int = None, in_level_limit_int = 30, in_level_iterator = 0):
    """L+,W+: Техническая функция: Получить иерархию вложенности UIO объекта по заданным корневому UIO объекту, координатам X и Y.

    """
    #Инициализация результирующего значения
    result_level = [{'index':in_uio_index_int,'element':in_uio}]
    result =[]
    #Получить координаты текущего объекта
    uio_box = Screen.BoxParse(get_rect(in_uio))
    point = Screen.PointParse(in_x,in_y)
    #Добавить объект в результирующий, если координаты попадают в него
    if Screen.PointIsInBox(point, uio_box):
        # ТОЧКА ВНУТРИ - ПРОДОЛЖИТЬ ПОИСК
        # РЕКУРСИВНЫЙ ВЫЗОВ ПО ДЕТЯМ - ВОЗМОЖНО ЕСТЬ УРОВЕНЬ ГЛУБЖЕ
        child_index=0
        flag_first_branch_found=False
        if in_level_iterator<in_level_limit_int:
            for child_uio in in_uio.children():
                if in_flag_stop_first==True and flag_first_branch_found==True: break;
                child_result = get_list_by_x_y(child_uio,in_x,in_y, in_show_root_bool=True,in_flag_stop_first=in_flag_stop_first, in_uio_index_int=child_index, in_level_limit_int = in_level_limit_int, in_level_iterator = in_level_iterator+1)
                for item in child_result:
                    if in_show_root_bool==True: result.append(result_level+item)
                    else: result.append(item)
                    flag_first_branch_found = True
                    if in_flag_stop_first==True and flag_first_branch_found==True: break;
                child_index=child_index+1
        if in_show_root_bool==True and len(result)==0:
            result.append(result_level)
    return result


#old: - GUISearchElementByRootXY
def __UIOXY_SearchChild_ListDict(inRootElement,inX,inY,inHierarchyList=None, inShowRootBool=False, inFlagSearchAll=False):
    result = get_list_by_x_y(in_uio=inRootElement,in_x=inX,in_y=inY, in_show_root_bool=inShowRootBool, in_flag_stop_first=(not inFlagSearchAll))
    if len(result)==0: return [] 
    else: return result

#old: - GUISearchElementByRootXY
UIDesktop.UIOXY_SearchChild_ListDict = __UIOXY_SearchChild_ListDict