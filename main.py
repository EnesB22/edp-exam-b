class Event:
    def __init__(self,payload):
        self.payload = payload
class OrderSubmittedEvent(Event):
    def __init__(self,payload):
        super().__init__(payload)
class OrderRejectedEvent(Event):
    def __init__(self,payload):
        super().__init__(payload)
class Store:
    def __init__(self,name):
        self.name = name
        self.queue =[]
    
    def process_event(self,event):
        if isinstance(event,OrderSubmittedEvent):
            print(f"Processing OrderSubmittedEvent: {event.payload}")
            self.queue.append(event)
        elif isinstance(event, OrderRejectedEvent):
            print(f"Processing OrderRejectedEvent: {event.payload}")
            self.queue.append(event)
        else:
            print("Unknown even type!")
    def show_queue(self):
        print("\nCurrent Event Queue:")
        for event in self.queue:
            print(f"Event: {Type(event).__name__}, Payload: {event.payload}")
class Customer:
    def __init__(self,name):
        self.name = name
    def submit_order(self,store,order_details):
        print(f"{self.name} is submitting an order.")
        event = OrderRejectedEvent(reason)
        store.process_event(event)
