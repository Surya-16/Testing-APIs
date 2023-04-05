from flask import Flask, request, Response
import requests
import json
app = Flask(__name__)

#below /webhook endpoint is to validate the webhook signature
@app.route('/webhook', methods=['GET','POST'])
def get():
    webhooksignature = request.headers["X-Webhook-Signature"]
    ts =request.headers["X-Webhook-Timestamp"]
    data = request.data
    signatureData = ts+data.decode("utf-8")
    message = bytes(signatureData, 'utf-8')
    signature = base64.b64encode(hmac.new(b'SecretKey', message,digestmod=hashlib.sha256).digest()) #Replace your SecretKey
    computed_signature=str(signature, encoding='utf8')
    print("Webhook_Signature  :"+webhooksignature +"\n" + "Computed_Signature :" + computed_signature)
    if(computed_signature==webhooksignature):
        print("WEBHOOK_VALIDATION_SUCCESS")
        return Response(status=200)
    else:
        print("WEBHOOK_VALIDATION_FAILED")
        return Response(status=500)
    
 #below /order endpoint is for return_url   
@app.route('/order', methods = ['GET'])
def order():
    orderid = request.args.get('order')
    print(orderid)
    url = "https://sandbox.cashfree.com/pg/orders/"+orderid #PROD endpoint: https://api.cashfree.com/pg
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
