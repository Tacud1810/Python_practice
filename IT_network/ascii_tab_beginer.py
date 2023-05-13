import binascii

print("ASCII tab beginner")
print("=============")

for i in range(26):
    for j in range(10):
        print(f"{i}{j}: {chr(i * 10 + j)}\t", end="")
    print("")
