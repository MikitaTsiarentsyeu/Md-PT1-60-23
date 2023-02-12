st = input('Enter the word:\n')

for i in st:
    if i == i.upper():
        st = st.replace(i, i.lower())

print(st)

for i in st:
    if i == i.lower():
        st = st.replace(i, i.upper())

print(st)