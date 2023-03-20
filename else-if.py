ingreso_mensual = 1000
gasto_mensual = 80000

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit")
    elif ingreso_mensual- gasto_mensual > 3000:
        print ("Bien pa, estas bien")
    else:
        print("y pa, estas gastando una banda")
elif ingreso_mensual > 1000:
    print("estas bien en latinoamerica")
elif ingreso_mensual > 500:
    print("Estas bien en argentina")
elif ingreso_mensual > 200:
    print("Estas bien en Venezuela")
