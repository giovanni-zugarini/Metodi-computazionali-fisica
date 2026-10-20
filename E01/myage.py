from datetime import datetime, timedelta

oggi = datetime.now()

ddnstr = input('inserisci la tua data come gg-mm-yr hr:min:sec ')
ddn = datetime.strptime(ddnstr, "%d-%m-%Y %H:%M:%S")
timediff = oggi - ddn
totyr = oggi.year-ddn.year
tots = timediff.total_seconds()
totd = tots/(3600*24)
print('La mia data di nascità è: ',ddn)
print('La mia età in anni è: {:d}'.format(totyr))
print('La mia età in giorni è: {:f}'.format(totd))
print('La mia età in annisecondi è: {:f}'.format(tots))
