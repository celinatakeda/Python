from datetime import date
cores = {'limpa':'\033[m', 'green':'\033[32m'}
neg = {'negative':'\033[7m'}
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {}{}{}{} é BISSEXTO'.format(neg['negative'], cores['green'], ano, cores['limpa']))
else:
    print('O ano {}{}{}{} NÃO é BISSEXTO'.format(neg['negative'], cores['green'], ano, cores['limpa']))