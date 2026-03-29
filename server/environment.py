from openenv.core import BaseEnv

class CustomEnvironment(BaseEnv):
    def __init__(self):
        super().__init__()
        
    def reset(self):
        print("Environment Reset")
        return {}
        
    def step(self, action):
        print(f"Action taken: {action}")
        return {}
