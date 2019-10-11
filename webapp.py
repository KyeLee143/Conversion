from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/Langauge")
def render_response():
    translate = request.args['language'] 
    if translate == "thank you!":
        response = "Xeixei!"
    else:
        response = "Xeixei"
    return render_template('response.html', responseFromServer=response)

@app.route("/Money")
def render_page2():
    return render_template('money.html')

@app.route("/Weight")
def render_page3():
    return render_template('weight.html')
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
