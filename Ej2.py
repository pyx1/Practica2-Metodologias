import re

if __name__ == '__main__':
    a = input()
    pattern = r"\b((E(\-|\ )?)?(\d{4})(\-|\ )?([A-Z]{3}))\b"
    lista = re.findall(pattern, a)
    for match in lista:
        print(match[0])