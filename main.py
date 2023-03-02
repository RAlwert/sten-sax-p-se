import random

val_möjligheter="sten","sax","påse"

vinst_dator=0
vinst_spelare=0
#få ut majoritet av rundor för att vinna
bäst_av=int(input("hur många rundor vill du spela?"))

if bäst_av%2==0:
    bäst_av=(bäst_av/2)+1
elif bäst_av%2!=0:
    bäst_av=(bäst_av/2)+0.5


game_over=False

while not game_over:
    #spelarens drag 
    spelare_drag=""
    while not spelare_drag in val_möjligheter:
        if not spelare_drag in val_möjligheter:
            print("du kan bara välja sten saxe eller påse")
        spelare_drag=input("Välj Sten,Sax eller Påse: ").lower()
        print()
    
    #datorns drag
    dator_drag=random.choice(val_möjligheter)
    print("Datorn valde "+dator_drag)
    print()

    #se om datorn har vunnit rundan
    if dator_drag=="sax" and spelare_drag=="påse":
        vinst_dator+=1
    elif dator_drag=="påse" and spelare_drag=="sten":
        vinst_dator+=1
    elif dator_drag=="sten" and spelare_drag=="sax":
        vinst_dator+=1

    #se om spelaren har vunnit rundan
    elif spelare_drag=="sax" and dator_drag=="påse":
        vinst_spelare+=1
    elif spelare_drag=="påse" and dator_drag=="sten":
        vinst_spelare+=1
    elif spelare_drag=="sten" and dator_drag=="sax":
        vinst_spelare+=1


    #vinstmedelande
    if vinst_spelare>= bäst_av:
        game_over=True
        print ("Grattis du har vunnit! ")
    if vinst_dator>= bäst_av:
        game_over=True
        print ("Du har förlorat bättre lycka nästa gång !")



