st = input('Enter the word:\n')

m = set("AaEeUuIiOoYy")

for i in st:
    if i in  m:
        st = st.replace(i,'')
print(st)