import requests



class Model:
    def __init__(self):
        self.url="https://transmit-checkout-absence-states.trycloudflare.com/api/"
    def get_req(self,q):
        self.data=requests.get(self.url,params={"q":q})
        return self.data.json()

