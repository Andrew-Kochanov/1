import string
def srv(s):
    if all(st.index(s[i]) <= st.index(s[i + 1]) for i in range(len(s) - 1)):
        return True         ## функция сравнивает индексы всех элементов строки попарно(текущий - следующий) в
    else:                   ## перевернутой "аски" строке
        return False


lb = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
rb = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'
c = '0123456789'           ## создаем "аски" строку для проверки: знаки препинания, цифры, латинские буквы
zp = string.punctuation    ## (большие и маленькие), русские буквы(большие и маленькие)
st = zp + c + lb + rb
st = st[::-1]              ## разворачиваем для обратного лексикографического порядка
print(srv(input('Введите строку: ')))