"""
Create a Phone class that represents a mobile phone.
The phone should implement a dial method that dials a phone number (or simulates doing so).

Implement a SmartPhone subclass that uses the Phone.dial method
but implements its own run_app method.

Now implement an iPhone subclass that implements not only a run_app method,
but also its own dial method, which invokes the parent’s dial method
but whose output is all in lowercase as a sign of its coolness.
"""

class Phone:
    def __init__(self):
        pass

    def dial(self, number):
        return f'LlAMANDO AL {number}'


class SmartPhone(Phone):
    def run_app(self, app):
        return f'Running app {app}'


class Iphone(SmartPhone):
    def dial(self, number):
        return super().dial(number).lower()



if __name__ == '__main__':
    phone_1 = Phone()
    print(phone_1.dial(658342872))
    phone_2 = SmartPhone()
    print(phone_2.dial(3454323434))
    print(phone_2.run_app('WhatsApp'))
    phone_3 = Iphone()
    phone_3.run_app('WhatsApp')
    print(phone_3.dial(234234234))
