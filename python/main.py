from flask import Flask, request, jsonify
app = Flask(__name__)

# super secure database
FANCY_DB=[
  {
    "id": 1,
    "name":"Phillip"
  }
]

'''
GET /

Route that returns whatever string you pass in the url
'''
@app.route('/<name>')
def hello_world(name):
  return f'Hello, {name}!'


'''
GET /int/{number}

Route that returns whatever integer you passed in the url
'''
@app.route('/int/<int:num>')
def return_int(num):
  return f'The integer passed was: {num}'


'''
GET /float/{number}

Route that returns whatever float you passed in the url
'''
@app.route('/float/<float:num>')
def return_float(num):
  return f'Hello World, {num}'


## CRUD

'''
GET /data

Route that returns all data in the fancy db
'''
@app.route('/data', methods=['GET'])
def get_all_data():
  return jsonify(FANCY_DB)


'''
POST /data

Route that returns whatever object it receives in the body of the request
'''
@app.route('/data', methods=["POST"])
def getData():
  FANCY_DB.append(request.json)
  return request.json


'''
PATCH /data

Route that returns whatever object it receives in the body of the request
'''
@app.route('/data/<int:id>', methods=["PATCH"])
def patchData(id):
  for i in FANCY_DB:
    if i["id"] == id:
      i["name"] = request.json["name"]
  return request.json


'''
DELETE /data

Route that returns whatever object it receives in the body of the request
'''
@app.route('/data/<int:id>', methods=["DELETE"])
def delData(id):
  for i in FANCY_DB:
    if i["id"] == id:
      FANCY_DB.remove(i)
  return request.json



if __name__ == '__main__':
  app.run(
     debug=True,
     port=3000,
     host="0.0.0.0"
  )