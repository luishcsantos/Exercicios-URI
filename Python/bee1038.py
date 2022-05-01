cod, qtd = input().split()
cod, qtd = int(cod), int(qtd)

if cod == 1:
    total = float(qtd * 4.00)
    print("Total: R$ {:.2f}".format(total))
elif cod == 2:
    total = float(qtd * 4.50)
    print("Total: R$ {:.2f}".format(total))
elif cod == 3:
    total = float(qtd * 5.00)
    print("Total: R$ {:.2f}".format(total))
elif cod == 4:
    total = float(qtd * 2.00)
    print("Total: R$ {:.2f}".format(total))
elif cod == 5:
    total = float(qtd * 1.50)
    print("Total: R$ {:.2f}".format(total))