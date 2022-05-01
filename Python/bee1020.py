d = int(input())

ianos = d // 365
d = d - ianos*365

imeses = d // 30
d = d - imeses*30

idias = d // 1
d = d - idias*1

print('{} ano(s)'.format(ianos))
print('{} mes(es)'.format(imeses))
print('{} dia(s)'.format(idias))