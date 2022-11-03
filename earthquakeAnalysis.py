#Name: Brent Hoover
#Project: Earthquake Education

"""This program demonstrates the use of modules, files, lists, and exception handling. The program
starts by writing 20 random Richter Scale values to a new text file. The random Richter values are
read from the file and placed in a list. Each Richter value from the list is used to
calculate the amount of energy produced from an earthquake in Joules and detonated TNT. Additionally,
they determine the earthquake's intensity on the Modified Mercalli Scale, the level of shaking produced,
and their impact on the environment. The results from the 20 earthquake analyses are written to a
separate text file. Exception handling is used to prevent the program from abruptly halting."""

def main():

    try:
        #Imports earthquake module containing functions
        import earthquake
        
        earthquake.about_function()

        #Opens new file in write mode; assigned to file variable
        file_richter = open('richter.txt', 'w')
        #Opens existing file in reading mode; assigned to file variable
        file_infile = open('richter.txt','r')
        #Opens separate file in append mode; assigned to file variable
        file_outfile = open('results_outfile.txt','w')

        #Random richter values generated and written to new file
        file_richter.write('List of Richter Values:\n\n')
        for x in range(20):
            r_value = earthquake.gen_richter()
            file_richter.write(str(r_value) + '\n')
        file_richter.close()

        #Random richter values read from existing file and placed in list 
        r_title = file_infile.readline()
        r_newline = file_infile.readline()
        #reads each line of file and places them in a list named r_list
        r_list = file_infile.readlines()
        index = 0 #index initially set to zero
        #newline characters stripped from each item in list
        while index < len(r_list):
            r_list[index] = r_list[index].rstrip('\n')
            index += 1  #running total for index; moves to next item in list
        #richter values in list converted to float-point numbers and used for calculations
        for r_string in r_list:
            richter_value = float(r_string)
            energy_joules = earthquake.calc_joules(richter_value)
            energy_TNT = earthquake.calc_TNT(energy_joules)
            MMI_value = earthquake.find_MMI(richter_value)
            shaking_value, impact_value = earthquake.find_shaking_impact(MMI_value)
            earthquake.print_all(richter_value, energy_joules, energy_TNT,
                                 MMI_value, shaking_value, impact_value)
            print()
        file_infile.close()

        #Earthquake values calculated and appended to new/existing file
        file_outfile.write('List of Earthquake Analyzes:\n\n')
        index = 0   #index reset and set to zero again
        #richter values in list converted to float-point numbers and used for calculations
        while index < len(r_list):
            richter_value = float(r_list[index])
            joules = earthquake.calc_joules(richter_value)
            TNT = earthquake.calc_TNT(joules)
            MMI = earthquake.find_MMI(richter_value)
            shaking, impact = earthquake.find_shaking_impact(MMI)
            file_outfile.write('Richter Value: ' + str(r_list[index]) + '\n')
            file_outfile.write('Joules: ' + str(joules) + '\n')
            file_outfile.write('TNT: ' + str(TNT) + '\n')
            file_outfile.write('MMI: ' + str(MMI) + '\n')
            file_outfile.write('Shaking Value: ' + str(shaking) + '\n')
            file_outfile.write('Impact: ' + str(impact) + '\n\n')
            index += 1  #running total for index; moves to next item in list
        file_outfile.close()

    except IOError:
        print('An error occurred trying to read file. File not found')
    except NameError as error:
        print('An error occurred:', error)
    except ValueError:
        print('An error occurred: non-numeric data found in file')
    except:
        print('An error occurred trying to run program.')

main()
    
