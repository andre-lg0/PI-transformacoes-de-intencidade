#!/usr/bin/env python3
# -*- coding: utf-8 -*
from TransformIntencidadade import TranformIntecidade





if __name__ == '__main__':
    intencidade  = TranformIntecidade('Img/lena.png')
    intencidade.carregarImagem()
    op = -1
    menu = ' \n \t Menu \nDigite 0 para sair\n'
    menu += '1 - Transformação para negativo\n'
    menu += '2  - Transformação Power Law\n'
    
    while op!= 0:
       # print(menu)
        op = input(menu)
        op = int(op)
        if op == 1:
            intencidade.negative()
        elif op == 2:
            print('Digite o valor do Gama e da constante')
            gama = float(input())
            c = float(input())
            intencidade.PowerLaw(gama,c) 
    
    print("Fim da execução")
    



    

