#coding=utf-8

import unittest
import requests

class AddEventTest(unittest.TestCase):

    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/guest/add_event/"

    def test_add_event_null(self):
        '''
        所有参数为空:
        '''
        r = requests.post(self.base_url)
        print(r.status_code)
        result = r.json()
        print(r.json())
        self.assertEqual(result['status'], 201)
        self.assertEqual(result['message'], "parameter error")


    def test_add_event_eid_error(self):
        '''
        eid 已存在:
        '''
        dataline = {'eid': 1, 'name': 'jingjing', 'start_time': '2016-08-22 12:00:00', 'address': 'beijing'}
        r = requests.post(self.base_url, data=dataline)
        print(r.status_code)
        result = r.json()
        print(r.json())
        self.assertEqual(result['status'], 202)
        self.assertEqual(result['message'], "eid already exist")

    def test_add_event_name_error(self):
        '''
        name 已存在:
        '''
        dataline = {'eid': 6, 'name': 'tiantian', 'start_time': '2016-08-22 12:00:00', 'address': 'beijing'}
        r = requests.post(self.base_url, data=dataline)
        print(r.status_code)
        result = r.json()
        print(r.json())
        self.assertEqual(result['status'], 203)
        self.assertIn(result['message'], "name already exist")

    # def test_add_event_success(self):
    #     '''
    #     新增event成功:
    #     '''
    #     dataline = {'eid': 7, 'name': 'jingjing', 'start_time': '2016-08-22 12:00:00', 'address': 'beijing'}
    #     r = requests.post(self.base_url, data=dataline)
    #     print(r.status_code)
    #     result = r.json()
    #     print(r.json())
    #     self.assertEqual(result['status'], 200)
    #     self.assertIn(result['message'], "add event success")

class SearchEventTest(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://127.0.0.1:8000/guest/search_event/"

    def test_search_event_null(self):
        '''
        所有参数为空:
        '''
        r = requests.get(self.base_url)
        print(r.status_code)
        result = r.json()
        print(r.json())
        self.assertEqual(result['status'], 201)
        self.assertEqual(result['message'], "parameter error")

    def test_search_event_eid_error(self):
        '''
        eid 不存在:
        '''
        dataline = {'eid': 99}
        r = requests.get(self.base_url, params=dataline)
        print(r.status_code)
        result = r.json()
        print(r.json())
        self.assertEqual(result['status'], 205)
        self.assertEqual(result['message'], "no this event")

    def test_search_event_eid_success(self):
        '''
        eid 存在:
        '''
        dataline = {'eid': 2}
        r = requests.get(self.base_url, params=dataline)
        print(r.status_code)
        result = r.json()
        print(r.json())
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "search event success")

    def test_search_event_name_error(self):
        '''
        name 不存在:
        '''
        dataline = {'name': 'mama'}
        r = requests.get(self.base_url, params=dataline)
        print(r.status_code)
        result = r.json()
        print(r.json())
        self.assertEqual(result['status'], 206)
        self.assertEqual(result['message'], "no this name")

    def test_search_event_name_success(self):
        '''
        name 存在:
        '''
        dataline = {'name': '波比生日派对'}
        r = requests.get(self.base_url, params=dataline)
        print(r.status_code)
        result = r.json()
        print(r.json())
        self.assertEqual(result['status'], 200)
        self.assertEqual(result['message'], "search name success")


if __name__ == '__main__':
    unittest.main()
