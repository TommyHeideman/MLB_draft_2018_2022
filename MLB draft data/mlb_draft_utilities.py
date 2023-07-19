# -*- coding: utf-8 -*-
"""
Created on Tue Apr 25 23:10:34 2023

@author: Tommy
"""

# Tommy Heideman and Joey Matusik 

import pandas as pd

# Read the dataset
df = pd.read_csv('Draft_History5years.csv', encoding='ISO-8859-1')

# Filter data for the last 5 years (2018-2022) and rounds <= 5
filtered_data = df[(df['Year'].between(2018, 2022)) & (df['Round'].str.isnumeric())]
filtered_data['Round'] = filtered_data['Round'].astype(int)

# Define the positions dictionary
positions = {
    'C': 'Catcher',
    '1B': 'First Baseman',
    '2B': 'Second Baseman',
    '3B': 'Third Baseman',
    'SS': 'Shortstop',
    'OF': 'Outfielder',
    'LHP': 'Left-Handed Pitcher',
    'RHP': 'Right-Handed Pitcher',
    'SHP': 'Switch-Handed Pitcher',
    'IF': 'Infielder'
}

# Group data by Year and Position and count occurrences
position_counts = filtered_data.groupby(['Year', 'Pos']).size().unstack().fillna(0)

# Get the top 5 positions in each year
top_5_positions = position_counts.apply(lambda row: row.nlargest(5).index.tolist(), axis=1)

# Print the top 5 positions in each year
for year, positions in top_5_positions.items():
    print(f"Year {year}: {', '.join(positions)}")















































"""def HSvCollege():

    # Create a list of years to loop over
    years = [2018,2019,2020,2021,2022]

    # Loop over the years and calculate the percentage difference in high school vs college picks
    for year in years:
    # Filter the data for the given year
        year_df = df[df['Year'] == year]
    
        # Calculate the number of high school and college picks
        hs_picks = (year_df['School'].str.contains('HS|Prep|High School')).sum()
        college_picks = (year_df['School'].str.contains('State|University|College|CC|Community College|')).sum()
    
        # Calculate the percentage difference
        total_picks = hs_picks + college_picks
        hs_percent = hs_picks / total_picks * 100
        college_percent = college_picks / total_picks * 100
        
    
        # Print the results
        print(f"Year: {year}")
        print(f"High school picks: {hs_picks}")
        print(f"College picks: {college_picks}")
        print(f"High school picks percentage: {hs_percent:.2f}%")
        print(f"College picks percentage: {college_percent:.2f}%")
       
    
        # Create the bar chart
        x_pos = np.arange(2)
        percentages = [hs_percent, college_percent]
        labels = ['High School', 'College']
        colors = ['blue', 'orange']
    
        plt.bar(x_pos, percentages, color=colors)
        plt.xticks(x_pos, labels)
        plt.title(f"High School vs College Picks in {year}")
        plt.xlabel("School Type")
        plt.ylabel("Percentage of Total Picks")
        plt.ylim([0, 100])
        plt.show()

    return 0

HSvCollege()

def TeamPosition():
    # Create a dictionary to map the position abbreviations to full names
    position_map = {'C': 'Catcher', '1B': 'First Baseman', '2B': 'Second Baseman',
                '3B': 'Third Baseman', 'SS': 'Shortstop', 'OF': 'Outfielder',
                'LHP': 'Left-Handed Pitcher', 'RHP': 'Right-Handed Pitcher',
                'SHP': 'Switch-Handed Pitcher', 'IF': 'Infielder'}

    # Loop over each team and print the breakdown of positions for their draft picks
    teams = df['Team'].unique()
    for team in teams:
        # Filter the data for the current team
        team_df = df[df['Team'] == team]
    
        # Count the number of picks for each position
        position_counts = team_df['Pos'].value_counts()
    
        # Convert the position abbreviations to full names using the position_map dictionary
        position_counts.index = position_counts.index.map(position_map)
    
        # Print the results
        print(f"Team: {team}")
        print(position_counts)
        print()
        
        # Plot the position counts as a bar graph
        position_counts_df.plot(kind='bar', stacked=True)
        plt.title("Position Breakdown for All Teams")
        plt.xlabel("Position")
        plt.ylabel("Number of Picks")
        plt.legend(title="Team")
        plt.show()

    return 0

TeamPosition()


def TopPositions():
    # Create a dictionary to map the position abbreviations to full names
    position_map = {'C': 'Catcher', '1B': 'First Baseman', '2B': 'Second Baseman',
                '3B': 'Third Baseman', 'SS': 'Shortstop', 'OF': 'Outfielder',
                'LHP': 'Left-Handed Pitcher', 'RHP': 'Right-Handed Pitcher',
                'SHP': 'Switch-Handed Pitcher', 'IF': 'Infielder'}

    # Filter out LHP, RHP, and SHP from the data
    filtered_df = df[~df['Pos'].isin(['LHP', 'RHP', 'SHP'])]
    
    # Count the number of picks for each position
    position_counts = filtered_df['Pos'].value_counts()
    
    # Convert the position abbreviations to full names using the position_map dictionary
    position_counts.index = position_counts.index.map(position_map)
    
    # Print the top 5 positions
    print("Top 5 Positions:")
    print(position_counts.head())

    return 0

TopPositions()


def TopPositions():
    # Create a dictionary to map the position abbreviations to full names
    position_map = {'C': 'Catcher', '1B': 'First Baseman', '2B': 'Second Baseman',
                    '3B': 'Third Baseman', 'SS': 'Shortstop', 'OF': 'Outfielder',
                    'LHP': 'Left-Handed Pitcher', 'RHP': 'Right-Handed Pitcher',
                    'SHP': 'Switch-Handed Pitcher', 'IF': 'Infielder'}

    # Filter out LHP, RHP, and SHP from the data
    filtered_df = df[~df['Pos'].isin(['LHP', 'RHP', 'SHP'])]

    # Count the number of picks for each position
    position_counts = filtered_df['Pos'].value_counts()

    # Convert the position abbreviations to full names using the position_map dictionary
    position_counts.index = position_counts.index.map(position_map)

    # Get the top 5 positions
    top_positions = position_counts.head()

    # Create a bar chart of the top 5 positions
    plt.bar(top_positions.index, top_positions.values)

    # Add labels and a title
    
    plt.xlabel('Position')
    plt.xticks(rotation=90)
    plt.ylabel('Number of Picks')
    plt.title('Top 5 Positions in the Draft')

    # Display the chart
    plt.show()
    
    return 0 
TopPositions()




def TopSchools():
    # Convert the 'Round' column to a numeric type
    df['Round'] = pd.to_numeric(df['Round'], errors='coerce')
    
    # Filter the data for the top 5 rounds
    top_5_df = df[df['Round'] <= 5]

    # Group the data by school and count the number of picks
    school_counts = top_5_df.groupby('School').size().sort_values(ascending=False)

    # Print the top 10 schools
    print("Top 10 Schools with Picks in Top 5 Rounds:")
    print(school_counts.head(10))

    # Create a bar chart of the top 10 schools
    top_10_schools = school_counts.head(10)
    plt.bar(top_10_schools.index, top_10_schools.values)
    plt.xticks(rotation=90)
    plt.xlabel('School')
    plt.ylabel('Number of Picks')
    plt.title('Top 10 Schools with Picks in Top 5 Rounds')
    plt.show()

    # Print school and pick count
    print("\nSchool and Pick Count:")
    for school, count in school_counts.head(10).items():
        print(f"{school}: {count}")
    
    return 0

TopSchools()"""
































