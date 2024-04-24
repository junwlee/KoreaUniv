def order_automator():
    print("Welcome to our Coffee Shop!")

    # Handling payment
    while True:
        # Taking orders
        x = int(input("How many Americanos would you like to order? "))
        y = int(input("How many Caffelattes would you like to order? "))
        z = int(input("How many Cappuccinos would you like to order? "))

        # Calculating totals
        total_americano = x * 2500
        total_caffelatte = y * 3000
        total_cappuccino = z * 3000
        sum_of_order = total_americano + total_caffelatte + total_cappuccino

        print("\nSummary of Your Order:")
        print(f"Americanos: {x} x 2500 = {total_americano} won")
        print(f"Caffelattes: {y} x 3000 = {total_caffelatte} won")
        print(f"Cappuccinos: {z} x 3000 = {total_cappuccino} won")
        print(f"Total: {sum_of_order} won\n")
        money = int(input("How much money will you pay? "))
        change = money - sum_of_order

        if sum_of_order > money:
            print("Insufficient funds. Please reorder the coffee!")
        elif sum_of_order == money:
            print("Exact amount received. Thank you for your purchase!")
            break
        else:
            print(f"Payment received: {money} won. Your change is {change} won. Thank you!")
            break

order_automator()
