import hashlib

secret_key = "bgvyzdsv"
num = 0

while True:
    input = secret_key + str(num)
    md5_hash = hashlib.md5(input.encode()).hexdigest()
    if md5_hash[:6] == "000000":
        break
    num += 1

print(input)