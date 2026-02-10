from storage import load_items, save_items
from typing import Optional

'''
1. Obtener items
2. Obtener items específicos( obtener items, buscar item por id, devolver resutlados)
3. Crear item (obtener items, ver id máximko, sumar 1)
4. Actualizar item(cargar items, busacr por id, recorrer clave-valor de data, guardar)
5. ELiminar item
'''

def get_items():
    return load_items()

def create_item(data:dict):
    items = load_items()
    if not items:
        item_id = 1
    for i in items:
        item_id = max(i[id])
    item_id += 1

    item = {"id":item_id, **data} # usamos ** para combinar datos al dict
    items.append(item)
    save_items(item)
    return item

def get_item_by_id(item_id:int):
    items= load_items()

    for item in items:
        if item["id"] == item_id:
            return item
    
    return None

def update_item(item_id:int, data:dict):
    items = load_items()  
    item = get_item_by_id(item_id)

    for clave, valor in data.items():
        if clave is not None:
            item[clave] = valor
    save_items(items)
    
    return None

# TO DO: delete_item(item_id)