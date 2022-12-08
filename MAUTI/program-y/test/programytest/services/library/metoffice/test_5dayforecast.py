import unittest
from programy.services.library.metoffice.metoffice import MetOffice5DayForecast


class MetOffice5DayForecastTests(unittest.TestCase):

    def test_parse_json(self):
        forecast = MetOffice5DayForecast()
        self.assertIsNotNone(forecast)

        json_data = {"SiteRep": {
                        "DV": {
                          "Location": {
                            "Period": [
                              {
                                "Rep": [
                                  {
                                    "$": "Day",
                                    "D": "S",
                                    "Dm": "15",
                                    "FDm": "13",
                                    "Gn": "16",
                                    "Hn": "54",
                                    "PPd": "0",
                                    "S": "9",
                                    "U": "4",
                                    "V": "VG",
                                    "W": "1"
                                  },
                                  {
                                    "$": "Night",
                                    "D": "SSW",
                                    "FNm": "7",
                                    "Gm": "16",
                                    "Hm": "86",
                                    "Nm": "9",
                                    "PPn": "57",
                                    "S": "7",
                                    "V": "GO",
                                    "W": "7"
                                  }
                                ],
                                "type": "Day",
                                "value": "2017-04-03Z"
                              },
                              {
                                "Rep": [
                                  {
                                    "$": "Day",
                                    "D": "N",
                                    "Dm": "13",
                                    "FDm": "11",
                                    "Gn": "11",
                                    "Hn": "82",
                                    "PPd": "49",
                                    "S": "7",
                                    "U": "2",
                                    "V": "GO",
                                    "W": "8"
                                  },
                                  {
                                    "$": "Night",
                                    "D": "NNW",
                                    "FNm": "4",
                                    "Gm": "11",
                                    "Hm": "81",
                                    "Nm": "5",
                                    "PPn": "9",
                                    "S": "4",
                                    "V": "VG",
                                    "W": "2"
                                  }
                                ],
                                "type": "Day",
                                "value": "2017-04-04Z"
                              },
                              {
                                "Rep": [
                                  {
                                    "$": "Day",
                                    "D": "NW",
                                    "Dm": "12",
                                    "FDm": "10",
                                    "Gn": "20",
                                    "Hn": "59",
                                    "PPd": "9",
                                    "S": "11",
                                    "U": "3",
                                    "V": "VG",
                                    "W": "8"
                                  },
                                  {
                                    "$": "Night",
                                    "D": "NNW",
                                    "FNm": "6",
                                    "Gm": "11",
                                    "Hm": "79",
                                    "Nm": "6",
                                    "PPn": "8",
                                    "S": "7",
                                    "V": "VG",
                                    "W": "7"
                                  }
                                ],
                                "type": "Day",
                                "value": "2017-04-05Z"
                              },
                              {
                                "Rep": [
                                  {
                                    "$": "Day",
                                    "D": "WNW",
                                    "Dm": "14",
                                    "FDm": "13",
                                    "Gn": "11",
                                    "Hn": "61",
                                    "PPd": "8",
                                    "S": "4",
                                    "U": "4",
                                    "V": "VG",
                                    "W": "7"
                                  },
                                  {
                                    "$": "Night",
                                    "D": "NW",
                                    "FNm": "7",
                                    "Gm": "9",
                                    "Hm": "81",
                                    "Nm": "7",
                                    "PPn": "10",
                                    "S": "4",
                                    "V": "VG",
                                    "W": "8"
                                  }
                                ],
                                "type": "Day",
                                "value": "2017-04-06Z"
                              },
                              {
                                "Rep": [
                                  {
                                    "$": "Day",
                                    "D": "WNW",
                                    "Dm": "13",
                                    "FDm": "12",
                                    "Gn": "11",
                                    "Hn": "66",
                                    "PPd": "11",
                                    "S": "4",
                                    "U": "3",
                                    "V": "VG",
                                    "W": "8"
                                  },
                                  {
                                    "$": "Night",
                                    "D": "NW",
                                    "FNm": "8",
                                    "Gm": "7",
                                    "Hm": "76",
                                    "Nm": "8",
                                    "PPn": "8",
                                    "S": "4",
                                    "V": "VG",
                                    "W": "7"
                                  }
                                ],
                                "type": "Day",
                                "value": "2017-04-07Z"
                              }
                            ],
                            "continent": "EUROPE",
                            "country": "ENGLAND",
                            "elevation": "4.0",
                            "i": "351747",
                            "lat": "51.4007",
                            "lon": "-0.3337",
                            "name": "HAMPTON COURT PALACE"
                          },
                          "dataDate": "2017-04-03T09:00:00Z",
                          "type": "Forecast"
                        },
                        "Wx": {
                          "Param": [
                            {
                              "$": "Feels Like Day Maximum Temperature",
                              "name": "FDm",
                              "units": "C"
                            },
                            {
                              "$": "Feels Like Night Minimum Temperature",
                              "name": "FNm",
                              "units": "C"
                            },
                            {
                              "$": "Day Maximum Temperature",
                              "name": "Dm",
                              "units": "C"
                            },
                            {
                              "$": "Night Minimum Temperature",
                              "name": "Nm",
                              "units": "C"
                            },
                            {
                              "$": "Wind Gust Noon",
                              "name": "Gn",
                              "units": "mph"
                            },
                            {
                              "$": "Wind Gust Midnight",
                              "name": "Gm",
                              "units": "mph"
                            },
                            {
                              "$": "Screen Relative Humidity Noon",
                              "name": "Hn",
                              "units": "%"
                            },
                            {
                              "$": "Screen Relative Humidity Midnight",
                              "name": "Hm",
                              "units": "%"
                            },
                            {
                              "$": "Visibility",
                              "name": "V",
                              "units": ""
                            },
                            {
                              "$": "Wind Direction",
                              "name": "D",
                              "units": "compass"
                            },
                            {
                              "$": "Wind Speed",
                              "name": "S",
                              "units": "mph"
                            },
                            {
                              "$": "Max UV Index",
                              "name": "U",
                              "units": ""
                            },
                            {
                              "$": "Weather Type",
                              "name": "W",
                              "units": ""
                            },
                            {
                              "$": "Precipitation Probability Day",
                              "name": "PPd",
                              "units": "%"
                            },
                            {
                              "$": "Precipitation Probability Night",
                              "name": "PPn",
                              "units": "%"
                            }
                          ]
                        }
                      }
                    }


        forecast.parse_json(json_data)

    def test_parse_json_siterep_missing(self):
        forecast = MetOffice5DayForecast()
        self.assertIsNotNone(forecast)

        json_data = {
                    }

        with self.assertRaises(ValueError):
            forecast.parse_json(json_data)
