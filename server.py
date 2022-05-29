from flask import Flask, request

app = Flask('__main__')


device ={
    "code":"112233",
    "descrip": "Proximity sensor",
    "value": 67
}



'''@app.route('/devices', methods=['GET'])
def go_home():
    return 'Hello world'
    #return device'''


'''@app.route('/users', methods=['POST'])
def save_user():
    user= request.json
    print(user)
    return user;'''


@app.route('/devices', methods=['POST'])
def save_device():
    device = request.json
    print(device)
    return device, 201


if __name__ == "__main__":
    app.run(debug=True, port=5000) 