import math

def jarak(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Contoh penggunaan dengan titik (0, 0) dan (3, 4)
hasil = jarak(0, 0, 3, 4)
print("Jarak =", hasil)