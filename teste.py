def pertence_sequencia_fibonacci(numero):
    a, b = 0, 1
    while a < numero:
        a, b = b, a + b
    if a == numero:
        return True
    else:
        return False

numero_informado = int(input("Informe um número: "))

if pertence_sequencia_fibonacci(numero_informado):
    print(f"O número {numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero_informado} não pertence à sequência de Fibonacci.")
