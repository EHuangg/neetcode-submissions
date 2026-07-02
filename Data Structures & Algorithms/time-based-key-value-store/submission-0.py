class TimeMap:

    def __init__(self):
        # name: bucket (list)
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        curr = ""
        history = self.hashmap[key]
        for i in range(len(history)):
            time = history[i][0]
            value = history[i][1]
            if time <= timestamp:
                curr = value
        return curr
            
            
        
        
