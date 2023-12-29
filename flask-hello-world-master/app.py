from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

def get500mb(number,password):
  headers = {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
      "Accept-Encoding": "gzip, deflate",
      "Accept-Language": "en,ar;q=0.9,en-US;q=0.8",
      "Cache-Control": "max-age=0",
      "Connection": "keep-alive",
      "Content-Length": "53",
      "Content-Type": "application/x-www-form-urlencoded",
      "Host": "www.ahmed-net.rf.gd",
      "Origin": "http://www.ahmed-net.rf.gd",
      "Referer": "http://www.ahmed-net.rf.gd/500MB.php?i=2",
      "Upgrade-Insecure-Requests": "1",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
      'Cookie':'__test=dee9cb7ddf5e1baab7f1ce0e453f1801'
  }


  data = {
    "number":f"{number}",
    "password":f"{password}",
    "submit": "Submit",
  }

  response = requests.post('http://www.ahmed-net.rf.gd/500MB.php', headers=headers,
                            data=data, verify=False).text
  soup=BeautifulSoup(response, "html.parser")
  
  data=soup.find("script")
  usf=re.findall(r"'(.*?)'", data.text, re.DOTALL)
  if usf[0] =="انت استخدمت البرومو كود النهاردة شكراً :)":
      return("taked")
  elif usf[0]=="الرقم غلط او الباسورد !":
      return("wrong")
  elif usf[0]=="تم اضافة 524 ميجا بنجاح":
      return("success")
  else:
      return("error")
@app.route('/', methods=['GET'])
def home():
    return"<h1>@usfnassar</h1>"
@app.route('/api/get_500mb', methods=['GET'])
def api_get_500mb():
    try:
        # Get parameters from the query string
        number = request.args.get('number')
        password = request.args.get('password')

        # Call the function
        result = get500mb(number, password)

        # Return the result as JSON
        return jsonify({'result': result})

    except Exception as e:
        # Handle exceptions and return an error response
        return jsonify({'error': str(e)}), 500

