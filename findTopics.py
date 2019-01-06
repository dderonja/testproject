import pandas as pd
import re
import numpy as np

list_contractnews = [['deal ', 10],
                     ['new coach', 10],
                     ['new head coach', 10],
                     ['retire', 5],
                     ['sign', 8],
                     ['transfer', 8],
                     ['one-year', 7],
                     ['two year', 7],
                     ['three-year', 7],
                     ['four-year', 7],
                     ['contract', 4],
                     ['join', 3],
                     ['loan', 6],
                     ['quit', 2],
                     ['fee', 4],
                     ['part company', 10],
                     ['part ways', 5],
                     ['leave club', 10]]

list_injurynews = [['injury', 10],
                   ['suffer', 6],
                   ['sustain', 3],
                   ['calf', 5],
                   ['muscle', 5],
                   ['ankle', 5],
                   ['illness', 5],
                   ['back in training', 3],
                   ['recover', 1],
                   ['comeback', 1],
                   ['ruled out', 4],
                   ['sidelined', 3],
                   ['miss', 1],
                   ['fitness', 4],
                   ['damage', 3],
                   ['bad news', 3],
                   ['absence', 3],
                   ['absent', 2],
                   ['return', 5],
                   ['one week', 2],
                   ['two weeks', 2],
                   ['three weeks', 2],
                   ['four weeks', 2],
                   ['five weeks', 2],
                   ['six weeks', 2],
                   ['one month', 1],
                   ['two months', 1],
                   ['three months', 1],
                   ['four months', 1],
                   ['five months', 1],
                   ['six months', 1],
                   ['seven months', 1],
                   ['train again', 6]]

list_statements = [['interview', 8],
                   ['exclusive', 7],
                   ['quote', 5],
                   ['"', 2],
                   ['bild', 3],
                   ['süddeutsche zeitung', 3],
                   ['westdeutsche zeitung', 3],
                   ['kicker', 3],
                   ['sportbuzzer', 3],
                   ['believe', 2],
                   ['say', 2],
                   ['tell', 2],
                   ['explain', 2],
                   ['enthuse', 2],
                   ['bundesliga.com', 2],
                   ['caught up', 1],
                   ['talks about', 1]]

list_features = [['stars of tomorrow', 30],
                 ['season so far', 15],
                 ['fact', 5],
                 ['we take a look back', 2],
                 ['closer look', 2],
                 ['talent', 1],
                 ['prospect', 1],
                 ['journey', 1],
                 ['path', 1],
                 ['success', 1]]

list_preview = [['will play', 10],
                ['will be without', 10],
                ['will miss', 3],
                ['preview', 20],
                ['match', 1],
                ['teaser', 8],
                ['probable line-ups', 15],
                ['possible line-ups', 15],
                ['line-ups and stats', 7],
                ['predict', 7],
                ['upcoming', 7],]

list_review = [['goals:', 40],
               ['match centre', 15],
               ['game-winnning', 10],
               ['victory', 7],
               ['loss', 7],
               ['secured', 4],
               ['decid', 1],
               ['minutes to go', 8],
               ['defeat', 3],
               ['late win', 2],
               ['draw', 2],
               ['match winner', 3]]

list_votings = [['blmvp:', 35],
                ['of the season', 5],
                ['of the month', 5],
                ['of the week', 5],
                ['of the year', 5],
                ['of the hinrunde', 5],
                ['candidate', 3],
                ['vote', 2],
                ['winner', 1],
                ['nominate', 5]]

df = pd.read_csv('csvs/dim_web_articles_with_text.csv', delimiter=';', encoding='iso-8859-1')

counter_contentgroup = 0
counter_headline = 0
counter_score = 0

