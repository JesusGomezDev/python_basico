try:
    x = 10
    y = 20

    z = x + y

    print(a)
except TypeError:
    print('Error de tipado')
except ZeroDivisionError:
    print('Error de division')
except Exception as e:
    print(e)

print('El codigo continua')