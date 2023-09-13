from .models import Employee
from import_export import resources

class EmployeeResource(resources.ModelResource):
    class meta:
        model=Employee