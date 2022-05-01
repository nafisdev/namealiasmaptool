from flask import Flask
from main import DataPrep

app = Flask(__name__)
@app.route('/hello/<string:name>/', methods=['GET', 'POST'])
def promptname(name):
    nickname_list = []
    alias_list =[]
    if name.lower() in dataprep.nickname_dict.keys():
        nickname_list = dataprep.nickname_dict[name.lower()]
    if name.lower() in dataprep.alias_dict.keys():
        alias_list = dataprep.alias_dict[name.lower()]

    return {"result": nickname_list+alias_list}

if __name__ == '__main__':
    dataprep = DataPrep()
    app.run(host='0.0.0.0', port=5454)