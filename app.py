from flask import Flask

app = Flask(__name__)

# API 가 있어야 한다!!
# 아래 코드가 API

@app.route('/', methods = ['GET'])
def hellow_world() :
    return 'Hellow World hihihi'

if __name__ == '__main__' :
    app.run()