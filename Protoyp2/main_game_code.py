#main_game_code.py file 

#imports 
from shipclass import Ship
from functions import *  


#main game 
main_game  = True

while main_game == True:

    print("\nwelcome to Sink the Ship")
    format_board(create_empty_board())

    ship_fleet = Ship.read_file() #read a random file 
        
    fleet_positions = []
    
    emperial_fleet = {}
    for index, ship in enumerate(ship_fleet): #this intialises all ship objects
        name = ship[0]
        num_blocks = int(ship[1])
        positions_blocks = ship[2]
        emperial_fleet[f'ship_{index}'] = Ship(name, num_blocks, positions_blocks) #this part initialises every ship!!
       
    #this parts creates the hidden game map with the hidden ship positions 
    hidden_map = create_empty_board()
    
    total_ship_blocks = 0
    

    for ship_key, ship_obj in emperial_fleet.items():

        total_ship_blocks += ship_obj.num_blocks

        positions_as_list = format_positions_as_list(ship_obj.position_blocks)
        for positions in positions_as_list:
            fleet_positions.append(positions)
        hidden_map = place_positions_on_board(positions_as_list, hidden_map) 

    print(fleet_positions)
    
    shooting_mode = True

    part = total_ship_blocks #this sets it for the first time 

    user_board = create_empty_board()  

    #enters shooting mode 

    old_user_input_cooridinates = []   #this list stores the coordinats that are inputed


    while shooting_mode == True:
       

        updated_map_and_status = shoot_enemy_ship(hidden_map, user_board, old_user_input_cooridinates)


        user_board = updated_map_and_status[0]

        status = updated_map_and_status[1]
        

        old_user_input_cooridinates.append(updated_map_and_status[2])



        percent_blocks_left, part, hit_or_miss = block_percentage_left(status, part, total_ship_blocks)

        print("\n _____Main Game Board_____")
      
        print(f"\nPercent of blocks left: {percent_blocks_left}%")
        print(f"\nstatus: {hit_or_miss}")


        format_board(user_board) #this prints and returns the updated map 
                
        

        if part == 0:

            user_menu = 3 

        else: 

            user_menu = main_menu_choices()

            

            if user_menu == 1: 

                continue 

            elif user_menu == 2:
            #reads the cheat file, translates positiosn, uses make hidden ship and formats the board
            
                print("\n _____Enemy Intel_____")
               
                
                enemy_intel_positions = read_cheat_file() #this returns the enemy positions as 1 list!
                

                combined_board = enemy_intel_map(enemy_intel_positions, user_board)
                            
                format_board(combined_board)

                continue
                    
            elif user_menu == 3: #done

                while True:
                    user_input = str(input("Do you want to see the enemy map? (Y/N):  "))
                    try:
                        if user_input == 'Y':
                            print("\n______Enemy Map_____")
                            #combine the current board with hidden board 
                            end_board = enemy_intel_map(fleet_positions, user_board)
                            format_board(end_board)

                            break #break makes it so that it goes out of loop and prints end message!!

                        elif user_input == 'N':
                            break 

                        else: 
                            raise ValueError 
                        
                    except ValueError as ve: 
                        print("Error: {ve}. Please enter (Y/N)")


                print("Thank you for playing!!")
                main_game = False
                shooting_mode = False
                break  




