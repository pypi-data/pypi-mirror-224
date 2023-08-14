from setuptools import setup, find_packages


long_description = """
This library provides a solution for automating SAP Business Objects (BOBJ) tasks. It has been designed to accelerate processes and empower practitioners with the following capabilities:

1. **User Management**
    - Listing: View all users
    - Creating: Add new users
    - Modifying/Updating: Edit existing user details
    - Deleting: Remove users

2. **Folder Management**
    - Listing: View all folders
    - Creating: Create new folders
    - Modifying/Updating: Edit existing folder details
    - Deleting: Remove folders

3. **Server Management**
    - Utilization: Monitor server usage
    - Hung-up Notification: Receive notifications for hung-up issues
    - Event Server Health: Check the health status of event servers
    - ... (Additional features)

4. **Instance Management**
    - Running Instances: View details of running instances, including:
        1. Historical Running Time
        2. Database Details
        3. History of Failures and Totals
    - Failed Instances: Examine details of failed instances, including:
        1. Historical Running Time
        2. Database Details
        3. History of Failures and Totals
    - Upcoming Instances: Preview details of upcoming instances, including:
        1. Historical Running Time
        2. Database Details
        3. History of Failures and Totals

This library serves as an essential tool for managing and maintaining SAP Business Objects efficiently and effectively.
"""




setup(
    name='bobj', # You can replace this with your chosen name
    version='0.1b3', # Indicating beta version
    packages=find_packages(),
    install_requires=[
        'requests>=2.25', # Required dependency
    ],
    author='Rajat Gupta',
    author_email='rajatgupta.1988@gmail.com',
    description='A comprehensive toolkit designed to streamline tasks for SAP Business Objects administrators',
    long_description=long_description,
    long_description_content_type="text/markdown", 
)
    
