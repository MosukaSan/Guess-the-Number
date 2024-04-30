import random

def main():
    input("Bem vindo ao adivinhe o número")
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
            tentar_dnv = input("Parabéns você acertou! Tentar novamente Y - sim, N - não")
            if (tentar_dnv == "Y"):
                main()
            elif (tentar_dnv == "N"):
                print("Se mata ent krl, porra, fdp.")
    escolha()
main()