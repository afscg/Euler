pen = set()
search = 10000

for i in range(1, search):
    pen.add(i * (3 * i - 1) // 2)

ret = search

for i in pen:
    for j in pen:
          if i + j in pen:
              if i + j + j in pen:
                  ret = min(ret, i)
                  print(i, j, i + j, i + j + j)
