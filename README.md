# Insurance Predictor For Nano-Entrepreneurs

## Project Description
This project provides a web-based application to predict health insurance costs based on various personal and health-related factors. It is designed to assist nano-entrepreneurs in estimating potential insurance expenses, enabling better financial planning. The application uses a machine learning model trained on a dataset of health insurance information.

## Features
*   **Web Interface:** User-friendly web form for inputting personal details.
*   **Insurance Cost Prediction:** Predicts insurance charges based on age, gender, BMI, number of children, smoking status, and region.
*   **Data Validation:** Basic server-side validation for input parameters.
*   **Machine Learning Model:** Utilizes a trained scikit-learn model for predictions.

## Technologies Used
*   **Python:** Core programming language.
*   **Flask:** Web framework for building the application.
*   **scikit-learn:** Machine learning library for model training and prediction.
*   **Pandas:** Data manipulation and analysis.
*   **NumPy:** Numerical operations.
*   **Materialize CSS:** Frontend framework for responsive and modern design.
*   **Jupyter Notebook:** For data analysis and exploration (`6_Health Insurance Cost Analysis and Prediction.ipynb`).

## Setup and Installation

To set up and run this project locally, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/TashonBraganca/Insurance-Predictor-For-Nano-Entrepreneurs.git
    cd Insurance-Predictor-For-Nano-Entrepreneurs
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    # On Windows
    .\venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Ensure the model is trained:**
    The `insurance_model.pkl` file should be present in the root directory. If it's missing or you wish to retrain the model, run:
    ```bash
    python train_model.py
    ```
    This will train the model using `insurance.csv` and save it as `insurance_model.pkl`.

## Usage

### Running the Web Application

To start the Flask web application:

```bash
python app.py
```

The application will typically run on `http://127.0.0.1:5000/`. Open this URL in your web browser to access the insurance predictor.

### Retraining the Model

If you update the `insurance.csv` dataset or want to retrain the model for any reason, simply run the `train_model.py` script:

```bash
python train_model.py
```
This will overwrite the existing `insurance_model.pkl` with the newly trained model.

## Project Structure

```
Insurance-Predictor-For-Nano-Entrepreneurs/
├── app.py                      # Flask web application
├── train_model.py              # Script to train and save the ML model
├── insurance_model.pkl         # Trained machine learning model (generated by train_model.py)
├── insurance.csv               # Dataset used for model training
├── requirements.txt            # Python dependencies
├── 6_Health Insurance Cost Analysis and Prediction.ipynb # Jupyter Notebook for data analysis
├── README.md                   # Project README file
├── sampleImages/               # Contains sample images related to analysis/deployment
│   ├── AgevsCharges.png
│   ├── Cor.png
│   ├── deployments.png
│   └── doc.gif
├── static/                     # Static files (CSS, JS) for the web application
│   ├── css/
│   │   ├── materialize.css
│   │   └── materialize.min.css
│   └── js/
│       ├── materialize.js
│       └── materialize.min.js
└── templates/                  # HTML templates for the web application
    ├── home.html               # Input form for predictions
    └── op.html                 # Output page for displaying predictions
```

## Model Details
The machine learning model used is a `Linear Regression` model combined with `Polynomial Features` (degree 2). This approach allows the model to capture non-linear relationships between the input features and the insurance charges.

**Data Preprocessing:**
*   Categorical features (`sex`, `smoker`, `region`) are converted into numerical representations.
*   `sex` and `smoker` are mapped to 0s and 1s.
*   `region` is one-hot encoded using `pandas.get_dummies` with `drop_first=True` to avoid multicollinearity.

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests.

## License
This project is open-source and available under the [MIT License](https://opensource.org/licenses/MIT).
