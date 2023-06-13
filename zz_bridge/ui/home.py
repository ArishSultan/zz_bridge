from .tabs import UsersTab, AttendanceTab
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QTabWidget, QLabel


class HomeWindow(QMainWindow):
    def __init__(self, users_service, attendance_service):
        super().__init__()

        self.setWindowTitle("Tab View Example")
        self.setGeometry(100, 100, 400, 300)

        # Create a central widget and set a layout
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create a QTabWidget
        tab_widget = QTabWidget(self)
        layout.addWidget(tab_widget)

        # Create tabs and add them to the tab widget
        tab1 = UsersTab(users_service)
        tab2 = AttendanceTab(attendance_service)

        tab_widget.addTab(tab1, 'Users')
        tab_widget.addTab(tab2, 'Attendance')


result = {'response': {'result': [{'745889000000288067': [
    {'EmailID': 'arish@sparkosol.com', 'CreatedTime': '1686038533933', 'Employee_type.id': '745889000000039959',
     'Date_of_birth': '', 'AddedTime': '06-Jun-2023 13:02:13',
     'Photo': 'https://contacts.zoho.com/file?ID=810053992&fs=thumb', 'Gender': 'Male', 'Marital_status': '',
     'ModifiedBy': '5-728268-23022007 - Muhammad - Arslan', 'ApprovalStatus': 'Approval Not Enabled',
     'Second_Reporting_To': '', 'Department': 'Sofrware Development', 'LocationName.ID': '745889000000275135',
     'tabularSections': {'Education Details': [{}], 'Work Experience': [{}], 'Dependent Details': [{}]},
     'AddedBy': '5-728268-23022007 - Muhammad - Arslan', 'Mobile.country_code': '', 'Tags': '',
     'Reporting_To': 'Usman Arshad 1-676979-20060501',
     'Photo_downloadUrl': 'https://contacts.zoho.com/file?ID=810053992&fs=thumb',
     'Source_of_hire.id': '745889000000275147', 'total_experience.displayValue': '3 year(s)',
     'Employeestatus': 'Active', 'Role': 'Admin', 'Experience': '3', 'Employee_type': 'Permanent',
     'AddedBy.ID': '745889000000254001', 'Role.ID': '745889000000035631', 'LastName': 'Sultan Khan',
     'EmployeeID': '3-444556-20060501', 'ZUID': '810053992', 'Dateofexit': '', 'Permanent_Address': '',
     'Second_Reporting_To.ID': '', 'Other_Email': '', 'LocationName': 'SparkoSol', 'Work_location': '',
     'Present_Address': '', 'Nick_Name': '', 'total_experience': '36', 'ModifiedTime': '1686048654617',
     'Reporting_To.MailID': 'usman@sparkosol.com', 'Zoho_ID': 745889000000288067,
     'Designation.ID': '745889000000275242', 'Source_of_hire': 'Co-Founder', 'Age': '0',
     'Designation': 'Co-Founder & CTO', 'Age.displayValue': '', 'FirstName': 'Muhammad Arish', 'AboutMe': '',
     'Dateofjoining': '05-Jun-2020', 'Experience.displayValue': '3 year(s)', 'Mobile': '', 'Extension': '',
     'ModifiedBy.ID': '745889000000254001', 'Reporting_To.ID': '745889000000275151', 'Work_phone': '',
     'Employeestatus.type': 1, 'Department.ID': '745889000000281022', 'Expertise': ''}]}, {'745889000000288048': [
    {'EmailID': 'mariam.rimsha@sparkosol.com', 'CreatedTime': '1685794797370', 'Date_of_birth': '',
     'AddedTime': '03-Jun-2023 17:19:57', 'Photo': 'https://contacts.zoho.com/file?ID=-1&fs=thumb', 'Gender': '',
     'Marital_status': '', 'ModifiedBy': '5-728268-23022007 - Muhammad - Arslan',
     'ApprovalStatus': 'Approval Not Enabled', 'Second_Reporting_To': '', 'Department': '', 'LocationName.ID': '',
     'tabularSections': {'Education Details': [{}], 'Work Experience': [{}], 'Dependent Details': [{}]},
     'AddedBy': '5-728268-23022007 - Muhammad - Arslan', 'Mobile.country_code': '', 'Tags': '', 'Reporting_To': '',
     'Photo_downloadUrl': 'https://contacts.zoho.com/file?ID=-1&fs=thumb', 'total_experience.displayValue': '',
     'Employeestatus': 'Active', 'Role': 'Team member', 'Experience': '0', 'Employee_type': '',
     'AddedBy.ID': '745889000000254001', 'Role.ID': '745889000000035635', 'LastName': 'Mariam',
     'EmployeeID': '6-728268-23052501', 'ZUID': '', 'Dateofexit': '', 'Permanent_Address': '',
     'Second_Reporting_To.ID': '', 'Other_Email': '', 'LocationName': '', 'Work_location': '', 'Present_Address': '',
     'Nick_Name': '', 'total_experience': '0', 'ModifiedTime': '1685796857954', 'Reporting_To.MailID': '',
     'Zoho_ID': 745889000000288048, 'Designation.ID': '', 'Source_of_hire': '', 'Age': '0', 'Designation': '',
     'Age.displayValue': '', 'FirstName': 'Rimsha', 'AboutMe': '', 'Dateofjoining': '', 'Experience.displayValue': '',
     'Mobile': '', 'Extension': '', 'ModifiedBy.ID': '745889000000254001', 'Reporting_To.ID': '', 'Work_phone': '',
     'Employeestatus.type': 1, 'Department.ID': '', 'Expertise': ''}]}, {'745889000000281118': [
    {'EmailID': 'accounts@sparkosol.com', 'CreatedTime': '1685451565449', 'Employee_type.id': '745889000000039959',
     'Date_of_birth': '', 'AddedTime': '30-May-2023 17:59:25',
     'Photo': 'https://contacts.zoho.com/file?ID=812381147&fs=thumb', 'Gender': '', 'Marital_status': '',
     'ModifiedBy': '5-728268-23022007 - Muhammad - Arslan', 'ApprovalStatus': 'Approval Not Enabled',
     'Second_Reporting_To': '', 'Department': '', 'LocationName.ID': '745889000000275135',
     'tabularSections': {'Education Details': [{}], 'Work Experience': [{}], 'Dependent Details': [{}]},
     'AddedBy': '5-728268-23022007 - Muhammad - Arslan', 'Mobile.country_code': '', 'Tags': '', 'Reporting_To': '',
     'Photo_downloadUrl': 'https://contacts.zoho.com/file?ID=812381147&fs=thumb', 'total_experience.displayValue': '',
     'Employeestatus': 'Active', 'Role': 'Admin', 'Experience': '0', 'Employee_type': 'Permanent',
     'AddedBy.ID': '745889000000254001', 'Role.ID': '745889000000035631', 'LastName': 'SparkoSol',
     'EmployeeID': '20060500', 'ZUID': '812381147', 'Dateofexit': '', 'Permanent_Address': '',
     'Second_Reporting_To.ID': '', 'Other_Email': '', 'LocationName': 'SparkoSol', 'Work_location': '',
     'Present_Address': '', 'Nick_Name': '', 'total_experience': '0', 'ModifiedTime': '1685600755069',
     'Reporting_To.MailID': '', 'Zoho_ID': 745889000000281118, 'Designation.ID': '', 'Source_of_hire': '', 'Age': '0',
     'Designation': '', 'Age.displayValue': '', 'FirstName': 'Accounts', 'AboutMe': '', 'Dateofjoining': '',
     'Experience.displayValue': '', 'Mobile': '', 'Extension': '', 'ModifiedBy.ID': '745889000000254001',
     'Reporting_To.ID': '', 'Work_phone': '', 'Employeestatus.type': 1, 'Department.ID': '', 'Expertise': ''}]}, {
                             '745889000000281001': [{'EmailID': 'haroon@sparkosol.com', 'CreatedTime': '1685447472220',
                                                     'Employee_type.id': '745889000000039959', 'Date_of_birth': '',
                                                     'AddedTime': '30-May-2023 16:51:12',
                                                     'Photo': 'https://contacts.zoho.com/file?ID=-1&fs=thumb',
                                                     'Gender': '', 'Marital_status': '',
                                                     'ModifiedBy': '5-728268-23022007 - Muhammad - Arslan',
                                                     'ApprovalStatus': 'Approval Not Enabled',
                                                     'Second_Reporting_To': '', 'Department': 'Business Development',
                                                     'LocationName.ID': '745889000000275135',
                                                     'tabularSections': {'Education Details': [{}],
                                                                         'Work Experience': [{}],
                                                                         'Dependent Details': [{}]},
                                                     'AddedBy': '5-728268-23022007 - Muhammad - Arslan',
                                                     'Mobile.country_code': '', 'Tags': '',
                                                     'Reporting_To': 'Usman Arshad 1-676979-20060501',
                                                     'Photo_downloadUrl': 'https://contacts.zoho.com/file?ID=-1&fs=thumb',
                                                     'Source_of_hire.id': '745889000000275147',
                                                     'total_experience.displayValue': '3 year(s)',
                                                     'Employeestatus': 'Active', 'Role': 'Admin', 'Experience': '3',
                                                     'Employee_type': 'Permanent', 'AddedBy.ID': '745889000000254001',
                                                     'Role.ID': '745889000000035631', 'LastName': 'Ashraf',
                                                     'EmployeeID': '3-676679-20060503', 'ZUID': '809002950',
                                                     'Dateofexit': '', 'Permanent_Address': '',
                                                     'Second_Reporting_To.ID': '', 'Other_Email': '',
                                                     'LocationName': 'SparkoSol', 'Work_location': '',
                                                     'Present_Address': '', 'Nick_Name': '', 'total_experience': '36',
                                                     'ModifiedTime': '1685600629972',
                                                     'Reporting_To.MailID': 'usman@sparkosol.com',
                                                     'Zoho_ID': 745889000000281001,
                                                     'Designation.ID': '745889000000275276',
                                                     'Source_of_hire': 'Co-Founder', 'Age': '0',
                                                     'Designation': 'Co-Founder & CBDO', 'Age.displayValue': '',
                                                     'FirstName': 'Haroon', 'AboutMe': '',
                                                     'Dateofjoining': '05-Jun-2020',
                                                     'Experience.displayValue': '3 year(s)', 'Mobile': '',
                                                     'Extension': '', 'ModifiedBy.ID': '745889000000254001',
                                                     'Reporting_To.ID': '745889000000275151', 'Work_phone': '',
                                                     'Employeestatus.type': 1, 'Department.ID': '745889000000281012',
                                                     'Expertise': ''}]}, {'745889000000275151': [
    {'EmailID': 'usman@sparkosol.com', 'CreatedTime': '1685101596177', 'Employee_type.id': '745889000000039959',
     'Date_of_birth': '', 'AddedTime': '26-May-2023 16:46:36', 'Photo': 'https://contacts.zoho.com/file?ID=-1&fs=thumb',
     'Gender': 'Male', 'Marital_status': '', 'ModifiedBy': '5-728268-23022007 - Muhammad - Arslan',
     'ApprovalStatus': 'Approval Not Enabled', 'Second_Reporting_To': '', 'Department': 'CEO Office',
     'LocationName.ID': '745889000000275135',
     'tabularSections': {'Education Details': [{}], 'Work Experience': [{}], 'Dependent Details': [{}]},
     'Permanent_Address.childValues': {'COUNTRY': 'PAKISTAN', 'ADDRESS1': 'N/A', 'COUNTRY_CODE': 'PK'},
     'AddedBy': '5-728268-23022007 - Muhammad - Arslan', 'Mobile.country_code': '', 'Tags': '', 'Reporting_To': '',
     'Photo_downloadUrl': 'https://contacts.zoho.com/file?ID=-1&fs=thumb', 'Source_of_hire.id': '745889000000275143',
     'total_experience.displayValue': '3 year(s)', 'Employeestatus': 'Active', 'Role': 'Admin', 'Experience': '3',
     'Employee_type': 'Permanent', 'AddedBy.ID': '745889000000254001', 'Role.ID': '745889000000035631',
     'LastName': 'Arshad', 'EmployeeID': '1-676979-20060501', 'ZUID': '812067074', 'Dateofexit': '',
     'Permanent_Address': 'N/A,PAKISTAN', 'Second_Reporting_To.ID': '', 'Other_Email': '', 'LocationName': 'SparkoSol',
     'Work_location': '', 'Present_Address': 'N/A,PAKISTAN', 'Nick_Name': '', 'total_experience': '36',
     'ModifiedTime': '1685101892480', 'Reporting_To.MailID': '', 'Zoho_ID': 745889000000275151,
     'Designation.ID': '745889000000275212', 'Source_of_hire': 'Founder', 'Age': '0', 'Designation': 'Founder & CEO',
     'Age.displayValue': '', 'FirstName': 'Usman', 'AboutMe': '', 'Dateofjoining': '05-Jun-2020',
     'Experience.displayValue': '3 year(s)', 'Mobile': '', 'Extension': '', 'ModifiedBy.ID': '745889000000254001',
     'Reporting_To.ID': '', 'Work_phone': '', 'Employeestatus.type': 1, 'Department.ID': '745889000000275027',
     'Present_Address.childValues': {'COUNTRY': 'PAKISTAN', 'ADDRESS1': 'N/A', 'COUNTRY_CODE': 'PK'},
     'Expertise': ''}]}, {'745889000000254001': [
    {'EmailID': 'manager.hr@sparkosol.com', 'CreatedTime': '1683615640277', 'Employee_type.id': '745889000000039959',
     'Date_of_birth': '30-Nov-1993', 'AddedTime': '09-May-2023 12:00:40',
     'Photo': 'https://contacts.zoho.com/file?ID=810577068&fs=thumb', 'Gender': 'Male', 'Marital_status': 'Single',
     'ModifiedBy': '5-728268-23022007 - Muhammad - Arslan', 'ApprovalStatus': 'Approval Not Enabled',
     'Second_Reporting_To': '', 'Department': 'Human Resources Department', 'LocationName.ID': '745889000000275135',
     'tabularSections': {'Education Details': [
         {'Specialization': 'International Trade & Economics', 'Degree': "Bachelor's", 'College': 'GXUFE',
          'Yearofgraduation': 'June 2020', 'tabular.ROWID': '745889000000275021'}], 'Work Experience': [
         {'Jobtitle': 'Training Manager - Islamabad', 'Employer': 'Medical Lien Management', 'RELEVANCE': 'Yes',
          'Previous_JobDesc': '', 'FromDate': '', 'Todate': '', 'tabular.ROWID': '745889000000275007',
          'RELEVANCE.id': '745889000000202025'}], 'Dependent Details': [{}]},
     'Permanent_Address.childValues': {'CITY': 'Multan', 'COUNTRY': 'PAKISTAN', 'STATE': 'Punjab',
                                       'ADDRESS1': 'Gulshan e Sadat Colony, Near Chowk Qadafi, Khanewal Road,',
                                       'PINCODE': '60650', 'STATE_CODE': 'PK-PB', 'COUNTRY_CODE': 'PK'}, 'AddedBy': '',
     'Mobile.country_code': 'pk', 'Tags': '', 'Reporting_To': 'Usman Arshad 1-676979-20060501',
     'Photo_downloadUrl': 'https://contacts.zoho.com/file?ID=810577068&fs=thumb',
     'Source_of_hire.id': '745889000000039975', 'total_experience.displayValue': '3 month(s)',
     'Employeestatus': 'Probation', 'Role': 'Admin', 'Experience': '0', 'Employee_type': 'Permanent', 'AddedBy.ID': '',
     'Role.ID': '745889000000035631', 'LastName': 'Arslan', 'EmployeeID': '5-728268-23022007', 'ZUID': '810577068',
     'Dateofexit': '',
     'Permanent_Address': 'Gulshan e Sadat Colony, Near Chowk Qadafi, Khanewal Road,,Multan,Punjab,PAKISTAN,60650',
     'Second_Reporting_To.ID': '', 'Other_Email': 'arsalan.baloch@protonmail.ch', 'LocationName': 'SparkoSol',
     'Work_location': '',
     'Present_Address': 'Gulshan e Sadat Colony, Near Chowk Qadafi, Khanewal Road,,Multan,Punjab,PAKISTAN,60650',
     'Nick_Name': 'Arsalan Baloch', 'total_experience': '3', 'ModifiedTime': '1685103850040',
     'Reporting_To.MailID': 'usman@sparkosol.com', 'Zoho_ID': 745889000000254001,
     'Designation.ID': '745889000000275230', 'Source_of_hire': 'Direct', 'Age': '29',
     'Designation': 'Human Resources Manager', 'Age.displayValue': '29 year(s) 6 month(s)',
     'Marital_status.id': '745889000000039985', 'FirstName': 'Muhammad', 'AboutMe': '', 'Dateofjoining': '20-Feb-2023',
     'Experience.displayValue': '3 month(s)', 'Mobile': '92-3123111115', 'Extension': '',
     'ModifiedBy.ID': '745889000000254001', 'Reporting_To.ID': '745889000000275151', 'Work_phone': '+92 300 6233355',
     'Employeestatus.type': 1, 'Department.ID': '745889000000275045',
     'Present_Address.childValues': {'CITY': 'Multan', 'COUNTRY': 'PAKISTAN', 'STATE': 'Punjab',
                                     'ADDRESS1': 'Gulshan e Sadat Colony, Near Chowk Qadafi, Khanewal Road,',
                                     'PINCODE': '60650', 'STATE_CODE': 'PK-PB', 'COUNTRY_CODE': 'PK'},
     'Expertise': ''}]}], 'message': 'Data fetched successfully', 'uri': '/api/forms/employee/getRecords', 'status': 0}}
