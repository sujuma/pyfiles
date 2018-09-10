import time
print("Welcome to the Aptitute quiz")
print("\n")
print("Choose one option from the answers and each carry one point")
print("There are ten questions and 0.25 negative mark for each wrong answer")
questions = ["The train having speed of 50m/s, crossing a man at 5 seconds, what is the length of train? ",
             "A train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train? ",
             "A train 125 m long passes a man, running at 5 km/hr in the same direction in which the train is going, in 10 seconds. The speed of the train is: ",
             "The length of the bridge, which a train 130 metres long and travelling at 45 km/hr can cross in 30 seconds, is: ",
             "Two trains running in opposite directions cross a man standing on the platform in 27 seconds and 17 seconds respectively and they cross each other in 23 seconds. The ratio of their speeds is:",
             "A train passes a station platform in 36 seconds and a man standing on the platform in 20 seconds. If the speed of the train is 54 km/hr, what is the length of the platform?",
             "A train 240 m long passes a pole in 24 seconds. How long will it take to pass a platform 650 m long? ",
             "Two trains of equal length are running on parallel lines in the same direction at 46 km/hr and 36 km/hr. The faster train passes the slower train in 36 seconds. The length of each train is: ",
             "A train 360 m long is running at a speed of 45 km/hr. In what time will it pass a bridge 140 m long?",
             "Two trains are moving in opposite directions @ 60 km/hr and 90 km/hr. Their lengths are 1.10 km and 0.9 km respectively. The time taken by the slower train to cross the faster train in seconds is:",
             "A jogger running at 9 kmph alongside a railway track in 240 metres ahead of the engine of a 120 metres long train running at 45 kmph in the same direction. In how much time will the train pass the jogger?"]
options = [["120","180","250","400"],["120","180","324","150"]]
for i in range(len(questions)):
    print(questions[i])
    for j in options:
        print(options[j])
    
    
