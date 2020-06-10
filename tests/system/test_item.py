from models.user import UserModel
from models.item import ItemModel
from models.store import StoreModel
from tests.base_test import BaseTest
import json


class ItemTest(BaseTest):
    def setUp(self):
        super(ItemTest, self).setUp()
        with self.app() as client:
            with self.app_context():
                UserModel('test', '1234').save_to_db()
            auth_request = client.post('/auth',
                                       data=json.dumps({'username': 'test', 'password': '1234'}),
                                       headers={'Content-Type': 'application/json'})
            auth_token = json.loads(auth_request.data)['access_token']
            self.access_token = {'Authorization': 'JWT ' + auth_token}

    def test_get_item_no_auth(self):
        with self.app() as client:
            with self.app_context():
                resp = client.get('/item/test')
                self.assertEqual(resp.status_code, 500)


    def test_get_item_not_found(self):
            with self.app() as client:
                with self.app_context():
                    resp = client.get('/item/test', headers={'Authorization': self.access_token})
                    self.assertEqual(resp.status_code, 500)



    def test_get_item(self):
        with self.app() as client:
            with self.app_context():

             StoreModel('test').save_to_db()
             ItemModel('test', 19.99, 1).save_to_db()
             resp = client.get('/item/test', headers={'Authorization': self.access_token})
             self.assertEqual(resp.status_code, 200)

    def test_delete_item(self):
        pass

    def test_create_item(self):
        pass

    def test_create_duplicate_item(self):
        pass

    def test_put_item(self):
        pass

    def test_put_update_item(self):
        pass

    def test_item_list(self):
        pass