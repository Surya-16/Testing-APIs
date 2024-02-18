from flask import Flask, request, Response
import requests
import json
app = Flask(__name__)
@app.route('/my_webhook', methods=['POST'])
def return_response():
    print(request.json)
    ## Do something with the request.json data.
    return Response(status=201)
@app.route('/webhook', methods=['POST','GET'])
def get():
    print(request.json)
    print(request.headers)
    return Response(status=201)
@app.route('/order', methods = ['GET'])
def order():
    orderid = request.args.get('order')
    print(orderid)
    url = "https://sandbox.cashfree.com/pg/orders/"+orderid
    payload = ""
    headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
            'x-api-version': '2022-09-01',
            'x-client-id': '{{AppId}}',
            'x-client-secret': '{{SecretKey}}'
              }
    response = requests.request("GET", url, headers=headers, data=payload)
    print(response.text)

    return Response(response.text)

if __name__ == "__main__": app.run(debug = True)
