from transitions.extensions import GraphMachine
from random import *

laughing = 0
hunger = 0
confuse = 0
energy = 0

stateID = 'I'
layer = 0

start = 0
charID = 0

#goal of specific character
goal_laughing = 5
goal_hunger = 0
goal_confuse = 0
goal_energy = 5

class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs
        )
        #update.message.reply_text("who you are playing with~~")

    
    ### initialize ###
    if start == 0:
       #update.message.reply_text("who you are playing with~~")
       #update.message.reply_text("4 charactors for you : Shinnosuke, Winnie, Shizuka, Rilakuma")
       global charID
       charID = randint(1,4)
       global goal_laughing
       global goal_hunger
       global goal_confuse
       global goal_energy
       if charID == 1:#Shinnosuke
          goal_laughing = randint(5,8)
          goal_hunger = randint(4,6)
          goal_confuse = randint(0,1)
          goal_energy = randint(0,1)
       elif charID == 2:#Winnie
          goal_laughing = randint(4,6)
          goal_hunger = randint(5,8)
          goal_confuse = randint(2,3)
          goal_energy = randint(0,2)
       elif charID == 3:#Shizuka
          goal_laughing = randint(0,3)
          goal_hunger = randint(0,2)
          goal_confuse = randint(5,8)
          goal_energy = randint(0,5)
       elif charID == 4:#Rilakuma
          goal_laughing = randint(0,3)
          goal_hunger = randint(0,5)
          goal_confuse = randint(0,2)
          goal_energy = randint(5,8)
 
    #def guess(self,update):
