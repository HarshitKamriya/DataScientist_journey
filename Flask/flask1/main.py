from flask import Flask,render_template ,request

app = Flask(__name__)

@app.route("/",methods = ["GET","POST"])
def hello_world():
    # if request.method == "POST":
    #     name = request.form["email"]
    #     password = request.form["password"]
    #     print(f"The name is {name} and the pasword is {password}")
    #     # Save it to database
    #     return "<b> Thanks for using facebook, you are know logged in </b>"

    name = "Harshit"
    language = "python"
    luckno = [28,37,38,11]

    return render_template("index.html",name = name,lang = language,lucky = luckno)



if __name__=="__main__":
    app.run(debug=True)

