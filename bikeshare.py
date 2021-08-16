import time
import pandas as pd
import numpy as np
print("Hello , Welcome to to this project")
Cities = ['chicago' , 'new york city', 'washington']
Months = ['january' , 'february', 'march' , 'april' , 'may' , 'june' , "all" ]
Days = ['monday' , 'tuesday', 'wednesday' , 'thursday' , 'friday' , 'saturday' , 'sunday', "all"]
print("and THIS change for Refactoring brach , HELLO")
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True :
        city = input ("Do you want to see the data for chicago, new york  or washington?\n").lower()
        if city not in  CITY_DATA :                                      
            print ("Please choose correct city from the avialable cities list")
        else :
            break
        
    # get user input for month (all, january, february, ... , june)
  
    while True :
        month = input ("choose a Month ! january, ... june or maybe 'all' !! ?\n").lower()
        if month != "all" and month not in  Months :                                      
            print ("incorrect month , please choose suitable month")
        else :
            break

    # get user input for day of week (all, monday, tuesday, ... sunday)
  
    while True :
        day = input ("choose a day ! monday, tuesday, ... sunday also you can choose 'all' too !! \n").lower()
        if day != "all" and day not in  Days :                                      
            print ("Please choose correct day from the avialable days list")
        else :
            break
            
            
    print('-'*40)
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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

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
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    month_mode = df['month'].mode()[0]

    print('Most Popular Month:', month_mode)

    # display the most common day of week
    day_of_week_mode = df['day_of_week'].mode()[0]

    print('Most Day Of Week:', day_of_week_mode)

    # display the most common start hour
    start_hour_mode = df['hour'].mode()[0]

    print('Most Common Start Hour:', start_hour_mode)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]

    print('Most Start Station:', start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]

    print('Most End Station:', end_station)

    # display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    The_combination = group_field.size().sort_values(ascending=False).head(1)
    print('The combination Between Start Station and End Station :\n', The_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    travel_time_sum = df['Trip Duration'].sum()

    print('Sum Travel Time:', travel_time_sum)

    # display mean travel time
    travel_time_mean = df['Trip Duration'].mean()

    print('Mean Travel Time:', travel_time_mean)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type review:')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender review:')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year review:')
        most_common_year = df['Birth Year'].mode()[0]
        print('Common Year:',most_common_year)
        most_recent_year = df['Birth Year'].max()
        print('Recent Year:',most_recent_year)
        earliest_year = df['Birth Year'].min()
        print('earliest Year:',earliest_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def data(df):
    
    raw_data = 0
    while True:
     answer = input("Do you want to see the raw data? Yes or No\n").lower()
     if answer not in ['yes', 'no']:
        answer = input("You wrote the wrong word. Please type Yes or No.\n").lower()
     elif answer == 'yes':
      raw_data += 5
      print(df.iloc[raw_data : raw_data + 5])
      again = input("Do you want to see more? Yes or No\n").lower()
      if again == 'no':
           break
     elif answer == 'no':
       return



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        data(df)
        
        restart = input('\nWould you like to To do ALL that Again ? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()