import datetime, time, os

timestamp = time.time()
dateRightNow = datetime.datetime.now()
print(dateRightNow)

# Listing all file in the directory
files = os.listdir(".")
file_path = os.getcwd()

# anotherD = os.listdir('../../Downloads') testing the function...

# Cheking to see if the folder 'logs' exists on your PC
for f in files:
    if f == 'logs':
        print('there is no log')
        break
else:
    os.mkdir('logs')

# Creating the file + text
file_path = os.path.join("logs", f"log - {timestamp}log.txt")

with open(file_path, "w")  as l:
    l.write(f"This is your log created at: {dateRightNow}")





