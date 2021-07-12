from flask import Flask, request
import json

#starts the app
app = Flask(__name__)

#the main route (home)
@app.route("/")
def index():
    return "<h1>You can make post request at http://192.168.1.13:5000/answers</h1> <h2>import .csv file in the body<h2>"

#generates the array of question answers
def generate_answers(cur):
    ret = []
    for i in range(4):
        obj = {
            "txt": cur[3+ i*2],
            "img": "",
            "sound": "",
            "video": ""
        }
        ret.append(obj)
    return ret

#generate the whole json for a single row
def generate_json(cur, i):
    arr = generate_answers(cur)
    obj = {
        "QuesID": i-1,
        "QuesType": "mcqV2",
        "QuesSubType": "b",
        "QuesScore": 1,
        "QuesTxt": cur[1][1:-1],
        "QuesImg": "{}.png".format(cur[2]),
        "QuesSound": "",
        "QuesVideo": "",
        "AnsImg": "",
        "QuesAns": arr,
        "AnsLink": "",
        "QuesRightAns": cur[13]
    }
    return obj



#making the route for post request
@app.route('/answers', methods=['POST']) 
def handle_post():
    
    #reads the file from the the body
    f = request.files['input']
    fstring = f.read()

    #handles arabic language error
    decoded = fstring.decode('UTF-8')

    #makes every line in a single array index
    arr = decoded.splitlines()
    
    ret = []
    for i in range(1,2):

        #an array of the current row
        cur = arr[i].split(',')

        #genertes the json file and add it to final return array
        ret.append(generate_json(cur, i))

    #make sure that file in JSON format
    #handles arabic language problem
    return json.dumps(ret, ensure_ascii=False).encode('utf8'), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')