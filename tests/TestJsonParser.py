import json
import unittest

from darcycui_mcp.https.response.weather.WeatherInfo import WeatherResponse


class TestJsonParser(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_parse_weather_json(self):
        mock_result = """

        {
            "city": "苏州",
            "realtime": {
                "temperature": "4",
                "humidity": "82",
                "info": "阴",
                "wid": "02",
                "direct": "西北风",
                "power": "3级",
                "aqi": "80"
            },
            "future": [
                {
                    "date": "2019-02-22",
                    "temperature": "1/7℃",
                    "weather": "小雨转多云",
                    "wid": {
                        "day": "07",
                        "night": "01"
                    },
                    "direct": "北风转西北风"
                }
            ]
        }
        """
        print(f"mock_result:{mock_result}")
        result_data = json.loads(mock_result)
        print(f"result_data:{result_data}")
        weather = WeatherResponse.success(result_data)
        tomorrow = (weather.result.future[0]).model_dump_json()
        print(f"tomorrow:{tomorrow}")
        expect_weather = """{"date":"2019-02-22","temperature":"1/7℃","weather":"小雨转多云","wid":{"day":"07","night":"01"},"direct":"北风转西北风"}"""
        self.assertEqual(expect_weather, tomorrow, "解析json失败")  # add assertion here


if __name__ == '__main__':
    unittest.main()
