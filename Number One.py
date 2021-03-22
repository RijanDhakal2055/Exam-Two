# This code works if the csv source files are in the same folder as the code itself 


import pandas as pd #These are all the libraries we need
import seaborn as sns
import matplotlib as mlb

def main():
    income_data_df = pd.read_csv('income_data.csv')# These are the data frames that we will be working on
    covid_data_df = pd.read_csv('US_COVID-19_Cases_ST.csv')
    population_df = pd.read_csv('US_state_pops.csv')
    state_name_df = pd.read_csv('state_abbrevs.csv')

    #Start of number one
    first_merge_df = pd.merge(left=state_name_df,right=covid_data_df, how='left', left_on='ST', right_on='ST') # Now, I am sure these mergers could have been done in one line but I could not find it
    second_merge_df = pd.merge(left=first_merge_df,right = population_df ,how ='left',left_on='State',right_on='State')
    final_merge_df = pd.merge(left=second_merge_df,right = income_data_df ,how ='left',left_on='State',right_on='State')
    #End of number one

    #Start of number two 
    filter_by_population_df = final_merge_df[final_merge_df.Population <= 10000000]#filter by popluation
    Final_filter_by_income_df = filter_by_population_df[filter_by_population_df['income(dollars)'] <= 55000]#Filter by income
    print(Final_filter_by_income_df) # print final data frame.
    #End of number two

    # Start of number three 
    sns.relplot(x= 'income(dollars)', y='conf_cases',data =final_merge_df,kind ='scatter')
    sns.relplot(x= 'Population', y='conf_cases',data =final_merge_df,kind ='scatter')
    #End of number three

main()

