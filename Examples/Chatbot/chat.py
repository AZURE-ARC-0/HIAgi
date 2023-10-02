from customagents.GenerateAgent import GenerateAgent
from customagents.ReflectAgent import ReflectAgent
from customagents.TheoryAgent import TheoryAgent
from customagents.ThoughtAgent import ThoughtAgent
from agentforge.utils.guiutils.listenforui import ListenForUI

gen = GenerateAgent()
ref = ReflectAgent()
theo = TheoryAgent()
thou = ThoughtAgent()
class Chatbot:

    def __init__(self):
        inbound = ListenForUI().BotApi()
        pass
    def run(self):
        pass

if __name__ == '__main__':
    api = listenforui.BotApi(callback=Chatbot().run)