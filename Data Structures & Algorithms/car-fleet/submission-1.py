class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        cars = [(p, s) for p, s in zip(position, speed)]
        cars.sort(reverse=True)

        for pos,spd in cars:
            hours_driving = (target - pos) / spd
            stack.append(hours_driving)
            print(stack)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return (len(stack))