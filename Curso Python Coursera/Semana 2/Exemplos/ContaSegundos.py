segundos_str = input("Por favor, entre com um número de segundos que deseja converter: ")
total_segundos = int(segundos_str)

horas = total_segundos // 3600
seg_restantes = total_segundos % 3600
minutos = seg_restantes // 60
seg_restantes_final = seg_restantes % 60

print(horas, "horas ", minutos, "minutos, e", seg_restantes_final, "segundos.")