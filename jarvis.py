"""
Jarvis AI Bot - Core Logic
Handles AI responses and commands
"""

import random
from datetime import datetime
from commands import CommandHandler

class JarvisBot:
    def __init__(self):
        self.name = "Jarvis"
        self.command_handler = CommandHandler()
        self.responses = {
            'greeting': [
                "Hello sir! Ready to assist you.",
                "Welcome back! How can I help?",
                "At your service, sir!"
            ],
            'confused': [
                "I didn't quite understand that. Could you rephrase?",
                "Sorry, I'm not sure what you mean.",
                "I didn't catch that. Try again?"
            ]
        }
    
    def greet(self):
        """Greet the user"""
        greeting = random.choice(self.responses['greeting'])
        self.say(greeting)
    
    def say(self, message):
        """Output a message from Jarvis"""
        print(f"\nJarvis: {message}")
    
    def process_command(self, user_input):
        """Process user input and return response"""
        user_input_lower = user_input.lower().strip()
        
        # Check for specific commands
        if any(word in user_input_lower for word in ['time', 'what time']):
            return self.command_handler.get_time()
        
        elif any(word in user_input_lower for word in ['date', 'what date', 'today']):
            return self.command_handler.get_date()
        
        elif any(word in user_input_lower for word in ['hello', 'hi', 'hey', 'greet']):
            return "Hello! How can I assist you today?"
        
        elif any(word in user_input_lower for word in ['joke', 'make me laugh', 'funny']):
            return self.command_handler.get_joke()
        
        elif any(word in user_input_lower for word in ['who are you', 'your name', 'what is your name']):
            return f"I am {self.name}, your AI assistant. Nice to meet you!"
        
        elif any(word in user_input_lower for word in ['help', 'what can you do', 'commands']):
            return self.get_help()
        
        elif any(word in user_input_lower for word in ['weather', 'temperature', 'outside']):
            return "I don't have weather access yet, but you can check weather.com"
        
        elif any(word in user_input_lower for word in ['calculate', 'math', 'add', 'subtract', 'multiply', 'divide']):
            return self.handle_math(user_input)
        
        elif any(word in user_input_lower for word in ['flip coin', 'coin toss', 'heads or tails']):
            return self.command_handler.flip_coin()
        
        elif any(word in user_input_lower for word in ['roll dice', 'roll die']):
            return self.command_handler.roll_dice()
        
        else:
            # Generate a generic response
            return self.generate_response(user_input)
    
    def handle_math(self, expression):
        """Handle basic math calculations"""
        try:
            # Remove common words
            math_expr = expression.lower()
            math_expr = math_expr.replace('calculate', '').replace('what is', '').replace('compute', '')
            
            # Simple evaluation (be careful with eval in production!)
            result = eval(math_expr)
            return f"The answer is {result}"
        except:
            return "I couldn't calculate that. Try asking differently."
    
    def generate_response(self, user_input):
        """Generate a generic response"""
        responses = [
            f"Interesting point about '{user_input}'. Tell me more?",
            f"That's an interesting thought. Can you elaborate?",
            "I'm learning. Can you help me understand better?",
            "That's fascinating! What else would you like to know?",
            "I see. Is there anything else I can help you with?"
        ]
        return random.choice(responses)
    
    def get_help(self):
        """Show available commands"""
        help_text = """
        I can help you with:
        - Time & Date (ask 'what time is it' or 'what's today')
        - Jokes (say 'tell me a joke')
        - Math (say 'calculate 5 + 3')
        - Coin flips (say 'flip a coin')
        - Dice rolls (say 'roll a dice')
        - General questions
        - Exit (say 'exit' or 'quit')
        """
        return help_text
