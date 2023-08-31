import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime


def display_full(data_frame: pd.DataFrame):
    pd.set_option("display.max_rows", 73)
    print(data_frame)
    pd.reset_option("display.max_rows")


def get_years(dates: list) -> list:
    unique_dates = set()

    for date in range(len(dates)):
        parsed_date = datetime.strptime(dates[date], "%d-%b-%y")
        year_20xx = parsed_date.strftime("20%y")
        unique_dates.add(year_20xx)

    return sorted(list(unique_dates))


data = pd.read_csv("//GOT_episodes_v4.csv", index_col=0)
duration_df = pd.DataFrame(data["Duration"])

# Inspect the first 10 values
print(duration_df[:10])

'''
In the file dates are represented in the following format: day-month-year (year is cut off)
I decided to extract the year using datetime as it will ensure the convenience
while plotting, for instance (check get_years func)
'''
release_year_data = [i for i in data["Release_date"]]
release_year_data = get_years(release_year_data)

print(release_year_data)

durations = [i for i in data["Duration"]]

# List to store the sum of all episodes by season
durations_sum = []

'''
Calculate the sums of 10 episodes for the first 6 seasons 
(since first 6 seasons have 10 episodes each)
'''
for i in range(0, 60, 10):
    durations_sum.append(sum(durations[i:i+10]))

'''
Calculate the sum of the next 7 episodes for season 7
'''
durations_sum.append(sum(durations[60:67]))

'''
Calculate the sum of the next 6 episodes for season 8
'''
durations_sum.append(sum(durations[67:]))
print(durations_sum)

# Plotting
# Create a figure
fig = plt.figure(figsize=(9, 6))

# Create a plot
plt.plot(release_year_data, durations_sum)

# Create a title
plt.title("Overall duration of seasons of GoT by year")

# Create x-axis and y-axis
plt.xlabel("Year")
plt.ylabel("Overall Duration (in minutes)")

# Add x-axis ticks
plt.xticks(rotation=45)

plt.show()
plt.clf()

'''
Now let's dive deeper and observe each episode's duration of each season
1. Create a list containing sub-lists corresponding to a season
2. Flatten durations (check further code)
3. Define colors for scatter plot
4. Create a scatter plot
'''

'''
1. Create a list containing sub-lists corresponding to a season
'''
# Define a list that shows how many episodes each season has
episodes_per_season = [10, 10, 10, 10, 10, 10, 7, 6]
# Convert "Duration DataFrame" to list
durations_list = data["Duration"].to_list()

'''
Define a list to store sub-lists with durations of each episode
Will contain 8 sub-lists (8 seasons)
'''
each_episode_duration = []

start = 0
for episode_num in episodes_per_season:
    # End will be "stop" in slicing
    end = start + episode_num
    # List of necessary durations
    current_episode_duration = durations_list[start:end]
    # Add this list to "each_episode_duration"
    each_episode_duration.append(current_episode_duration)
    # Change start to end
    start = end


print(each_episode_duration)

'''
2. Flatten durations (check further code)
'''
seasons = [i for i in range(1, 9)]
flattened_durations = [duration for season in each_episode_duration for duration in season]
x_axis_values = [season for season, sublist in zip(seasons, each_episode_duration) for _ in sublist]

'''
3. Define colors for scatter plot
'''
colors = []

for episode_duration in flattened_durations:
    if 70 < episode_duration < 90:
        colors.append("red")
    elif 60 < episode_duration < 75:
        colors.append("orange")
    else:
        colors.append("green")


'''
4. Create a scatter plot
'''
plt.scatter(x_axis_values, flattened_durations, c=colors)
plt.title("Game of Thrones - each episode's duration by season")
plt.xlabel("Season")
plt.ylabel("Episode's duration (in minutes)")
plt.yticks([50, 55, 60, 65, 70, 75, 80], ["50 min", "55 min", "60 min", "65 min", "70 min", "75 min", "80 min"])
plt.show()