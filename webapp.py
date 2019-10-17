from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/responseLanguage")
def render_responseLanguage():
    translate = request.args['language'] 
    if translate == "thank you":
        response = "Xeixei!"
    elif translate == "cheers":
       response = "Ganbei" 
       
    elif translate == "sorry":
        response = "Dubuqui"
    else:
        translate == "love"
        response = "Wo ai ni"
  
        
    return render_template('response.html', responseFromServer=response)       

@app.route("/responseMoney")
def render_responseMoney():    
    convertM = request.args['money']
    if convertM == "one":
        response = "108.86"
    elif convertM == "5.00":
        response = "544.30"
        
    elif convertM == "twenty":
        response = "2170.30"
    else:
        convertM == "hundred"
        response = "10851.50"
    
    return render_template('response.html', responseFromServer=response)

@app.route("/responseWeight")
def render_responseWeight():    
    convertW = request.args['weight']
    if convertW == "One":
        response = ".453592"
    elif convertW == "Five":
        response = "2.26796"
        
    elif convertW == "Fifteen":
        response = "6.80389"
    else:
        convertW == "Fifty"
        response = "22.6796"
    
    return render_template('response.html', responseFromServer=response)   

    
@app.route("/Language")
def render_page1():
    return render_template('language.html')
    
@app.route("/Money")
def render_page2():
    return render_template('money.html')

@app.route("/Weight")
def render_page3():
    return render_template('weight.html')
    
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
