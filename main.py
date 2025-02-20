import time

def find_coins_greedy(amount):
    coins = [50, 25, 10, 5, 2, 1]
    change = {}
    
    for coin in coins:
        if amount >= coin:
            change[coin] = amount // coin
            amount %= coin
    
    return change

def find_min_coins(amount):
    coins = [50, 25, 10, 5, 2, 1]
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    used_coins = [0] * (amount + 1)
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                used_coins[i] = coin
    
    change = {}
    while amount > 0:
        coin = used_coins[amount]
        if coin in change:
            change[coin] += 1
        else:
            change[coin] = 1
        amount -= coin
    
    return change

# Тестування та замір часу
amount = 113

start = time.time()
print("Жадібний алгоритм:", find_coins_greedy(amount))
print("Час виконання жадібного алгоритму:", time.time() - start)

start = time.time()
print("Динамічне програмування:", find_min_coins(amount))
print("Час виконання алгоритму динамічного програмування:", time.time() - start)