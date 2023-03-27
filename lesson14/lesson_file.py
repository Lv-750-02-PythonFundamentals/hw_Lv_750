# file = open("input.data")
# file2 = open("input2.data", 'w')
#
# # print(file.read())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.readline())
# # print(file.readlines())
# for line in file.readlines():
#     print(line)
# file.close()
# file2.close()
#
# img = open("icon.png", "rb")
# print(img.read())
# img.close()
import datetime
import time
#
# file = open("out.txt", "w")
# file.write("test11\n")
# file.write("test11\n")
# file.write("test11\n")
# file.writelines("test2\n")
# file.writelines("test2")
# file.close()
# time.sleep(10)
import datetime
with open("out2.txt", "w") as file:
    for i in range(4):
        current_time = datetime.datetime.now()
        file.write(f"curent time {current_time}\n")
        time.sleep(1)
