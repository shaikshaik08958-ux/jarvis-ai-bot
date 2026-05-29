#!/usr/bin/env python3
"""
Jarvis AI Bot - Main Entry Point
A simple voice-activated AI assistant
"""

import sys
from jarvis import JarvisBot

def main():
    print("="*50)
    print("Welcome to Jarvis AI Bot")
    print("="*50)
    print("Starting Jarvis...\n")
    
    jarvis = JarvisBot()
    jarvis.greet()
    
    while True:
        try:
            user_input = input("\nYou: ").strip()
            
            if not user_input:
                continue
            
            # Exit commands
            if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
                jarvis.say("Goodbye! Have a great day!")
                break
            
            # Get response from Jarvis
            response = jarvis.process_command(user_input)
            jarvis.say(response)
            
        except KeyboardInterrupt:
            print("\n\nJarvis shutting down...")
            break
        except Exception as e:
            print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
