import random
import time
import os

def main():
    print("Bem vindo ao adivinhe o número")
    time.sleep(2)
    print("Escolha o intervalo:")
    intervalo = int(input("- "))
    numero_real = random.randint(1, intervalo)
    
    
    print("Escolha um número: ")
    
    def escolha():
        num_esc = int(input("- "))
        if num_esc > numero_real:
            print("Menor!")
            escolha()
        elif num_esc < numero_real:
            print("Maior!")
            escolha()
        elif num_esc == numero_real:
            print("Parabéns você acertou! Tentar novamente Y - sim, N - não")
            tentar_dnv = input("- ")
            if (tentar_dnv == "Y"):
                os.system("clear")
                main()
            elif (tentar_dnv == "N"):
                print("Se mata ent krl, porra, fdp.")
                time.sleep(3)
                exit()
    escolha()
main()
