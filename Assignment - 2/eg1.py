#1. Convert the time entered in hh, min and sec into seconds.

hh = int(input('Enter the hours:'))
min = int(input('Enter the minutes:'))
sec = int(input('enter the seconds:'))

total_seconds = (hh * 3600)+(min * 60)+ sec

print('Total Secons =',total_seconds)