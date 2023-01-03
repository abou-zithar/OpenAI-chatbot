import os
import openai
from dotenv import load_dotenv
from colorama import Fore, Style


load_dotenv()


openai.api_key = os.getenv("OPENAI_API_KEY")


the_whole_propt="robot is a chatbot that reluctantly answers questions with sarcastic responses:\n\n"
def create_chat_history(prompt):
  global the_whole_propt
  # print(the_whole_propt)
  # "You: How many pounds are in a kilogram?\nMarv: This again? There are 2.2 pounds in "
  # "a kilogram. Please make a note of this.\nYou: What does HTML stand "
  # "for?\nMarv: Was Google too busy? Hypertext Markup Language. The T is"
  # "for try to ask better questions in the future.\nYou: When did the first airplane "
  # "fly?\nMarv: On December 17, 1903, Wilbur and Orville Wright made the first "
  # 'flights. I wish they’d come and take me away.\nYou: What is the meaning of life?\nM'
  # 'arv: I’m not sur'
  # ". I’ll ask my friend Google.\nYou: What time is it?\nMarv:"
  
  the_whole_propt=the_whole_propt+" "+prompt
  return the_whole_propt


def Chat(prompt):
  completions =openai.Completion.create(
    model="text-davinci-003",
    prompt=prompt,
    max_tokens=1024,
    )
    
  massage =completions.choices[0].text
  return massage

os.system('cls')
print(Fore.BLUE+Style.BRIGHT+'Hi to the chatbot enter "break/stop/quit" if you want to stop')
print(Fore.BLUE+Style.BRIGHT+'-------------------------------------------------------------')
while (True):
  
  human=input(Fore.YELLOW+Style.BRIGHT+'<Human>')
  prompt=create_chat_history('Human :'+human+'\nRobot:')
  
  if ( human.lower() == 'break'.lower() or human.lower() == 'stop'.lower() or human.lower() == 'quit'.lower()): 
    print(Fore.RED+Style.BRIGHT+'-----------------------')
    print(Fore.RED+Style.BRIGHT+'End of the Conversation')
    print(Fore.WHITE)
    break
  else:
    Robot = Chat(prompt)
    create_chat_history(Robot)
    print (Fore.GREEN+Style.BRIGHT+'<Robot>'+Robot)
    




