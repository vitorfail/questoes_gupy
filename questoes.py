def teste_fibonachi(n):
    # Olha se o número é um quadrado perfeito

    def quadrado_perfeito(x):
        s = int(x**0.5)
        return s * s == x
    #returna true ou false
    return quadrado_perfeito(5 * n * n + 4) or quadrado_perfeito(5 * n * n - 4)
def contar_a(s):
    # Conta a quantidade de vezes que a letra 'a' se repete na string
    count = s.lower().count('a')
    return count

def main():
    questao_input = input("Digite 1 ou 2 para escolher entre uma dessas questões:")
    if questao_input.isdigit() and int(questao_input) ==1:
            usuario_input = input("Digite um número e pressione enter para verificar se pertence à sequência de Fibonacci: ")
            if usuario_input.isdigit():  # Verifica se o valor digitado é um numero positivo
                numero = int(usuario_input)
                if numero < 0:
                    print("Número deve ser não-negativo.")
                else:
                    if teste_fibonachi(numero):
                        print(f"O número {numero} \033[32mpertence\033[0m à sequência de Fibonacci.")
                    else:
                        print(f"O número {numero} \033[31mnão pertence\033[0m à sequência de Fibonacci.")
            else:
                print("Por favor, digite um número.")

    if questao_input.isdigit() and int(questao_input) ==2:
        usuario_input = input("Digite uma palavra para verificar quantas vezes a letra 'a' aparece denrtro:")
        if contar_a(usuario_input) ==0:
            print("A letra 'a' não aparace \033[31mnenhuma\033[0m vez dentro da string")
        if contar_a(usuario_input) ==1:
            print(f"A letra 'a' aparece \033[32m{contar_a(usuario_input)}\033[0m veze dentro da string")
        else:
            print(f"A letra 'a' aparece \033[32m{contar_a(usuario_input)}\033[0m vezes dentro da string")

if __name__ == "__main__":
    main()
