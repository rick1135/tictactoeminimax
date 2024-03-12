def resultado(tabuleiro):
    print("Estado atual do tabuleiro : \n\n");
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n");
        if(tabuleiro[i]==0):
            print("- ",end=" ");
        if (tabuleiro[i]==1):
            print("O ",end=" ");
        if(tabuleiro[i]==-1):    
            print("X ",end=" ");
    print("\n\n");

def player1(tabuleiro):
    pos=input("Escolha uma posição entre [1...9] para X: ");
    pos=int(pos);
    if(tabuleiro[pos-1]!=0):
        print("Wrong Move!!!");
        exit(0) ;
    tabuleiro[pos-1]=-1;

def player2(tabuleiro):
    pos=input("Escolha uma posição entre [1...9] para O: ");
    pos=int(pos);
    if(tabuleiro[pos-1]!=0):
        print("Wrong Move!!!");
        exit(0);
    tabuleiro[pos-1]=1;

#MinMax function.
def minimax(tabuleiro,player):
    x=acoes(tabuleiro);
    if(x!=0):
        return (x*player);
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(tabuleiro[i]==0):
            tabuleiro[i]=player;
            score=-minimax(tabuleiro,(player*-1));
            if(score>value):
                value=score;
                pos=i;
            tabuleiro[i]=0;

    if(pos==-1):
        return 0;
    return value;
    
def CompTurn(tabuleiro):
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(tabuleiro[i]==0):
            tabuleiro[i]=1;
            score=-minimax(tabuleiro, -1);
            tabuleiro[i]=0;
            if(score>value):
                value=score;
                pos=i;
 
    tabuleiro[pos]=1;


def acoes(tabuleiro):
    cb=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];

    for i in range(0,8):
        if(tabuleiro[cb[i][0]] != 0 and
           tabuleiro[cb[i][0]] == tabuleiro[cb[i][1]] and
           tabuleiro[cb[i][0]] == tabuleiro[cb[i][2]]):
            return tabuleiro[cb[i][2]];
    return 0;

def ganhador(tabuleiro):
    x = acoes(tabuleiro)
    if x == 0:
        return None  #empate
    elif x == -1:
        return 'X'  #X venceu
    elif x == 1:
        return 'O'  #O venceu


def main():
    choice = input("Digite 1 para iniciar, 2 para sair: ")
    choice = int(choice)
    tabuleiro = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    if choice == 1:
        print("IA : O Vs. você : X")
        player = input("Digite 1 para começar jogando ou 2 para IA começar: ")
        player = int(player)
        
        for i in range(0, 9):
            if acoes(tabuleiro) != 0:
                break
            if (i + player) % 2 == 0:
                CompTurn(tabuleiro)
            else:
                resultado(tabuleiro)
                player1(tabuleiro)
                
    else:
        print("Você escolheu sair!")
        return 0

    winner = ganhador(tabuleiro)
    if winner is None:
        resultado(tabuleiro)
        print("Empate!!!")
    else:
        resultado(tabuleiro)
        print(f"{winner} venceu!")

#---------------#
main()
#---------------#
