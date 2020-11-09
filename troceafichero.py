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
import sys
import argparse

dir = "tmp"

'''
 Funcion check_Opciones encargada de validar las opciones de entrada
'''
def check_Opciones():
    # creamos objeto analizador argparse e indicamos que argumentos esperamos
    # contructor ArgumentParser toma varios argumentos
    parser = argparse.ArgumentParser(
        description = 'Trocea fichero en el numero de lineas que se indican',
        prog = 'python3 troceafichero.py', usage='%(prog)s [-h]'
    )
    parser.add_argument("-f", "--inputfile", help="fichero a trocear")
    parser.add_argument("-t", "--chucksize", help="tamaño fichero salilda en lineas", type = int, default = 0)
    #parser.add_argument("-f", "--inputfile", help="fichero a trocear", default = "rockyou.txt")
    #parser.add_argument("-t", "--chucksize", help="tamaño fichero salilda en lineas", type = int, default = 20000)
    parser.add_argument("-V", "--version", action='version', version='%(prog)s version 1.1')
    parser.add_argument("-v", "--verbose", help="output verbose", action="store_true")
    args = parser.parse_args()
    fileinput = args.inputfile
    chunk_size = args.chucksize
    #print(args)
    return fileinput, chunk_size

'''
Funcion main: principal
'''
def main():
    (filename, chunk_size) = check_Opciones()
    if ( chunk_size == 0 or not filename):
        print( "Faltan argumentos")
        exit()

    try:
        os.mkdir(dir)
    except OSError:
        print("Error al crear el directorio, ya existe directorio: %s" % dir)
        sys.exit()
    else:
        print("Directorio %s creado con exito" % dir)
    try:
        fileout = None
        for i, line in enumerate(fileinput.input(filename)):
            if i % chunk_size == 0:
                if fileout: fileout.close()
                fileout = open(dir + "/" + 'salida%d.txt' % (i/chunk_size), 'w')
            fileout.write(line)
        fileout.close()
    except IOError:
        print("No existe fichero %s" % filename)

if __name__ == "__main__":
    main()
