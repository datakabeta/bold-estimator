from flask import Flask, jsonify, request, render_template
import pandas as pd
from preprocessor import preprocess #prepares data for model prediction
from predictor import predict #handles prediction


# Create the application.
app = Flask(__name__)

#home page
@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])

def index():
    return render_template('index.html')

#estimation result
@app.route('/estimate', methods=['GET'])

def show_prediction():

    #construct dataframe
    cols = ['sc_ct', 'ai_conv_widget_ct', 'agent_widget_ct', 'complex_providers_ct', 'is_middleware_dev', 'is_sso', 'kb_ct', 'team_ct','import_none_and_content_available', 'frontend_branding_none_or_simple','delays_prod_bugs_significant_mtgs_cr_partner_beaur','providers_entities']

    args = [request.args['sc_ct'], request.args['ai_conv_widget_ct'], request.args['agent_widget_ct'], request.args['complex_providers_ct'], request.args['is_middleware_dev'], request.args['is_sso'], request.args['kb_ct'], request.args['team_ct'], request.args['import_none_and_content_available'], request.args['frontend_branding_none_or_simple'], request.args['delays_prod_bugs_significant_mtgs_cr_partner_beaur'], request.args['providers_entities']]

    data = pd.DataFrame(args,cols) 
    data = data.T

    # print("data rcvd: ")
    # print("shape: ", data.shape)
    # print(data)

    #pre process data 
    data_processed = preprocess(data)
    
    #predict
    budget_lower,budget_upper = predict(data_processed) #predict 

    # print('data_processed')
    # print("shape ", data_processed.shape)
    # print(data_processed)
    # print('budget ',budget)
    # message = "The lower bound is {0} and upper bound is {1}."
    # return jsonify({'The project is at an estimated': message.format(budget_lower,budget_upper)  })

    return render_template('index.html', prediction_text='{0} hrs - {1} hrs'.format(budget_lower,budget_upper))

if __name__ == '__main__':
    app.debug=True
    app.run()

