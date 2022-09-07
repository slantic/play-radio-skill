from mycroft.skills.common_play_skill import CommonPlaySkill, CPSMatchLevel

from mycroft.util.parse import match_one


track_dict = {
    'npo radio 1': 'http://icecast.omroep.nl/radio1-bb-mp3',
    'npo radio 2': 'http://icecast.omroep.nl/radio2-bb-mp3'
}

class PlayRadio(CommonPlaySkill):
    def CPS_match_query_phrase(self, phrase):
        """ This method responds wether the skill can play the input phrase.
            The method is invoked by the PlayBackControlSkill.
            Returns: tuple (matched phrase(str),
                            match level(CPSMatchLevel),
                            optional data(dict))
                     or None if no match was found.
        """
        # Get match and confidence
        match, confidence = match_one(phrase, track_dict)
        # If the confidence is high enough return a match
        if confidence > 0.5:
            return (match, CPSMatchLevel.EXACT, {"track": match})
        # Otherwise return None
        else:
            return None

    def CPS_start(self, phrase, data):
        """ Starts playback.
            Called by the playback control skill to start playback if the
            skill is selected (has the best match level)
        """
        url = data['track']
        self.audioservice.play(url)

def create_skill():
    return PlayRadio()

