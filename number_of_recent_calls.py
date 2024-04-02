class RecentCounter:

    def __init__(self):
        self.pings = []

    def ping(self, t: int) -> int:
        ranges = (t - 3000, t)
        self.pings.append(t)
        count = 0
        for p in self.pings:
            if p >= ranges[0] and p <= ranges[1]:
                count += 1
        return count


obj = RecentCounter()
param_1 = obj.ping(1)
param_2 = obj.ping(100)
param_3 = obj.ping(3001)
param_4 = obj.ping(3002)
print(param_1, param_2, param_3, param_4)