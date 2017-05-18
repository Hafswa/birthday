import calendar
name=input('ENTER NAME: ')
days=['Monday', 'Tuesday','Wednesday', 'Thursday',
      'Friday', 'Saturday', 'Sunday']
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']
print('Hey '+name+', I can tell the day of your Birthday')
D=input('Enter Day(1-31): ')
M=input('Enter Month(1-12): ')
Y=input('Enter Year: ')
day_number=int(D)
month_number=int(M)
year_number=int(Y)
day=calendar.weekday(month=month_number, day=day_number, year=year_number)
print(name+', your day of birth is '+ days[day]+' '+D+endings[day_number-1]+'/'+M+'/'+Y)
input('Press <Enter> to Exit')
