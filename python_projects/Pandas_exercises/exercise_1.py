import pandas as pd


pd.set_option('display.expand_frame_repr', False)

test = pd.read_csv('CRM_PEOPLE (5).csv').drop(columns=['Tendency_1_Label', 'Tendency_2_Label', 'Tendency_3_Label',
                                                       'Tendency_4_Label', 'Tendency_5_Label', 'twitter_url',
                                                       'linkedin_url', 'url', 'OneKey', 'Role 2', 'Specialty 2'])

#print(test)
test_df = test[test['town'].str.contains('London|Middlesbrough', regex=True)]
print(test_df)


#print(test_df)
#middlesbrough_hcps =
#print(middlesbrough_hcps.sample(10))