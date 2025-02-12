class CommandPublisher:
    _subscribers = []

    @classmethod
    def subscribe(cls, subscriber):
        cls._subscribers.append(subscriber)

    @classmethod
    def unsubscribe(cls, subscriber):
        cls._subscribers.remove(subscriber)

    @classmethod
    def notify(cls, command):
        for subscriber in cls._subscribers:
            subscriber.on_command_received(command)
