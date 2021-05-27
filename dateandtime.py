#jaspreet singh

from main import GetDateTime

now = GetDateTime()
print("Here is the Current Date and Time Showing")
print("***********************************************")
print(now.strftime("%y-%m-%d %H:%M:%S"))