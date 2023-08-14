
import requests
from .login import BOValidation
from .users import UserManagement
# Import other necessary modules...


class validate:
    def __init__(self, url, **kwargs):
        self._session = requests.Session()
        self.url = url
        self.login = BOValidation(self.url, **kwargs)
        self.user_management = UserManagement()
        # Create other class instances and pass kwargs...

    def list_users(self, **kwargs):
        return self.user_management.list_users(**kwargs)



# # core.py
# class Validate:
#     def __init__(self, url, **kwargs):
#         self._session = requests.Session()
#         self.url = url
#         self.login = BOValidation(self.url, **kwargs)
#         self.user_management = UserManagement()
#         # self.folders_management = FoldersManagement()
        
#         self._generate_methods()

#     def _generate_methods(self):
#         method_sources = {
#             "list_users": self.user_management,
#             "create_user": self.user_management,
#             # Add other method names and sources from users.py...
            
#             "list_folders": self.folders_management,
#             "create_folder": self.folders_management,
#             # Add other method names and sources from folders.py...
#         }
        
#         for method_name, source in method_sources.items():
#             setattr(self, method_name, getattr(source, method_name))

