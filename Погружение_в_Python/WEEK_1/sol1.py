import sys
num_steps = int(sys.argv[1])
for i in range(num_steps):
    a = " "*(num_steps-(i+1))
    b = (i+1)*"#"
    print(a+b)
print("check")
ук
