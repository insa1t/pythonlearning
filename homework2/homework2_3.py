n = int(input("Введите число n: "))
lst = [(1+1/i)**i for i in range(1,n+1)]
print(f"Полученная сумма последовательности (1+1/n)^n равнна {round(sum(lst),2)}")