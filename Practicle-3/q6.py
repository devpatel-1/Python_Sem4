# Go to String below and if the length of a word is even print "even!".
st='I love doing python programming in spyder'


l1 = st.split()
print(l1)

for i in l1:
    l = len(i)
    if l % 2 == 0:
        print(i, "even", sep=" : ")
