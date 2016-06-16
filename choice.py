#Write a program that asks the user for a number n and gives him the possibility to choose between #computing the sum and computing the product of 1,…,n.


s = int(input("Please enter a number:\n"))
    p = input("Choose sum or product. Please input s for sum, p for product, or e for exit:\n")
    if p in ("sum", "s"):
        total = sum(range(1, s + 1))
        print(total)
    elif p in ("product", "p"):
        product = 1
        for i in range(1, s + 1):
            product *= i
        print(product)
    elif p in ("exit", "e"):