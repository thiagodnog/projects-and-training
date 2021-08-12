segundos_str = input("Por favor, entre com um número de segundos que deseja converter: ")
total_segundos = int(segundos_str)

dias = total_segundos // 86400
seg_restantes = total_segundos % 86400
horas = seg_restantes // 3600
seg_restantes_2 = seg_restantes % 3600
minutos = seg_restantes_2 // 60
seg_restantes_final = seg_restantes_2 % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", seg_restantes_final, "segundos.")