#functions.py file 

#imports
import random


#functions
def create_empty_board(): #done
    '''this function creates an empty board and returns it '''

    num_rows = 6 
    num_columns = 6

    board = []

    #use a for loop to create the empty board 
    for i in range (num_rows):
        row = []
        board.append(row)
        for j in range(num_columns):
            row.append('_')
        

    c = 0
    for i in range (len(board)): #makes the coordinate axis for the columns
        if c < len(board[0]):
            board [0][c] = c
        c  += 1

    letters = ['', 'A', 'B', 'C', 'D', 'E'] #make the coordinate axis for the rows
    for i in range(len(board)):
        if i < len(letters):
            board[i][0] = letters[i]
        

        
    return board


def translate_coordinates(raw_coordinates):#done
    
    '''this function takes in a string representing coordinates, such as 'A1', 
    and translates it to matrix format, such as [1, 1], for the game board.'''

    try:
        row_coordinate = raw_coordinates[0].upper()  # ensure the row letter is uppercase very usefull
        column_coordinate = int(raw_coordinates[1:])  # convert column part to integer

        row_dict = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5}  # dictionary mapping letters to row numbers
        row_coordinate = row_dict.get(row_coordinate, 0)  #maps the row letter to the corresponding number

        if row_coordinate == 0 or column_coordinate < 1 or column_coordinate > 5:
            raise ValueError("Coordinates are out of range")  #raise an error for invalid coordinates

        return [row_coordinate, column_coordinate] #coordinates are returned here

    except ValueError as ve:
        print(f"Invalid input: {ve}. Please enter coordinates in the format 'A1' to 'E5'.")
        return None


def translate_user_inputs(old_user_input_coordinates): #done
    
    """this function uses translate_coordinates as its base if there are any errors with the function they are handeled here 
        the purpose of this function is to ensure that the user enters the correct coodinates that can be recieved
        1. if the input is invalid is handeled above 
        2. if the input is already been used before it is looped until a new input is given here!!"""
    

    while True: 

        try:
            user_coordinates = input("Enter coordinates to launch Missile: ")


            if user_coordinates in old_user_input_coordinates:
                print("coordinates have been used, try again") 
                continue

            translated_user_coordinates = translate_coordinates(user_coordinates) 

            if translated_user_coordinates is None: 
                raise ValueError

            old_user_input_coordinates.append(user_coordinates)

            return translated_user_coordinates #this function only returns the translated coordinates
        
        except ValueError as ve:
            print(f"{ve}: Invalid coordinates")     


def make_ship_positions(ship_positions): #done

    '''takes in several raw ship coordinates, loops and translates them all 
        the function returns i list of translated coordinates
        this function is resused several times'''

    
    translated_positions = []

    for positions in ship_positions:
    
        block_positions = translate_coordinates(positions)
        translated_positions.append(block_positions)
    
    return translated_positions


def place_positions_on_board(raw_ship_positions, empty_board): #done

    '''this function takes in all ship positions translates them 
        and places them onto the empty board
        this function is reused several times'''

    ship_positions = make_ship_positions(raw_ship_positions)
    for positions in ship_positions:

        #used to seperate every block coordinate
        #take the individual coordinate then sperate it into some format like [1][1]
        #and change that part into x!! 

        row = positions[0]
        column = positions[1]

        empty_board[row][column] = 'x'

        game_board = empty_board
       

    return game_board # a board with the placed ships are returned
    

def format_board (game_board): #done
    '''this function formats to board that is seen by the user 
        ths function is reused several times in the game'''

    #this automatically prints the board so you do not need a for loop!!
        
    divider = "-------------------------"
    for row in game_board: 
        print(divider) #prints the divider on the top
        formated_row = []
        for block in row: #formats every block in the row 
            formated_block = f"| {block} "
            formated_row.append(formated_block)

        formated_row_string = ''.join(formated_row) + "|" #this avoids the double line problem!!
        print(formated_row_string)
            
    print(divider)


def read_cheat_file(): #done

    '''this function reads a random cheat file when the user menu value is 2 
        the function reads the file, takes only the positions and then translates them'''

    file_number = random.randint(1,10)

  
    file_name = rf'C:ship_file_no{file_number}.txt'


    fleet_info = [] #all info of every ship is here!!
    
    with open(file_name , "r") as file:
        content = file.read().splitlines()
        for line in content:
            fleet_info.append(line)
            
       
    #split all info using .split(':')

    final_fleet = []
    for ship in fleet_info: #splits into list in list with parts this works!!
        parts = ship.split(':')

        final_fleet.append(parts)
    

    ship_positions = []

    for ship in final_fleet: 
        
        positions = ship[2]
        
        position_blocks = positions.split(',')
        ship_positions.extend(position_blocks)


    return ship_positions #the translated ship positions are returend here


