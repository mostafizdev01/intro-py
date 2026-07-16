## ===========>>>>>> List comprehensions <<<<<<<<<==============

li = ["apple", "banana", "orange", "mango"]
fruits = [fruit.capitalize() for fruit in li]

print(fruits)

li_len = [len(x) for x in li]
print(li_len)

cube_list = [x*x*x for x in range(1, 11)]
print(cube_list)

cube_list_2 = [x for x in range(1, 11) if x % 2 == 1]
print(cube_list_2)

cube_list_3 = [x*x*x for x in range(1, 11) if x % 2 ==1]
print(cube_list_3)

## ===========>>>>>> Dictionary comprehensions <<<<<<<<<==============

li = [(1, "One"), (2, "Two"), (3, "Three")]
dt = {k:v for k, v in li}
print(dt)

dt = {v:k for k, v in li}
print(dt)


## ===========>>>>>> Set comprehensions <<<<<<<<<==============

s = 'asdfhoasdfhasw'

unique_letters = {c for c in s}
print(unique_letters)

# dictionary to set
colors_choice = [("messi", "blue"), ("rolando", "red"), ("neymar", "yellow"), ("mbappe", "blue"), ("lamini", "black")]

colors_dt = {name:color for name, color in colors_choice}
print(colors_dt)

colors_set = {color for color in colors_dt.values()}
print(colors_set)