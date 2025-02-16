Voltaje_teo = [4.21 , 1.514, 4.21 , 0.5316, 0.6878, 0.3543, 0.3543, 0.1875, 0.3731, 0.125, 0.125]
Voltaje_exp = [4.20, 1.579, 4.20 , 0.499, 0.680, 0.348, 0.348, 0.180, 0.378, 0.123, 0.123]
error_volt = []
suma_error_volt = 0

corriente_teo = [ 4.21e-4, 3.148e-4 , 4.21e-4 , 1.063e-4 ,6.878e-4, 7.0866e-4, 3.5433e-4, 3.7516e-5, 3.7516e-5, 2.5e-5, 1.25e-5 ]
corriente_exp = [ 4.20e-4, 3.12e-4 , 4.20e-4 , 1.06e-4 ,6.850e-4, 7.063e-4, 3.496e-4, 3.720e-5, 3.720e-5, 2.5471e-5, 1.238e-5 ]
error_amp = []
suma_error_amp = 0

for i in range(len(Voltaje_exp)):
    v0 = float(Voltaje_exp[i]) - float(Voltaje_teo[i])
    v = abs(v0)
    error_volt.append(v)
    c0 = float(corriente_exp[i]) - float(corriente_teo[i])
    c = abs(c0)
    error_amp.append(c)
    
for i in range(len(error_amp)):
    suma_error_volt += suma_error_volt + error_volt[i]
    suma_error_amp += suma_error_amp + error_amp[i]
    
prom_error_volt = suma_error_volt / len(error_volt)
prom_error_amp = suma_error_amp / len(error_amp)
    
    
print('El error asociado al voltaje es:',error_volt, '\n') 
print('El error asociado al amperaje es:',error_amp, '\n')
print('El error promedio del voltaje es', prom_error_volt, '\n')
print('El error promedio de la corriente es:', prom_error_amp, '\n')

Rteo = 23.737e+3
Rexp = 23.8e+3
Volt = 10

Pteo = Volt**2/Rteo
Pexpo = Volt**2/Rexp
deltaP = abs(Pteo - Pexpo)

print('La Potencia teórica es:', Pteo , '; mientras que la experimental es:', Pexpo, 'Junco con su incertidumbre asociada de:', deltaP)

