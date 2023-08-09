# try:
#     f=open("../4-oy darslar/1-dars/1-dars.py", "r")
#     s=f.read()
#     print(s)
# except Exception as e:
#     print("Error",e)

# print(f.closed)

try:
    with open("../4-oy darslar/1-dars/mmmmmmmmmm.txt","r+") as f:
        s=f.read()
        print(s)
        f.write("\n"+input("suz yozing:"))
except Exception as e:
    print("Xato",e)


print(f.closed)