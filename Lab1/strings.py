#ex1
message="Please,buy some cookies"
print(len(message))

#ex2
txt="North is to your left"
x=txt[0]
print(x)

#ex3
txt="Welcome to New York!"
x=txt[3:7]
print(x)

#ex4
txt= "  Physics is natural science of matter   "
print(txt.strip())

#ex5
txt="Do not enter"
txt=txt.upper()
print(txt)

#ex6
txt="Right below"
txt=txt.lower()
print(txt)

#ex7
txt="Shy is found!"
txt=txt.replace("h", "p")
print(txt)

#ex8
cost=15
txt="These new items costed me {} dollars"
print(txt.format(cost))