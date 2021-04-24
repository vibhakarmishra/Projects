#Game to take user input and replace the list and play again
# Displaying game list options

def display_game(game_list):
    print("Here is the current list: ")
    print(game_list)

# Taking user choice of index
def position_choice():
    
    choice = 'wrong'
    
    accepted_index = ['0','1','2']
    
    while choice not in accepted_index:
        
        choice = input("Pick a position from (0,1 or 2) : ")
        
        if choice not in accepted_index:
            
            print("Sorry, Invalid Choice!!")
    
    return int(choice)

# Taking user's choice for replacement and returing updated list
def replacement_choice(game_list,choice):
    
    user_placement = input('Type a string to place at position')
    
    game_list[choice] = user_placement
    return game_list

# Asking to continue playing or NOT
def gameon_choice():
    
    choice = 'wrong'
    
    accepted_choice = ['Y', 'N']
    
    while choice not in accepted_choice:
        
        choice = input("Keep Playing (Y or N) : ")
        
        if choice not in accepted_choice:
            
            print("Sorry, Wrong input, please choose Y or N!!")
    
    if choice == 'Y':
        return True
    else:
        return False

game_on = True
game_list = [0,1,2]

while game_on == True:
    #Displaying initial game list
    display_game(game_list)
    
    #Asking for user's position choice
    position = position_choice()
    
    #Replacement choice along with replace string
    game_list = replacement_choice(game_list, position)
   
    #Printing updated list   
    display_game(game_list)
    
    #User input for continuing with game
    game_on = gameon_choice()