import sys

with open(sys.argv[1], "r", encoding="utf-8") as f1:
   lines = f1.readlines()
   coords = lines[0].split()
   x = int(coords[0])
   y = int(coords[1])
   radius = int(lines[1])

with open(sys.argv[2], "r", encoding="utf-8") as f2:
    infs = []
    lines = f2.readlines()
    if len(lines) <= 100 and len(lines) >= 1:
       for f in lines:
          f = f.split()
          fx = int(f[0])
          fy = int(f[1])
          sq_x = (fx - x) ** 2
          sq_y = (fy - y) ** 2
          dist = (sq_x + sq_y) ** 0.5
          if dist < radius:
            infs.append(1)
          elif dist == radius:
            infs.append(0)
          else:
            infs.append(2)
       print(*infs, sep='\n')
    else:
       print("Недопустимое количество точек")
