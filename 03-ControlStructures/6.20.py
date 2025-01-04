dec = int(input("Enter decimal number: "))
num_dec = dec
num_bin = ""
while num_dec > 0:
    bin = int(num_dec % 2)
    num_bin = str(bin) + num_bin
    num_dec = num_dec // 2 


print(f'{dec}(10) = {num_bin}(2)')
