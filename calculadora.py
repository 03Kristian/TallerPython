# calculadora basica


# variables


volver = "y"

while volver == "y":
# condicionales
    if volver == "y":
        
        num1 = float(input("Digite un numero :"))
        num2 = float(input("Digite un segundo numero :"))
        operacion = input("Digite un operador + - % * ")
        if operacion == "+":
            print(" ")
            print(" RESPUESTA: ", num1,"+",num2,"=", num1+num2)
        elif operacion == "-":
            print(" ")
            print(" RESPUESTA: ", num1,"-",num2,"=", num1-num2)
        elif operacion=="*":
            print(" ")
            print(" RESPUESTA: ", num1,"*",num2,"=", num1*num2)
        else:
            if num2 != 0:
                print(" RESPUESTA: ", num1/num2)
    else:
        input("OPERACION IMPOSIBLE")

    print("----------------------------------------------------------------")
    print("--------------------------CONTINUAR?----------------------------")
    volver= input("VOLVER Y/N: ")
#result = float(num1) + float(num2)


# retorno