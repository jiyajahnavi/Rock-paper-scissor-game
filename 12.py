#rock paper scissor game
import random

print("Welcome to rock paper scissor game\n\n")
user = int(input("choose number for rock(0),paper(1),scissor(2)\n"))
comp = random.randint(0,2)

#0 for rock,1 for paper,2 for scissor
if (comp==0 and user== 0):
    print("Match draw\ncomputer choosed rock\nyou choosed rock")
elif (comp==1 and user== 1):
    print("Match draw\ncomputer choosed paper\nyou choosed paper")
elif (comp==2 and user== 2):
    print("Match draw\ncomputer choosed scissor\nyou choosed scissor")
elif (comp==0 and user==1):
    print("You won\ncomputer choosed rock\nyou choosed paper")
elif (comp==0 and user==2):
    print("You loose\ncomputer choosed rock\nyou choosed scissor")
elif (comp==1 and user==2):
    print("You won\ncomputer choosed paper\nyou choosed scissor")
elif (comp==1 and user==0):
    print("You loose\ncomputer choosed paper\nyou choosed rock")
elif (comp==2 and user==1):
    print("You loose\ncomputer choosed scissor\nyou choosed paper")
elif (comp==2 and user==0):
    print("You won\ncomputer choosed scissor\nyou choosed rock")
    
    print("\n\nTHANK YOU")