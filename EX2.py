def fibonacci_sequence(n):
    a, b = 0, 1
    sequence = [a]
    
    while b <= n:
        sequence.append(b)
        a, b = b, a + b
    
    return sequence

#Solicitando um número 
num = int(input("Informe um número: "))

#Obtendo a sequência até o número informado
sequence = fibonacci_sequence(num)
print(f"Sequência de Fibonacci: {sequence}")

#Verificando se o número pertence à sequência
if num in sequence:
    print(f"O número {num} pertence à sequência.")
else:
    print(f"O número {num} não pertence à sequência.")