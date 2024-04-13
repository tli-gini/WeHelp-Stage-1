# Task 1
# We just received messages from 5 friends in JSON format, and we want to take the green
# line, including Xiaobitan station, of Taipei MRT to meet one of them. Write code to find out
# the nearest friend and print name, based on any given station currently located at and
# station count between two stations.
print("===== Task 1 =====")

def find_and_print(messages, current_station):
    stations_order = [
        [
            "Songshan", "Nanjing Sanmin", "Taipei Arena", "Nanjing Fuxing",
            "Songjiang Nanjing", "Zhongshan", "Beimen", "Ximen", "Xiaonanmen",
            "Chiang Kai-Shek Memorial Hall", "Guting", "Taipower Building",
            "Gongguan", "Wanlong", "Jingmei", "Dapinglin", "Qizhang",
            "Xindian City Hall", "Xindian"
        ],
        [
            "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "",
            "Xiaobitan", "", ""
        ]
    ]

    def find_station_position(station_name):
        for y, line in enumerate(stations_order):
            for x, station in enumerate(line):
                if station == station_name:
                    return x, y
        return -1, -1

    current_station_index = find_station_position(current_station)

    closest_friend = ""
    closest_distance = float('inf')

    for name, message in messages.items():
        for station in sum(stations_order, []):  
            if station and station in message:
                friend_index = find_station_position(station)
                distance = abs(current_station_index[0] - friend_index[0]) + \
                           abs(current_station_index[1] - friend_index[1])

                if distance < closest_distance:
                    closest_distance = distance
                    closest_friend = name

    print(closest_friend)

messages = {
    "Leslie": "I'm at home near Xiaobitan station.",
    "Bob": "I'm at Ximen MRT station.",
    "Mary": "I have a drink near Jingmei MRT station.",
    "Copper": "I just saw a concert at Taipei Arena.",
    "Vivian": "I'm at Xindian station waiting for you."
}

find_and_print(messages, "Wanlong")  # print Mary
find_and_print(messages, "Songshan")  # print Copper
find_and_print(messages, "Qizhang")  # print Leslie
find_and_print(messages, "Ximen")  # print Bob
find_and_print(messages, "Xindian City Hall")  # print Vivian


# Task 2
# Assume we have consultants for consulting services. Help people book the best matching
# consultant in a day, based on hours, service durations, and selection criteria.
# 1. Booking requests are one by one, order matters.
# 2. A consultant is only available if there is no overlapping between already booked time
#    and an incoming request time.
# 3. If the criteria is "price", choose the available consultant with the lowest price.
# 4. If the criteria is "rate", choose the available consultant with the highest rate.
# 5. If every consultant is unavailable, print "No Service".
print("===== Task 2 =====")

schedule = {}

def book(consultants, hour, duration, criteria):
    global schedule
    available_consultants = []

    for consultant in consultants:
        available = True
        for j in range(hour, hour + duration):
            if consultant['name'] in schedule and j in schedule[consultant['name']]:
                available = False
                break
        if available:
            available_consultants.append(consultant)

    if criteria == "price":
        available_consultants.sort(key=lambda x: x['price'])
    elif criteria == "rate":
        available_consultants.sort(key=lambda x: x['rate'], reverse=True)

    if not available_consultants:
        print("No Service")
        return

    your_consultant = available_consultants[0]
    if your_consultant['name'] not in schedule:
        schedule[your_consultant['name']] = {}
    for i in range(hour, hour + duration):
        schedule[your_consultant['name']][i] = True

    print(your_consultant['name'])

consultants = [
    {"name": "John", "rate": 4.5, "price": 1000},
    {"name": "Bob", "rate": 3, "price": 1200},
    {"name": "Jenny", "rate": 3.8, "price": 800},
]

book(consultants, 15, 1, "price")  # Jenny
book(consultants, 11, 2, "price")  # Jenny
book(consultants, 10, 2, "price")  # John
book(consultants, 20, 2, "rate")  # John
book(consultants, 11, 1, "rate")  # Bob
book(consultants, 11, 2, "rate")  # No Service
book(consultants, 14, 3, "price")  # John


# Task 3
# Find out whose middle name is unique among all the names, and print it. You can assume
# every input is a Chinese name with 2 ~ 5 words. If there are only 2 words in a name, the
# middle name is defined as the second word. If there are 4 words in a name, the middle name
# is defined as the third word.
print("===== Task 3 =====")

def func(*data):
    words_list = {}

    for index, str in enumerate(data):
        if len(str) in [2, 3]:
            middle_name = str[1]
        elif len(str) in [4, 5]:
            middle_name = str[2]
        else:
            middle_name = None

        if middle_name not in words_list:
            words_list[middle_name] = []

        words_list[middle_name].append(index)

    unique_index = []
    for word in words_list:
        if len(words_list[word]) == 1:
            unique_index.append(words_list[word][0])

    if len(unique_index) == 0:
        print("沒有")
    else:
        for i in unique_index:
            print(data[i])


func("彭大牆", "陳王明雅", "吳明")  # print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花")  # print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花")  # print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆")  # print 夏曼藍波安


# Task 4
# There is a number sequence: 0, 4, 8, 7, 11, 15, 14, 18, 22, 21, 25, …
# Find out the nth term in this sequence.
print("===== Task 4 =====")

def get_number(index):
    a = 0
    for i in range(1, index + 1):
        if i % 3 == 0:
            a -= 1
        else:
            a += 4
    print(a)

get_number(1)  # print 4
get_number(5)  # print 15
get_number(10) # print 25
get_number(30) # print 70