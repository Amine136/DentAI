from flask import Flask, render_template, request
from integration import pred
import pandas as pd


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        v1 = request.form['num1']
        v2 = request.form['num2']
        v3 = request.form['num3']
        v4 = request.form['num4']
        v5 = request.form['num5']
        v6 = request.form['num6']
        v7 = request.form['num7']
        v8 = request.form['num8']
        v9 = request.form['num9']
        v10 = request.form['num10']
        v11 = request.form['num11']


        data_test = exemple = pd.DataFrame({"Douleur Spontanée" : [v1] ,
                                            "Douleur Provoquée" : [v2] ,
                                            "Mobilité" : [v3] ,
                                            "Vitalité" : [v4] ,
                                            "Palpation Apicale" : [v5] ,
                                            "Fievre" : [v6] ,
                                            "Asthenie" : [v7] ,
                                            "Odeur Fétide" : [v8] ,
                                            "Médication ATG" : [v9] ,
                                            "Soulager " : [v10], 
                                            "Observations Exobuccales ( remarque generale ) " : [v11]
                                            } )


         
        result = pred(data_test)
            
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
