class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        position_speed = list(zip(position, speed))
        position_speed.sort(key=lambda x : x[0])
        time_left = [(target-ps[0])/ps[1] for ps in position_speed]
        print(time_left)
        stack = [time_left[-1]]
        n = len(time_left)
        for i in range(n-2,-1,-1):
            if (stack[-1] < time_left[i]):
                    stack.append(time_left[i])
                
        return len(stack)        