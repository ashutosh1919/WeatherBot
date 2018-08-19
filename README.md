# WeatherBot
This is the bot which will give weather details of any place in the world.

I have developed this bot step by step. 
I have used Apixu portal for getting information about weather.
I have used ngrok as medium between computer source and slack.
Bot is responding quickly to the direct messages.
I have used rasa_core and rasa_nlu to train the models.
I have attached the code of online training (online_training.py) as well as offline training (nlu_model.py).

Code is developed in this sequence : config_spacy.json --> data --> weather_domain.yml --> nlu_model.py --> actions.py --> train_init.py                                         --> train_online.py --> dialog_management_model.py --> rasa_slack_connector.py --> run_app.py


![Output Image of Bot Running on Slack](https://github.com/ashutosh1919/WeatherBot/blob/master/slack_output.PNG)
