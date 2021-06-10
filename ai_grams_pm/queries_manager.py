import requests
import pandas as pd

def get_forecasts(token, market, zone, starting_date=None, ending_date=None):

	"""
	A method to retrieve forecasts on different market's gates for a specific day.

	Args:
		token (string): private token to be used in order to retreive forecasts.
		market (string): market's gate of interest (e.g. MI3).
		zone (string): macrozone of interest (e.g. NORTH/SOUTH).
		starting_date (string, optional): starting date (included into the output) for forecasts (%YYYY%MM%dd). If not specified the forecasts for the day ahead will be provided.
		ending_date (string, optional): ending date (excluded from the output) for forecasts (%YYYY%MM%dd). If not specified the forecasts for the day ahead will be provided.

	Examples:
		get_forecasts('token','MI3', 'SOUTH', '20210529', '20210531') \n
		get_forecasts('token','MI3', 'NORTH')

	"""

	if (starting_date != None) and (ending_date != None):
		url_string = str('https://aigrams.herokuapp.com/api/v1/resources/forecasts?token=' + str(token) + '&starting_date=' + str(starting_date) + '&ending_date=' + str(ending_date) + '&market=' + str(market) + '&zone=' + str(zone))
	else:
		url_string = str('https://aigrams.herokuapp.com/api/v1/resources/forecasts?token=' + str(token) + '&market=' + str(market) + '&zone=' + str(zone))

	forecasts_request = requests.get(url_string)

	try:
		df = pd.read_json(forecasts_request.text)
		return df
	except:
		return forecasts_request.text