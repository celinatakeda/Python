from math import radians, sin, cos, tan
cores = {'limpa':'\033[m', 'blue':'\033[34m'}
a = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))
print('O ângulo de {}{}{} tem SENO de {:.2f}'.format(cores['blue'], a, cores['limpa'], seno))
print('O ângulo de {}{}{} tem COSSENO de {:.2f}'.format(cores['blue'], a, cores['limpa'], cos))
print('O ângulo de {}{}{} tem a TANGENTE de {:.2f}'.format(cores['blue'], a, cores['limpa'], tan))
