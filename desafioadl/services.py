from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    x = [{'tarea': tarea, 'subtareas': tarea.subtareas.filter(eliminada=False)} for tarea in Tarea.objects.filter(eliminada=False)]
    imprimir_en_pantalla(x)

def crear_nueva_tarea(d):
    t = Tarea.objects.create(descripcion=d)
    t.save()
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(tarea_id):
    d_st = input('Ingresa sub tareas: ')
    t = Tarea.objects.get(pk=tarea_id)
    st = SubTarea.objects.create(descripcion=d_st,tarea_id=t)
    st.save()
    return recupera_tareas_y_sub_tareas()

def elimina_tarea():
    d = input('Ingresa tarea a eliminar: ')
    tarea = Tarea.objects.filter(descripcion=d).update(eliminada=True)
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea():
    d_st = input('Ingresa sub tarea a eliminar: ')
    sub_tarea = SubTarea.objects.filter(descripcion=d_st).update(eliminada=True)
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(datos):
    for dato in datos:
        print(f"[{dato['tarea'].id}] {dato['tarea'].descripcion}")
        for subtarea in dato['subtareas']:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")