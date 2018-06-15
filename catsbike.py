import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """

    print('\033[1m' + 'Hello! Let\'s explore some US bikeshare data!' + '\033[0m')
    # get user input for city (chicago, new york city, washington).
    city = ['chicago', 'new york city', 'washington']

    while True:
        city = input(str('\033[1m' + '\nWhich city would you like to see data on?  Chicago, New York City, Washington?\n' + '\033[0m').lower())
        if city in ('chicago', 'new york city', 'washington'):
            break
        else:
            print('Please ensure you wrote in lower case OR we do not have data on that city, please choose one of the three cities listed.')

    # get user input for month (all, january, february, ... , june)
    months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']

    while True:
        month = input(str('\033[1m' + 'Would you like to search by one of the following months?  January, February, March, April, May, June, or all? ' + '\033[0m').lower())
        if month in months:
            break
        else:
            print('We only have data for the first six months, please choose one of the listed months, or choose all.')

    days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # get user input for day of week (all, monday, tuesday, ... sunday)

    while True:
        day = input(str('\033[1m' + '\nWould you like to search by one of the following days?\nSunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or all of them?\n' + '\033[0m').lower())
        if day in days:
            break
        else:
            print('Your answer does not match any of the above options, please try again!\n')


    print('-'*40)
    return (city, month, day)

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    if month != 'all':
        #use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequest times of travel."""

    print('\033[1m' + '\nCalculating the most frequent times of travel...\n' + '\033[0m')
    start_time = time.time()

    """
    Based on the chosen city, month and day, find and prints the most popular
    month
    Arguments:  DataFrame
    Returns:  The most popular month
    """

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    print('\033[1m' + 'Most popular month:' + '\033[0m', popular_month)

    """
    Based on the chosen city, month and day, find and prints the most popular
    day
    Arguments:  DataFrame
    Returns:  Most popular day
    """

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.dayofweek
    popular_day = df['day'].mode()[0]
    print('\033[1m' + 'Most popular day:' + '\033[0m', popular_day)

    """
    Based on the chosen city, month and day, find and prints the most popular
    hour of the day
    Arguments:  DataFrame
    Returns:  Most Popular hour
    """

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('\033[1m' + 'Most Popular Start Hour:' + '\033[0m', popular_hour)

    print("\nThis took %s seconds."%(time.time()-start_time))
    print('-'*40)

def station_stats(df):
    """
    Calculating the most popular stations and trips
    Arguments:  DataFrame
    Returns:  Statistics on the most popular stations and trips.
    """

    print('\033[1m' + 'Calculating the most popular stations and trip...\n' + '\033[0m')
    start_time = time.time()

    # display the most commonly used start station

    start_stn = df['Start Station'].mode()[0]
    print('Most popular start station is {}.'.format(start_stn))

    # display the most commonly used end station

    end_stn = df['End Station'].mode()[0]
    print('Most popular end station is {}.'.format(end_stn))

    # Display the most frequent combination of start and end stations
    df['Most_Common_Trip'] = df["Start Station"]+ " to " + df["End Station"]
    most_common = df['Most_Common_Trip'].mode()[0]
    print('The most common trip is {}.'.format(most_common))

    print("\nThis took %s seconds."%(time.time()-start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip durations."""

    print('\033[1m' + 'Calculating the statistics on the total and average trip durations...\n' + '\033[0m')
    start_time = time.time()

    # display the total travel time

    total_travel_time = df['Trip Duration'].sum()
    m, s = divmod(total_travel_time, 60)
    h, m = divmod(m, 60)

    print('The total travel time is {} hours, {} minutes and {} seconds.'.format(h, m, s))

    # display mean travel time

    mean_travel_time = df['Trip Duration'].mean()
    m, s = divmod(mean_travel_time, 60)
    h, m = divmod(m, 60)

    print('The mean travel time is {} hours, {} minutes and {} seconds.'.format(h, m, s))

    print("\nThis took %s seconds." %(time.time()-start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\033[1m' + 'Calculating User Stats...\n' + '\033[0m')
    start_time = time.time()

    # find the breakdown of user_types
    print('User types:\n')
    user_type = df['User Type'].value_counts()
    print(user_type)

    print("\nThis took %s seconds." %(time.time()-start_time))
    print('-'*40)

    # find the breakdown of gender
def gender_age(df, city):
    """Displays statistics on bikeshare users."""
    #city = get_filters
    if city == 'chicago' or city == 'new york city':
        print('\033[1m' + 'Calculating Gender and Age stats...\n' + '\033[0m')
        start_time = time.time()

        print('\nGender:\n')

        gender = df['Gender'].value_counts()
        print(gender)

    # Display earliest, most recent, and most common year of birth
        print('\nInformation related to Birth Years:\n')
        oldest = int(df['Birth Year'].min())
        youngest = int(df['Birth Year'].max())
        most_common = int(df['Birth Year'].mode())

        print('\nThe oldest users were born in {}.\nThe youngest users were born in {}.'
              '\nMost users were born in {}.'.format(oldest, youngest, most_common))

        print("\nThis took %s seconds." %(time.time()-start_time))
        print('-'*40)

def display_data(df):
    '''Displays five lines of data if the user specifies that they would like to.
    After displaying five lines, ask the user if they would like to see five more.
    Continues asking until they say stop.
    Arguments:  DataFrame
    Returns:  If the user says yes then this function returns the next five lines
              of the dataframe and then asks the question again by calling this
              function again.  If the user says no then this function returns,
              but without any value
    '''
    first = 0
    last = 5
    while True:
        display = input('\033[1m' + '\nWould you like to view individual trip data? '
                        'Type in lowercase \'yes\' or \'no\'.\n' + '\033[0m')
        if display == 'no':
            break
        elif display == 'yes':
            print(df[df.columns[0:-1]].iloc[first:last])
        while True:
            display_more = input('\033[1m' + '\nWould you like to view more individual'
                                 ' trip data? Type \'yes\' or \'no\'.\n' + '\033[0m')
            if display_more == 'no':
                break
            elif display_more == 'yes':
                first += 5
                last += 5
                print(df[df.columns[0:-1]].iloc[first:last])
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        gender_age(df, city)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()
