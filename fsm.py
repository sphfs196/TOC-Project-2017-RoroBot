from transitions.extensions import GraphMachine
from random import *

laughing = 0
hunger = -10
confuse = -10
sadness = 0

stateID = 'I'
layer = 0

start = 0
charID = 0

#goal of specific character
goal_laughing = 5
goal_hunger = 0
goal_confuse = 0
goal_sadness = 5

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
       global goal_sadness
       if charID == 1:#Shinnosuke
          goal_laughing = randint(5,8)
          goal_hunger = randint(4,6)
          goal_confuse = randint(0,1)
          goal_sadness = randint(0,1)
       elif charID == 2:#Winnie
          goal_laughing = randint(4,6)
          goal_hunger = randint(5,8)
          goal_confuse = randint(2,3)
          goal_sadness = randint(0,2)
       elif charID == 3:#Shizuka
          goal_laughing = randint(0,3)
          goal_hunger = randint(0,2)
          goal_confuse = randint(5,8)
          goal_sadness = randint(0,5)
       elif charID == 4:#Rilakuma
          goal_laughing = randint(0,3)
          goal_hunger = randint(0,5)
          goal_confuse = randint(0,2)
          goal_sadness = randint(5,8)
 
    #def guess(self,update):
        #text = update.message.reply_text
        #charID = randint(1,4)
        #if charID == 1
           


    def goto_L(self, update):
        if layer == 0:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(1,3)
              print('laughing = ',laughing)
              update.message.reply_text("Ha")
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
           elif text == 'attack!':
              global sadness
              sadness += randint(0,3)
              print('sadness = ',sadness)
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

    def goto_S(self, update):
        global sadness
        global goal_sadness
        global stateID #remember to change in on_enter!!!
        if sadness >= goal_sadness and stateID == 'I':
           return True 
        #text = update.message.text
        #return text.lower() == 'goto s'

    def goto_LH(self, update):
        if layer == 1:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(1,3)
              print('laughing = ',laughing)
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
           elif text == 'attack!':
              global sadness
              sadness += randint(0,3)
              print('sadness = ',sadness)
        #global hunger
        global goal_hunger
        #global laughing
        global goal_laughing
        global stateID #remember to change in on_enter!!!
        if (hunger >= goal_laughing and stateID == 'L') or (laughing >= goal_laughing and stateID == 'H'):
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

    def goto_LS(self, update):
        global sadness
        global goal_sadness
        global laughing
        global goal_laughing
        global stateID #remember to change in on_enter!!!
        if (sadness >= goal_sadness and stateID == 'L') or (laughing >= goal_laughing and stateID == 'S'):
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

    def goto_HS(self, update):
        global sadness
        global goal_sadness
        global hunger
        global goal_hunger
        global stateID #remember to change in on_enter!!!
        if (sadness >= goal_sadness and stateID == 'H') or (hunger >= goal_hunger and stateID == 'S'):
           return True
        #text = update.message.text
        #return text.lower() == 'goto hs'

    def goto_CS(self, update):
        if layer == 1:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(1,3)
              print('laughing = ',laughing)
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
           elif text == 'attack!':
              global sadness
              sadness += randint(0,3)
              print('sadness = ',sadness)
        #global sadness
        global goal_sadness
        #global confuse
        global goal_confuse
        global stateID #remember to change in on_enter!!!
        if (sadness >= goal_sadness and stateID == 'C') or (confuse >= goal_confuse and stateID == 'S'):
           return True

    def goto_LHC(self, update):
        if layer == 2:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(1,3)
              print('laughing = ',laughing)
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
           elif text == 'attack!':
              global sadness
              sadness += randint(0,3)
              print('sadness = ',sadness)
        #global confuse
        global goal_confuse
        #global hunger
        global goal_hunger
        #global laughing
        global goal_laughing
        global stateID #remember to change in on_enter!!!
        if (confuse >= goal_confuse and stateID == 'LH') or (hunger >= goal_hunger and stateID == 'LC') or (laughing >= goal_laughing and stateID == 'HC'):
           return True

    def goto_LHS(self, update):
        if layer == 2:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(1,3)
              print('laughing = ',laughing)
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
           elif text == 'attack!':
              global sadness
              sadness += randint(0,3)
              print('sadness = ',sadness)
        #global hunger
        global goal_hunger
        #global laughing
        global goal_laughing
        #global sadness
        global goal_sadness
        if (sadness >= goal_sadness and stateID == 'LH') or (hunger >= goal_hunger and stateID == 'LS') or (laughing >= goal_laughing and stateID == 'HS'):
           return True

    def goto_LCS(self, update):
        global laughing
        global goal_laughing
        global confuse
        global goal_confuse
        global sadness
        global goal_sadness
        if (sadness >= goal_sadness and stateID == 'LC') or (confuse >= goal_confuse and stateID == 'LS') or (laughing >= goal_laughing and stateID == 'CS'):
           return True



    def goto_HCS(self, update):
        global hunger
        global goal_hunger
        global confuse
        global goal_confuse
        global sadness
        global goal_sadness
        if (sadness >= goal_sadness and stateID == 'HC') or (confuse >= goal_confuse and stateID == 'HS') or (hunger >= goal_hunger and stateID == 'CS'):
           return True

    def goto_LHCS(self, update):
        if layer == 3:
           text = update.message.text
           if text == 'itching':
              global laughing
              laughing += randint(1,3)
              print('laughing = ',laughing)
           elif text == 'eating':
              global hunger
              hunger += randint(0,3)
              print('hunger = ',hunger)
           elif text == 'sleeping':
              global confuse
              confuse += randint(0,3)
              print('confuse = ',confuse)
           elif text == 'attack!':
              global sadness
              sadness += randint(0,3)
              print('sadness = ',sadness)        
        #global laughing
        global goal_laughing
        #global hunger
        global goal_hunger
        #global confuse
        global goal_confuse
        #global sadness
        global goal_sadness
        if (sadness >= goal_sadness and stateID == 'LHC') or (confuse >= goal_confuse and stateID == 'LHS') or (hunger >= goal_hunger and stateID == 'LCS') or (laughing >= goal_laughing and stateID == 'HCS'):
           return True
    
    #def goto_init(self, update):
    #    text = update.message.text
    #    return text.lower() == 'go back'

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

    def on_enter_goal_S(self, update):
        global stateID
        stateID = 'S'
        global layer
        layer += 1
        update.message.reply_text("state = S")

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

    def on_enter_goal_LS(self, update):
        global stateID
        stateID = 'LS'
        global layer
        layer += 1
        update.message.reply_text("state = LS")

    def on_enter_goal_HC(self, update):
        global stateID
        stateID = 'HC'
        global layer
        layer += 1
        update.message.reply_text("state = HC")

    def on_enter_goal_HS(self, update):
        global stateID
        stateID = 'HS'
        global layer
        layer += 1
        update.message.reply_text("state = HS")

    def on_enter_goal_CS(self, update):
        global stateID
        stateID = 'CS'
        global layer
        layer += 1
        update.message.reply_text("state = CS")

    def on_enter_goal_LHC(self, update):
        global stateID
        stateID = 'LHC'
        global layer
        layer += 1
        update.message.reply_text("state = LHC")

    def on_enter_goal_LHS(self, update):
        global stateID
        stateID = 'LHS'
        global layer
        layer += 1
        update.message.reply_text("state = LHS")

    def on_enter_goal_LCS(self, update):
        global stateID
        stateID = 'LCS'
        global layer
        layer += 1
        update.message.reply_text("state = LCS")

    def on_enter_goal_HCS(self, update):
        global stateID
        stateID = 'HCS'
        global layer
        layer += 1
        update.message.reply_text("state = HCS")

    def on_enter_goal_LHCS(self, update):
        global stateID
        stateID = 'LHCS'
        global layer
        layer += 1
        update.message.reply_text("state = LHCS")

    #def on_exit_goal_L(self, update):
    #    update.message.reply_text("i'm exiting state1")
    #    print('Leaving state1')


    #def on_exit_goal_H(self, update):
    #    update.message.reply_text("i'm exiting state2")
    #    print('Leaving state2')


    #def on_exit_goal_C(self, update):
    #    update.message.reply_text("i'm exiting state3")
    #    print('Leaving state3')


