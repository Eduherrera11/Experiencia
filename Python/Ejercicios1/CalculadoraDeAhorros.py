name = input('Como es tu nombre? ')
print('Es un placer ', name.title())

dinero = int(input('Cuanto dinero ganas por hora? '))
horas = int(input('Cuantas horas trabajas a la semana ? '))
salario_semanal = dinero*horas
ganancias_anuales = salario_semanal*52
print(name,' Tienes unas ganancias anuales de ', ganancias_anuales, ' de euros')
gastos_semanales = int(input('Cuanto gastas a la semana ? '))
gasto_anual = gastos_semanales*52
ahorro = ganancias_anuales - gasto_anual

print(name,' tu ahorro anual es de ', ahorro)
