nums = []
total = 0
summ = 0

while True:
    nums.append(input("Уведіть число: "))
    if nums[-1] == '':
        nums.pop()
        break

print(nums)

for el in nums:
    summ += int(el)
total = len(nums)
avg = summ / total
print('Середнє значення: ', avg)

print("Числа не більше середнього значення: ")
for el in nums:
    if float(el) <= avg:
        print(el, end=' ')
print('')
print("Числа більше середнього значення: ")
for el in nums:
    if float(el) > avg:
        print(el, end=' ')