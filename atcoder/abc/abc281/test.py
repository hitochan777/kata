for i in range(10**5+1):
    for j in range(1,5):
        for k in range(10**j):
            val = str(i) + "." + str(k).zfill(j)
            f = float(val)
            print(val, f, round(f*10000), int(f*10000))
            assert round(f*10000) == int(f*10000)
