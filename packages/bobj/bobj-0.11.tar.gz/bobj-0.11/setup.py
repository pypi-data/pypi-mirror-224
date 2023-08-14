from setuptools import setup, find_packages
long_description = """
This library provides a solution for automating SAP Business Objects (BOBJ) tasks. It has been designed to accelerate processes and empower practitioners with the following capabilities:

1. **User Management**
   <table border="0" cellspacing="0" cellpadding="0">
     <tr>
       <td>Listing: View all users</td>
       <td>Creating: Add new users</td>
     </tr>
     <tr>
       <td>Modifying/Updating: Edit existing user details</td>
       <td>Deleting: Remove users</td>
     </tr>
   </table>

2. **Folder Management**
   <table border="0" cellspacing="0" cellpadding="0">
     <tr>
       <td>Listing: View all folders</td>
       <td>Creating: Create new folders</td>
     </tr>
     <tr>
       <td>Modifying/Updating: Edit existing folder details</td>
       <td>Deleting: Remove folders</td>
     </tr>
   </table>

3. **Server Management**
   <table border="0" cellspacing="0" cellpadding="0">
     <tr>
       <td>Utilization: Monitor server usage</td>
       <td>Hung-up Notification: Receive notifications for hung-up issues</td>
     </tr>
     <tr>
       <td>Event Server Health: Check the health status of event servers</td>
       <td>... (Additional features)</td>
     </tr>
   </table>

4. **Instance Management**
   <table border="0" cellspacing="0" cellpadding="0">
     <tr>
       <td>Running Instances: View details including Historical Running Time, Database Details, History of Failures and Totals</td>
       <td>Failed Instances: Examine details including Historical Running Time, Database Details, History of Failures and Totals</td>
     </tr>
     <tr>
       <td>Upcoming Instances: Preview details including Historical Running Time, Database Details, History of Failures and Totals</td>
       <td></td>
     </tr>
   </table>

This library serves as an essential tool for managing and maintaining SAP Business Objects efficiently and effectively.
"""




setup(
    name='bobj', # You can replace this with your chosen name
    version='0.0011', # Indicating beta version
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
    
