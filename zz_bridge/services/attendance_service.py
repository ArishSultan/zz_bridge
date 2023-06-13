from ..api import ZohoAPI, ZkAPI


class AttendanceService:
    def __init__(self, zk_api, zoho_api):
        self.zk_api = zk_api
        self.zoho_api = zoho_api

    def get_device_attendance(self):
        return self.zk_api.get_attendance()

    def sync_to_zoho(self):
        attendances = self.zk_api.get_attendance()

        for attendance in attendances:
            self.zoho_api.post_attendance({
                'dateFormat': 'yyyyMMddHHmmss',
                'empId': attendance.user_id,
                ('checkOut' if attendance.punch == 0 else 'checkIn'):
                    str(attendance.timestamp).replace(':', '').replace(' ', '').replace('-', '')
            })

        self.zk_api.clear_attendance()

    def live_capture(self, func):
        for _ in self.zk_api.live_capture():
            func()

    @staticmethod
    def resolve_status(status):
        if status == 0:
            return 'Check In'
        elif status == 1:
            return 'Check Out'

# CTO
# DEV
# 44 45 56
