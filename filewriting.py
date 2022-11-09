# f = open("prasad.txt", "w")
# a = f.write("Prasad is in Second Year of Engineering\n")
# f.write("Prasad is in TSEC\n")
# print(a)
# f.close()

# f = open("prasad.txt", "a")
# a = f.write("Prasad is in Second Year of Engineering\n")
# f.write("Prasad is in TSEC\n")
# print(a)
# f.close()


# Handle Read and Write both
f = open("prasad.txt", "r+")
print(f.read())
f.write("Thank you")
