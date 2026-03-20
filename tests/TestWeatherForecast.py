import unittest

from darcycui_mcp.https.http_manager import forecast


class TestWeatherForecast(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_forecast_shanghai(self):
        weather = forecast("上海")
        print(f"weather:{weather}")
        expect_weather = """{"date":"2026-03-20","temperature":"7/15℃","weather":"阴","wid":{"day":"02","night":"02"},"direct":"东风"}"""
        self.assertEqual(expect_weather, weather, "获取天气信息失败")  # add assertion here


if __name__ == '__main__':
    unittest.main()
