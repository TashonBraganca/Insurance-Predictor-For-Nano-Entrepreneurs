from flask import Flask, request, url_for, redirect, render_template
import pickle

import numpy as np
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd

app = Flask(__name__, template_folder='./templates', static_folder='./static')

Pkl_Filename = "insurance_model.pkl" 
with open(Pkl_Filename, 'rb') as file:  
    model = pickle.load(file)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract features from form
        age = int(request.form['age'])
        sex = int(request.form['gender']) # 0 for male, 1 for female
        bmi = float(request.form['bmi'])
        children = int(request.form['children'])
        smoker = int(request.form['smoker']) # 0 for no, 1 for yes
        region = int(request.form['region']) # 0: Northwest, 1: Northeast, 2: Southeast, 3: Southwest

        # Basic server-side validation
        if not (1 <= age <= 100):
            return render_template('op.html', pred='Error: Age must be between 1 and 100.')
        if not (10 <= bmi <= 60): # Reasonable BMI range
            return render_template('op.html', pred='Error: BMI must be between 10 and 60.')
        if not (0 <= children <= 10):
            return render_template('op.html', pred='Error: Number of children must be between 0 and 10.')

        # Create a DataFrame for the input, matching the training data's column names
        # This is crucial for PolynomialFeatures and the model to work correctly
        input_data = pd.DataFrame([[age, sex, bmi, children, smoker, region]],
                                  columns=['age', 'sex', 'bmi', 'children', 'smoker', 'region'])

        # Manually apply one-hot encoding for 'region' to match training data
        # The order of columns must match the training data after get_dummies(drop_first=True)
        # Assuming the original regions were 'northeast', 'northwest', 'southeast', 'southwest'
        # And drop_first=True means 'northeast' is the dropped one (index 1 in home.html)
        # So, if region is 1 (Northeast), all region_dummy columns are 0.
        # If region is 0 (Northwest), region_northwest is 1, others 0.
        # If region is 2 (Southeast), region_southeast is 1, others 0.
        # If region is 3 (Southwest), region_southwest is 1, others 0.
        
        region_dummies = pd.DataFrame(0, index=input_data.index, columns=['region_northwest', 'region_southeast', 'region_southwest'])
        if region == 0: # Northwest
            region_dummies['region_northwest'] = 1
        elif region == 2: # Southeast
            region_dummies['region_southeast'] = 1
        elif region == 3: # Southwest
            region_dummies['region_southwest'] = 1
        # If region == 1 (Northeast), all dummy columns remain 0, which is correct for drop_first=True

        # Combine original features with one-hot encoded region features
        # Ensure the order of columns matches the X used during model training
        # The order should be: age, sex, bmi, children, smoker, region_northwest, region_southeast, region_southwest
        final_features = pd.concat([input_data[['age', 'sex', 'bmi', 'children', 'smoker']], region_dummies], axis=1)
        
        # Apply PolynomialFeatures transformation
        # The model pipeline already handles this, so we need to ensure the input to the pipeline is correct.
        # The pipeline expects the raw features, and it will apply PolynomialFeatures internally.
        # So, 'final_features' should be the input to the model.

        pred = model.predict(final_features)[0]

        if pred < 0:
            return render_template('op.html', pred='Error: Cannot calculate a negative insurance amount. Please check your inputs.')
        else:
            return render_template('op.html', pred='Expected amount is ${0:.2f}'.format(pred))

    except ValueError:
        return render_template('op.html', pred='Error: Invalid input. Please ensure all fields are filled correctly with numerical values.')
    except Exception as e:
        return render_template('op.html', pred=f'An unexpected error occurred: {e}')

if __name__ == '__main__':
    app.run(debug=False) # Set debug to False for production