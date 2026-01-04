from clr import clear_screen
from obrfile import readplos, txtwrite

if __name__ == '__main__':

    clear_screen()
    spr = input("\nВведите номер файла:")
    ms = spr.strip().split(',')

    fi1 = './in/N06040.' + ms[0].strip()

    if len(ms)>1:
        numberline = int(ms[1].strip())
        print(f"Показываем строку {numberline}")
    else:
        tx1 = readplos(fi1)
        file_path2 = './out/' + ms[0].strip() + '.txt'
        print("Записываем", file_path2)
        txtwrite(file_path2, tx1)

#    print(f"{spr=}")
#    fi1 = './in/N06040.008'
#    fi2 = './in/N06040.009'

    #tx1 = readplos(fi1)
    #print(tx1)

#    tx2 = readplos(fi2)
    #print(tx2)