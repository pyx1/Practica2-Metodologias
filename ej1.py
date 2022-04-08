import re

if __name__ == '__main__':
    textt = input()
    expr = r"(^|\D)(\d{4})(\D|$)"
    li = re.findall(expr, textt)
    #print(li)
    for el in li:
        print(el[1])
