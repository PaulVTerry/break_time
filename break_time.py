import time
import webbrowser

n = 0

print("this program started on " + time.ctime())
while n < 3:
	time.sleep(3) #starts the program every '3' seconds
	webbrowser.open("https://www.youtube.com/watch?v=5qap5aO4i9A")
	n = n + 1