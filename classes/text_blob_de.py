from textblob_de import TextBlobDE


class TextBlobClass:

        @staticmethod
        def get_sentiment(comment):
            test = TextBlobDE(comment)
            polarity = test.sentiment.polarity
            print(test.sentiment.polarity)

            if polarity > 0.5:
                sentiment = 'positiv '
            elif polarity < -0.3:
                sentiment = 'negativ '
            else:
                sentiment = 'neutral '
            return sentiment


