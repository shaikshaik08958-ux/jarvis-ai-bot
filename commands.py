"""
Jarvis AI Bot - Command Handlers
Handles specific utility commands
"""

import random
from datetime import datetime

class CommandHandler:
    def __init__(self):
        self.jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What do you call a fake noodle? An impasta!",
            "Why don't eggs tell jokes? They'd crack each other up!",
            "What did the ocean say to the beach? Nothing, it just waved!",
            "Why did the coffee file a police report? It got mugged!",
            "How does a penguin build its house? Igloos it together!",
            "Why don't skeletons fight each other? They don't have the guts!"
        ]
    
    def get_time(self):
        """Get current time"""
        current_time = datetime.now().strftime("%H:%M:%S")
        return f"The current time is {current_time}"
    
    def get_date(self):
        """Get current date"""
        current_date = datetime.now().strftime("%A, %B %d, %Y")
        return f"Today is {current_date}"
    
    def get_joke(self):
        """Return a random joke"""
        return random.choice(self.jokes)
    
    def flip_coin(self):
        """Flip a coin"""
        result = random.choice(['Heads', 'Tails'])
        return f"Coin flip result: {result}!"
    
    def roll_dice(self):
        """Roll a six-sided dice"""
        result = random.randint(1, 6)
        return f"Dice roll result: {result}!"
