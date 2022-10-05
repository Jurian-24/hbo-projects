mealCost = int(input(''))

tax = (mealCost / 100) * 21
tip = (mealCost / 100) * 15

print('Tax: '+ str(mealCost * 0.21) + ', Tip: ' + str(mealCost * 0.15) + ', Total: ' + str((mealCost + (mealCost * 0.21) + (mealCost * 0.15))))

# print('Tax: '+ str(tax) + ', Tip: ' + str(tip) + ', Total: ' + str((mealCost + tax + tip)))
