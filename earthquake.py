

#Function: about_function
#Purpose: displays what the program is about
#Parameters: None
#Returns: Nothing
#Called by: main function
#Calls: None
#Global variables used: None
def about_function():
    print()
    print('Welcome to the Earthquake Education Center. If you are curious about earthquakes, '
           'you\'ve come to the right place!')
    print()
    
#Function: gen_richter
#Purpose: imports the random module; generates and displays a random Richter value
#Parameters: None
#Returns: r_value (random Richter value)
#Called by: main function
#Calls: None
#Global variables used: None
def gen_richter():
    import random
    r_value= random.uniform(1,10)
    return r_value

#Function: calc_joules
#Purpose: calculates the amount of energy produced in Joules
#Parameters: r_value (random Richter value)
#Returns: joules (amount of energy in Joules)
#Called by: main function
#Calls: None
#Global variables used: None
def calc_joules(r_value):
    joules= 10**(1.5* r_value +4.8)
    return joules

#Function: calc_TNT
#Purpose: calculates the amount of energy produced in detonated TNT
#Parameters: joules (amount of energy in Joules)
#Returns: tnt_tons (amount of detonated TNT in tons)
#Called by: main function
#Calls: None
#Global variables used: None
def calc_TNT(joules):
    tnt_tons= joules*((2.390057361377)*10**(-7))/ 1000
    return tnt_tons

#Function: find_MMI
#Purpose: determines the earthquake's intensity on the Modified Mercalli Scale
#         based on the random Richter value
#Parameters: r_value (random Richter value)
#Returns: M_value (Modified Mercalli intensity level)
#Called by: main function
#Calls: None
#Global variables used: None
def find_MMI(r_value):
    if r_value < 2.0:
        M_value = 'I'
    elif r_value <= 3.0:
        M_value = 'II'
    elif r_value < 4.0:
        M_value = 'III'
    elif r_value == 4.0:
        M_value = 'IV'
    elif r_value < 5.0:
        M_value = 'V'
    elif r_value < 6.0:
        M_value = 'VI'
    elif r_value == 6.0:
        M_value = 'VII'
    elif r_value <7.0:
        M_value = 'VIII'
    elif r_value == 7.0:
        M_value = 'IX'
    elif r_value < 8.0:
        M_value = 'X'
    elif r_value == 8.0:
        M_value = 'XI'
    else:
        M_value = 'XII'
    return M_value

#Function: find_shaking_impact
#Purpose: determines the level of shaking produced and the earthquake's impact on the environment
#         based on the Modified Mercalli intensity level
#Parameters: M_value (Modified Mercalli intensity level)
#Returns: shake_value (level of shaking)
#         impact_value (impact on environment)
#Called by: main function
#Calls: None
#Global variables used: None
def find_shaking_impact(M_value):
    if M_value == 'I':
        shake_value = 'Not felt'
        impact_value = 'Not felt except by very few under especially favorable conditions'
    elif M_value == 'II':
        shake_value = 'Weak'
        impact_value = 'Felt only by a few people at rest, especially on upper floors'
    elif M_value == 'III':
        shake_value = 'Weak'
        impact_value = ('Felt quite noticeably by people indoors, especially on upper '+
              'floors of buildings. Many people do not recognize it as an earthquake. '+
              'Standing motorcars may rock slightly. Vibrations similar to the '+
              'passing of a truck. Duration estimated.')
    elif M_value == 'IV':
        shake_value = 'Light'
        impact_value = ('Felt indoors by many, outdoors by few during the day. At night, '+
              'some awakened dishes, windows, doors disturbed; walls make cracking sounds. '+
              'Sensation like heavy truck striking building. Standing motor cars rocked noticeably.')
    elif M_value == 'V':
        shake_value = 'Moderate'
        impact_value = ('Felt by nearly everyone; many awakened. Some dishes, wondows broken. '+
              'Unstable objects overturned. Pendulum clocks may stop.')
    elif M_value == 'VI':
        shake_value = 'Strong'
        impact_value = ('Felt by all, many frightened. Some heavy furniture moved; '+
              'a few insteances of fallen plaster. Damage slight.')
    elif M_value == 'VII':
        shake_value = 'Very strong'
        impact_value = ('Damage negligible in buildings of good design and construction; '+
              'slight to moderate in well-built ordinary structures; '+
              'damage considerable in poorly built or badly designed structures; some chimneys broken.')
    elif M_value == 'VIII':
        shake_value = 'Severe'
        impact_value = ('Damage slight in specially designed structures; '+
              'considerable damage in ordinary substantial buildings with parital collapse. '+
              'Damage great in poorly built structures. Fall of chimneys, factory stacks, columns, '+
              'monuments, walls. Heavy furniture overturned.')
    elif M_value == 'IX':
        shake_value = 'Violent'
        impact_value = ('Damage considerable in specially designed structures; '+
              'well-designed frame structures thrown out of plumb. Damage great in substantial '+
              'buildings, with partial collapse. Buildings shifted off foundations. Liquefaction.')
    elif M_value == 'X':
        shake_value = 'Extreme'
        impact_value = ('Some well-built wooden structures destroyed; most masonry and frame structures '+
              'destroyed with foundations. Rails bent.')
    elif M_value == 'XI':
        shake_value = 'Extreme'
        impact_value = ('Few, if any, (masonry) structures remain standing. Bridges destroyed. '+
              'Broad fissures in ground. Underground pipe lines completely out of service. '+
              'Earth slumps and land slips in soft ground. Rails bent greatly.')
    else:
        shake_value = 'Shaking value: Extreme'
        impact_value = ('Damage total. Waves seen on ground surfaces. Lines of sight and level distorted. '+
             'Objects thrown upward into the air.')
    return(shake_value, impact_value)

#Function: print_all
#Purpose: displays random Richter value, energy in Joules, energy in detonated TNT,
#         Modified Mercalli intensity level, level of shaking produced, and impact on environment
#Parameters: r_value(random Richter value)
#            joules(amount of energy in Joules)
#            TNT(amount of detonated TNT in tons)
#            M_value (Modified Mercalli intensity level)
#            S_value (level of shaking)
#            I_value (ipact on environment)
#Returns: None
#Called by: main function
#Calls: None
#Global variables used: None
def print_all(r_value, joules, TNT, M_value, S_value, I_value):
    print('\n','*****~~~~~'*10,'\n',sep='')
    print('\t\t\tThe random Richter value chosen for you is ', format(r_value, '.1f'),'!!!', sep='')
    print()
    print('*****~~~~~'*10)
    print()
    print('\nHere is your earthquake analysis:\n')
    print (format('','>5'),'Richter Value:', format(r_value,'.1f'))
    print(format('','>5'),'Energy in Joules:', format(joules,',.2f'),'Joules')
    print(format('','>5'),'Energy in TNT:', format(TNT,',.2f'),'tons')
    print(format('','>5'),'Modified Mercalli Scale Value:', M_value)
    print(format('','>5'),'Shaking Value:', S_value)
    print(format('','>5'),'Impact of earthquake:')
    print(format('','>5'), I_value)
