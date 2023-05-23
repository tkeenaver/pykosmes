from random import randint

class Die:
    """A class representing a single die."""
    
    def __init__(self, num_sides=6):
        """Assume a six-sided die."""
        self.num_sides = num_sides
        
    def roll(self):
        """"Return a random value between 1 and number of sides."""
        return randint(1, self.num_sides)

if __name__ == '__main__':
    print('\n이 파일은 class Die의 구현 부분이며, 단순 실행코드는 없습니다.\n')
