#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = [] #Creamos nuestra lista
    for num in my_list: #Recorremos el elemento iterable
        if num == search: #El elemento va a ser igual a search que es el valor a remplazar
            new_list.append(replace)#Usamos .aprrend para agregar un valor a nuestra lista en este caso replace
        else:
            new_list.append(num)
    return new_list
