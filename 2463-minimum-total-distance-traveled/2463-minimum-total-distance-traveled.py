class Solution:
    MAX = 10000000000000
    
    def mincost(self, robot: List[int], robo_pos: int, factories: List[int], fact_pos: int, mem: List[List[int]]) -> int:
        if robo_pos < 0:
            return 0  # If all robots are repaired
        if fact_pos < 0:
            return self.MAX  # If some robots are left but factories are over
        if mem[robo_pos][fact_pos] != -1:
            return mem[robo_pos][fact_pos]
        
        include = abs(robot[robo_pos] - factories[fact_pos]) + self.mincost(robot, robo_pos - 1, factories, fact_pos - 1, mem)
        exclude = self.mincost(robot, robo_pos, factories, fact_pos - 1, mem)
        
        mem[robo_pos][fact_pos] = min(include, exclude)
        return mem[robo_pos][fact_pos]
    
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        robot.sort()
        factory.sort()
        
        # Convert multi-instance factory to single instance
        factories = []
        for pos, count in factory:
            factories.extend([pos] * count)
        
        mem = [[-1] * len(factories) for _ in range(len(robot))]
        return self.mincost(robot, len(robot) - 1, factories, len(factories) - 1, mem)
        