hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

mh=(mins+dura)%60
hh=((mins+dura)//60+hour)%24

print('The finishing time is =',hh,':',mh,'mins')
