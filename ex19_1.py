def nintendo_switch(ns_price, game_price):
    print(f"the ns's price is {ns_price}")
    print(f"the game's price is {game_price}")
    print("the total price is {0}".format(ns_price + game_price))


# way1
print('way1')
nintendo_switch(2000, 300)

# way2
print('way2')
nintendo_switch(1800+200, 300)

# way3
print('way3')
the_price_of_ns = 2000
the_price_of_game = 300
nintendo_switch(the_price_of_ns, the_price_of_game)

# way4
print('way4')
nintendo_switch(the_price_of_ns+100, the_price_of_game+200)