def main_menu_choices (): #done

    '''this function is the main menu that is displayed to the user 
        which returns only the option chosen '''

    while True: #checks for value error here
        try:
            print("Enter number to choose an option")
            print("1. Shoot Enemy Ship")
            print("2. Cheat a little, get enemy intel")
            print("3. End Game ")

            user_input = int(input("Enter your choice (1-3): "))
            break 
        except ValueError:
            print
            print("\nplease enter a value from 1 to 3")
        #add in Except value error checks here!! 


    return user_input


def check_coordinates_with_map(hidden_map, translated_coordinates): #done
    '''this function checks the coordiantes that have been translated with the hidden map 
        if False then the missile has missed
        if True then the missile has hit a ship block'''

    row_block = translated_coordinates[0]
    column_block = translated_coordinates[1]

    coodinate_checker = False
    if hidden_map[row_block][column_block] != '_':
        coodinate_checker = True
    
    return coodinate_checker


def update_user_board( translated_coordinates, hidden_map, game_board): #done
        '''uses the function above to check if coordinates from user is correct
        updates the old board with the coordinates that is seen by the player
        this is then updated with o if missed 
        or # if hit
        returns user_board which is a matris with the updated block '''

        coordinate_checker = check_coordinates_with_map(hidden_map, translated_coordinates)

        row_coordinate = translated_coordinates[0]
        column_coordinate = translated_coordinates[1]

        
        
        if coordinate_checker == True: #update empty_user_board with '#' for hit 
            game_board[row_coordinate][column_coordinate] = '#'
        if coordinate_checker == False: #update empty_user_board with 'o' for miss 
            game_board[row_coordinate][column_coordinate] = 'o'


        return game_board , coordinate_checker


def shoot_enemy_ship(hidden_map, game_board, old_user_input_coordinates): #done

    '''this function takes in the hidden map, game board, and already inputed coordinates from the user 
        it loops tranlate_user_coordinates till a vaild input is given 
        then runs through update user board function and check it with the hidden map 
        it then returns the status of if it has hit or missed '''

    translated_coordinates = translate_user_inputs(old_user_input_coordinates)

    updated_map_and_status = update_user_board(translated_coordinates, hidden_map, game_board)

    updated_map = updated_map_and_status[0]

    status = updated_map_and_status[1]

    return updated_map , status , translated_coordinates #returns as needed
    

def format_positions_as_list(dictionary_positions): #done
    '''takes in a string as dictionary_positions 
        returns a list with with the position seperated 
        for example (A1, B1, C1) becomes [ A1, B1, C1] use the split funciton '''
    
    position_list = dictionary_positions.split(',')

    return position_list


def block_percentage_left(status, part, whole): #done
    '''this function calculates the precentage of blocks left
        and returns whether or not the missile has hit or missed '''

    #lesson learnt: it is possible to return several values from a function 
    #to acces the individual values treat it as a list 

    hit_or_miss = ()
    percent = 100
    rounded_percent = 100
     
    if status == True: 
        part -= 1 #decease part when hit is true 
        percent = (part/whole) * 100 
        hit_or_miss = 'hit'
        rounded_percent = round(percent, 1) #usefull function that rounds to the nearest second digit specified in function

    elif status == False: 
        #this fixes the issue that I hade earlier 
        percent = (part/whole) * 100 
        rounded_percent = round(percent , 1)
        hit_or_miss = 'miss'



    return rounded_percent, part, hit_or_miss


def enemy_intel_map (enemy_intel_positions, game_board): #review pending
    '''the enemy_intel_positions are a list of all the ships position info 
        takes in positions 
            formats positions as a enemy board 
            combines enemy board with game board 
            returns combined board'''
    
    
    enemy_intel_board = create_empty_board() #creates empty board

    ship_positions = make_ship_positions(enemy_intel_positions) #converts positions from [A1] to [11]
    #there might be issues with this

    for row, column in ship_positions: 
        enemy_intel_board[row][column] = 'x' 
   

    for row in range(len(game_board)):
        for col in range(len(game_board[row])):
            
            if game_board[row][col] == '#':
                enemy_intel_board[row][col] = '#'
            elif game_board[row][col] == 'o':
                enemy_intel_board[row][col] = 'o'
        

    return enemy_intel_board
    

