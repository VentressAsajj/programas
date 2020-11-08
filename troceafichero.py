"""
@nuria_imeq
Los ficheros worldlist generalmente son muy tochos.
este programa divide el fichero rockyou en ficheros
de 20000 lineas, lo cual es mas asumible si vas a lanzar
un ataque de fuerza bruta
"""
import fileinput

chunk_size = 20000
fout = None
for i, line in enumerate(fileinput.input('rockyou.txt')):
	if i % chunk_size == 0:
		if fout: fout.close()
		fout = open('salida%d.txt' % (i/chunk_size), 'w')
	fout.write(line)
fout.close()
