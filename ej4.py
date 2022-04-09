import re 

if __name__ == '__main__':
    inp = input()
    expr = r"\b(C\/|Calle)\s([A-ZÁÉÍÓÚ\u00d1]{1}[a-zà-ÿ\u00f1]+)\,?\s*([Nn]\º?)?\s*(\d+)\,\s*(\d{5})\b"
    result = re.findall(expr, inp)
    for el in result:
        #print(el)
        print(f"{el[4]}-{el[1]}-{el[3]}")#CP-NombreC/-SOLONUMERO