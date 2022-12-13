lut = {"ABC"[i] + " " + "XYZ"[j]: 1+((i + (j-1))%3)+j*3 for i in range(3) for j in range(3)}

with open("input") as f:
    print(sum(lut[i.rstrip()] for i in f))
