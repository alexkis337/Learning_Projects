import pandas as pd

input = pd.read_csv('_input/athena.csv')

def checker(publication, digital, sponsor, societies, trials):
    if int(publication) == 0:
        return 'Check Publications Score'
    elif int(digital) == 0:
        return 'Check DAS Score'
    elif int(sponsor) == 0:
        return 'Check Payments Score'
    elif int(societies) == 0:
        return 'Check Societies Score'
    elif int(trials) == 0:
        return 'Check CT Score'


input['Checker'] = input.apply(lambda x: checker(x.Publications_score, x.Digital_activator_score, x.Sponsorship_score,\
                                                 x.Societies_score, x.Clinical_trials_score), axis=1)

input.to_excel('_output/out.xlsx')
