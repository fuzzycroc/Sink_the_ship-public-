#shipclass.py
#imports 
import random 
from functions import * 


#class
class Ship: #done



    def __init__(self, name, num_blocks, position_blocks): #done
        '''this gives the attribute for every initialisation of the class Ship'''
            
        self.name = name 
        self.num_blocks = num_blocks
        self.position_blocks = position_blocks
 

    def read_file(): #done
        '''this function reads the first file for the hidden map'''

        file_number = random.randint(1,10)

    
        file_name = rf'ship_file_no{file_number}.txt'
       
        fleet_info = []

        with open(file_name, 'r') as file:
            content = file.read().splitlines()
            for line in content:
                fleet_info.append(line)


        #split all info using .split(':') 

        final_fleet = []
        for ship in fleet_info: #this part divids all info for each ship!!
            parts = ship.split(':')
            final_fleet.append(parts)


        print(f"file number is {file_number}")
        return final_fleet
    
    
