#https://www.youtube.com/watch?v=awxaRgUB4Kw Neet code solution!

def countBits(n):
    return [bin(i).count('1') for i in range(n+1)]

print(countBits(5))

