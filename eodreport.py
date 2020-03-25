import datetime, os
currentUser = os.path.expanduser("~")
print(currentUser)
reportStorage = currentUser + "/Desktop/End of Day Reports"
if not os.path.exists(reportStorage):
    os.mkdir(reportStorage)
today = datetime.date.today()
strToday = today.strftime("%x")
strToday = strToday.replace("/", "-")
todaysReport = reportStorage + "/" + strToday + ".txt"
if not os.path.exists(todaysReport):
    f = open(reportStorage + "/" + strToday + ".txt", "x")
else:
    f = open(reportStorage + "/" + strToday + ".txt", "a")
print("Welcome! Type /quit to exit. \n")
while True:
    userInput = input("What are you working on?: ")
    if userInput == "/quit":
        break
    else:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        f.write("[" + current_time + "]" + "\n" + userInput + "\n" + "\n")
        f.flush()

f.close()
    
