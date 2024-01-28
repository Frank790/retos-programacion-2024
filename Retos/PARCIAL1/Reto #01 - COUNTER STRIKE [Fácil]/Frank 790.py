l=int(input('Ingrese cantidad de participantes=  '))
acum=0
acumu=0
cont=0
band= True

for i in range (l):
    nombre= input('Ingrese el nombre del jugador: ')
    equipo= int(input('Indique a que equipo pertenece: presione 1 si es Profesor, 2 si es Estudiante  '))
    ene_elimi=int(input('Ingrese cantidad de enemigos que eliminó el jugador=  '))
    vec_elimi=int(input('Ingrese las veces que fue eliminado el jugador=  '))
    if equipo == 2:
        acum=acum+ene_elimi
        cont=cont+1
        
    if ene_elimi >= 100 and band:
         primer_jugador=nombre         
         equi_jugador=equipo
         band=False
         
    if equipo==1: 
        acumu=acumu+vec_elimi
         
prom=acum/cont
print(f'El promedio de enemigos que eliminaron los estudiantes fue= {prom:.2f}')
if equi_jugador==1:
    print(f'El jugador {primer_jugador} fue el primero en eliminar 100 enemigos y pertenece al equipo de Profesores ')
else:
    print(f'El jugador {primer_jugador} fue el primero en eliminar 100 enemigos y pertenece al equipo de Estudiantes ')
print(f'La cantidad total de veces que fueron eliminados jugadores del equipo de profesores fue= {acumu}')      

         
    
    
    
   