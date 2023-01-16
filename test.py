import hmac
import hashlib
import base64
from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return name#'welcome %s' % name

@app.route('/webhook',methods = ['POST', 'GET'])
def webhook():
   if request.method == 'GET':
      data = request.form['data']
      timestamp = request.form['timestamp']
      secretKey = request.form['secretKey']
      if data == "" and timestamp =="" and secretKey =="" :
            return redirect(url_for('success',name = "Please enter all the values"))
      else:
            webhook_signature = "i7atHb5HSwhV3pLo073LDTMX+ERgTxqRpA5PyA1cqpQ=" #signature recieved from Cashfree
            signatureData = timestamp+data
            message = bytes(signatureData, 'utf-8')
            signature = base64.b64encode(hmac.new(bytearray(secretKey,encoding='utf8'), message,digestmod=hashlib.sha256).digest())
            computed_signature=str(signature, encoding='utf8')
            print("Webhook_Signature  :"+webhook_signature +"\n" + "Computed_Signature :" + computed_signature)
            if(computed_signature==webhook_signature):
                return redirect(url_for('success',name = "Webhook Verification Success"))
            else:
                return redirect(url_for('success',name = "Webhook Verification Failed"))            
   else:
      user = request.args.get('data')
      timestamp= request.args.get('timestamp')
      return redirect(url_for('success',name = user+timestamp))

if __name__ == '__main__':
   app.run(debug = True)