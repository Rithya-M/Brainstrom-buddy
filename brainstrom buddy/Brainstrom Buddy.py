import random 
# Define lists of story elements 
beginnings = ["Once upon a time", "In a land far away", "Long ago, in a kingdom", "In 
the mystical realm of Eldoria"] 
characters = ["a brave knight", "a wise wizard", "a curious adventurer", "an intrepid explorer", "a 
cunning rogue", "a noble princess"]
actions = ["set out on a quest", "discovered a hidden treasure", "encountered a magical creature", 
"sought the legendary artifact", "journeyed into the unknown", "unveiled a long-forgotten 
prophecy"] 
conflicts = ["a great war", "an evil sorcerer's plot", "a curse upon the land", "a dragon terrorizing 
the kingdom", "a dark force threatening the balance of the world", "a sinister conspiracy unfolding 
in the shadows"] 
endings = ["and they lived happily ever after.", "and the world was never the same again.", "and 
peace was restored to the kingdom.", "and the dawn of a new era began."] 
# Generate a story with a specific character def 
generate_story(character): 
beginning = random. 
choice(beginnings) action = random. 
choice(actions) conflict = random. 
choice(conflicts) ending = random. 
choice(endings) 
8
story = f"{beginning}, {character} {action} to overcome {conflict}, {ending}" 
return story 
# Input names of characters 
characters = input ("Enter names of characters (comma-separated): "). split 
(",") 
# Choose a character for the full story character 
= random. choice(characters) 
# Print the generated story in three 
paragraphs print ("\n Generated Story:") for _ 
in range (16): 
print(generate_story(character)) 
print("\n") 
for _ in range (17): 
print(generate_story(character)) 
print("\n") 
for _ in range (17): 
print(generate_story(character))