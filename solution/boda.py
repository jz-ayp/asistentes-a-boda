"""
Asistentes a la boda
Concurso otoño 2024
Problema propuesto por Alex Villa
18:05 - 18:11
"""

# Entradas
invitados = set(eval(input()))
confirmados = set(eval(input()))
llegados = set(eval(input()))

# Proceso
colados = llegados - invitados
faltantes = invitados - llegados
confirmados_llegados = confirmados & llegados
invitados_llegados = invitados & llegados

# Salidas
print(len(colados))
print(len(faltantes))
print(len(confirmados_llegados))
print(len(invitados_llegados))
