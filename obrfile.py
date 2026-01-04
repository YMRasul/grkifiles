def readplos(fi):
    print(f"Открываем файла {fi}")
    txt = []
    k = 0
    with open(fi, 'r',encoding='cp866') as file:
        for line in file:
            k = k + 1
            ms =  line.split('\x1d')
            s =  str(k).ljust(7," ")
            kol = len(ms)
            for i in range(kol-1):
                s =  s + " # " + ms[i]
            txt.append(s+'\n')
    return txt

#--------------------------------
def txtwrite(path,txt):
    e = 1
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(txt)
    return e
