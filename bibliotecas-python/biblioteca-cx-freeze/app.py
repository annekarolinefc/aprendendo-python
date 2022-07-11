import os

inscritor_recentes = ['Rebeca', 'Rafael', 'Jeferson', 'Maria']

with open('inscritos.txt', 'w', newline='') as file:
    for line in inscritor_recentes:
        file.write(line + os.linesep)