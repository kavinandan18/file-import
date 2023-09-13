from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from .models import Employee
from .resources import EmployeeResource
from tablib import Dataset

# Create a class-based view for handling file uploads
class SimpleUploadView(View):
    # Specify the template name for rendering
    template_name = 'uploadfile.html'

    # Define the logic for handling HTTP GET requests
    def get(self, request, *args, **kwargs):
        # Handle GET request logic here
        return render(request, self.template_name)

    # Define the logic for handling HTTP POST requests
    def post(self, request, *args, **kwargs):
        # Instantiate the EmployeeResource for data processing
        emp_resource = EmployeeResource()
        
        # Get the uploaded file from the request
        emp_data = request.FILES.get('myfiles')

        try:
            # Check if a file was uploaded
            if not emp_data:
                raise ValueError("No file was uploaded.")

            # Check if the uploaded file has a .xlsx extension
            if not emp_data.name.endswith('.xlsx'):
                raise ValueError("Invalid file format. Please upload a .xlsx file.")

            # Create a Dataset for handling the file data
            dataset = Dataset()

            # Load the data from the uploaded file using the 'xlsx' format
            imported_data = dataset.load(emp_data.read(), format='xlsx')

            # Iterate through the imported data and create Employee objects
            for data in imported_data:
                employee = Employee(
                    uid=data[0],
                    ename=data[1],
                    age=data[2],
                    salary=data[3],
                    location=data[4],
                )
                employee.save()

            # Display a success message if data was uploaded and saved successfully
            messages.success(request, 'Data uploaded and saved successfully.')
        
        except ValueError as e:
            # Display a custom error message for invalid file or no file uploaded
            messages.error(request, str(e))
        
        except Exception as e:
            # Display a generic error message for other exceptions
            messages.error(request, f'An error occurred: {str(e)}')

        # Render the template with appropriate messages
        return render(request, self.template_name)
