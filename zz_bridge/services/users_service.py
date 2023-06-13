from zk import const
from ..api import ZohoAPI, ZkAPI


class UsersService:
    def __init__(self, zk_api, zoho_api):
        self.zk_api = zk_api
        self.zoho_api = zoho_api

    def get_device_users(self):
        return self.zk_api.get_users()

    def sync_to_device(self):
        raw_employees = self.zoho_api.fetch_employees()
        employees = {}
        for employee in raw_employees:
            eid = list(employee.keys())[0]
            employees[eid] = employee[eid][0]

        for uid in employees:
            if uid not in employees:
                continue

            employee = employees[uid]
            emp_id = employee['EmployeeID']

            try:
                self.zk_api.create_user(
                    user_id=emp_id,
                    name=f'{employee["FirstName"]} {employee["LastName"]}',
                    privilege=const.USER_DEFAULT,
                )
            except Exception as err:
                print(err)
