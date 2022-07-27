#HackerRank - Count Apples And Oranges

def countApplesAndOranges(s, t, a, b, apples, oranges):

    apples_in_house = 0
    oranges_in_house = 0

    for apple in apples:
        verify_apple = a + apple
        if verify_apple >= s and verify_apple <= t:
            apples_in_house += 1

    for orange in oranges:
        verify_orange = b + orange
        if verify_orange >= s and verify_orange <= t:
            oranges_in_house += 1
    
    apple_return= print(apples_in_house)
    orange_return = print(oranges_in_house)

    return apple_return, orange_return

macas = [2, 3, -4]

laranjas = [3, -2, -4]

countApplesAndOranges(7, 10, 4, 12, macas, laranjas)
