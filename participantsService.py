import urllib.request, json
from participant import Participant

class ParticipantsService:
    def __init__(self):
        return
    
    def getMockedUsers(self, mockedUsersList):
        url = "https://raw.githubusercontent.com/lukelima/hackathon-shawee/feature/mocked-data/mockedData.json?token=AK6HG2EB6YNZKLHODF7SAYS5RLDCU"
        response = urllib.request.urlopen(url)
        mockedUsersList.append(json.loads(response.read()))
        print(mockedUsersList)

    