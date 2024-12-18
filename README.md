# CSV Analysis Django Project

This project is a Django web application that allows users to upload CSV files and perform basic data analysis. The application reads the uploaded CSV file, displays the first few rows, provides summary statistics, handles missing values, and generates histograms for numerical columns.

## Features

- Upload CSV files for analysis.
- Display the first few rows of the dataset.
- Provide summary statistics of the dataset.
- Identify and display missing values.
- Generate histograms for numerical columns.

## Setup Instructions

### Prerequisites

- Python 3.13.1
- Django 5.1.4
- Pandas
- NumPy
- Matplotlib

### Installation

1. **Clone the Repository**

      ```bash
      git clone https://github.com/theomvirsingh/Django-Assignment.git
      cd csv-analysis
      ```
2. **Create a Virtual Environment**

   ```python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```pip install -r requirements.txt```

4. **Run Migrations**

   ```python manage.py migrate```

5. **Start the Development Server**

   ```python manage.py runserver```

6. **Access the Application**

   Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

### Project Structure

   `csv_analysis/`: Main project directory containing settings and configurations.
   
   `analyzer/`: Django app responsible for handling file uploads and data analysis.
   
   `templates/`: Directory containing HTML templates for the application.
   
   `static/`: Directory for static files (CSS, JavaScript, images).

### Usage

   1. Navigate to the upload page.
      
   2. Select a CSV file from your local machine.
      
   3. Click the "Upload" button to analyze the file. (Sample `organizations-100.csv` is provided)
      
   4. View the analysis results, including data preview, statistics, missing values, and histograms.

### Acknowledgments

Django: https://www.djangoproject.com/

Pandas: https://pandas.pydata.org/

NumPy: https://numpy.org/

Matplotlib: https://matplotlib.org/
