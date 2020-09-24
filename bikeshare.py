import time
import pandas as pd
import numpy as np

#Step 1: ------------------------------------------

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters(city, month, day):
    """
    Asks user to specify a city, month, and day. User answers will determine analysis.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    cities: ['Chicago','New York City','Washington']
    months: ['January', 'February', 'March', 'April', 'May', 'June']
    days:{'M':'Monday', 'T': 'Tuesday', 'W':'Wednesday', 'Th':'Thursday', 'F':'Friday'}
    # TO DO: get user input for city (chicago, new york city, washington).
    #HINT: Use a while loop to handle invalid inputs


    while True:
        city = input('Which of these cities do you want to explore : Chicago, New York or Washington? \n> ').lower()

        if city not in CITY_DATA:
            print("\nInvalid answer\n")
            continue
        else:
<<<<<<< HEAD
          print('I am sorry, I did not catch that. Please type your answer again')

||||||| merged common ancestors
          print('I am sorry, I did not catch that. Please type your answer again')

=======
            break

>>>>>>> refactoring

    # TO DO: get user input for month (all, january, february, ... , june)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        time = input('Would you like to filter the data by month, day, both, or not at all? Type "none" for no time filter.').lower()
        if time == 'month':
          month = input('Which month? January, February , March , April , May , or June?').lower()
          break

        elif time == 'day':
          day = input('Which day? Please type your response as a letter value. (M , T, W, Th, F, Sa, Su)').lower()
          break

        elif time == 'both':
          month = input('Which month? January, February , March , April , May , or June?').lower()
          day = input('Which day? Please type your response as a letter value. (M , T, W, Th, F, Sa, Su)').lower()
          break

        elif time == 'none':
          break

        else:
            input('I am sorry, I did not catch that. Please type your answer again').lower()
            break


    print('-'*40)
    return city, month, day

#Step2: --------------------------------------------------------------------------------


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

     # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

      # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


  #Step3: -----------------------------------------------------------------------
   # print('Would like to see the raw data of your selected filters? -Yes or No')
   # print('Would like to see 5 more rows of the data?')
   
    def raw_data(df):
        """Displays 5 lines of raw data upon request by the user."""
        i=0
        user_question=input('Would you like to see the raw data?\ntpye yes or no').lower()
    while user_question in ['yes','y','yep','yea'] and i+5 < df.shape[0]:
        print(df.iloc[i:i+5])
        i += 5
        user_question = input('Would you like to see more data? Please enter yes or no:').lower()

#Step4: ------------------------------------------------------------

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print(df.to_string())
    common_month = df['month'].mode()
    print(common_month)
    print('The most common month to cycle is: {}'.format(common_month))

    # TO DO: display the most common day of week
    common_dow = df['day_of_week'].dt.week.mode().index[0]
    print('The most common day of the week to cycle is: {}'.format(common_dow))

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode().index[0]
    print('The most common hour of the day to cycle is: {}'.format(common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#Step5: ---------------------------------------------------------------------

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start station'].mode().index[0]
    print('The most commonly used start station is: {}'.format(common_start))

    # TO DO: display most commonly used end station
    common_end = df['End station'].mode().index[0]
    print('The most commonly used end station is: {}'.format(commen_end))

    # TO DO: display most frequent combination of start station and end station trip
    combination = df['Start station','End station'].mode().index[0]
    print('The most frequent combination of start and end station is: {}'.format(combination))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


#Step6: -------------------------------------------------------------------------------

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum
    print('The total travel time is: {}'.format(total_time))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean
    print('The mean travel time is: {}'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


  #Step7:--------------------------------------------------------------------

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types: {}'.format(user_types))

    # TO DO: Display counts of gender
    if 'Gender' in df:
     gender = df['Gender'].value_counts()
     print('Male: {}, Female: {}'.format(gender.loc['Male'], gender.loc['Female']))
    else:
     print('There is no gender data for this city.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
     oldest_age_user = df['Birth Year'].min()
     youngest_age_user = df['Birth Year'].max()
     majority_age_user = df['Birth Year'].mode()
     print('The oldest user is: {}'.format(oldest_age_user))
     print('The youngest user is: {}'.format(youngest_age_user))
     print('The majority of users are: {}'.format(majority_age_user))

    else:
     print('There is no birth year data for this city.')

     print("\nThis took %s seconds." % (time.time() - start_time))
     print('-'*40)

  #Step8: -----------------------------------------------------------------------

def main():
    city = ""
    month = 0
    day = 0
    while True:
        city, month, day = get_filters(city, month, day)
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
