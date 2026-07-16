fp = open("myfile.txt", "w")

lines = ["Apple\n", "Banana\n", "Coconut\n"]
# lines = "this is text file"

fp.writelines(lines)
print(fp)

fp.close()

# read mode
fp = open("myfile.txt", "r")

# lines = ["Apple", "Banana", "Coconut"]
# lines = "this is text file"
data = fp.read()
# fp.writelines(lines)
print(data)

fp.close()

# # append mode 
fp = open("myfile.txt", "a")

lines = ["Apple\n", "Banana\n", "Coconut\n"]
# # lines = "this is text file"

fp.writelines(lines)

fp.close()