import mongolian
time_periods = ['1207']

def time_select(time_periods):
    print(time_periods)
    years = int(input ("You are a time traveler, where do you wish to go?"))
    if years == (1207):
        print("Welcome to the Mongolian period")
        mongolian.chose_mongolian()

time_select(time_periods)
