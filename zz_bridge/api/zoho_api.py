import json

import httpx
from urllib.parse import quote
import requests

_client_id = '1000.JG8AEU1WMJMU7CIZNR81AQ6BHOQS9Y'
_client_secret = 'a495995e06f6c55ddccc8cff30bee6829543c5e536'


class ZohoAPI:
    # instance = ZohoAPI()

    def __init__(self):
        self._access_token = None

    def _get_access_token(self):
        try:
            response = httpx.post(
                url='https://accounts.zoho.com/oauth/v2/token',
                # params={
                #     'client_id': _client_id,
                #     'grant_type': 'authorization_code',
                #     'redirect_uri': 'https://github.com/ArishSultan/zz_bridge',
                #     'client_secret': _client_secret,
                #     'code': '1000.372f5387162b63a20d00c30ade275fb6.b6b1ae3c4146e6cefecbcab1553a8bc2'
                #     # 'refresh_token': '1000.5c9e9ecbd02552296f3aba6e3057a0f3.fc8d6c649f81717bad5407e1250dd6cb',
                # }
                params={
                    'client_id': _client_id,
                    'grant_type': 'refresh_token',
                    'client_secret': _client_secret,
                    'refresh_token': '1000.262255905744628cf6c6586656d78f9f.e16a2c92a23695e235d0aa8ad23346c8',
                }
            )

            response.raise_for_status()
            self._access_token = response.json()['access_token']
            print(response.json())
        except Exception as ex:
            print(f"Error getting access token: {ex}")
            return None

    def fetch_employees(self):
        try:
            response = httpx.get(
                params={'sIndex': 1, 'limit': 100},
                headers={'Authorization': f'Zoho-oauthtoken {self._access_token}'},
                url='https://people.zoho.com/people/api/forms/employee/getRecords?',
            )

            response.raise_for_status()
            return response.json()['response']['result']
        except httpx.HTTPStatusError as err:
            if err.response.status_code == 401:
                self._get_access_token()
                return self.fetch_employees()
            else:
                print(err.request)
                print(err.args)
        except Exception as err:
            print(err)

    def post_attendance(self, data):
        try:
            response = httpx.post(
                params=data,
                headers={'Authorization': f'Zoho-oauthtoken {self._access_token}'},
                url='https://people.zoho.com/people/api/attendance',
            )

            response.raise_for_status()
            print(response.request)
            print(response.url)
            print(response.json())

            return response.json()
        except httpx.HTTPStatusError as err:
            print(err)
            if err.response.status_code == 401:
                self._get_access_token()
                return self.post_attendance(data)
            else:
                print(err.request)
                print(err.args)
        except Exception as err:
            print(err)
