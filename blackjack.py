import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,11]


def dealdealer(hand,cards):
    aces=0
    totalp=sum(dealer)
    
    while totalp<17:
        x=random.choice(cards)
        print("Dealer draw: ",x)
        if x==11:
            aces+=1
        
        hand.append(x)
        totalp+=x
                
        if aces and totalp>21:
            aces-=1
            totalp-=10

      
        elif totalp>21:
                      
            return "Busted"
    return totalp
           
def dealplayer(hand,cards):
    aces=0
    totalp=sum(user)
    if totalp==21:
        return "Blackjack"

    gameon=True
    
    while gameon:
        choice=input("Hit or Stand (h/s) ")
        if choice=="h":
            
            x=random.choice(cards)
            
            if x==11:
                aces+=1
            
            hand.append(x)
            totalp+=x
            
            
            if aces and totalp>21:
                aces-=1
                totalp-=10
            print("Player draw: ",x)
            print("Player total: ", totalp)

            if totalp>21:
                      
                return "Busted"

        else:
            gameon=False
            
    return totalp

def initdeal(hand,cards):
    x=random.choice(cards)
    hand.append(x)

gameon=True

while gameon:

    user=[]
    dealer=[]
    initdeal(user,cards)
    initdeal(dealer,cards)
    initdeal(user,cards)
    initdeal(dealer,cards)
    print(user,"user total:",sum(user))
    print(dealer[0],"Dealer' card")
    
    totalplayer=dealplayer(user,cards)
    
    if totalplayer=="Blackjack":
        print("Player wins. Blackjack")
    elif totalplayer=="Busted":
        print("Player lose. Busted")
    else:
        totaldealer=dealdealer(dealer,cards)
        if totaldealer=="Busted":
            print("Player win. Dealer Busted")
        elif totalplayer>totaldealer:
             print("Player win.")
        elif totalplayer<totaldealer:
             print("Delaer win.") 
        elif totalplayer==totaldealer:
             print("Draw.")    
    
    print(user," Player's total: ",totalplayer)
    print(dealer," Dealer's total: ",sum(dealer))
    again=input ("Wanna play again? y or n: ")
    if again=="y":
        gameon=True
    else:
        gameon=False
