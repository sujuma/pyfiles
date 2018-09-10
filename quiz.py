import time
print("Welcome to quiz")
print("Choose one from the multiple choice")

questions = ["A train running at the speed of 60 km/hr crosses a pole in 9 seconds. What is the length of the train?",
      "A train 125 m long passes a man, running at 5 km/hr in the same direction in which the train is going, in 10 seconds. The speed of the train is:",
      "The length of the bridge, which a train 130 metres long and travelling at 45 km/hr can cross in 30 seconds, is:",
      "Two trains running in opposite directions cross a man standing on the platform in 27 seconds and 17 seconds respectively and they cross each other in 23 seconds. The ratio of their speeds is:",
      "A train passes a station platform in 36 seconds and a man standing on the platform in 20 seconds. If the speed of the train is 54 km/hr, what is the length of the platform?",
      "A train 240 m long passes a pole in 24 seconds. How long will it take to pass a platform 650 m long?",
      "Two trains of equal length are running on parallel lines in the same direction at 46 km/hr and 36 km/hr. The faster train passes the slower train in 36 seconds. The length of each train is:",
      "A train 360 m long is running at a speed of 45 km/hr. In what time will it pass a bridge 140 m long?",
      "Two trains are moving in opposite directions @ 60 km/hr and 90 km/hr. Their lengths are 1.10 km and 0.9 km respectively. The time taken by the slower train to cross the faster train in seconds is:",
      "	A jogger running at 9 kmph alongside a railway track in 240 metres ahead of the engine of a 120 metres long train running at 45 kmph in the same direction. In how much time will the train pass the jogger?"]
options = [["120 mtrs","180 mtrs","324 mtrs","150 mtrs"],
           ["45 km/hr","50 km/hr","54 km/hr","55 km/hr"],
           ["200 m","225 m","245 m","250 m"],
           ["1:3","3:2","3:4","None of these"],
           ["120 m","240 m","300 m","None of these"],
           ["65 s","89 s","100 s","150 s"],
           ["50 m","72 m","80 m","82 m"],
           ["40","42","45","48"],
           ["36","45","48","49"],
           ["3.6 s","18 s","36 s","72 s"]]
rightAnswers = ["4","2","3","2","2","2","1","1","3","3"]
points = 0

def run(x):
    print("Q.no",x+1,"...",questions[x])
    print("1. ",options[x][0])
    print("2. ",options[x][1])
    print("3. ",options[x][2])
    print("4. ",options[x][3])
for y in range(0,10):
    run(y)
    answer = input("Answer :  ")
    if(answer == "1" or answer == "2" or answer == "3" or answer == "4"):
        if(answer == rightAnswers[y]):
            points += 1
        else:
            points -= 0.25
    else:
        print("Invalid answer")
print("Points = ",points)


