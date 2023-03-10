x = int(input("Введите число символов\n")) -1
hvost = 0
space = " "
x1 = 0
flag = True
flag2 = True
mr = 0
jj= ""

while flag:
    with open("text.txt", "r", encoding = 'Windows-1251') as st:
        k = 1  
        st.seek(x1)
        while flag2:
            x1 = 1
            flag2 = False
        st = st.read(x)   
        stprov = st
        stprov = [r for r in stprov]
        if len(stprov) < x:
            st = st.strip()
            with open("text2.txt", "a", encoding = 'Windows-1251') as stt:
                stt.write(st)
            flag = False
            break
        st = st.strip()
        
        if "\n" in st:
            st = st.split("\n")
            sthvost = st[1]
            st = st[0]
            sthvost = [r for r in sthvost]
            hvost = len(sthvost)
            x1 = (x1 + x) - hvost
            with open("text2.txt", "a") as stt:
                stt.write(st)
                stt.write("\n")
            continue

        st = st.split(" ")           
        tut = st.pop(-1) 
        hvost = len(tut)+1

        for d in range(len(st)-1):
            st.insert(k, space)
            k = k+2
        stkost = jj.join(st)
        stkost = [r for r in stkost]

        while True:
            k = 1
            while len(stkost) < x: 
                    st.insert(k, space)
                    k = k+2
                    if k>= (len(st)):
                        k = 1
                    stkost = jj.join(st)
                    stkost = [r for r in stkost]
            else:
                break
        x1 = (x1 + x) - hvost    
                    
    with open("text2.txt", "a", encoding = 'Windows-1251') as stt:
        if stkost.count("Ђ"): #без этого символа кодировки сьедают пробел, так как апостроф кодируется двумя а в некоторых и тремя символами
            st.insert(1, 2*space)
        st = jj.join(st)
        stt.write(st)
        stt.write("\n")
       

    
    



