def largestAltitude(gain):
    altitude = 0      
    highest = 0       

    for g in gain:
        altitude = altitude + g
        if altitude > highest:
            highest = altitude

    return highest

gain = [-5, 1, 5, 0, -7]
print(largestAltitude(gain))

gain = [-4, -3, -2, -1, 4, 3, 2]
print(largestAltitude(gain))


