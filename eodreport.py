import datetime, os
currentUser = os.path.expanduser("~")
print(currentUser)
reportStorage = currentUser + "/Desktop/End of Day Reports"
if not os.path.exists(reportStorage):
    os.mkdir(reportStorage)
today = datetime.date.today()
strToday = today.strftime("%x")
strToday = strToday.replace("/", "-")
now = datetime.datetime.now()
todaysReport = reportStorage + "/" + strToday + ".txt"
if not os.path.exists(todaysReport):
    f = open(reportStorage + "/" + strToday + ".txt", "x")
else:
    f = open(reportStorage + "/" + strToday + ".txt", "a")
current_time = now.strftime("%H:%M:%S")
print("Welcome! Type /quit to exit. \n")
while True:
    userInput = input("What are you working on?: ")
    if userInput == "/quit":
        break
    else:
        f.write("[" + current_time + "]" + "\n" + userInput + "\n" + "\n")
    
