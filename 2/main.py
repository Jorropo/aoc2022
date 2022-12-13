lut = {"ABC"[i] + " " + "XYZ"[j]: 1 + j + (3 if i == j else 6 if ((i + 1 ) % 3 == j) else 0) for i in range(3) for j in range(3)}

with open("input") as f:
    print(sum(lut[i.rstrip()] for i in f))
