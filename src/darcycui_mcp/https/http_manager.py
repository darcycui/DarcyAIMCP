import httpx

from darcycui_mcp.https.response.weather.WeatherInfo import WeatherResponse


def get_app_key_weather() -> str:
    """
    获取聚合接口的 app_key
    :return: app_key
    """
    # app_key = os.environ.get("JUHE_APPKEY_WEATHER")
    # if not app_key:
    #     raise ValueError("JUHE_APPKEY_WEATHER 未设置")
    app_key = "b91d6815998fdcd0d3bd54a09aff41c6"
    return app_key


def forecast(city: str) -> str:
    """
    通过聚合接口查询天气信息
    :param city: 城市名称
    :return: 明天的天气信息
    """
    try:
        params = {'key': get_app_key_weather(), 'city': city}
        r = httpx.get('https://apis.juhe.cn/simpleWeather/query', params=params)
        # dict (字典)
        result: dict = r.json()
        print(f"api result-->{result}")
        # result_data = json.loads(result)
        weather = result
        weather = WeatherResponse.success(result['result'])
        if weather.error_code != 0:
            return "查询失败，返回本地默认值: 明天的天气晴转多云，最低气温 1度。"
        # 转换为 JSON 字符串
        return weather.result.future[0].model_dump_json()
    except Exception as e:
        print(f"查询异常：{e}")
        # 打印堆栈
        import traceback
        traceback.print_exc()
        return "查询失败，返回本地默认值: 明天的天气晴转多云，最低气温 2度。"

if __name__ == '__main__':
    print(forecast("上海"))