import spacyimport spacynlp = spacy.load("en_core_web_sm")nlp = spacy.load("en_core_web_sm")sentence = "We will be learning NLP today!"sentence = "We will be learning NLP today!"print ("{:<15} | {:<8} | {:<15} | {:<30} | {:<20}".format('Token','Relation','Head', 'Children', 'Meaning'))print ("{:<15} | {:<8} | {:<15} | {:<30} | {:<20}".format('Token','Relation','Head', 'Children', 'Meaning'))print ("-" * 115)print ("-" * 115)for token in doc:    # Print the token, dependency nature, head, all dependents of the token, and meaning of the dependency    print ("{:<15} | {:<8} | {:<15} | {:<30} | {:<20}"            .format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children]) , str(spacy.explain(token.dep_))[:17] ))for token in doc:    # Print the token, dependency nature, head, all dependents of the token, and meaning of the dependency    print ("{:<15} | {:<8} | {:<15} | {:<30} | {:<20}"            .format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children]) , str(spacy.explain(token.dep_))[:17] ))for token in doc:    # Print the token, dependency nature, head, all dependents of the token, and meaning of the dependency    print ("{:<15} | {:<8} | {:<15} | {:<30} | {:<20}"            .format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children]) , str(spacy.explain(token.dep_))[:17] ))for token in doc:    # Print the token, dependency nature, head, all dependents of the token, and meaning of the dependency    print ("{:<15} | {:<8} | {:<15} | {:<30} | {:<20}"            .format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children]) , str(spacy.explain(token.dep_))[:17] ))for token in doc:    # Print the token, dependency nature, head, all dependents of the token, and meaning of the dependency    print ("{:<15} | {:<8} | {:<15} | {:<30} | {:<20}"            .format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children]) , str(spacy.explain(token.dep_))[:17] ))import beneparimport beneparbenepar.download('benepar_en3')benepar.download('benepar_en3')import spacyimport spacynlp = spacy.load("en_core_web_md")nlp = spacy.load("en_core_web_md")if spacy.__version__.startswith('2'):    nlp.add_pipe(benepar.BeneparComponent("benepar_en3"))else:    nlp.add_pipe("benepar", config={"model": "benepar_en3"})if spacy.__version__.startswith('2'):    nlp.add_pipe(benepar.BeneparComponent("benepar_en3"))else:    nlp.add_pipe("benepar", config={"model": "benepar_en3"})if spacy.__version__.startswith('2'):    nlp.add_pipe(benepar.BeneparComponent("benepar_en3"))else:    nlp.add_pipe("benepar", config={"model": "benepar_en3"})if spacy.__version__.startswith('2'):    nlp.add_pipe(benepar.BeneparComponent("benepar_en3"))else:    nlp.add_pipe("benepar", config={"model": "benepar_en3"})if spacy.__version__.startswith('2'):    nlp.add_pipe(benepar.BeneparComponent("benepar_en3"))else:    nlp.add_pipe("benepar", config={"model": "benepar_en3"})doc = nlp("Johnson was compelled to ask the EU for an extension of the deadline, which was granted")doc = nlp("Johnson was compelled to ask the EU for an extension of the deadline, which was granted")sent = list(doc.sents)[0]sent = list(doc.sents)[0]print(sent._.parse_string)print(sent._.parse_string)import spacyimport spacynlp = spacy.load("en_core_web_md")nlp = spacy.load("en_core_web_md")sent = "John Smith works at Tangible AI"sent = "John Smith works at Tangible AI"doc = nlp(sent)doc = nlp(sent)entities = []entities = []for ent in doc.ents:    sent = sent.replace(ent.text, "^/" + ent.label_ + "/" + ent.text + "^")for ent in doc.ents:    sent = sent.replace(ent.text, "^/" + ent.label_ + "/" + ent.text + "^")for ent in doc.ents:    sent = sent.replace(ent.text, "^/" + ent.label_ + "/" + ent.text + "^")print(sent)print(sent)import spacyimport spacynlp = spacy.load('en_core_web_md')nlp = spacy.load('en_core_web_md')import neuralcorefimport neuralcorefneuralcoref.add_to_pipe(nlp)neuralcoref.add_to_pipe(nlp)doc = nlp(u'My sister has a dog. She loves him.')doc = nlp(u'My sister has a dog. She loves him.')doc._.coref_clustersdoc._.coref_clustersfrom allennlp.predictors.predictor import Predictorfrom allennlp.predictors.predictor import Predictorimport allennlp_models.taggingimport allennlp_models.taggingpredictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2021.03.10.tar.gz")predictor = Predictor.from_path("https://storage.googleapis.com/allennlp-public-models/coref-spanbert-large-2021.03.10.tar.gz")predictor.predict(predictor.predict(def find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonedef find_greeting(s):    """ Return greeting str (Hi, etc) if greeting pattern matches """    if s[0] == 'H':        if s[:3] in ['Hi', 'Hi ', 'Hi,', 'Hi!']:            return s[:2]        elif s[:6] in ['Hello', 'Hello ', 'Hello,', 'Hello!']:            return s[:5]    elif s[0] == 'Y':        if s[1] == 'o' and s[:3] in ['Yo', 'Yo,', 'Yo ', 'Yo!']:            return s[:2]    return Nonefind_greeting('Hi Mr. Turing!')find_greeting('Hi Mr. Turing!')find_greeting('Hello, Rosa.')find_greeting('Hello, Rosa.')find_greeting("Yo, what's up?")find_greeting("Yo, what's up?")find_greeting("Hello")find_greeting("Hello")print(find_greeting("hello"))print(find_greeting("hello"))print(find_greeting("HelloWorld"))print(find_greeting("HelloWorld"))import reimport relat = r'([-]?[0-9]?[0-9][.][0-9]{2,10})'lat = r'([-]?[0-9]?[0-9][.][0-9]{2,10})'lon = r'([-]?1?[0-9]?[0-9][.][0-9]{2,10})'lon = r'([-]?1?[0-9]?[0-9][.][0-9]{2,10})'sep = r'[,/ ]{1,3}'sep = r'[,/ ]{1,3}'re_gps = re.compile(lat + sep + lon)re_gps = re.compile(lat + sep + lon)re_gps.findall('http://...maps/@34.0551066,-118.2496763...')re_gps.findall('http://...maps/@34.0551066,-118.2496763...')re_gps.findall("https://www.openstreetmap.org/#map=10/5.9666/116.0566")re_gps.findall("https://www.openstreetmap.org/#map=10/5.9666/116.0566")re_gps.findall("Zig Zag Cafe is at 45.344, -121.9431 on my GPS.")re_gps.findall("Zig Zag Cafe is at 45.344, -121.9431 on my GPS.")us = r'((([01]?\d)[-/]([0123]?\d))([-/]([0123]\d)\d\d)?)'us = r'((([01]?\d)[-/]([0123]?\d))([-/]([0123]\d)\d\d)?)'mdy = re.findall(us, 'Santa came 12/25/2017. An elf appeared 12/12.')mdy = re.findall(us, 'Santa came 12/25/2017. An elf appeared 12/12.')mdymdydates = [{'mdy': x[0], 'my': x[1], 'm': int(x[2]), 'd': int(x[3]),    'y': int(x[4].lstrip('/') or 0), 'c': int(x[5] or 0)} for x in mdy]dates = [{'mdy': x[0], 'my': x[1], 'm': int(x[2]), 'd': int(x[3]),    'y': int(x[4].lstrip('/') or 0), 'c': int(x[5] or 0)} for x in mdy]dates = [{'mdy': x[0], 'my': x[1], 'm': int(x[2]), 'd': int(x[3]),    'y': int(x[4].lstrip('/') or 0), 'c': int(x[5] or 0)} for x in mdy]datesdatesfor i, d in enumerate(dates):    for k, v in d.items():        if not v:            d[k] = dates[max(i - 1, 0)][k]  # <1>for i, d in enumerate(dates):    for k, v in d.items():        if not v:            d[k] = dates[max(i - 1, 0)][k]  # <1>for i, d in enumerate(dates):    for k, v in d.items():        if not v:            d[k] = dates[max(i - 1, 0)][k]  # <1>for i, d in enumerate(dates):    for k, v in d.items():        if not v:            d[k] = dates[max(i - 1, 0)][k]  # <1>for i, d in enumerate(dates):    for k, v in d.items():        if not v:            d[k] = dates[max(i - 1, 0)][k]  # <1>datesdatesfrom datetime import datefrom datetime import datedatetimes = [date(d['y'], d['m'], d['d']) for d in dates]datetimes = [date(d['y'], d['m'], d['d']) for d in dates]datetimesdatetimeseu = r'((([0123]?\d)[-/]([01]?\d))([-/]([0123]\d)?\d\d)?)'eu = r'((([0123]?\d)[-/]([01]?\d))([-/]([0123]\d)?\d\d)?)'dmy = re.findall(eu, 'Alan Mathison Turing OBE FRS (23/6/1912-7/6/1954) \    was an English computer scientist.')dmy = re.findall(eu, 'Alan Mathison Turing OBE FRS (23/6/1912-7/6/1954) \    was an English computer scientist.')dmy = re.findall(eu, 'Alan Mathison Turing OBE FRS (23/6/1912-7/6/1954) \    was an English computer scientist.')dmydmydmy = re.findall(eu, 'Alan Mathison Turing OBE FRS (23/6/12-7/6/54) \    was an English computer scientist.')dmy = re.findall(eu, 'Alan Mathison Turing OBE FRS (23/6/12-7/6/54) \    was an English computer scientist.')dmy = re.findall(eu, 'Alan Mathison Turing OBE FRS (23/6/12-7/6/54) \    was an English computer scientist.')dmydmyyr_19xx = (    r'\b(?P<yr_19xx>' +    '|'.join('{}'.format(i) for i in range(30, 100)) +    r')\b'    )  # <1>yr_19xx = (    r'\b(?P<yr_19xx>' +    '|'.join('{}'.format(i) for i in range(30, 100)) +    r')\b'    )  # <1>yr_19xx = (    r'\b(?P<yr_19xx>' +    '|'.join('{}'.format(i) for i in range(30, 100)) +    r')\b'    )  # <1>yr_19xx = (    r'\b(?P<yr_19xx>' +    '|'.join('{}'.format(i) for i in range(30, 100)) +    r')\b'    )  # <1>yr_19xx = (    r'\b(?P<yr_19xx>' +    '|'.join('{}'.format(i) for i in range(30, 100)) +    r')\b'    )  # <1>yr_19xx = (    r'\b(?P<yr_19xx>' +    '|'.join('{}'.format(i) for i in range(30, 100)) +    r')\b'    )  # <1>yr_20xx = (    r'\b(?P<yr_20xx>' +    '|'.join('{:02d}'.format(i) for i in range(10)) + '|' +    '|'.join('{}'.format(i) for i in range(10, 30)) +    r')\b'    )  # <2>yr_20xx = (    r'\b(?P<yr_20xx>' +    '|'.join('{:02d}'.format(i) for i in range(10)) + '|' +    '|'.join('{}'.format(i) for i in range(10, 30)) +    r')\b'    )  # <2>yr_20xx = (    r'\b(?P<yr_20xx>' +    '|'.join('{:02d}'.format(i) for i in range(10)) + '|' +    '|'.join('{}'.format(i) for i in range(10, 30)) +    r')\b'    )  # <2>yr_20xx = (    r'\b(?P<yr_20xx>' +    '|'.join('{:02d}'.format(i) for i in range(10)) + '|' +    '|'.join('{}'.format(i) for i in range(10, 30)) +    r')\b'    )  # <2>yr_20xx = (    r'\b(?P<yr_20xx>' +    '|'.join('{:02d}'.format(i) for i in range(10)) + '|' +    '|'.join('{}'.format(i) for i in range(10, 30)) +    r')\b'    )  # <2>yr_20xx = (    r'\b(?P<yr_20xx>' +    '|'.join('{:02d}'.format(i) for i in range(10)) + '|' +    '|'.join('{}'.format(i) for i in range(10, 30)) +    r')\b'    )  # <2>yr_20xx = (    r'\b(?P<yr_20xx>' +    '|'.join('{:02d}'.format(i) for i in range(10)) + '|' +    '|'.join('{}'.format(i) for i in range(10, 30)) +    r')\b'    )  # <2>yr_cent = r'\b(?P<yr_cent>' + '|'.join(    '{}'.format(i) for i in range(1, 40)) + r')'  # <3>yr_cent = r'\b(?P<yr_cent>' + '|'.join(    '{}'.format(i) for i in range(1, 40)) + r')'  # <3>yr_cent = r'\b(?P<yr_cent>' + '|'.join(    '{}'.format(i) for i in range(1, 40)) + r')'  # <3>yr_ccxx = r'(?P<yr_ccxx>' + '|'.join(    '{:02d}'.format(i) for i in range(0, 100)) + r')\b'  # <4>yr_ccxx = r'(?P<yr_ccxx>' + '|'.join(    '{:02d}'.format(i) for i in range(0, 100)) + r')\b'  # <4>yr_ccxx = r'(?P<yr_ccxx>' + '|'.join(    '{:02d}'.format(i) for i in range(0, 100)) + r')\b'  # <4>yr_xxxx = r'\b(?P<yr_xxxx>(' + yr_cent + ')(' + yr_ccxx + r'))\b'yr_xxxx = r'\b(?P<yr_xxxx>(' + yr_cent + ')(' + yr_ccxx + r'))\b'yr = (    r'\b(?P<yr>' +    yr_19xx + '|' + yr_20xx + '|' + yr_xxxx +    r')\b'    )yr = (    r'\b(?P<yr>' +    yr_19xx + '|' + yr_20xx + '|' + yr_xxxx +    r')\b'    )yr = (    r'\b(?P<yr>' +    yr_19xx + '|' + yr_20xx + '|' + yr_xxxx +    r')\b'    )yr = (    r'\b(?P<yr>' +    yr_19xx + '|' + yr_20xx + '|' + yr_xxxx +    r')\b'    )yr = (    r'\b(?P<yr>' +    yr_19xx + '|' + yr_20xx + '|' + yr_xxxx +    r')\b'    )yr = (    r'\b(?P<yr>' +    yr_19xx + '|' + yr_20xx + '|' + yr_xxxx +    r')\b'    )groups = list(re.finditer(    yr, "0, 2000, 01, '08, 99, 1984, 2030/1970 85 47 `66"))groups = list(re.finditer(    yr, "0, 2000, 01, '08, 99, 1984, 2030/1970 85 47 `66"))groups = list(re.finditer(    yr, "0, 2000, 01, '08, 99, 1984, 2030/1970 85 47 `66"))full_years = [g['yr'] for g in groups]full_years = [g['yr'] for g in groups]full_yearsfull_yearsmon_words = 'January February March April May June July ' \    'August September October November December'mon_words = 'January February March April May June July ' \    'August September October November December'mon_words = 'January February March April May June July ' \    'August September October November December'mon = (r'\b(' + '|'.join('{}|{}|{}|{}|{:02d}'.format(    m, m[:4], m[:3], i + 1, i + 1) for i, m in enumerate(mon_words.split())) +    r')\b')mon = (r'\b(' + '|'.join('{}|{}|{}|{}|{:02d}'.format(    m, m[:4], m[:3], i + 1, i + 1) for i, m in enumerate(mon_words.split())) +    r')\b')mon = (r'\b(' + '|'.join('{}|{}|{}|{}|{:02d}'.format(    m, m[:4], m[:3], i + 1, i + 1) for i, m in enumerate(mon_words.split())) +    r')\b')mon = (r'\b(' + '|'.join('{}|{}|{}|{}|{:02d}'.format(    m, m[:4], m[:3], i + 1, i + 1) for i, m in enumerate(mon_words.split())) +    r')\b')re.findall(mon, 'January has 31 days, February the 2nd month of 12, has 28, except in a Leap Year.')re.findall(mon, 'January has 31 days, February the 2nd month of 12, has 28, except in a Leap Year.')day = r'|'.join('{:02d}|{}'.format(i, i) for i in range(1, 32))day = r'|'.join('{:02d}|{}'.format(i, i) for i in range(1, 32))eu = (r'\b(' + day + r')\b[-,/ ]{0,2}\b(' +    mon + r')\b[-,/ ]{0,2}\b(' + yr.replace('<yr', '<eu_yr') + r')\b')eu = (r'\b(' + day + r')\b[-,/ ]{0,2}\b(' +    mon + r')\b[-,/ ]{0,2}\b(' + yr.replace('<yr', '<eu_yr') + r')\b')eu = (r'\b(' + day + r')\b[-,/ ]{0,2}\b(' +    mon + r')\b[-,/ ]{0,2}\b(' + yr.replace('<yr', '<eu_yr') + r')\b')us = (r'\b(' + mon + r')\b[-,/ ]{0,2}\b(' +    day + r')\b[-,/ ]{0,2}\b(' + yr.replace('<yr', '<us_yr') + r')\b')us = (r'\b(' + mon + r')\b[-,/ ]{0,2}\b(' +    day + r')\b[-,/ ]{0,2}\b(' + yr.replace('<yr', '<us_yr') + r')\b')us = (r'\b(' + mon + r')\b[-,/ ]{0,2}\b(' +    day + r')\b[-,/ ]{0,2}\b(' + yr.replace('<yr', '<us_yr') + r')\b')date_pattern = r'\b(' + eu + '|' + us + r')\b'date_pattern = r'\b(' + eu + '|' + us + r')\b'list(re.finditer(date_pattern, '31 Oct, 1970 25/12/2017'))list(re.finditer(date_pattern, '31 Oct, 1970 25/12/2017'))import datetimeimport datetimedates = []dates = []for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)for g in groups:    month_num = (g['us_mon'] or g['eu_mon']).strip()    try:        month_num = int(month_num)    except ValueError:        month_num = [w[:len(month_num)]            for w in mon_words].index(month_num) + 1    date = datetime.date(        int(g['us_yr'] or g['eu_yr']),        month_num,        int(g['us_day'] or g['eu_day']))    dates.append(date)datesdatesimport spacyimport spacyen_model = spacy.load('en_core_web_md')en_model = spacy.load('en_core_web_md')sentence = ("In 1541 Desoto wrote in his journal that the Pascagoula people " +    "ranged as far north as the confluence of the Leaf and Chickasawhay rivers at 30.4, -88.5.")sentence = ("In 1541 Desoto wrote in his journal that the Pascagoula people " +    "ranged as far north as the confluence of the Leaf and Chickasawhay rivers at 30.4, -88.5.")sentence = ("In 1541 Desoto wrote in his journal that the Pascagoula people " +    "ranged as far north as the confluence of the Leaf and Chickasawhay rivers at 30.4, -88.5.")parsed_sent = en_model(sentence)parsed_sent = en_model(sentence)parsed_sent.entsparsed_sent.ents' '.join(['{}_{}'.format(tok, tok.tag_) for tok in parsed_sent])' '.join(['{}_{}'.format(tok, tok.tag_) for tok in parsed_sent])from spacy.displacy import renderfrom spacy.displacy import rendersentence = "In 1541 Desoto wrote in his journal about the Pascagoula."sentence = "In 1541 Desoto wrote in his journal about the Pascagoula."parsed_sent = en_model(sentence)parsed_sent = en_model(sentence)with open('pascagoula.html', 'w') as f:    f.write(render(docs=parsed_sent, page=True, options=dict(compact=True)))with open('pascagoula.html', 'w') as f:    f.write(render(docs=parsed_sent, page=True, options=dict(compact=True)))with open('pascagoula.html', 'w') as f:    f.write(render(docs=parsed_sent, page=True, options=dict(compact=True)))import pandas as pdimport pandas as pdfrom collections import OrderedDictfrom collections import OrderedDictdef token_dict(token):    return OrderedDict(ORTH=token.orth_, LEMMA=token.lemma_,        POS=token.pos_, TAG=token.tag_, DEP=token.dep_)def token_dict(token):    return OrderedDict(ORTH=token.orth_, LEMMA=token.lemma_,        POS=token.pos_, TAG=token.tag_, DEP=token.dep_)def token_dict(token):    return OrderedDict(ORTH=token.orth_, LEMMA=token.lemma_,        POS=token.pos_, TAG=token.tag_, DEP=token.dep_)def token_dict(token):    return OrderedDict(ORTH=token.orth_, LEMMA=token.lemma_,        POS=token.pos_, TAG=token.tag_, DEP=token.dep_)def doc_dataframe(doc):    return pd.DataFrame([token_dict(tok) for tok in doc])def doc_dataframe(doc):    return pd.DataFrame([token_dict(tok) for tok in doc])def doc_dataframe(doc):    return pd.DataFrame([token_dict(tok) for tok in doc])doc_dataframe(en_model("In 1541 Desoto met the Pascagoula."))doc_dataframe(en_model("In 1541 Desoto met the Pascagoula."))pattern = [{'TAG': 'NNP', 'OP': '+'}, {'IS_ALPHA': True, 'OP': '*'},           {'LEMMA': 'meet'},           {'IS_ALPHA': True, 'OP': '*'}, {'TAG': 'NNP', 'OP': '+'}]pattern = [{'TAG': 'NNP', 'OP': '+'}, {'IS_ALPHA': True, 'OP': '*'},           {'LEMMA': 'meet'},           {'IS_ALPHA': True, 'OP': '*'}, {'TAG': 'NNP', 'OP': '+'}]pattern = [{'TAG': 'NNP', 'OP': '+'}, {'IS_ALPHA': True, 'OP': '*'},           {'LEMMA': 'meet'},           {'IS_ALPHA': True, 'OP': '*'}, {'TAG': 'NNP', 'OP': '+'}]pattern = [{'TAG': 'NNP', 'OP': '+'}, {'IS_ALPHA': True, 'OP': '*'},           {'LEMMA': 'meet'},           {'IS_ALPHA': True, 'OP': '*'}, {'TAG': 'NNP', 'OP': '+'}]from spacy.matcher import Matcherfrom spacy.matcher import Matcherdoc = en_model("In 1541 Desoto met the Pascagoula.")doc = en_model("In 1541 Desoto met the Pascagoula.")matcher = Matcher(en_model.vocab)matcher = Matcher(en_model.vocab)matcher.add('met', None, pattern)matcher.add('met', None, pattern)m = matcher(doc)m = matcher(doc)mmdoc[m[0][1]:m[0][2]]doc[m[0][1]:m[0][2]]doc = en_model("October 24: Lewis and Clark met their" \               "first Mandan Chief, Big White.")doc = en_model("October 24: Lewis and Clark met their" \               "first Mandan Chief, Big White.")doc = en_model("October 24: Lewis and Clark met their" \               "first Mandan Chief, Big White.")m = matcher(doc)[0]m = matcher(doc)[0]mmdoc[m[1]:m[2]]doc[m[1]:m[2]]doc = en_model("On 11 October 1986, Gorbachev and Reagan met at Höfði house")doc = en_model("On 11 October 1986, Gorbachev and Reagan met at Höfði house")matcher(doc)matcher(doc)doc = en_model("On 11 October 1986, Gorbachev and Reagan met at Hofoi house")doc = en_model("On 11 October 1986, Gorbachev and Reagan met at Hofoi house")pattern = [{'TAG': 'NNP', 'OP': '+'}, {'LEMMA': 'and'},           {'TAG': 'NNP', 'OP': '+'},           {'IS_ALPHA': True, 'OP': '*'}, {'LEMMA': 'meet'}]pattern = [{'TAG': 'NNP', 'OP': '+'}, {'LEMMA': 'and'},           {'TAG': 'NNP', 'OP': '+'},           {'IS_ALPHA': True, 'OP': '*'}, {'LEMMA': 'meet'}]pattern = [{'TAG': 'NNP', 'OP': '+'}, {'LEMMA': 'and'},           {'TAG': 'NNP', 'OP': '+'},           {'IS_ALPHA': True, 'OP': '*'}, {'LEMMA': 'meet'}]pattern = [{'TAG': 'NNP', 'OP': '+'}, {'LEMMA': 'and'},           {'TAG': 'NNP', 'OP': '+'},           {'IS_ALPHA': True, 'OP': '*'}, {'LEMMA': 'meet'}]matcher.add('met', None, pattern)  # <1>matcher.add('met', None, pattern)  # <1>m = matcher(doc)m = matcher(doc)mmdoc[m[-1][1]:m[-1][2]]  <3>doc[m[-1][1]:m[-1][2]]  <3>re.split(r'[!.?]+[ $]', "Hello World.... Are you there?!?! I'm going to Mars!")re.split(r'[!.?]+[ $]', "Hello World.... Are you there?!?! I'm going to Mars!")re.split(r'[!.?] ', "The author wrote \"'I don't think it's conscious.' Turing said.\"")re.split(r'[!.?] ', "The author wrote \"'I don't think it's conscious.' Turing said.\"")re.split(r'[!.?] ', "The author wrote \"'I don't think it's conscious.' Turing said.\" But I stopped reading.")re.split(r'[!.?] ', "The author wrote \"'I don't think it's conscious.' Turing said.\" But I stopped reading.")re.split(r'(?<!\d)\.|\.(?!\d)', "I went to GT.You?")re.split(r'(?<!\d)\.|\.(?!\d)', "I went to GT.You?")from nlpia.data.loaders import get_datafrom nlpia.data.loaders import get_dataregex = re.compile(r'((?<!\d)\.|\.(?!\d))|([!.?]+)[ $]+')regex = re.compile(r'((?<!\d)\.|\.(?!\d))|([!.?]+)[ $]+')examples = get_data('sentences-tm-town')examples = get_data('sentences-tm-town')wrong = []wrong = []for i, (challenge, text, sents) in enumerate(examples):    if tuple(regex.split(text)) != tuple(sents):        print('wrong {}: {}{}'.format(i, text[:50], '...' if len(text) > 50 else ''))        wrong += [i]for i, (challenge, text, sents) in enumerate(examples):    if tuple(regex.split(text)) != tuple(sents):        print('wrong {}: {}{}'.format(i, text[:50], '...' if len(text) > 50 else ''))        wrong += [i]for i, (challenge, text, sents) in enumerate(examples):    if tuple(regex.split(text)) != tuple(sents):        print('wrong {}: {}{}'.format(i, text[:50], '...' if len(text) > 50 else ''))        wrong += [i]for i, (challenge, text, sents) in enumerate(examples):    if tuple(regex.split(text)) != tuple(sents):        print('wrong {}: {}{}'.format(i, text[:50], '...' if len(text) > 50 else ''))        wrong += [i]for i, (challenge, text, sents) in enumerate(examples):    if tuple(regex.split(text)) != tuple(sents):        print('wrong {}: {}{}'.format(i, text[:50], '...' if len(text) > 50 else ''))        wrong += [i]len(wrong), len(examples)len(wrong), len(examples)