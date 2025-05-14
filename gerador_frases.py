import random

def obter_frase():
    frases = [
        "Acredite em você e todo o resto virá naturalmente.",
        "O sucesso é a soma de pequenos esforços repetidos dia após dia.",
        "Não espere por oportunidades, crie-as.",
        "A persistência é o caminho do êxito.",
        "Transforme seus sonhos em planos e seus planos em realidade.",
        "Cada dia é uma nova chance para mudar sua vida.",
        "O único lugar onde o sucesso vem antes do trabalho é no dicionário.",
        "Não importa a velocidade, mas sim a direção.",
        "A coragem não é a ausência do medo, mas a decisão de que algo é mais importante que o medo.",
        "Você é capaz de coisas incríveis."
    ]
    return random.choice(frases)

def main():
    print("=== Gerador de Frases Motivacionais ===")
    while True:
        input("Pressione ENTER para receber uma frase motivacional ou digite 'sair' para encerrar: ")
        frase = obter_frase()
        print(f"\n💡 {frase}\n")
        comando = input("Deseja outra frase? (ENTER para sim / 'sair' para não): ").strip().lower()
        if comando == 'sair':
            print("Até a próxima! Mantenha-se motivado!")
            break

if __name__ == "__main__":
    main()
