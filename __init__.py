from mycroft import MycroftSkill, intent_file_handler


class PlayRadio(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('radio.play.intent')
    def handle_radio_play(self, message):
        self.speak_dialog('radio.play')


def create_skill():
    return PlayRadio()

