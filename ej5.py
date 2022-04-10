import re

if __name__ == '__main__':
    inp = input()
    exp = r"(\w+)\s+\d+\s+\-\-\-\s+\[(\w+)\]\s*(\w+\.)*([A-Z]{1}\w+)\s*\:\s*(.+)"
    resul = re.findall(exp, inp)
    for el in resul:
        print(f"""\"{el[0]}","{el[1]}","{el[3]}","{el[4]}\"""")