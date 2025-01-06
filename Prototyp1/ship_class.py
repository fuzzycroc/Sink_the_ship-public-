#this is the first protoype in the P-uppgift

class Ship: 

    def __init__(self, name, num_blocks, position_blocks): #done
    
        self.name = name 
        self.num_blocks = num_blocks
        self.position_blocks = position_blocks

    
    def read_file(): #pending

        file_number = 1 

        file_name = rf'ship_file_no{file_number}.txt'


        fleet_temp = [] 

        with open (file_name, 'r') as file:
            content = file.read().splitlines()
            for line in content: 
                fleet_temp.append(line)

        final_fleet = [] 

        for ship in fleet_temp: 
            parts = ship.split(':')
            final_fleet.append(parts)

        #add in code here that initialise the ships! 
        #check if the intialised ships are returned outside the function or not 


        return final_fleet
    

    def make_hidden_map(raw_ship_coordinates): #pending

        
        for ship in raw_ship_coordinates:
            for blocks in ship: 
                row_coordinate = blocks[0]
                column_cooridnate = int(blocks[1])

                if row_coordinate == 'A':
                    row_coordinate = 1
                if row_coordinate == 'B':
                    row_coordinate = 2 
                if row_coordinate == 'C':
                    row_coordinate = 3 
                if row_coordinate == 'D':
                    row_coordinate = 4 
                if row_coordinate == 'E':
                    row_coordinate = 5
