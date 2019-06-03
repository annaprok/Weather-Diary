import datetime
import json
import doctest


# Получить все записи из дневника
def getAll():
    """Get all elements from array.

                  """
    with open("data.json", "r") as read_file:
        days = json.load(read_file)
    return days


# Получить один елемент по id, None если не найден
def getById(id):
    """Get element by id from array.

                Return element if it exists and id > 0.

                Else return None


                >>> getById(-1)


                >>> getById('a')

              """
    if isinstance(id, str) :
        if not id.isnumeric():
            return None
        if id.int()<0:
            return None
    elif id < 0:
        return None

    data = getAll()
    for day in data:
        if day['id'] == id:
            return day
    return None


# Добавить запись с уникальным id температурой и типом погоды(солнечно, дождь и тд.) и текушей датой
# вертает True когда добавило и False наоборот
def add(id, temperature, weather):
    """Add element with specified id, temperature, weather type and current date to array.

            Return True if the id is unique and element is successfully added.

            Else return false


            >>> add(-1,"f","f")
            False

            >>> add(1,None,"f")
            False

            >>> add(1,"f",None)
            False

            >>> add(0,"0","Sunny")
            True

            >>> add(0,"0","Sunny")
            False

            """
    if temperature is None or weather is None or id < 0:
        return False
    if getById(id) is None:
        elem = {'id': id, 'date': datetime.date.today().strftime("%m, %d, %Y"), 'temperature': temperature,
                'weather': weather}
        days = getAll()

        days.append(elem)
        with open("data.json", 'w') as f:
            json.dump(days, f)
        return True
    return False


# Удалить по id, возвращает удаленній елемент
def delById(id):
    """Delete element with specified id from array.

        Return the deleted element if it exists.

        Else return None


        >>> delById(-1)

        None

        >>> delById("s")

        None

        """
    days = getAll()
    elem = getById(id)
    if elem is not None:
        days.remove(elem)
        with open("data.json", 'w') as f:
            json.dump(days, f)
            return elem
    return None

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    delById(0)


#print(add(3,  25, "sunny"))
# print(delById(3))
# print(getById())
# print(getAll())
