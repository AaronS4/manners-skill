from mycroft import MycroftSkill, intent_file_handler


class Manners(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('manners.intent')
    def handle_manners(self, message):
        self.speak_dialog('manners')


def create_skill():
    return Manners()

