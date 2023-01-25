#Выполнено по формуле Кардано с сайта http://www.cleverstudents.ru/equations/cubic_equations.html#Cardano_formula.
import cmath, math
print ('укажите коофициенты согласно схеме a*x**3+b*x**2+c*x+d=0')
a = float(input("Коэффициет а\n"))
b = float(input("Коэффициет b\n"))
c = float(input("Коэффициет c\n"))
d = float(input("Коэффициет d\n"))
if a == 0:
    print ('уравнение не является кубическим, выберите другой коофициент')
else:
    b1 = float(b/a)
    b2 = float(c/a)
    b3 = float(d/a)
    p = float(-((b1**2)/3)+b2)
    q = float(((2*(b1**3))/27)-((b1*b2)/3)+b3)
    y = (((-q/2)+((q**2/4)+(p**3/27))**(1/2))**(1/3)+((-q/2)-((q**2/4)+(p**3/27))**(1/2))**(1/3))
        #тут получается комплексное число, я не уверен что корректно использовать его в рамках задания.    
    x = (y-b1/3)
    x1 = (x.real)
    print(round(x1,2))
