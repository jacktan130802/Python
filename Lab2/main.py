# PyProg Lab2

def KRG():
    #King's rice grain exe 2.1
    print(2**64)

def MT():
    #Multiplication table exe 2.2
    num1= int(input("Enter an integer: "))
    for i in range(1,13):
        print(num1,' x ',i,' = ',num1*i)

def WIBR():
    #Will I be rich exe 2.4
    age=25
    annual_salary=3000*(12+3)
    annual_saving=annual_salary*0.3
    invest_in_jan=0
    amount_in_dec=0

    while(amount_in_dec<1000000):
        print("%2d\t%7d\t%7d\t%7d\t%7d" % (age, annual_salary, annual_saving, invest_in_jan, amount_in_dec))
        age=age+1
        annual_salary=annual_salary*1.1
        invest_in_jan=annual_saving+amount_in_dec
        annual_saving=annual_salary*0.3
        amount_in_dec=invest_in_jan*1.1
    print("%2d\t%7d\t%7d\t%7d\t%7d" % (age, annual_salary, annual_saving, invest_in_jan, amount_in_dec))


# Press the green button in the gutter to run the script.
count=0
while count<10:
    print(1)
    count+=3

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
