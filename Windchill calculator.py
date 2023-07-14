



'''
Author: Matthew Harris
File: W13_Prove.py
'''



def wind_chill(temp_far, speed):
    feel = 35.74 + (0.6215 * temp_far) - 35.75 * (speed ** 0.16) + (0.4275 * temp_far) * (speed ** 0.16)
    print(f'At temperature {temp_far:.2f}F, and wind speed {speed} mph, the windchill is: {feel:.2f}F')
    



speed = 5

temp = int(input('What is the temperature? '))
scale = input('Is that in C or F? ')

if scale.upper() == 'F':
    temp_far = temp

else:
    temp_far = (temp * (9 / 5)) + 32



while speed < 61:
    wind_chill(temp_far, speed)
    speed += 5














