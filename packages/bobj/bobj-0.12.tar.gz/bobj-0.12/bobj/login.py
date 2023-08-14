import requests
from urllib.parse import urlparse
from .Support import inform_bobj_error, notify

        

class BOValidation:
    

    def __init__(self, url, **kwargs):
        
        self.url = url
        self.mode = kwargs.get('mode', None)
        self._validate_url()


        self.validate_kwargs(kwargs)  # Passing kwargs as an argument
        if not self._is_logon_token_valid():
            
            self._validate_params(**kwargs)
            self._generate_logon_token()



    def validate_kwargs(self, kwargs):  # Accepting kwargs as a parameter
        for param, value in kwargs.items():
            if param not in ['username', 'password', 'auth_type', 'prompt', 'mode']:                
                notify(f"Invalid parameter: {param} with value: {value}. Please check the parameters again.", code="Exit")



    def _validate_url(self):
        parsed_url = urlparse(self.url)
        
        # Check if the scheme is missing a forward slash
        if parsed_url.scheme and not parsed_url.netloc:
            notify(f"{parsed_url.scheme} passed seem to be have some issue with syntax. Please correct the URL.", code="Exit")
            return False
        
        if parsed_url.scheme and parsed_url.netloc:
            return True  # URL is valid
    
        # Check with "https" and "http" prefixes
        for scheme in ['https', 'http']:
            modified_url = f"{scheme}://{self.url}"
            parsed_url = urlparse(modified_url)
            if parsed_url.scheme and parsed_url.netloc:
                notify(f"The URL works with '{scheme}' prefix. Please include the correct prefix.", code="Exit")
                return True
    
        notify("Invalid URL. Please check the URL again.", code=1)
        return False



    def _is_logon_token_valid(self):
        
        # Check if the logon_token attribute exists
        if not hasattr(self, 'logon_token'):
            return False
          
        # Making a request to the BO server with the existing token to check its validity
        headers = {'X-SAP-LogonToken': self.logon_token}
        response = requests.get(f'{self.url}/check_token_endpoint', headers=headers)  # Replace with the appropriate endpoint for token validation
        response_json = response.json()
        
          
        # Check the response status and content to determine if the token is valid
        if response.status_code == 200:
            return True
              
        elif response.status_code == 401:  # Unauthorized
            if self.mode == 'secure':
                notify("Logon token has expired. Please enter your password again.", code="TokenExpired")
                self.password = input("Enter password: ")
                self._generate_logon_token()  # Regenerate the token with the new password
            else:
                notify("Logon token is invalid. Response Code: {response.status_code}", code="Error")
            return False
          
        else:
            
            inform_bobj_error(response_json)
            return False

 

    def _validate_params(self, **kwargs):
        
        # Extract parameters from kwargs
        self.username = kwargs.get('username').strip() if kwargs.get('username') else None
        self.password = kwargs.get('password').strip() if kwargs.get('password') else None
        self.auth_type = kwargs.get('auth_type').strip() if kwargs.get('auth_type') else None

       
        # Check if any of the required parameters are missing
        missing_params = [param for param in ['username', 'password', 'auth_type'] if getattr(self, param) is None]
    
        # If all three are missing, prompt user to enter them
        if len(missing_params) == 3:
            notify("All required parameters (username, password, auth_type) are missing. Please enter them.", code = 1)
            self.username = input("Enter username: ")
            self.password = input("Enter password: ")
            self.auth_type = input("Enter authentication type: ")
            return True
    
        # If not all three are missing, ask user to enter missing values or all values
        elif missing_params:
            choice = int(input(f"Some required parameters are missing: {', '.join(missing_params)}. Enter '0' to enter missing values or '1' to enter all values: "))
            if choice == 0:
                for param in missing_params:
                    setattr(self, param, input(f"Enter {param}: "))
            elif choice == 1:
                self.username = input("Enter username: ")
                self.password = input("Enter password: ")
                self.auth_type = input("Enter authentication type: ")
            else:
                notify("Invalid choice. Please try again.", code = 1)
                return False
    
        # Check for any other kwargs and notify user
          
        return True


    def _generate_logon_token(self):
        # Endpoint to generate the logon token (replace with the actual endpoint as per the BO server's API documentation)
        endpoint = f'{self.url}/logon/long'
    
        # Request body containing the username, encrypted password, and authentication type
        request_body = {
            "userName": self.username,
            "password": self.password,  # Encrypting the password
            "auth": self.auth_type
        }
    
        # Making a POST request to the BO server to generate the logon token
        response = requests.post(endpoint, json=request_body)
    
        # Checking the response status code and content to determine if the token generation was successful
        if response.status_code == 200:
            response_json = response.json()
    
            if 'logonToken' in response_json:
                self.logon_token = response_json.get('logonToken')
                if self.mode == 'secure':
                    del self.password
                return True
    
            else:
                
                # Mapping the error code and notifying the user with the corresponding error message
                inform_bobj_error(response_json)
                return False
    
        else:
            notify(f"Cannot process request due to {response.status_code}", code = 'Exit')
