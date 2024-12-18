import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')  # Use the 'Agg' backend for non-GUI environments
import matplotlib.pyplot as plt
import os
from django.shortcuts import render
from analyzer.form import UploadFileForm
from django.conf import settings
from io import BytesIO
import base64

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['file']
            
            # Read the CSV file using pandas
            try:
                df = pd.read_csv(uploaded_file)
            except Exception as e:
                return render(request, 'upload.html', {'form': form, 'error': f"Error reading CSV: {str(e)}"})

            # Perform basic data analysis
            first_rows = df.head().to_html()
            stats = df.describe().to_html()

            # Handling missing values
            missing_values = df.isnull().sum().to_frame(name='Missing Values').to_html()

            # Generate histograms for numerical columns
            img_str = generate_histograms(df)

            context = {
                'form': form,
                'first_rows': first_rows,
                'stats': stats,
                'missing_values': missing_values,
                'histograms': img_str,
            }
            return render(request, 'results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


def generate_histograms(df):
    img_str = None
    try:
        # Create a plot for each numerical column
        numerical_cols = df.select_dtypes(include=np.number).columns
        if len(numerical_cols) > 0:
            plt.figure(figsize=(10, 6))
            df[numerical_cols].hist(bins=20, figsize=(10, 6), layout=(len(numerical_cols), 1))
            plt.tight_layout()

            # Convert plot to image
            buffer = BytesIO()
            plt.savefig(buffer, format='png')
            buffer.seek(0)
            img_str = base64.b64encode(buffer.read()).decode('utf-8')
            plt.close()
    except Exception as e:
        print(f"Error generating histograms: {e}")
    return img_str