data = [
   {"Name": "Charlotte", "Age": 17},
   {"Name": "Ahmed", "Age": 18},
   {"Name": "Jean Paul", "Age": 18},
   {"Name": "Fatima", "Age": 17}
]
for item in data:
   for key, value in item.items():
       print(key, ":", value)
   print("-" * 10)

y = 0
while y < 15:
    print("you are stil playing")
while y > 15:
    print("You have finished")

text = "digital"
for str in text:
    print(str)