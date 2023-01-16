from flask import Flask, request, Response
app = Flask(__name__)
data=""
@app.route('/my_webhook', methods=['POST'])
def return_response():
    print(request.json);
    data=request.json
    ## Do something with the request.json data.
    return Response(status=201)
@app.route('/webhook', methods=['GET'])
def get():
    print(data)
    return Response(status=200)
if __name__ == "__main__": app.run()