def otkr(files: str):
    with open (files, 'r' ) as f:
        data = f.read()
        rows = data.split('\n')
        result = []
        for row in rows:
            row = row.strip()
            if len(row) == 0:
                continue
            elems = row.split(' ')
            result += [[float(e) for e in elems]]
    acc = {}                                          
    for x, y, w in result:                            
        acc[(x, y)] = acc.get((x, y), 0) + w          # если такого ключа нету, то словаь место ошибки вернет значение 0
    clear_resul = [[x, y, w] for (x, y), w in acc.items()]   # items() - перебирает и ключи и значение
    clear_resul.sort()
    return clear_resul


if __name__ == '__main__':
    print("Работает как скрипт")