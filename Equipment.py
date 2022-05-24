import random
class Guesser: 
    words = ("tree","mars","class", "scissor", "papper", "rock", "fire" )
    def __init__(self):
        self.random = ''

    def get_ramdom_word(self):
        self.random = self.get_word()

    def get_word(self):
        word = random.choice(self.words)
        return word

    def guess(self,letter):
        indices_of_letter = []
        for i, ch in enumerate(self.random):
            if ch == letter:
                indices_of_letter.append(i)
        temp = indices_of_letter
        return temp

class Equipment:
    #It executes actions/not actions for the jumper
    def __init__(self):
        """ It constructs the parachute and sky diver  to display the results of the game
        """     
        self.parachute= ['  ————\n' , '/ ———— \ \n' , '\      /\n',' \    /']
        self.skydiver= [' 0\n','/|\ \n','/ \ ']
        self.grass='^^^^^^^^'
        self.word=''
        get_word=Guesser()
        self.word=get_word.get_word()
        self.letters=get_word.guess()
        
    def blast_parachute(self,parachute):
        parachute=self.parachute
        if self.word == True:
            parachute.pop(0)
            print (f"Attempts left: {len(parachute)+1}")
        return parachute

    def parachute_safe(self):
        letters=self.letters
        if self.word==False:
            
            pass
        return 
    

# display=Equipment()
# Text_for_Input=input('Write a letter between A-Z')
