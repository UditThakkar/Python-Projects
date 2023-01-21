from art import logo, vs
from data import data
import sys, subprocess
import random

'''
{
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    }
'''

def get_random_person():
    return random.choice(data)

def formated_data(person):
    name = person['name']
    desc = person['description']
    country = person['country']
    return f"{name}, a {desc}, from {country}"

def compare_followers(a,b):
    if a > b:
        return "A"
    else:
        return "B"

def play():
    print(logo)
    personA = get_random_person()
    personB = get_random_person()
    score = 0
    gameOver = False
    while not gameOver:
        personA = personB
        if personA == personB:
            personB = get_random_person()
        print(f"Compare A: {formated_data(personA)} ")
        print(vs)
        print(f"Compare B: {formated_data(personB)} ")
        followerA = personA['follower_count']
        followerB = personB['follower_count']
        print(f"pss followers are here A: {followerA} B: {followerB}")
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        ans = compare_followers(followerA, followerB)
        if guess == ans:
            score += 1
            print(f"You are correct. your current score is {score} ")
            
        else:
            subprocess.run('cls', shell=True)
            print(logo)
            print(f"Your final score is {score} great work!")
            break

while input("Do you want to play Higher or Lower? (y/n): ") == "y":
    subprocess.run('cls', shell=True)
    play()