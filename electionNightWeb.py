from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)             # create an app instance

@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return  render_template("home.html")
         # which returns "hello world"

@app.route("/background_process_testEdison", methods=['GET'])
def background_process_testEdison():
    state = request.args.get('state')
    if state == 'texas':
        state = 'TX'
    elif state == 'georgia':
        state = 'GA'
    elif state == 'arizona':
        state = 'AZ'
    elif state == 'north_carolina':
        state = 'NC'
    elif state == 'ohio':
        state = 'OH'
    elif state == 'florida':
        state = 'FL'
    elif state == 'new_hampshire':
        state = 'NH'
    elif state == 'iowa':
        state = 'IA'
    elif state == 'nevada':
        state = 'NV'
    elif state == 'michigan':
        state = 'MI'
    elif state == 'wisconsin':
        state = 'WI'
    elif state == 'pennsylvania':
        state = 'PA'
    elif state == 'indiana':
        state = 'IN'
    url = "https://politics-elex-results.data.api.cnn.io/results/view/2020-county-races-PG-{}.json".format(state)
    response = requests.get(url) 
    jsonFile = response.json()
    return json.dumps(jsonFile)

@app.route("/background_process_testAP", methods=['GET'])
def background_process_test():
    state = request.args.get('state')
    if state == 'texas':
        state = 'TX'
    elif state == 'georgia':
        state = 'GA'
    elif state == 'arizona':
        state = 'AZ'
    elif state == 'north_carolina':
        state = 'NC'
    elif state == 'ohio':
        state = 'OH'
    elif state == 'florida':
        state = 'FL'
    elif state == 'new_hampshire':
        state = 'NH'
    elif state == 'iowa':
        state = 'IA'
    elif state == 'nevada':
        state = 'NV'
    elif state == 'michigan':
        state = 'MI'
    elif state == 'wisconsin':
        state = 'WI'
    elif state == 'pennsylvania':
        state = 'PA'
    elif state == 'indiana':
        state = 'IN'
    url = "https://apps.npr.org/elections20-interactive/data/counties/{}-0.json".format(state)
    response = requests.get(url)
    jsonFile = response.json()
#   print(jsonFile['stateMapData'][list(jsonFile['stateMapData'].keys())[1]]['candidates'][0]['name'])
    return jsonFile

@app.route("/background_process_testDDHQ", methods=['GET'])
def background_process_testDDHQ():
    state = request.args.get('state')
    if state == 'texas':
        state = 'tx'
    elif state == 'georgia':
        state = 'ga'
    elif state == 'arizona':
        state = 'az'
    elif state == 'north_carolina':
        state = 'nc'
    elif state == 'ohio':
        state = 'oh'
    elif state == 'florida':
        state = 'fl'
    elif state == 'new_hampshire':
        state = 'nh'
    elif state == 'iowa':
        state = 'ia'
    elif state == 'nevada':
        state = 'nv'
    elif state == 'michigan':
        state = 'mi'
    elif state == 'wisconsin':
        state = 'wi'
    elif state == 'pennsylvania':
        state = 'pa'
    elif state == 'indiana':
        state = 'in'
    url = "https://embeds.ddhq.io/api/v2/2020general_results/2020general_{}".format(state)
    response = requests.get(url)
    jsonFile = response.json()
#   print(jsonFile['stateMapData'][list(jsonFile['stateMapData'].keys())[1]]['candidates'][0]['name'])
    return jsonFile 
"""
@app.route("/background_process_testAZ", methods=['GET'])
def background_process_testAZ():
    response = requests.get("https://cdn1.arizona.vote/data/18/0/all_county_races_18_0_en_8252.json")
    jsonFile = response.json()

@app.route("/background_process_testNC", methods=['GET'])
def background_process_testNC():
    response = requests.get("https://er.ncsbe.gov/enr/20201103/data/results_0.txt?v=2-16-38")
    jsonFile = response.json()

@app.route("/background_process_testTX", methods=['GET'])
def background_process_testTX():
    response = requests.get("https://results.texas-election.com/static/data/election/44144/110/OfficeSummary.json")
    jsonFile = response.json()

@app.route("/background_process_testOH", methods=['GET'])
def background_process_testOH():
    response = requests.get("https://liveresults.ohiosos.gov/Api/v1/Contest/GetContestDetailsObject?contestName=President%20and%20Vice%20President&contestObjectId=_AE5DCDB4E60A432FE0533390EE0A0876&resultsLevel=County&countyId=")
    jsonFile = response.json()
"""
if __name__ == "__main__":        # on running python app.py
    app.run(debug=True)      