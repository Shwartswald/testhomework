# my_name = "Parna"

# for char in my_name:
#     print(char)

# for i in range(10):
#     print(i)

# for i in range(10):
#     print(str(i) + "a")

# name1 = str(input("name1"))
# name2 = str(input("name2"))
# vowels_in_name1 = 0
# vowels_in_name2 = 0

# for char in name1:
#     if char in "aeiou":
#         vowels_in_name1 += 1

# for char in name2:
#     if char in "aeiou":
#         vowels_in_name2 += 1

# if vowels_in_name1 > vowels_in_name2:
#     print("vowel in name 1 is more and contains{}".format(vowels_in_name1))
# if vowels_in_name2 > vowels_in_name1:
#     print("vowel in name 2 is more and contains{}".format(vowels_in_name2))

# print(5 != 10)

# print("a" not in "sjdhsjdhjs")



name1 = str(input("name1"))
name2 = str(input("name2"))

consonant1_in_name1 = 0
consonant2_in_name2 = 0


for char in name1:
    if char not in "aeiou":
        consonant1_in_name1 += 1

for char in name2:
    if char not in "aeiou":
        consonant2_in_name2 += 1

if consonant1_in_name1 > consonant2_in_name2:
    print("the amount of consonants in nam1 is more and it contains {} consonants".format(consonant1_in_name1))
elif consonant1_in_name1 < consonant2_in_name2:
    print("the amount of consonants in nam2 is more and it contains {} consonants".format(consonant2_in_name2))
else:
    print ("they have equal amount of consonants")


