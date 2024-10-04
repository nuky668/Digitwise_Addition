### Digitwise Addition ###

 # Test Constraints:
    # 1 <= n <= 10 ** 9
    # 1 <= k <= 10 ** 5
    # Expected Time Complexity: O(k * log(n))

def digitwise_addition(n, k):
   """K krát přidá 1 ke každému číslu v N"""

   # hlavní cyklus
   while k != 0:
        # 1. čísla zvětšíme o 1 a naházíme do listu
        n = str(n)
        list1 = []
        for digit in n:
            digit = int(digit) + 1
            list1.append(digit)

        n = ""

        # 2. vybereme čísla z listu a uděláme proměnnou n
        for item in list1:
            n = n + str(item)

        k -= 1

   return len(str(n))   # kolik číslic má upravené číslo "n"
    


a = digitwise_addition(789, 3)
print(a)
