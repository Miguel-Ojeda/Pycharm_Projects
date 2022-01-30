import datetime
import time

date = datetime.datetime.now()  # nos retorna un datetime object con todo los datos sobre ahora!!
print(date)  # --> 2022-01-30 21:29:25.717355

print(date.year, date.month, date.day, date.hour, date.minute, date.second, date.microsecond)
# --> 2022 1 30 21 30 54 951731

# Podemos convertir un UNIX epoch time a datetime...

ahora = datetime.datetime.fromtimestamp(time.time())
print(ahora)

# Lo anterior sirve para cualquier epoch timestamp que tengamos...

# Podemso comparar estos objetos, utilizando ==, > etc
halloween2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)
newyears2020 = datetime.datetime(2020, 1, 1, 0, 0, 0)
oct31_2019 = datetime.datetime(2019, 10, 31, 0, 0, 0)

print(halloween2019 == oct31_2019)  # --> True

# Si solo nos interesan fechas, podemos utilziar simplemente, un objeto tipo date
today = datetime.date.today()
print(today)

# Cuántos días he vivido??
# today = datetime.date(time.time())
birthday = datetime.date(1968, 9, 16)
dias_vividos = today - birthday
print(f'Días vividos: {dias_vividos.days}')  # utilizamos el atributo días, pq si no sería un timedelta tb con H, m, s


# timedelta data type: sirven para llevar la duración o tiempo transcurrido ...
delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)
# delta.days, delta.seconds, delta.microseconds  --> (11, 36548, 0)
print(delta.total_seconds())

# Cuándo será 1000 días después de hoy??
today = datetime.datetime.today()
thousand_days = datetime.timedelta(days=1000)
print(today + thousand_days)  # --> 2024-10-26 21:43:20.629638

# Converting datetime Objects into Strings: usando método strftime()  (f de formatear=
# Pasando una string a datetime: método strptime()  (p de parse)
# Ver documentación mejor...

