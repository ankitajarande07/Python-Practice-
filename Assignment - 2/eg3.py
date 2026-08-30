#3. Convert distant given in feet and inches into meter and centimeter.

feet = int(input('Enter the distance of feet:'))
inches = int(input('Enter the distance of inches:'))

Total_inches = feet * 12 + inches
cm = Total_inches*2.54
Meter = cm/100

print('Distance in meters:', Meter)
print('Distance in centimeters:', cm)

