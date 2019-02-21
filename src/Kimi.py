import json
import os

DataManager = dict()

def kimiSpeaks(words):
    print("Kimi：{0}".format(words))

class Is:
    subject = "空"
    objectKimi = "空"

    def __init__(self,subject,objectKimi):
        self.subject = subject
        self.objectKimi = objectKimi

for fileName in os.listdir('./knowledge'):
    if '.json' in fileName:
        className = fileName.split('.json')[0]
        DataManager[className] = set()
        # TODO: import file content into DataManager

while True:
    demand = input("你：")
    # TODO: configure which classes this program is sensitive to
    if demand == "exit" :
        break
    elif "是" in demand:
        rawList = demand.split("是")
        realization = Is(rawList[0],rawList[1])
        DataManager[Is.__name__].add(realization)
        kimiSpeaks("我认识到 {0} 是 {1}".format(realization.subject,realization.objectKimi))
        # TODO: anti-duplicate
    else:
        kimiSpeaks("一脸懵逼……")

kimiSpeaks("Saving sessions. Please wait ...")
for classKimi in DataManager:
    f = open("./knowledge/{0}.json".format(classKimi),'w',encoding='utf-8')
    classSet = DataManager.get(classKimi)
    classList = list()
    for instance in classSet:
        classList.append(instance.__dict__)
    f.write(json.dumps(classList,indent=4,ensure_ascii=False))
    f.close()
kimiSpeaks("Sessions saved.")
kimiSpeaks("See you!")
input()