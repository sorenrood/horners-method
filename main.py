def horner(poly, n, x): 
    result = poly[0]   
    for i in range(1, n): 
        result = result * x + poly[i]
        print(result)
    return result 

x = 3
poly = [2, 5, 0, -4]
horner(poly, len(poly), x)