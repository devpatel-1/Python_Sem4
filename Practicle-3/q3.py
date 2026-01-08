# Create a program that will print out words that start with 's' from the below given statement.


st="Print only the words that start with s in this sentence"

l1 = st.split()
print(l1)

for i in l1:
    if i[0] =='s':
        print(i)

for i in l1:
    if(i.startswith('s')):
        print(i)
