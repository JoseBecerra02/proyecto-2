import os
import sys
import easygui as eg
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import horse as horse
import random


def main():
    def limpiar_consola():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    colores = ['white', 'brown', 'orange', 'purple', 'green', 'blue', 'black']
    cmap = ListedColormap(colores)

    tipoBusqueda = 0

    def cargarArchivo():
        # archivo = eg.fileopenbox(msg='Seleccione el archivo de entrada',
        #                          title='Goku Smart',
        #                          default="pruebas/000 horse.txt",
        #                          filetypes=["*.txt"],
        #                          multiple=False,
        #                          )
        archivo = "pruebas/000 horse.txt"
        if archivo is None:
            sys.exit(0)
        archivoInput = open(archivo, 'r')
        matriz = list()

        for i in range(8):
            listaT = []
            for j in range(8):
                listaT.append(int(archivoInput.readline(1)))
                archivoInput.readline(1)
            matriz.append(listaT)
        archivoInput.close()
        caballoB=0
        caballoN=0
        while caballoN==caballoB:
            caballoN=(random.randint(0, 7),random.randint(0, 7))
            caballoB=(random.randint(0, 7),random.randint(0, 7))
        print(caballoN)
        print(caballoB)
        matriz[caballoN[0]][caballoN[1]]=8
        matriz[caballoB[0]][caballoB[1]]=9

        for i in range(1,8):
            print(i)
            posicionN=(random.randint(0, 7),random.randint(0, 7))
            if matriz[posicionN[0]][posicionN[1]]==0:
                matriz[posicionN[0]][posicionN[1]]=i
            else:
                i=i-1

        for i  in range(len(matriz)):
            print(matriz[i])
        
        plt.imshow(matriz, cmap=cmap)
        plt.xticks([])
        plt.yticks([])
        plt.savefig('images/mallaGokuSmart.png',
                    bbox_inches='tight', pad_inches=0.05)
        plt.close()
        return matriz

    def preguntarTipoBusqueda():
        tipoBusqueda = eg.indexbox(msg='¿Qué tipo de búsqueda desea realizar con el siguiente input?',
                                   title='Goku Smart',
                                   choices=['Horse 1'],
                                   image='images/mallaGokuSmart.png'
                                   )

        if (tipoBusqueda == 0):
            print("Usted seleccionó Profundidad Evitando Ciclos, una ventana aparecerá cuando el algoritmo acabe, si el proceso es demorado significa que sigue expandiendo nodos, si considera que es mucho tiempo puede cortar la ejecución.\n")
            horse.profundidadEvitandoCiclos(matriz)
        else:
            sys.exit(0)

    
    limpiar_consola()
    matriz = cargarArchivo()
    tipoBusqueda = preguntarTipoBusqueda()

if __name__ == '__main__':
    main()