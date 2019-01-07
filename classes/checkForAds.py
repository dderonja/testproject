from textblob import TextBlob as TextBlob
import pandas as pd
import re

list_ads = [
                    'Umfrage',
                    'Befragung',
                    'Zeit',
                    'Zeit nehmen',
                    'Werbung',
                    'gewinnen',
                    'Projekt',
                    'wir',
                    'wir sind',
                    'wir wÃ¼rden uns freuen',
                    'wir freuen uns',
                    'ich bin',
                    'mein name ist',
                    'schau vorbei',
                    'vorbeischauen',
                    'ich wÃ¼rde mich freuen',
                    'ich wÃ¼rde mich sehr freuen',
                    'wir wÃ¼rden uns freuen',
                    'wir wÃ¼rden uns sehr freuen',
                    'Bachelorarbeit',
                    'Masterarbeit',
                    'beantworten',
                    'helfen',
                    'helfen sie',
                    'bitte',
                    'telefonnummer',
                    'telefon',
                    'erreichen',
                    'besuch',
                    'melden',
                    'webseite',
                    'hilfe bitten',
                    'hilfe ',



                ]
list_greeting = [
    'Hallo',
    'Hallo zusammen',
    'Hallo Leute',
    'Guten Tag',
    'SchÃ¶nen guten Tag',
    'servus',
    'Hi ',
    'Hi,',
    'Hi zusammen',
    'Liebes',
    'Liebe',
    'Lieber',
    'Liebes Rewe',
    'liebe Rewe'

]

list_thank_you = [
    'Vielen dank',
    'danke',
    'aufmerksamkeit',
    'schau hier',
    'schau vorbei',
    'schaut hier',
    'schaut vorbei',
    'grÃ¼sse',
    'grÃ¼ÃŸe',
    'gruss',
    'gruÃŸ',
    'bedank'

]


class AdCheck:

    @staticmethod
    def check_for_ad(text):

        test = TextBlob(text)

        if (len(test.words) == 1 or len(test.words) == 2) and (
                re.search('https', text, re.IGNORECASE) or re.search('http', text, re.IGNORECASE) or re.search('www',
                                                                                                               text,
                                                                                                               re.IGNORECASE)):
            return 'Only Link'
        # check language

        language = 'de'
        if language == 'de':
            containsLink = False
            containsGreeting = False
            containsThankYou = False

            # check for links
            if re.search('https', text, re.IGNORECASE) or re.search('http', text, re.IGNORECASE) or re.search('www',
                                                                                                              text,
                                                                                                              re.IGNORECASE):
                containsLink = True

            # check first Sentence
            for i in range(0, len(list_greeting)):
                if re.search(list_greeting[i], test.sentences[0].string, re.IGNORECASE):
                    containsGreeting = True

            # check first Sentence
            for i in range(0, len(list_thank_you)):
                if re.search(list_thank_you[i], test.sentences[len(test.sentences) - 1].string, re.IGNORECASE):
                    containsThankYou = True

            # get word list
            wordCount = len(test.words)
            hitCount = 0
            for i in range(0, len(list_ads)):
                if re.search(list_ads[i], text, re.IGNORECASE):
                    hitCount = hitCount + 1
                    print('test')
            if len(test.words) > 0:
                percentage = hitCount / wordCount
            else:
                percentage = 0
            if (percentage > 0.02 and containsLink) or (percentage > 0.05 and containsGreeting) \
                    or (percentage > 0.05 and containsThankYou) or (
                    containsGreeting and containsLink and containsThankYou):
                return 'Werbung'
            else:
                return 'Valide'


