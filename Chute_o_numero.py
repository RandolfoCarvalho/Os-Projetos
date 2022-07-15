# Projeto 3 - Chute o número
# Objetivo: Criar um algoritimo que gera um valor aleatório e eu tenho que ficar tentando até eu acertar

import random 
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
    
    def Iniciar(self):
        #layout
        layout = [
            [sg.Text("Seu chute", size=(20,0))],
            [sg.Input(size=(18,0), key="ValorChute")],
            [sg.Button("Chutar!")],
            [sg.Output(size=(20,10))]
        ]
        #criar uma janela
        self.janela = sg.Window("Chute o numero!", layout=layout)
        #fazer alguma coisa com esses valores

        self.GerarNumeroAleatorio()
        try:
            while True:
                # Receber Valores
                self.LerValoresDaTela()
                
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            print("Chute um valor mais baixo")
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            print("Chute um valor mais alto!")
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            print("Parabens, voce acertou!!")
                            self.tentar_novamente = False
                            break
        except:
            print("Por favor Digitar apenas numeros!")
            self.Iniciar()
        
    def LerValoresDaTela(self):
        self.evento, self.valores = self.janela.Read()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

chute = ChuteONumero()
chute.Iniciar()