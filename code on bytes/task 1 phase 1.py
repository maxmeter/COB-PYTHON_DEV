file=open(r'C:\Users\anish\OneDrive\Desktop\code on bytes\sample.txt')
freq={}
for line in file:
    
    for word in line.split():
        if word in freq:
            freq[word]+=1
        else:
            freq[word]=1
print(freq)