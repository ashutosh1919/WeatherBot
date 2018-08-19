from rasa_core.channels import HttpInputChannel
from rasa_core.agent import Agent
from rasa_core.interpreter import RasaNLUInterpreter
from rasa_slack_connector import SlackInput

nlu_interpreter = RasaNLUInterpreter('./models/nlu/default/weathernlu')
agent = Agent.load('./models/dialogue',interpreter=nlu_interpreter)

input_channel = SlackInput('xoxp-343254100417-345792302070-419286672101-142d02301db377fcdad8ae574adb1729','xoxb-343254100417-418425218496-K2sJO2SRtWSB5NpjhLex2tSI','5srxGlhhehymv6sQJ87MKfgv',True)

agent.handle_channel(HttpInputChannel(5004,'/',input_channel))