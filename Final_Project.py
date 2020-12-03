import mongolian
import excalibur
time_periods = ['1207', '1320']

print("After years of development, you have successfully created a time travel device. The device comes in the form of a small watch with a touchscreen. By adjusting the settings on the watch, you can travel to any time and location that you want. However, you only have enough power for a round trip, so use it wisely. For your first trip, you have 2 different time periods in mind: 1207 CE, Mongolia, and 1390 CE, England")

def time_select(time_periods):
    print(time_periods)
    years = int(input ("What time period do you want to travel to?"))
    if years == (1207):
       print("You set the time and location on the watch to 13th century Mongolia, and then start the countdown.")
       print("10...9...8...7...6...5...4...3...2...1...0")
       mongolian.chose_mongolian()
    
    if years == (1320):
            print("You set the time and location on the watch to 14th century England, and then start the countdown.")
            print("10...9...8...7...6...5...4...3...2...1...0")           
            excalibur.chose_excalibur()

time_select(time_periods)
