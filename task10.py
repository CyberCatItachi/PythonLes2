def min_flips(coins):
    count_heads = coins.count('1')
    count_tails = coins.count('0')
    
    if count_heads <= count_tails:
        return count_heads
    else:
        return count_tails

coins = input("Введите последовательность монет (1 - орел; 0 - решка): ")
print("Минимальное количество монет, которые нужно перевернуть:", min_flips(coins))