ItemsInCart = 0

# 2 items will be added in the cart

if ItemsInCart != 2:  # raise Exception("Products count not matching")
    pass

assert (ItemsInCart == 0)

try:
    with open('tes.txt') as reader:
        reader.read()
except Exception as e:
    print(e)
finally:
    print("Hello")