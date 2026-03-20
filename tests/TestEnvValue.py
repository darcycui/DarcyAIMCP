import unittest

from darcycui_mcp.https.http_manager import get_app_key_weather


class TestEnvValue(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_env_value_app_key_weather(self):
        app_key = get_app_key_weather()
        print(f"app_key={app_key}")
        self.assertIsNotNone(app_key, "获取聚合接口的 app_key 失败")  # add assertion here


if __name__ == '__main__':
    unittest.main()
