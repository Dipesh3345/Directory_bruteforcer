import requests

file = open('wordlist.txt')
# Enter full url eg:https://google.com/
u = input("Enter the target url: ")

for i in range(397):
	a = file.readline()
	r = requests.get(u+a)
	print(u+a)
	print(r.status_code) 
	


	









