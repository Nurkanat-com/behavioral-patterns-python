# ==========================================
# 1. ITERATOR
# ==========================================

class NumberCollection:
    def __init__(self, numbers):
        self.numbers = numbers

    def __iter__(self):
        return NumberIterator(self.numbers)


class NumberIterator:
    def __init__(self, numbers):
        self.numbers = numbers
        self.index = 0

    def __next__(self):
        if self.index >= len(self.numbers):
            raise StopIteration

        value = self.numbers[self.index]
        self.index += 1
        return value


print("1. ITERATOR")

collection = NumberCollection([10, 20, 30, 40])

for number in collection:
    print(number)


# ==========================================
# 2. OBSERVER
# ==========================================

class Subscriber:
    def __init__(self, name):
        self.name = name

    def update(self, message):
        print(f"{self.name} received: {message}")


class YouTubeChannel:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, message):
        for subscriber in self.subscribers:
            subscriber.update(message)


print("\n2. OBSERVER")

channel = YouTubeChannel()

user1 = Subscriber("Arman")
user2 = Subscriber("Ali")

channel.subscribe(user1)
channel.subscribe(user2)

channel.notify("New video uploaded!")


# ==========================================
# 3. STRATEGY
# ==========================================

class CardPayment:
    def pay(self, amount):
        print(f"Paid {amount}$ by Card")


class CashPayment:
    def pay(self, amount):
        print(f"Paid {amount}$ by Cash")


class CryptoPayment:
    def pay(self, amount):
        print(f"Paid {amount}$ by Crypto")


class PaymentSystem:
    def __init__(self, strategy):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


print("\n3. STRATEGY")

payment = PaymentSystem(CardPayment())
payment.pay(100)

payment.set_strategy(CashPayment())
payment.pay(50)

payment.set_strategy(CryptoPayment())
payment.pay(200)


# ==========================================
# 4. CHAIN OF RESPONSIBILITY
# ==========================================

class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    def handle(self, request):
        if self.next_handler:
            return self.next_handler.handle(request)


class LowLevelSupport(Handler):
    def handle(self, request):
        if request == "simple":
            print("Low Level Support solved the problem")
        else:
            super().handle(request)


class MiddleLevelSupport(Handler):
    def handle(self, request):
        if request == "medium":
            print("Middle Level Support solved the problem")
        else:
            super().handle(request)


class HighLevelSupport(Handler):
    def handle(self, request):
        if request == "hard":
            print("High Level Support solved the problem")
        else:
            print("Nobody can solve the problem")


print("\n4. CHAIN OF RESPONSIBILITY")

low = LowLevelSupport()
middle = MiddleLevelSupport()
high = HighLevelSupport()

low.set_next(middle).set_next(high)

low.handle("simple")
low.handle("medium")
low.handle("hard")


# ==========================================
# 5. COMMAND
# ==========================================

class Light:
    def turn_on(self):
        print("Light is ON")

    def turn_off(self):
        print("Light is OFF")


class TurnOnCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_on()


class TurnOffCommand:
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.turn_off()


class RemoteControl:
    def execute_command(self, command):
        command.execute()


print("\n5. COMMAND")

light = Light()

turn_on = TurnOnCommand(light)
turn_off = TurnOffCommand(light)

remote = RemoteControl()

remote.execute_command(turn_on)
remote.execute_command(turn_off)
