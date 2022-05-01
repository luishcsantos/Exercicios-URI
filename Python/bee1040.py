N1, N2, N3, N4 = input().split()
N1, N2, N3, N4 = float(N1), float(N2), float(N3), float(N4)
N1, N2, N3, N4 = round(N1, 1), round(N2, 1), round(N3, 1), round(N4, 1)

Media = ((N1*2) + (N2*3) + (N3*4) + (N4*1)) / 10
Media = round(Media, 1)
print("Media: {}".format(Media))

if Media >= 7.0:
    print("Aluno aprovado.")
elif Media < 5.0:
    print("Aluno reprovado.")
elif Media < 7.0 and Media >= 5.0:
    print("Aluno em exame.")
    
    NE = float(input())
    NE = round(NE, 1)
    print("Nota do exame: {}".format(NE))
    Media = (Media + NE) / 2
    
    if Media >= 5.0:
        print("Aluno aprovado.")
    elif Media < 5.0:
        print("Aluno reprovado.")
    
    print("Media final: {}".format(Media))