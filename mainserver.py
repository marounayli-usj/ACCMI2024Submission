from flask import Flask, request, jsonify
from flask_cors import CORS
import testGenerator
import gptAPI
import json
import uuid
import importlib


from datetime import datetime

tag2tag = {
    "button":"button",
    "link":"a",
    "Span":"span",
    "DropDown":"select",
    "input":"input"
}

action2function = {
    "click":"click",
    "type":"send_keys",
    "check":"assert"
}
def save_test_to_file(data):
    try:
        with open("testdb.json", 'r') as f:
            contents = f.read()
            if contents:
                data_list = json.loads(contents)
            else:
                data_list = []
    except FileNotFoundError:
        data_list = []
    
    data_list.append(data)
    
    with open("testdb.json", 'w') as f:
        json.dump(data_list, f, indent=4)

def parsePayload(payload):
    sentences = []
    res = {
        "base_url": payload["base_url"],
        "test_name" :payload["test_name"],
        "date_created":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "last_run_status":"N/A"

    } 

    for elt in payload["sentences"]:
        
        gptdesc=""
        # gptdesc = gptAPI.desc_to_dict(elt["description"])
        obj = {
            "action" : action2function[elt["action"]],
            "tag" : tag2tag[elt["tag"]],
            "description" : json.loads(gptdesc) if gptdesc!= "" else {}
        }   
        if(obj["action"]=='send_keys' or obj["action"]=="assert"):
            obj["actionarg"] = elt["value"]
            obj["value"] = ""
        else:
            obj["value"]=elt["value"]
            obj["actionarg"] = ""
        obj["descdict"] = {'tag':obj['tag'],"value":obj["value"], "attrs":obj["description"]}
        sentences.append(obj)
    res["sentences"] = sentences
    return {str(uuid.uuid4()):res} , res
app = Flask(__name__)



@app.route('/create-test/', methods=['POST'])
def create_test():
    data = request.get_json()
    parsed_payload  = parsePayload(data)
    save_test_to_file(parsed_payload[0])

    testGenerator.generateScript(parsePayload(data)[1])
    return jsonify(data)


@app.route('/tests', methods=['GET'])
def get_tests():
    with open('testdb.json') as f:
        data = json.load(f)
    return jsonify(data)


@app.route('/run-test', methods=['POST'])
def run_test():
    test_id = request.json['id']
    print("test set to run with id" , test_id)
    
    with open('testdb.json', 'r') as file:
    # Load the JSON data from the file into a dictionary
        data = json.load(file)
    for obj in data:
        if test_id in obj:
            test_data = obj
            break
    print(test_data)
    for elt in test_data:
        test_script = importlib.import_module("generatedTests."+test_data[elt]["test_name"])
        test_script.main()
    return ""

if __name__ == '__main__':
    CORS(app)
    app.run(debug=True, port=5000)
    