#    text = update.message.reply_text
#       if (text == 'Shinnosuke' and charID == 1) or (text =='Winnie' and charID == 2) or (text == 'Shizuka' and charID == 3) or (text == 'Rilakuma' and charID == 4):
#		    update.message.reply_text("guessing correct!!")
			#send picture!!
			#return True
		#charID = randint(1,4)
        #if charID == 1
           


    def goto_L(self, update):
        if layer == 0:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("Ha")
           elif text == 'gaming~~':
              laughing += randint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("yaya")
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
              update.message.reply_text("<3")
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("....zz")
           elif text == 'daydream':
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("...zzzzz")
           elif text == 'attack!':
              global energy
              energy += randint(0,3)
              print('energy = ',energy)
              update.message.reply_text("yah TOT")
        global goal_laughing
        global stateID #remember to change in on_enter!!!
        if laughing >= goal_laughing and stateID == 'I':
           return True
        #text = update.message.text
        #if text == 'goto L':
        #   global laughing
        #   laughing += 1
        #   print('laughing = ' , laughing)
        #if laughing == 3:
        #   return True
        #return laughing == 3 ???
        #return text.lower() == 'go to state1'

    def goto_H(self, update):
        global hunger
        global goal_hunger
        global stateID #remember to change in on_enter!!!
        if hunger >= goal_hunger and stateID == 'I':
           return True
        #text = update.message.text
        #return text.lower() == 'goto h'
    
    def goto_C(self, update):
        global confuse
        global goal_confuse
        global stateID #remember to change in on_enter!!!
        if confuse >= goal_confuse and stateID == 'I':
           return True 
        #text = update.message.text
        #return text.lower() == 'goto c'

    def goto_E(self, update):
        global energy
        global goal_energy
        global stateID #remember to change in on_enter!!!
        if energy >= goal_energy and stateID == 'I':
           return True 
        #text = update.message.text
        #return text.lower() == 'goto s'

    def goto_LH(self, update):
        if layer == 1:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("Ha")
           elif text == 'gaming~~':
              laughing += tandint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("yaya")
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
              update.message.reply_text("<3")
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("....zz")
           elif text == 'daydream':
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("...zzzzz")
           elif text == 'attack!':
              global energy
              energy += randint(0,3)
              print('energy = ',energy)
              update.message.reply_text("yah TOT")
        #global hunger
        global goal_hunger
        #global laughing
        global goal_laughing
        global stateID #remember to change in on_enter!!!
        if (hunger >= goal_hunger and stateID == 'L') or (laughing >= goal_laughing and stateID == 'H'):
           return True 
        #text = update.message.text
        #return text.lower() == 'goto lh'

    def goto_LC(self, update):
        global confuse
        global goal_confuse
        global laughing
        global goal_laughing
        global stateID #remember to change in on_enter!!!
        if (confuse >= goal_confuse and stateID == 'L') or (laughing >= goal_laughing and stateID == 'C'):
           return True
        #text = update.message.text
        #return text.lower() == 'goto lc'

    def goto_LE(self, update):
        global energy
        global goal_energy
        global laughing
        global goal_laughing
        global stateID #remember to change in on_enter!!!
        if (energy >= goal_energy and stateID == 'L') or (laughing >= goal_laughing and stateID == 'E'):
           return True
        #text = update.message.text
        #return text.lower() == 'goto ls'

    def goto_HC(self, update):
        global confuse
        global goal_confuse
        global hunger
        global goal_hunger
        global stateID #remember to change in on_enter!!!
        if (confuse >= goal_confuse and stateID == 'H') or (hunger >= goal_hunger and stateID == 'C'):
           return True
        #text = update.message.text
        #return text.lower() == 'goto hc'

    def goto_HE(self, update):
        global energy
        global goal_energy
        global hunger
        global goal_hunger
        global stateID #remember to change in on_enter!!!
        if (energy >= goal_energy and stateID == 'H') or (hunger >= goal_hunger and stateID == 'E'):
           return True
        #text = update.message.text
        #return text.lower() == 'goto hs'

    def goto_CE(self, update):
        if layer == 1:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("Ha")
           elif text == 'gaming~~':
              laughing += tandint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("yaya")
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
              update.message.reply_text("<3")
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("....zz")
           elif text == 'daydream':
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("...zzzzz")
           elif text == 'attack!':
              global energy
              energy += randint(0,3)
              print('energy = ',energy)
              update.message.reply_text("yah TOT")
        #global energy
        global goal_energy
        #global confuse
        global goal_confuse
        global stateID #remember to change in on_enter!!!
        if (energy >= goal_energy and stateID == 'C') or (confuse >= goal_confuse and stateID == 'E'):
           return True

    def goto_LHC(self, update):
        if (layer == 2) and (stateID == HC):
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("Ha")
           elif text == 'gaming~~':
              laughing += tandint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("yaya")
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
              update.message.reply_text("<3")
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("....zz")
           elif text == 'daydream':
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("...zzzzz")
           elif text == 'attack!':
              global energy
              energy += randint(0,3)
              print('energy = ',energy)
              update.message.reply_text("yah TOT")
        #global confuse
        global goal_confuse
        #global hunger
        global goal_hunger
        #global laughing
        global goal_laughing
        #global stateID #remember to change in on_enter!!!
        if (confuse >= goal_confuse and stateID == 'LH') or (hunger >= goal_hunger and stateID == 'LC') or (laughing >= goal_laughing and stateID == 'HC'):
           return True

    def goto_LHE(self, update):
        if (layer == 2) and (statdID != LE):
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("Ha")
           elif text == 'gaming~~':
              laughing += tandint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("yaya")
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
              update.message.reply_text("<3")
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("....zz")
           elif text == 'daydream':
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("...zzzzz")
           elif text == 'attack!':
              global energy
              energy += randint(0,3)
              print('energy = ',energy)
              update.message.reply_text("yah TOT")
        #global hunger
        global goal_hunger
        #global laughing
        global goal_laughing
        #global energy
        global goal_energy
        if (energy >= goal_energy and stateID == 'LH') or (hunger >= goal_hunger and stateID == 'LE') or (laughing >= goal_laughing and stateID == 'HE'):
           return True

    def goto_LCE(self, update):
        if layer == 2:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("Ha")
           elif text == 'gaming~~':
              laughing += tandint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("yaya")
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
              update.message.reply_text("<3")
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("....zz")
           elif text == 'daydream':
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("...zzzzz")
           elif text == 'attack!':
              global energy
              energy += randint(0,3)
              print('energy = ',energy)
              update.message.reply_text("yah TOT")
        #global laughing
        global goal_laughing
        #global confuse
        global goal_confuse
        #global energy
        global goal_energy
        if (energy >= goal_energy and stateID == 'LC') or (confuse >= goal_confuse and stateID == 'LE') or (laughing >= goal_laughing and stateID == 'CE'):
           return True



    def goto_HCE(self, update):
        global hunger
        global goal_hunger
        global confuse
        global goal_confuse
        global energy
        global goal_energy
        if (energy >= goal_energy and stateID == 'HC') or (confuse >= goal_confuse and stateID == 'HE') or (hunger >= goal_hunger and stateID == 'CE'):
           return True

    def goto_LHCE(self, update):
        if layer == 3:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("Ha")
           elif text == 'gaming~~':
              laughing += tandint(0,3)
              print('laughing = ',laughing)
              update.message.reply_text("yaya")
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
              update.message.reply_text("<3")
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("....zz")
           elif text == 'daydream':
              confuse += randint(0,3)
              print('confuse = ',confuse)
              update.message.reply_text("...zzzzz")
           elif text == 'attack!':
              global energy
              energy += randint(0,3)
              print('energy = ',energy)
              update.message.reply_text("yah TOT")
        #global laughing
        global goal_laughing
        #global hunger
        global goal_hunger
        #global confuse
        global goal_confuse
        #global energy
        global goal_energy
        if (energy >= goal_energy and stateID == 'LHC') or (confuse >= goal_confuse and stateID == 'LHE') or (hunger >= goal_hunger and stateID == 'LCE') or (laughing >= goal_laughing and stateID == 'HCE'):
           return True
    
    def goto_init(self, update):
        global layer
        global charID
        if layer == 4:
           update.message.reply_text("it's final, you got me <3")
           update.message.reply_text("here is a present for you")
           if charID == 1:
              update.message.reply_photo("https://imgur.com/1ysXp7V")#shin
           elif charID == 2:
              update.message.reply_photo("https://imgur.com/i0YvyEH")#winnie
           elif charID == 3:
              update.message.reply_photo("https://imgur.com/Cv3jlMq")#shizuka
           elif charID == 4:
              update.message.reply_photo("https://imgur.com/6uV8ZK9")#rilakuma
           charID = randint(1,4)
           global goal_laughing
           global goal_hunger
           global goal_confuse
           global goal_energy
           if charID == 1:#Shinnosuke
              goal_laughing = randint(5,8)
              goal_hunger = randint(4,6)
              goal_confuse = randint(0,1)
              goal_energy = randint(0,1)
           elif charID == 2:#Winnie
              goal_laughing = randint(4,6)
              goal_hunger = randint(5,8)
              goal_confuse = randint(2,3)
              goal_energy = randint(0,2)
           elif charID == 3:#Shizuka
              goal_laughing = randint(0,3)
              goal_hunger = randint(0,2)
              goal_confuse = randint(5,8)
              goal_energy = randint(0,5)
           elif charID == 4:#Rilakuma
              goal_laughing = randint(0,3)
              goal_hunger = randint(0,5)
              goal_confuse = randint(0,2)
              goal_energy = randint(5,8)

           return True
        else: 
           text = update.message.text
        if (text == 'Shinnosuke' and charID == 1) or (text =='Winnie' and charID == 2) or (text == 'Shizuka' and charID == 3) or (text == 'Rilakuma' and charID == 4):
           update.message.reply_text("correct answer!!")
           update.message.reply_text("here is a present for you")
           if charID == 1:
              update.message.reply_photo("https://imgur.com/1ysXp7V")#shin
           elif charID == 2:
              update.message.reply_photo("https://imgur.com/i0YvyEH")#winnie
           elif charID == 3:
              update.message.reply_photo("https://imgur.com/Cv3jlMq")#shizuka
           elif charID == 4:
              update.message.reply_photo("https://imgur.com/6uV8ZK9")#rilakuma
           charID = randint(1,4)
           #global goal_laughing
           #global goal_hunger
           #global goal_confuse
           #global goal_energy
           if charID == 1:#Shinnosuke
              goal_laughing = randint(5,8)
              goal_hunger = randint(4,6)
              goal_confuse = randint(0,1)
              goal_energy = randint(0,1)
           elif charID == 2:#Winnie
              goal_laughing = randint(4,6)
              goal_hunger = randint(5,8)
              goal_confuse = randint(2,3)
              goal_energy = randint(0,2)
           elif charID == 3:#Shizuka
              goal_laughing = randint(0,3)
              goal_hunger = randint(0,2)
              goal_confuse = randint(5,8)
              goal_energy = randint(0,5)
           elif charID == 4:#Rilakuma
              goal_laughing = randint(0,3)
              goal_hunger = randint(0,5)
              goal_confuse = randint(0,2)
              goal_energy = randint(5,8)
           return True
        else:
           if text == 'Shinnosuke' or text == 'Winnie' or text == 'Shizuka' or text == 'Rilakuma':
              update.message.reply_text("wrong answer~")
              update.message.reply_photo("https://imgur.com/e1RmpQo")
              update.message.reply_text("keep trying!!")
           else:
              print("not guessing")

    def on_enter_goal_L(self, update):
        global stateID
        stateID = 'L'
        global layer
        layer += 1
        update.message.reply_text("state = L")
        #self.go_back(update)

    def on_enter_goal_H(self, update):
        global stateID
        stateID = 'H'
        global layer
        layer += 1
        update.message.reply_text("state = H")

    def on_enter_goal_C(self, update):
        global stateID
        stateID = 'C'
        global layer
        layer += 1
        update.message.reply_text("state = C")

    def on_enter_goal_E(self, update):
        global stateID
        stateID = 'E'
        global layer
        layer += 1
        update.message.reply_text("state = E")

    def on_enter_goal_LH(self, update):
        global stateID
        stateID = 'LH'
        global layer
        layer += 1
        update.message.reply_text("state = LH")

    def on_enter_goal_LC(self, update):
        global stateID
        stateID = 'LC'
        global layer
        layer += 1
        update.message.reply_text("state = LC")

    def on_enter_goal_LE(self, update):
        global stateID
        stateID = 'LE'
        global layer
        layer += 1
        update.message.reply_text("state = LE")

    def on_enter_goal_HC(self, update):
        global stateID
        stateID = 'HC'
        global layer
        layer += 1
        update.message.reply_text("state = HC")

    def on_enter_goal_HE(self, update):
        global stateID
        stateID = 'HE'
        global layer
        layer += 1
        update.message.reply_text("state = HE")

    def on_enter_goal_CE(self, update):
        global stateID
        stateID = 'CE'
        global layer
        layer += 1
        update.message.reply_text("state = CE")

    def on_enter_goal_LHC(self, update):
        global stateID
        stateID = 'LHC'
        global layer
        layer += 1
        update.message.reply_text("state = LHC")

    def on_enter_goal_LHE(self, update):
        global stateID
        stateID = 'LHE'
        global layer
        layer += 1
        update.message.reply_text("state = LHE")

    def on_enter_goal_LCE(self, update):
        global stateID
        stateID = 'LCE'
        global layer
        layer += 1
        update.message.reply_text("state = LCE")

    def on_enter_goal_HCE(self, update):
        global stateID
        stateID = 'HCE'
        global layer
        layer += 1
        update.message.reply_text("state = HCE")

    def on_enter_goal_LHCE(self, update):
        global stateID
        stateID = 'LHCE'
        global layer
        layer += 1
        update.message.reply_text("state = LHCE")
        goto_init(self,update)
        #global charID
        #if charID == 

    def on_enter_init(self,update):
        update.message.reply_text("restart~~")
        global stateID
        stateID = 'I'
        global layer
        layer = 0
        global charID
        charID = randint(1,4)
        global goal_laughing
        global goal_hunger
        global goal_confuse
        global goal_energy
        if charID == 1:#Shinnosuke
           goal_laughing = randint(5,8)
           goal_hunger = randint(4,6)
           goal_confuse = randint(0,1)
           goal_energy = randint(0,1)
        elif charID == 2:#Winnie
           goal_laughing = randint(4,6)
           goal_hunger = randint(5,8)
           goal_confuse = randint(2,3)
           goal_energy = randint(0,2)
        elif charID == 3:#Shizuka
           goal_laughing = randint(0,3)
           goal_hunger = randint(0,2)
           goal_confuse = randint(5,8)
           goal_energy = randint(0,5)
        elif charID == 4:#Rilakuma
           goal_laughing = randint(0,3)
           goal_hunger = randint(0,5)
           goal_confuse = randint(0,2)
           goal_energy = randint(5,8)
		
    #def on_exit_goal_L(self, update):
    #    update.message.reply_text("i'm exiting state1")
    #    print('Leaving state1')


    #def on_exit_goal_H(self, update):
    #    update.message.reply_text("i'm exiting state2")
    #    print('Leaving state2')


    #def on_exit_goal_C(self, update):
    #    update.message.reply_text("i'm exiting state3")
    #    print('Leaving state3')


