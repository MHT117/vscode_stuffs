x= [1, 2, 3, 4]
for i in range(10):
    print(x)






'''tic_tac = [[0,0,0],[0,0,0],[0,0,0],]

def game_board(row = 0, column = 0,player = 0):
    try:
        print("   a  b  c")
        tic_tac[row][column] = player
        for count, row in enumerate(tic_tac):
            print(count,row)
    except IndexError as e:
        print('Error: index must be between 0-2.',e)
    except Exception as e:
        print("u fucked up something very badly",e)
game_board()


game_board(row = 2, column = 2,player = 1)
'''
'''print("   a  b  c")

for count, row in enumerate(tic_tac):
    print(count,row)'''

print('My Set-up is done')