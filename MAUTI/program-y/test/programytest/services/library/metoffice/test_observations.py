import unittest
from programy.services.library.metoffice.metoffice import MetOfficeObservation


class MetOfficeObservationTests(unittest.TestCase):

    def test_parse_json(self):
        observation = MetOfficeObservation()
        self.assertIsNotNone(observation)

        json_data = { "SiteRep": {
                        "DV": {
                            "Location": {
                                "Period": [
                                    {
                                        "Rep": [
                                            {
                                                "$": "660",
                                                "D": "W",
                                                "Dp": "3.2",
                                                "H": "57.3",
                                                "P": "1021",
                                                "Pt": "R",
                                                "S": "11",
                                                "T": "11.2",
                                                "V": "35000",
                                                "W": "3"
                                            },
                                            {
                                                "$": "720",
                                                "D": "WSW",
                                                "Dp": "2.2",
                                                "H": "51.6",
                                                "P": "1021",
                                                "Pt": "R",
                                                "S": "9",
                                                "T": "11.7",
                                                "V": "35000",
                                                "W": "1"
                                            },
                                            {
                                                "$": "780",
                                                "D": "WSW",
                                                "Dp": "2.6",
                                                "H": "50.7",
                                                "P": "1021",
                                                "Pt": "F",
                                                "S": "10",
                                                "T": "12.4",
                                                "V": "35000",
                                                "W": "1"
                                            },
                                            {
                                                "$": "840",
                                                "D": "W",
                                                "Dp": "2.9",
                                                "H": "49.4",
                                                "P": "1020",
                                                "Pt": "F",
                                                "S": "14",
                                                "T": "13.1",
                                                "V": "35000",
                                                "W": "1"
                                            },
                                            {
                                                "$": "900",
                                                "D": "WSW",
                                                "Dp": "3.7",
                                                "H": "50.3",
                                                "P": "1020",
                                                "Pt": "F",
                                                "S": "9",
                                                "T": "13.7",
                                                "V": "35000",
                                                "W": "3"
                                            },
                                            {
                                                "$": "960",
                                                "D": "W",
                                                "Dp": "3.8",
                                                "H": "51.0",
                                                "P": "1020",
                                                "Pt": "F",
                                                "S": "13",
                                                "T": "13.6",
                                                "V": "35000",
                                                "W": "1"
                                            },
                                            {
                                                "$": "1020",
                                                "D": "WSW",
                                                "Dp": "3.4",
                                                "H": "52.6",
                                                "P": "1021",
                                                "Pt": "R",
                                                "S": "11",
                                                "T": "12.7",
                                                "V": "35000",
                                                "W": "1"
                                            },
                                            {
                                                "$": "1080",
                                                "D": "WSW",
                                                "Dp": "3.3",
                                                "H": "56.2",
                                                "P": "1021",
                                                "Pt": "R",
                                                "S": "9",
                                                "T": "11.6",
                                                "V": "35000",
                                                "W": "1"
                                            },
                                            {
                                                "$": "1140",
                                                "D": "WSW",
                                                "Dp": "3.1",
                                                "H": "63.9",
                                                "P": "1022",
                                                "Pt": "R",
                                                "S": "3",
                                                "T": "9.5",
                                                "V": "30000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "1200",
                                                "D": "SSW",
                                                "Dp": "3.2",
                                                "H": "70.8",
                                                "P": "1022",
                                                "Pt": "R",
                                                "S": "6",
                                                "T": "8.1",
                                                "V": "29000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "1260",
                                                "D": "SSW",
                                                "Dp": "2.8",
                                                "H": "73.7",
                                                "P": "1022",
                                                "Pt": "R",
                                                "S": "6",
                                                "T": "7.1",
                                                "V": "29000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "1320",
                                                "D": "SSW",
                                                "Dp": "2.2",
                                                "H": "69.6",
                                                "P": "1022",
                                                "Pt": "R",
                                                "S": "8",
                                                "T": "7.3",
                                                "V": "30000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "1380",
                                                "D": "SSW",
                                                "Dp": "2.4",
                                                "H": "71.7",
                                                "P": "1022",
                                                "Pt": "F",
                                                "S": "10",
                                                "T": "7.1",
                                                "V": "29000",
                                                "W": "0"
                                            }
                                        ],
                                        "type": "Day",
                                        "value": "2017-04-02Z"
                                    },
                                    {
                                        "Rep": [
                                            {
                                                "$": "0",
                                                "D": "SSW",
                                                "Dp": "2.5",
                                                "H": "73.2",
                                                "P": "1021",
                                                "Pt": "F",
                                                "S": "9",
                                                "T": "6.9",
                                                "V": "29000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "60",
                                                "D": "SW",
                                                "Dp": "2.4",
                                                "H": "74.7",
                                                "P": "1021",
                                                "Pt": "F",
                                                "S": "7",
                                                "T": "6.5",
                                                "V": "30000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "120",
                                                "D": "SW",
                                                "Dp": "3.0",
                                                "H": "76.0",
                                                "P": "1020",
                                                "Pt": "F",
                                                "S": "8",
                                                "T": "6.9",
                                                "V": "30000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "180",
                                                "D": "WSW",
                                                "Dp": "1.9",
                                                "H": "71.1",
                                                "P": "1020",
                                                "Pt": "F",
                                                "S": "6",
                                                "T": "6.7",
                                                "V": "30000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "240",
                                                "D": "WSW",
                                                "Dp": "2.0",
                                                "H": "79.5",
                                                "P": "1020",
                                                "Pt": "F",
                                                "S": "5",
                                                "T": "5.2",
                                                "V": "30000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "300",
                                                "D": "SW",
                                                "Dp": "2.1",
                                                "G": "19",
                                                "H": "73.2",
                                                "P": "1019",
                                                "Pt": "F",
                                                "S": "8",
                                                "T": "6.5",
                                                "V": "30000",
                                                "W": "0"
                                            },
                                            {
                                                "$": "360",
                                                "D": "WNW",
                                                "Dp": "1.8",
                                                "H": "79.5",
                                                "P": "1019",
                                                "Pt": "F",
                                                "S": "2",
                                                "T": "5.0",
                                                "V": "30000",
                                                "W": "1"
                                            },
                                            {
                                                "$": "420",
                                                "D": "NNW",
                                                "Dp": "2.5",
                                                "H": "80.7",
                                                "P": "1019",
                                                "Pt": "F",
                                                "S": "1",
                                                "T": "5.5",
                                                "V": "30000",
                                                "W": "1"
                                            },
                                            {
                                                "$": "480",
                                                "D": "SSW",
                                                "Dp": "3.0",
                                                "H": "65.2",
                                                "P": "1018",
                                                "Pt": "F",
                                                "S": "7",
                                                "T": "9.1",
                                                "V": "35000",
                                                "W": "1"
                                            },
                                            {
                                                "$": "540",
                                                "D": "SW",
                                                "Dp": "3.6",
                                                "H": "62.3",
                                                "P": "1018",
                                                "Pt": "F",
                                                "S": "15",
                                                "T": "10.4",
                                                "V": "35000",
                                                "W": "7"
                                            },
                                            {
                                                "$": "600",
                                                "D": "SW",
                                                "Dp": "3.9",
                                                "H": "61.6",
                                                "P": "1018",
                                                "Pt": "F",
                                                "S": "15",
                                                "T": "10.9",
                                                "V": "35000",
                                                "W": "7"
                                            },
                                            {
                                                "$": "660",
                                                "D": "SW",
                                                "Dp": "4.2",
                                                "H": "57.3",
                                                "P": "1017",
                                                "Pt": "F",
                                                "S": "10",
                                                "T": "12.3",
                                                "V": "35000",
                                                "W": "3"
                                            }
                                        ],
                                        "type": "Day",
                                        "value": "2017-04-03Z"
                                    }
                                ],
                                "continent": "EUROPE",
                                "country": "SCOTLAND",
                                "elevation": "57.0",
                                "i": "3166",
                                "lat": "55.928",
                                "lon": "-3.343",
                                "name": "EDINBURGH/GOGARBANK"
                            },
                            "dataDate": "2017-04-03T11:00:00Z",
                            "type": "Obs"
                        },
                        "Wx": {
                            "Param": [
                                {
                                    "$": "Wind Gust",
                                    "name": "G",
                                    "units": "mph"
                                },
                                {
                                    "$": "Temperature",
                                    "name": "T",
                                    "units": "C"
                                },
                                {
                                    "$": "Visibility",
                                    "name": "V",
                                    "units": "m"
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
                                    "$": "Weather Type",
                                    "name": "W",
                                    "units": ""
                                },
                                {
                                    "$": "Pressure",
                                    "name": "P",
                                    "units": "hpa"
                                },
                                {
                                    "$": "Pressure Tendency",
                                    "name": "Pt",
                                    "units": "Pa/s"
                                },
                                {
                                    "$": "Dew Point",
                                    "name": "Dp",
                                    "units": "C"
                                },
                                {
                                    "$": "Screen Relative Humidity",
                                    "name": "H",
                                    "units": "%"
                                }
                            ]
                        }
                    }
                }

        observation.parse_json(json_data)

        self.assertIsNotNone(observation.get_observations)
        self.assertEquals(25, len(observation.get_observations()))
        self.assertIsNotNone(observation.get_latest_observation())
        self.assertEquals(3, len(observation.get_last_n_observations(3)))
