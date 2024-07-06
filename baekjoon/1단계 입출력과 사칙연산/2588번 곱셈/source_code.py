multiplicand = int(input())
multiplier = int(input())

hundred = multiplier // 100
multiplier = multiplier % 100
ten = multiplier // 10
one = multiplier % 10

one_product = multiplicand * one
ten_product = multiplicand * ten
hundred_product = multiplicand * hundred

print(one_product)
print(ten_product)
print(hundred_product)
print(hundred_product * 100 + ten_product * 10 + one_product)