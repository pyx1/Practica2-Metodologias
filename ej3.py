import re

if __name__ == '__main__':
    expral = r"\b([a-zA-Z]{1})(\.)(\w{2,})(\.)(\d{4})(\@alumnos\.urjc\.es)\b" #Nos interesa el 2 y el 4
    exprpr = r"\b([a-zA-Z]+)(\.)([a-zA-Z]+)(\@urjc\.es)\b" #Nos interesa el 0 y el 2
    inp = input()
    lial = re.findall(expral, inp)
    lipr = re.findall(exprpr, inp)
    for el in lial:
        print(f"alumno {el[2]} matriculado en {el[4]}")
    for el in lipr:
        print(f"profesor {el[0]} apellido {el[2]}")