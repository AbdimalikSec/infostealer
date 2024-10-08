from flask import Flask , request

app = Flask(__name__)


@app.post("/")
def root():
	data = request.json('info')

	with open("taregt_information.txt","w") as file:
		file.write(data)

	return "ok"

if __name__ == "__main__":	
	app.run(port=3333)
