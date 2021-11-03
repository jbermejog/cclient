''' Aplicación ejemplo activadades SCRUM
Calculadora de riesgo máximo para clientes empresa
Solicitamos mediante input la antiguedad de la empresa,
Los ingresos del año en curso y los gastos
Hacemos un cálculo que no tiene ningún fundamento real
el función de lo obtenido he definido varios propiedades
100000 no tienes credito
200000 Riesgo Alto hasta 20000 euros máx
300000 Riesgo Medio hasta 30000 euros máx
400000 Riesgo Bajo hasta 40000 euros máx
500000 Riesgo Muy Bajo hasta 50000 euros máx
------ SIN RIESGO Cliente perfecto, no hay límite, que pida lo que quiera

Como ejemplo introducir años 10 , ingresos 100000, gastos 50000, balance 10000
'''

from pywebio.input import input, FLOAT
from pywebio.output import put_html


def financialRisk():
    company = input("Nombre completo de la empresa：")
    year = input("Cuantos años tiene la empresa：", type=FLOAT)
    income = input("Importe de ingresos obtenidos el año pasado：", type=FLOAT)
    expense = input("Importe de gastos el año pasado ：", type=FLOAT)
    current = input("Balance a día de hoy de la empresa ：", type=FLOAT)
    fundation = 2021 - year
    years = 70 - year
    amount = income - expense * 0.5

    total = amount * years + current

    top_place = [(1000000, 'Muy Alto,'),
                 (2000000, 'Alto,'),
                 (3000000, 'Medio,'),
                 (4000000, 'Bajo,'),
                 (5000000, 'Muy Bajo,'),
                 (float('inf'), 'NINGUNO Cliente perfecto, no hay límite, que pida lo que quiera')]

    put_html('<h2>RESUMEN EJECUTIVO</h2><p>Hemos analizado el riesgo para la empresa <strong>%s</strong> \n<br/>Fundada en el año %s y hemos obtenido el siguiente resultado:</p>\n' % (
        company, fundation))

    for top, status in top_place:
        if total <= top:
            put_html('<p>Después de un calculo avanzado el sistema ha determinado el límite de crédito es: %.2f euros.</p>\n<p>El riesgo de impago por parte del cliente es <strong>%s</strong><br/> por lo que no recomendamos superar el importe de %.2f euros.</p>\n' % (
                total/100, status, top/100))
            break

    put_html('<h3>Gracias por utilizar el sistema de gestión financiera avanzada de Guns N&#39; Roses</h3>')

if __name__ == '__main__':
    financialRisk()
