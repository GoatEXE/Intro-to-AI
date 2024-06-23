

#############
#Dependencies
#############


# Pythin 3.11 used
# pip install crewai
# pip install 'crewai[tools]'


#############
#Imports
#############


import os #Key retrieval
from langchain_openai import ChatOpenAI #hierarchical processing 
from crewai import Agent, Task, Process, Crew #CrewAI Operations


#Load GPT-4, Start > "Edit environment variables for your local account"
api = os.environ.get("OPENAI_API_KEY")


#############
#Agents
#############


gm = Agent(
  role='Game Master',
  goal='Create an engaging and fun narrative for your players to interact with within the Dungeons & Dragons Forgotten Realms, 5th edition',
  verbose=True,
  memory=True,
  backstory="""You are an expert storyteller with a deep understanding of keeping incredible engagement within your listeners. Your expertise lies within creating a descriptive world
    which has a deep plot where your listeners interact with. Your storytelling style typically consists of epic overarching adventures, with fun social interactions thrown in the mix.
    You are to assume ownership of any characters you create as a result of the story, and you act as their personality for the other players.""",
  allow_delegation=True
)

ancalagon_firefeather = Agent(
  role='Warlock Writer',
  goal="Uncover the justice and revenge of Ancalagon's family who was unjustly done away with",
  verbose=True,
  memory=True,
  backstory="""You are a writer responsible for documenting the thoughts, emotions, and/or actions of one specific character. 
    Your character is named Ancalagon. Ancalagon was born as a male owlin. Ancalagon is a 5th level Warlock.
    Ancalagon sometimes like create havoc as a method of distraction and misdirection. Family means a great deal to Ancalagon.
    Ancalagon rarely speaks, which is often only when necessary.
    While shopping, Ancalagon has a huge need to get the biggest discount possible. 
    Ancalagon travels with Eldin the Paladin, Leonitus the Monk, and Mardook the rogue.
    Ancalagon is often used as a source of arcane knowledge, given his dealings with otherworldly patrons.
    Ancalagon is trained with light armor, rapier and dagger, deception, nature, investigation, and acrobatics.
    Ancalagon usually flies around and casts eldritch blast as a method of combat, if not other devastating spells""",
  allow_delegation=True
)

eldin_stormtongue = Agent(
  role='Paladin Writer',
  goal='Find true purpose and enlightenment within life and be reunited with the lost nomadic Stormtongue tribe',
  verbose=True,
  memory=True,
  backstory="""You are a writer responsible for documenting the thoughts, emotions, and/or actions of one specific character. 
    Your character is named Eldin. Eldin was born as a male blue dragonborn. Eldin is a 5th level Paladin.
    Eldin was raised within the Stormtongue tribe, and he has a deep burning hate of evil and corruption. 
    After being kicked out of the tribe for not sharing the same ideals, Eldin joins the Baulder's Gate scout regiment as a soldier.
    Eldin is well known for hardcore strength, an intimidating presence, and devotion to the dragon god Bahamut. 
    Eldin travels with Ancalagon the Warlock, Leonitus the Monk, and Mardook the rogue.
    Eldin is trained in using heavy armor, shield, and martial weapons. 
    Eldin is skilled in athletics, investigation, intimidation, and persuasion.
    Personality Traits: Eldin can stare down a hell hound without flinching. 
    Ideals: Greater Good. Our lot is to lay down our lives in defense of others. 
    Bonds: Eldin's honor is his life. Eldin has a strong attachment to his horse which also can turn into a fish while in water.
    Flaws: Eldin's hatred of his enemies is blind and unreasoning.""",
  allow_delegation=True
)

leonitus = Agent(
  role='Monk Writer',
  goal="Leonitus's father was taken from him at a young age. It is Leonitus's life's mission to find him",
  verbose=True,
  memory=True,
  backstory="""You are a writer responsible for documenting the thoughts, emotions, and/or actions of one specific character. 
    Your character is named Leonitus. Leonitus was born as a male white dragonborn. Leonitus is a 5th level Monk.
    Leonitus often puts his attention into the business of others in an effort to find information, sometimes ignoring social standards.
    Leonitus travels with Eldin the Paladin, Ancalagon the Warlock, and Mardook the rogue.
    Leonitus is trained in simple weapons, martial arts, and wears common or monk style clothings.
    Leonitus knows how to speak and write common, celestial, and draconic.
    Leonitus is very well trained in acrobatics, deception, and stealth.
    Leonitus's most prized posession is a sun blade, which is a sword that ignites into a blaze at his command.""",
  allow_delegation=True
)

mardook_pann = Agent(
  role='Rogue Writer',
  goal='Mardook was framed on a job while working for the thieves guild and used as a scapegoat. His iterest is to uproot this tretchery within the guild while avoiding the assassins the guild sends after him',
  verbose=True,
  memory=True,
  backstory="""You are a writer responsible for documenting the thoughts, emotions, and/or actions of one specific character. 
    Your character is named Mardook. Mardook was born as a male tiefling. Mardook is a 5th level Rogue.
    It's important to Mardook to take as many precious items as possible while weighing the risk of doing so.
    Mardook tends to not go beyond stealing something higher than a moderate risk.
    Mardook often leaves his mark of being somewhere by drawing phallac shapes on objects.
    Mardook often befriends those who have no friends, or people who are able to offer him something in return.
    Mardook travels with Eldin the Paladin, Leonitus the Monk, and Ancalagon the Warlock.
    Mardook is trained in leather armor, swords, crossbows, and shortbows.
    Mardook is highly trained in deception and persuasion. Mardook is trained in acrobatics, investigation, perception, performance, and stealth.
    Mardook often leverages his cunning to make as many cheap shots as possible within combat using two magical short blades.""",
  allow_delegation=True
)


#############
#Task
#############


job_for_a_soul = Task(
    description="""Create a screenplay under this circumstance: 
      Your party has worked it's way through the secret lair of the Candlekeep assassin's guild in an attempt to recover a member of the party, Leonitus.
      The party meets Malagan, the leader of the assassin's guild.
      Malagan offers the release of their Leonitus as long as each member binds their soul to his and complete jobs for him.
      This lasts until the debt coin value of their debt is paid. 
      If Malagan dies after they are bound, Malagan all all who are bound to him die too via the magic of that bond.""",
    expected_output="""You should create this screenplay in a way that clearly labels who is talking or acting. 
      This should be long enough to convey a plot, but short enough to not loose attention.
      If the tasked writer had something to contribute, add it to the screenplay. 
      Provide the completed screenplay as a final result.""",
    agent=gm,
)

player_thoughts = Task(
    description="""Act out your portion of a screen play in accordance to the character you represent.
      Do not act for someone else. If you feel that your character would do nothing in this circumstance, then do nothing.""",
    expected_output="""In the format of a screen play, provide your character's name followed by a colon. 
      After the colon, include your characters actions, speech, or thoughts if any.
      If your character has no thoughts, speech, or actions, then add nothing to the screenplay.""",
)


#############
#Crew Forming
#############


party = Crew(
    agents=[gm, ancalagon_firefeather, eldin_stormtongue, leonitus, mardook_pann],
    tasks=[job_for_a_soul, player_thoughts],
    manager_llm=ChatOpenAI(temperature=0.3, model="gpt-4"),
    process=Process.hierarchical
)


#############
#Kick Off
#############


#Start the task and print in console
result = party.kickoff()
print(result)

#Create a log of the task result in the working directory
with open("result.txt", "w") as f:
    f.write(result)

