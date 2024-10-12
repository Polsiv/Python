
#!/usr/bin/env python3

#Lists are mutable

#Lists =============================================

tcp_ports = [21, 22, 25, 80, 443, 8080, 445, 69]
cve_list = ['CVE-2023-1435', 'CVE-2022-45761', 'CVE-2023-7663']
attacks = ['Phishing', 'DDoS', 'SQL INJECTION', 'Man In the Middle', 'Cross-site Scripting']

print("xd", attacks[:])
#Remove and append ===============================

tcp_ports.append(1337)
cve_list.remove('CVE-2023-1435')

#Iterate through list=============================

for port in tcp_ports:
    print(f'port: {port}')

#Reverse =========================

tcp_ports.sort(reverse = True)
print(tcp_ports)

attacks.reverse()
print(attacks)

#index ====================================

first_attack = attacks[0]

#Range====================================

#From the last element, print the next (penultimate) and so on
another_attacks_list = attacks[:-1]
print(another_attacks_list)


more_attacks = attacks[0:3]
print(more_attacks)


#Iterate w/ while ==========================

counter = 0

while counter < len(tcp_ports):
    print(tcp_ports[counter])
    counter+=1

#enumerate elements=========================

for i, j in enumerate(attacks):
    print(f'#{i + 1} Attack: {j}')


#UpercasING ===========================

a_uppercase = [ letter.upper() for letter in attacks]
print(a_uppercase)


# Combining lists ==========================

names = ['lol', 'lol2', 'lol3', 'lol4']
ages = [1, 2, 3, 4]

for name, age in zip(names, ages):
    print(name, age)

#removing elements

del names[3] #idx
names.remove('lol')

#WIpe list ===================

names.clear()


#Remove last element==================

index_removed = ages.pop(2)
print(index_removed)

ages[-1] = 90

#insert on specific index ===============

ages.insert(0, "silv")
print(ages)

#append elements ==================
more_ages = [10, 20, 30, 40]

ages.extend(more_ages)
print(ages)


numbers4 = [1, 2, 3, 4, 5, 6]
print(numbers4)