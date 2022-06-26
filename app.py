from flask import Flask

app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    return "Starting Machine Learning Project and CI CD Pipeline has been Established"


if __name__=="__main__":
    app.run(debug=True)