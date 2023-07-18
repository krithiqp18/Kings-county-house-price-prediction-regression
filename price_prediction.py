from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('modelpickleR.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input features from the form
    bedrooms = float(request.form['bedrooms'])
    bathrooms = float(request.form['bathrooms'])
    sqft_living = float(request.form['sqft_living'])
    sqft_lot = float(request.form['sqft_lot'])
    floors = float(request.form['floors'])
    waterfront = float(request.form['waterfront'])
    view = float(request.form['view'])
    grade = float(request.form['grade'])
    sqft_above = float(request.form['sqft_above'])
    sqft_basement = float(request.form['sqft_basement'])
    yr_renovated = float(request.form['yr_renovated'])
    lat = float(request.form['lat'])
    sqft_living15 = float(request.form['sqft_living15'])

    # Create a list of input features
    features = [bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view,
                grade, sqft_above, sqft_basement, yr_renovated, lat, sqft_living15]

    # Reshape the features to match the model's input shape
    features = [features]

    # Use the loaded model to predict the house price
    predicted_price = model.predict(features)

    # Render the template with the predicted price
    return render_template('index.html', predicted_price=predicted_price[0])

if __name__ == '__main__':
    app.run(debug=True)