for idx, row in df.iterrows():
    if pd.isnull(df.loc[idx, 'topic']):
        # live
        if df.loc[idx, 'content_group'] == 'Live' \
                or re.search('live', df.loc[idx, 'article'], re.IGNORECASE):
            df.loc[idx, 'topic'] = 'Live'
            counter_contentgroup = counter_contentgroup +1
            continue
        # fantasy bundesliga
        if df.loc[idx, 'content_group'] == 'Games' \
                or re.search('fantasy', df.loc[idx, 'article'], re.IGNORECASE):
            df.loc[idx, 'topic'] = 'Fantasy Bundesliga'
            counter_contentgroup = counter_contentgroup + 1
            continue
        # dfl & agenda
        if df.loc[idx, 'content_group'] == 'DFL & Agenda' \
                or re.search('dfl', df.loc[idx, 'article'], re.IGNORECASE) \
                or df.loc[idx, 'content_group'] == 'DFL Services':
            df.loc[idx, 'topic'] = 'DFL & Agenda'
            counter_contentgroup = counter_contentgroup + 1
            continue
        # bundesliga daily
        if (re.search('bundesliga daily', df.loc[idx, 'article'], re.IGNORECASE)):
            df.loc[idx, 'topic'] = 'Bundesliga Daily'
            counter_headline = counter_headline + 1
            continue

        # match preview
        if (re.search('previe', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('teaser', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('five things to look out for', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('possible line-ups', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('probable line-ups', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('match preview', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('match-preview', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('line-ups', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('line up', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('fifa prediction', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('fifa predicts', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('build-up', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('build up', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('FIFA 17 Predicts:', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('FIFA 16 Predicts:', df.loc[idx, 'article'], re.IGNORECASE)):
            df.loc[idx, 'topic'] = 'Match Preview'
            counter_headline = counter_headline + 1
            continue

        # match review
        if (re.search('top five talking points', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('statistical breakdown', df.loc[idx, 'article'])
                or re.search('report', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('reaction', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('post-match', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('post match', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('match-report', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('match report', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('round-up', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('as it happened', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('moment of the matchday', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('stat-attack', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('statistical review', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('review', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('statistical gems', df.loc[idx, 'article'], re.IGNORECASE)):
            df.loc[idx, 'topic'] = 'Match Review'
            counter_headline = counter_headline + 1
            continue

        # votings
        if (re.search('award', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('vote for', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('of the season', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('of the month', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('of the week', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('of the year', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('of the hinrunde', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('blmvp', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('ballon', df.loc[idx, 'article'], re.IGNORECASE)):
            df.loc[idx, 'topic'] = 'Votings'
            counter_headline = counter_headline + 1
            continue

        # statements
        if (re.search('"', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search(": '", df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('interview', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('exclusive', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('exclusive', df.loc[idx, 'url'], re.IGNORECASE)
                or re.search('interview', df.loc[idx, 'url'], re.IGNORECASE)
                or re.search('&#x93;', df.loc[idx, 'article']) or re.search('&#x94;', df.loc[idx, 'article'])):
            df.loc[idx, 'topic'] = 'Statements'
            counter_headline = counter_headline + 1
            continue

        # injurynews
        if (re.search('injury', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('injury', df.loc[idx, 'url'], re.IGNORECASE)
                or re.search('suffer', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('absent', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('illness', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('ruled out', df.loc[idx, 'article'], re.IGNORECASE)):
            df.loc[idx, 'topic'] = 'Injurynews'
            counter_headline = counter_headline + 1
            continue

        # Contractnews
        if (re.search('retire', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('retire', df.loc[idx, 'url'], re.IGNORECASE)
                or re.search('join', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('join', df.loc[idx, 'url'], re.IGNORECASE)
                or re.search('contract', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('contract', df.loc[idx, 'url'], re.IGNORECASE)
                or re.search('deal', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('sign', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('loan', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('signing', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('interim', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('part company', df.loc[idx, 'article'], re.IGNORECASE)):
            df.loc[idx, 'topic'] = 'Contractnews'
            counter_headline = counter_headline + 1
            continue

        # Other Competitions
        if (re.search('uefa euro', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('uefa champions league', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('euro league', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('europa league', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('world cup', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('copa america', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('africa cup', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('confed', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('concacaf', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('dfb cup', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('supercup', df.loc[idx, 'article'], re.IGNORECASE)):
            df.loc[idx, 'topic'] = 'Other Competitions'
            counter_headline = counter_headline + 1
            continue

        if pd.notnull(df.loc[idx, 'competition']):
            if (re.search('champions league', df.loc[idx, 'competition'], re.IGNORECASE)
                    or re.search('copa america', df.loc[idx, 'competition'], re.IGNORECASE)
                    or re.search('dfb cup', df.loc[idx, 'competition'], re.IGNORECASE)
                    or re.search('europa league', df.loc[idx, 'competition'], re.IGNORECASE)
                    or re.search('national team', df.loc[idx, 'competition'], re.IGNORECASE)
                    or re.search('uefa euro', df.loc[idx, 'competition'], re.IGNORECASE)):
                df.loc[idx, 'topic'] = 'Other Competitions'
                counter_headline = counter_headline + 1
                continue

        # features
        if df.loc[idx, 'content_group'] == 'Features':
            df.loc[idx, 'topic'] = 'Features'
            counter_headline = counter_headline + 1
            continue

        # features
        if (re.search('10 reasons', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('10 things', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('5 reasons', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('short history of', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('advent calendar', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('all you need to know', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('bundesliga basics', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('bundesliga cathedrals', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('bundesliga legends', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('bundeliga media days', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('stars of tomorrow', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('bundesliga world tour', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('der klassiker', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('klassiker', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('five reasons', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('five things', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('hinrunde highlights', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('season so far', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('teenage kicks', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('ten reasons', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('ten things', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('story so far', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('Top 5 Talking points', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('revierderby', df.loc[idx, 'article'], re.IGNORECASE)
                or re.search('bundesliga50k', df.loc[idx, 'article'], re.IGNORECASE)):
            df.loc[idx, 'topic'] = 'Features'
            counter_headline = counter_headline + 1
            continue



        sc_contractnews = 0
        sc_injurynews = 0
        sc_statements = 0
        sc_features = 0
        sc_preview = 0
        sc_review = 0
        sc_votings = 0

        w_content = 1
        w_abstract = 3
        w_headline = 5

        # contractnews score

        for i in range (0, len(list_contractnews)):
            if pd.notnull(df.loc[idx, 'content']) and pd.notnull(df.loc[idx, 'abstract']):
                if re.search(list_contractnews[i][0], df.loc[idx, 'content'], re.IGNORECASE)\
                or re.search(list_contractnews[i][0], df.loc[idx, 'article'], re.IGNORECASE) \
                or re.search(list_contractnews[i][0], df.loc[idx, 'abstract'], re.IGNORECASE):
                    sc_contractnews = sc_contractnews + df.loc[idx, 'content'].count(list_contractnews[i][0]) * list_contractnews[i][1] * w_content
                    sc_contractnews = sc_contractnews + df.loc[idx, 'abstract'].count(list_contractnews[i][0]) * list_contractnews[i][1] * w_abstract
                    sc_contractnews = sc_contractnews + df.loc[idx, 'article'].count(list_contractnews[i][0]) * list_contractnews[i][1] * w_headline
                    print(list_contractnews[i][0], df.loc[idx, 'content'].count(list_contractnews[i][0]),
                          df.loc[idx, 'abstract'].count(list_contractnews[i][0]),
                          df.loc[idx, 'article'].count(list_contractnews[i][0]))

        # injury score
        for i in range(0, len(list_injurynews)):
            if pd.notnull(df.loc[idx, 'content']) and pd.notnull(df.loc[idx, 'abstract']):
                if re.search(list_injurynews[i][0], df.loc[idx, 'content'], re.IGNORECASE)\
                or re.search(list_injurynews[i][0], df.loc[idx, 'article'], re.IGNORECASE) \
                or re.search(list_injurynews[i][0], df.loc[idx, 'abstract'], re.IGNORECASE):
                    sc_injurynews = sc_injurynews + df.loc[idx, 'content'].count(list_injurynews[i][0]) * list_injurynews[i][1] * w_content
                    sc_injurynews = sc_injurynews + df.loc[idx, 'abstract'].count(list_injurynews[i][0]) * list_injurynews[i][1] * w_abstract
                    sc_injurynews = sc_injurynews + df.loc[idx, 'article'].count(list_injurynews[i][0]) * list_injurynews[i][1] * w_headline
                    print(list_injurynews[i][0], df.loc[idx, 'content'].count(list_injurynews[i][0]), df.loc[idx, 'abstract'].count(list_injurynews[i][0]), df.loc[idx, 'article'].count(list_injurynews[i][0]))


        # statements score
        for i in range(0, len(list_statements)):
            if pd.notnull(df.loc[idx, 'content']) and pd.notnull(df.loc[idx, 'abstract']):
                if re.search(list_statements[i][0], df.loc[idx, 'content'], re.IGNORECASE)\
                or re.search(list_statements[i][0], df.loc[idx, 'article'], re.IGNORECASE) \
                or re.search(list_statements[i][0], df.loc[idx, 'abstract'], re.IGNORECASE):
                    sc_statements = sc_statements + df.loc[idx, 'content'].count(list_statements[i][0]) * list_statements[i][1] * w_content
                    sc_statements = sc_statements + df.loc[idx, 'abstract'].count(list_statements[i][0]) * list_statements[i][1] * w_abstract
                    sc_statements = sc_statements + df.loc[idx, 'article'].count(list_statements[i][0]) * list_statements[i][1] * w_headline


        # features score
        for i in range(0, len(list_features)):
            if pd.notnull(df.loc[idx, 'content']) and pd.notnull(df.loc[idx, 'abstract']):
                if re.search(list_features[i][0], df.loc[idx, 'content'], re.IGNORECASE)\
                or re.search(list_features[i][0], df.loc[idx, 'article'], re.IGNORECASE) \
                or re.search(list_features[i][0], df.loc[idx, 'abstract'], re.IGNORECASE):
                    sc_features = sc_features + df.loc[idx, 'content'].count(list_features[i][0]) * list_features[i][1] * w_content
                    sc_features = sc_features + df.loc[idx, 'abstract'].count(list_features[i][0]) * list_features[i][1] * w_abstract
                    sc_features = sc_features + df.loc[idx, 'article'].count(list_features[i][0]) * list_features[i][1] * w_headline


        # preview score
        for i in range(0, len(list_preview)):
            if pd.notnull(df.loc[idx, 'content']) and pd.notnull(df.loc[idx, 'abstract']):
                if re.search(list_preview[i][0], df.loc[idx, 'content'], re.IGNORECASE)\
                or re.search(list_preview[i][0], df.loc[idx, 'article'], re.IGNORECASE) \
                or re.search(list_preview[i][0], df.loc[idx, 'abstract'], re.IGNORECASE):
                    sc_preview = sc_preview + df.loc[idx, 'content'].count(list_preview[i][0]) * list_preview[i][1] * w_content
                    sc_preview = sc_preview + df.loc[idx, 'abstract'].count(list_preview[i][0]) * list_preview[i][1] * w_abstract
                    sc_preview = sc_preview + df.loc[idx, 'article'].count(list_preview[i][0]) * list_preview[i][1] * w_headline


        # review score
        for i in range(0, len(list_review)):
            if pd.notnull(df.loc[idx, 'content']) and pd.notnull(df.loc[idx, 'abstract']):
                if re.search(list_review[i][0], df.loc[idx, 'content'], re.IGNORECASE)\
                or re.search(list_review[i][0], df.loc[idx, 'article'], re.IGNORECASE) \
                or re.search(list_review[i][0], df.loc[idx, 'abstract'], re.IGNORECASE):
                    sc_review = sc_review + df.loc[idx, 'content'].count(list_review[i][0]) * list_review[i][1] * w_content
                    sc_review = sc_review + df.loc[idx, 'abstract'].count(list_review[i][0]) * list_review[i][1] * w_abstract
                    sc_review = sc_review + df.loc[idx, 'article'].count(list_review[i][0]) * list_review[i][1] * w_headline


        # votings score
        for i in range(0, len(list_votings)):
            if pd.notnull(df.loc[idx, 'content']) and pd.notnull(df.loc[idx, 'abstract']):
                if re.search(list_votings[i][0], df.loc[idx, 'content'], re.IGNORECASE)\
                or re.search(list_votings[i][0], df.loc[idx, 'article'], re.IGNORECASE) \
                or re.search(list_votings[i][0], df.loc[idx, 'abstract'], re.IGNORECASE):
                    sc_votings = sc_votings + df.loc[idx, 'content'].count(list_votings[i][0]) * list_votings[i][1] * w_content
                    sc_votings = sc_votings + df.loc[idx, 'abstract'].count(list_votings[i][0]) * list_votings[i][1] * w_abstract
                    sc_votings = sc_votings + df.loc[idx, 'article'].count(list_votings[i][0]) * list_votings[i][1] * w_headline


        maxtopic = {'Contractnews' : sc_contractnews,
                    'Features' : sc_features,
                    'Injurynews' : sc_injurynews,
                    'Match Preview' : sc_preview,
                    'Match Review' : sc_review,
                    'Statements' : sc_statements,
                    'Votings' : sc_votings}

        print('Topic', max(maxtopic, key=maxtopic.get))
        print(df.loc[idx, 'article_id'], df.loc[idx, 'article'])
        print('Contract', sc_contractnews)
        print('Injury', sc_injurynews)
        print('Features', sc_features)
        print('Preview', sc_preview)
        print('Review', sc_review)
        print('Statements', sc_statements)
        print('Votings', sc_votings)
        print('___________')

        if (max(sc_contractnews,sc_features,sc_injurynews,sc_preview,sc_review,sc_statements,sc_votings) < 15):
            if (df.loc[idx, 'content_group'] == 'News'):
                df.loc[idx, 'topic'] = 'Other News'
                counter_score = counter_score + 1
            else:
                df.loc[idx, 'topic'] = 'Other Articles'
                counter_score = counter_score + 1
        else:
            df.loc[idx, 'topic'] = max(maxtopic, key=maxtopic.get)
            counter_score = counter_score + 1
        #print(df.loc[idx, 'topic'])



# competition
#  if (re.search('UEFA euro', df.loc[idx, 'article'], re.IGNORECASE) or re.search('uefa champions league', df.loc[idx, 'article'], re.IGNORECASE) or re.search('europa league', df.loc[idx, 'article'], re.IGNORECASE) or re.search('world cup',df.loc[idx, 'article'], re.IGNORECASE) or re.search('euro league', df.loc[idx, 'article'], re.IGNORECASE) or re.search('copa america', df.loc[idx, 'article'], re.IGNORECASE) or re.search('africa cup', df.loc[idx, 'article'], re.IGNORECASE) or re.search('confed', df.loc[idx, 'article'], re.IGNORECASE) or re.search('concacaf', df.loc[idx, 'article'], re.IGNORECASE) or re.search('dfb cup', df.loc[idx, 'article'],re.IGNORECASE)):
#     df.loc[idx, 'topic'] = 'other competitions'
# continue
# if pd.isnull(df.loc[idx, 'competition']):
# continue
# else:
#  if (re.search('champions league', df.loc[idx, 'competition'], re.IGNORECASE)
#             or re.search('copa america', df.loc[idx, 'competition'], re.IGNORECASE)
#            or re.search('dfb cup', df.loc[idx, 'competition'], re.IGNORECASE)
#           or re.search('europa league', df.loc[idx, 'competition'], re.IGNORECASE)
#          or re.search('international', df.loc[idx, 'competition'], re.IGNORECASE)
#         or re.search('national team', df.loc[idx, 'competition'], re.IGNORECASE)
#        or re.search('uefa euro', df.loc[idx, 'competition'], re.IGNORECASE)):
#   df.loc[idx, 'topic'] = 'other competitions'
#  continue


print('ContentGroup: ', counter_contentgroup, ' Headline: ', counter_headline, ' Scoring: ', counter_score )

# drop columns
df.drop('publishing_date', axis=1, inplace=True)
df.drop('season', axis=1, inplace=True)
df.drop('matchday', axis=1, inplace=True)
df.drop('match', axis=1, inplace=True)
df.drop('abstract', axis=1, inplace=True)
df.drop('content', axis=1, inplace=True)

# if 'report' in df.loc[idx, 'article']:
# df.loc[idx, 'topic'] = 'Match Report'


# , case=False
# df.loc[df['article'].astype(str).str.contains('report'), "topic"] = "Match Report"


df.to_csv("csvs/dim_web_articles_topic.csv", encoding='iso-8859-1', sep=';', index=False)
