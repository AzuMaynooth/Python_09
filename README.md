# Python_09
In this exercise, you will optimize the rain prediction program from the previous exercise. You will create a class `WeatherForecast` that will handle reading and writing to a file, as well as making requests to the API. An object of the `WeatherForecast` class must correctly implement the following four methods:

- `__setitem__`
- `__getitem__`
- `__iter__`
- `items`

Instructions:

1. Define a `WeatherForecast` class. This class will handle the operations related to weather forecasting.

2. The `__setitem__` method should allow you to set a weather forecast for a particular date.

3. The `__getitem__` method should allow you to get the weather forecast for a particular date.

4. The `__iter__` method should allow you to iterate over all the dates for which the weather forecast is known.

5. The `items` method should return a generator of tuples in the format `(date, weather)` for already saved results.

6. After implementing the `WeatherForecast` class, update your code to use this class. The `WeatherForecast` object should be able to handle the following queries:

  - `weather_forecast[date]` will give the weather forecast for the given date.
  - `weather_forecast.items()` will return a generator of tuples in the format `(date, weather)` for already saved results.
  - `weather_forecast` is an iterator returning all the dates for which the weather is known.

Hints:

- Use Python's special (dunder) methods to customize the behavior of your class.
- The `__setitem__` method should be implemented to allow setting an item's value with square bracket notation (`obj[key] = value`).
- The `__getitem__` method should be implemented to allow accessing an item's value with square bracket notation (`value = obj[key]`).
- The `__iter__` method should be implemented to allow iterating over the object.
- The `items` method should return a generator of tuples. You can create a generator using a function with the `yield` keyword.
