n = input("I can find the second largest number\nEnter any numbers(separated by commas)\n")
n = n.split(',')
m_largest = 0
m_second = 0
for i in range(len(n)):
    if int(i) > int(m_largest):
        m_largest = n[i]
for i in range(len(n)):
    if int(i) > int(m_second) and int(i) != int(m_largest):
        m_second = n[i]
print(m_second)


