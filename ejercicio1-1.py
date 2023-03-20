este_curso = 1.5
minimo_curso = 2.5
promedio_curso = 4.0
maximo_curso = 7.0
crudo_este_curso = 3.5
crudo_promedio = 5.0

diferencia1 = ((minimo_curso - este_curso)/minimo_curso)*100
diferencia2 = round(((maximo_curso - este_curso)/maximo_curso)*100,2)
diferencia3 = ((promedio_curso - este_curso)/promedio_curso)*100

#respuesta A
print("---------------------------------------")
print(f"La diferencia porcentual con el mas rapido es: {diferencia1}%")
print(f"La diferencia porcentual con el mas lento es: {diferencia2}%")
print(f"La diferencia porcentual con el promedio es: {diferencia3}%")

#respuesta B
print("---------------------------------------")
diferencia4 = round(((crudo_este_curso - este_curso)/crudo_este_curso)*100,2)
diferencia5 = round(((crudo_promedio - promedio_curso)/crudo_promedio)*100,2)
print(f"El porcentaje de material inservible se reduce en un {diferencia4}%")
print(f"El porcentaje de material inservible se reduce en un {diferencia5}%")

#respueta C

comparativa_promedio = round(promedio_curso / este_curso * 10, 2)
comparativa_promedio_reves = round(este_curso / promedio_curso * 10, 2)

print("---------------------------------------")
print(f"10 hs de este curso equivale a ver: {comparativa_promedio} hs de los otros cursos")
print(f"10 hs de otros cursos equivale a ver : {comparativa_promedio_reves} hs del curso de Dalton")
print("---------------------------------------")


