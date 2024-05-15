p = int(input("Enter public key 'p' value: "))
g = int(input("Enter public key 'g' value: "))
a = int(input("Enter private key 'a' value: "))
b = int(input("Enter private key 'b' value: "))

# p = 23
# g = 9
# a = 4
# b = 3
# secret_key = 9

value_a = pow(g, a) % p
value_b = pow(g, b) % p

key_a = pow(value_b, a) % p
key_b = pow(value_a, b) % p

if key_a == key_b:
    print("Secret key for both users:", key_a)
else:
    print("Secret key is not same for both!")
    print("Secret key for user A:", key_a)
    print("Secret key for user B:", key_b)
