import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv'}
# to be added at the beggining <helper>
Cities = ['chicago', 'new york', 'washington']

Months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

Days = ['saturday', 'sunday', 'monday', 'tuesday',
    'wednesday', 'thursday', 'friday',  'all']
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')


    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
      city = input(
          "Kindly choose a city to filter by? New York , Chicago or Washington?\n")
      if city.lower() not in Cities:
        print("you didn't choose a listed city.")
        continue
      else:
        print('you have chosed : {}'.format(city).title())
        break

# make sure you doesn't need .title() after city <helper>

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
      month=input(
          "Kindly choose a month to filter by? January, February, March, April, May, June or choose all by typing 'all'\n")
      if month.lower() not in Months:
        print("Sorry, you didn't choose a listed month.")
        continue
      else:
        print('you have chosed : {}'.format(month).title())
        break

# TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day=input(
        "kindly choose a Day to filter by? saturday, sunday, monday, tuesday, wednesday, thursday, friday or choose all by typing all\n")
      if day.lower() not in Days:
        print("you didn't choose a listed day.")
      else:
        print("you have chosed : {}".format(day).title())
        break

    print('-' * 40)
    return city, month, day


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

    df = pd.read_csv(CITY_DATA[city.lower()])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        month =  Months.index(month.lower()) + 1
        df = df[ df['month'] == month ]
    if day != 'all':
        df = df[ df['day_of_week'] == day.title()]
    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time=time.time()

    # TO DO: display the most common month
    most_com_month=df['month'].mode()[0]
    print('The most Common Month is: ', most_com_month)
    # TO DO: display the most common day of week
    most_com_day=df['day_of_week'].mode()[0]
    print('The most common day is: ', most_com_day)
    # TO DO: display the most common start hour
    most_com_hour=int(df['hour'].mode())
    print("The most common start hour is: ", most_com_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time=time.time()

    # TO DO: display most commonly used start station
    MCSS=df['Start Station'].mode()[0]
    print("Most common Start Station is: ({})".format(MCSS))

    # TO DO: display most commonly used end station
    MCES=df['End Station'].mode()[0]
    print("Most common End Station is: ({})".format(MCES))

    # TO DO: display most frequent combination of start station and end station trip
    Most_com_comb = df[['Start Station', 'End Station']].mode().loc[0]
    print("Most frequent combination of start station and end station trip: Start: ({}) End: ({})".format(Most_com_comb[0], Most_com_comb[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time=time.time()

    # TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print("Total Travel Time is: {}".format(total_travel_time))

    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('Mean Travel Time is: {}'.format(mean_travel_time))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time=time.time()

    # TO DO: Display counts of user types
    user_types=df.groupby(['User Type']).sum()
    print('User Types\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender_counts=df['Gender'].value_counts()
        print("Gender Counts:")
        print(gender_counts)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        early_year=df['Birth Year'].max()
        late_year=df['Birth Year'].min()
        common_year=df['Birth Year'].mode()
        print('The earliest birth year is: {}'.format(early_year))
        print('The most recent birth year is: {}'.format(late_year))
        print('The most common birth year is: {}'.format(common_year))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)
def display_raw_data(df):
    show_rows = 5
    rows_start = 0
    rows_end = show_rows - 1

    print('Do you like to view some raw data from the current set ?')
    while True:
        raw_data = input('(y or n):')
        if raw_data.lower() == 'y':
            print('Displaying rows {} to {}:'.format(rows_start + 1, rows_end + 1))
            print('\n', df.iloc[rows_start : rows_end + 1])
            rows_start += show_rows
            rows_end += show_rows
            print('Would you like to see the next {} rows?'.format(show_rows))
            continue
        else:
            break

def main():

    while True:
        city, month, day=get_filters()
        df=load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart=input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
