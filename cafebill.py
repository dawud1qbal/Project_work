TAX_RATE = 0.2 #20%

item1 = float(input("Enter the price of the first item: "))
item2 = float(input("Enter the price of the second item: "))


print("\nChoose a tip amount: ")
print("1.0%")
print("2.5%")
print("3.10%")
print("4.20%")

choice = int(input("Enter your choice (1-4): "))

if choice == 1:
    tip_rate = 0.0
elif choice == 2:
    tip_rate = 0.05
elif choice == 3:
    tip_rate = 0.10
elif choice == 4:
    tip_rate = 0.20

else:
    tip_rate = 0.0
    print("Invalid choice. No tip added.")

subtotal = item1 + item2
tax = subtotal * TAX_RATE
tip = subtotal * tip_rate
total = subtotal + tax + tip

print("\n--- Bill Breakdown ---")
print("Subtotal: £", round(subtotal, 2))
print("Tax (20%): £", round(tax, 2))
print("Tip: £", round(tip, 2))
print("Total: £", round(total, 2))