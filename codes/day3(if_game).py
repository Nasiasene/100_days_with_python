#choice game based in if stantement.

print('''
*******************************************************************************

          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /

*******************************************************************************
''')
print("Welcome to Treasure Island!.")
print("Your mission is to find the treasure!.") 


print('\n'*5)
print('''
************************************************************

                        ,sdPBbs.
                      ,d$$$$$$$$b.
                     d$P'`Y'`Y'`?$b
                    d'    `  '  \ `b
                   /    |        \  \
                  /    / \       |   \
             _,--'        |      \    |
           /' _/          \   |        \
        _/' /'             |   \        `-.__
    __/'       ,-'    /    |    |     \      `--...__
  /'          /      |    / \     \     `-.           `\
 /    /;;,,__-'      /   /    \            \            `-.
/    |;;;;;;;\                                             \

*************************************************************
''')
choice1 = input("you're at a mountain, you can't climb it, but you can round. Where do you want to go? \nType 'right' if you want to go right or 'left' if you want to go left: ").lower()


if choice1 == "right":
    print('\n'*2)
    print('''
**********************************************************
    _      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
    _      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,__ 
_      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
_      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
_      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
_      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_
_      _      _      _      _      _      _      _
)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_)`'-.,_

**********************************************************
    ''')
    choice2 = input("You came to a river, do you want to swim or wait for a boat? \nType 'swim' if you want to swim or 'wait' if you want to wait for a boat: ").lower()


    if choice2 == "wait":
        print('\n'*2)
        print('''
***********************************

                 ;~
               ./|\.
             ./ /| `\.
            /  | |   `\.
           |   | |     `\.
           |    \|       `\.
         .  `----|__________\.
          \-----''----.....___
           \               ""/
      ~^~^~^~^~^`~^~^`^~^~^`^~^~^
       ~^~^~`~~^~^`~^~^~`~~^~^~

************************************
''')
        print("A boat came to take you to the other side of the river", '\n'*2)
        print('''
**********************************************************
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|

**********************************************************
        ''')
        choice3 = input("You see a house with 3 doors. One red, one yellow and one blue. Which color do you choose? \nType 'red', 'yellow' or 'blue': ").lower()

        if choice3 == "blue":
            print("\n" *2,"You found the treasure! You Win!", "\n"*2)
            print('''
*******************************************************************************

          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /

*******************************************************************************
            ''')
        elif choice3 == "red":
            print("\n" *2, "It's a room full of fire. Game Over.", "\n" *2)
            print('''

****************************************************

               (  .      )
           )           (              )
                 .  '   .   '  .  '  .
        (    , )       (.   )  (   ',    )
         .' ) ( . )    ,  ( ,     )   ( .
      ). , ( .   (  ) ( , ')  .' (  ,    )
     (_,) . ), ) _) _,')  (, ) '. )  ,. (' )

************************************************
            ''')
        
        elif choice3 == "yellow":
            print("\n" *2, "You walked into a room full of bees and were stung to death. \nGame Over!")
            print('''
*********************************************************************************
     %           %
         %           %
            %           %
                 %          %
                   %          %                   :::
                    %          %                ::::::
                 %%%%%%  %%%%%%%%%            ::::::::
              %%%%%ZZZZ%%%%%%   %%%ZZZZ     ::::::::::         ::::::
             %%%ZZZZZ%%%%%%%%%%%%%%ZZZZZZ  :::::::::::    :::::::::::::::::
             ZZZ%ZZZ%%%%%%%%%%%%%%%ZZZZZZZ::::::::::***:::::::::::::::::::::
          ZZZ%ZZZZZZ%%%%%%%%%%%%%%ZZZZZZZZZ:::::`(::::::::::::::::::::
      ZZ%ZZZZZZZZZZZZZZZZZZZ%%%%% | | %ZZZ *:::::::::::::::::::
      Z%ZZZZZZZZZZZZZZZ%%%%%%%%%%%%%%%ZZZ::::::::::::::::::::::::::
       ZZZZZZZZZZZ%%%%%ZZZZZZZZZZZZZZZZZ%%%%:::ZZZZ:::::::::::::::::
         ZZZZ%%%%%ZZZZZZZZZZZZZZZZZZ%%%%%ZZZ%%ZZZ%ZZ%%*:::::::::::
            ZZZZZZZZZZZZZZZZZZ%%%%%%%%%ZZZZZZZZZZ%ZZ%:::*:::::::
            *:::%%%%%%%%%%%%%%%%%%%%%%%ZZZZZZZZZZ%%%*::::*::::
          *:::::::%%%%%%%%%%%%%%%%%%%%%%%ZZZZZ%%      *:::Z
         **:ZZZZ:::%%%%%%%%%%%%%%%%%%%%%%%%%%%ZZ      ZZZZZ
        *:ZZZZZZZ       %%%%%%%%%%%%%%%%%%%%%ZZZZ    ZZZZZZZ
       *::::ZZZZZZ         %%%%%%%%%%%%%%%ZZZZZZZ      ZZZ
        *::ZZZZZZ           Z%%%%%%%%%%%ZZZZZZZ%%
          ZZZZ              ZZZZZZZZZZZZZZZZ%%%%%
                           %%%ZZZZZZZZZZZ%%%%%%%%
                          Z%%%%%%%%%%%%%%%%%%%%%
                          ZZ%%%%%%%%%%%%%%%%%%%
                          %ZZZZZZZZZZZZZZZZZZZ
                          %%ZZZZZZZZZZZZZZZZZ
                           %%%%%%%%%%%%%%%%
                            %%%%%%%%%%%%%
                             %%%%%%%%%
                              ZZZZ
                              ZZZ
                             ZZ
                            Z

*********************************************************************************
            ''')
        else:
            print("\n" *10, "Dumb ****! you chose a door that doesn't exist. \nGame Over.")
            print('''
*************************

     _.--""--._
    /  _    _  \
 _  ( (_\  /_) )  _
{ \._\   /\   /_./ }
/_"=-.}______{.-="_\
 _  _.=("""")=._  _
(_'"_.-"`~~`"-._"'_)
 {_"            "_}

*************************
            ''')
    elif choice2 == "swim":
        print('\n'*3, "************************************\n\nYou've be attacked by a Kraken!\nGame Over!")
        print('''
************************************

                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`

**********************************
        ''')
    else:
        print("invalid text. Please type 'wait' or 'swim' in the next time.")
elif choice1 == "left":
    print("\n"*3, "*********************************\nAs you went to the left, you tripped over a rock that caused a landslide. \nGame Over!")
    print('''
*********************************

                            ,--.
                           {    }
                           K,   }
                          /  ~Y`
                     ,   /   /
                    {_'-K.__/
                      `/-.__L._
                      /  ' /`\_}
                     /  ' /
             ____   /  ' /
      ,-'~~~~    ~~/  ' /_
    ,'             ``~~~  ',
   (                        Y
  {                         I
 {      -                    `,
 |       ',                   )
 |        |   ,..__      __. Y
 |    .,_./  Y ' / ^Y   J   )|
 \           |' /   |   |   ||
  \          L_/    . _ (_,.'(
   \,   ,      ^^""' / |      )
     \_  \          /,L]     /
       '-_~-,       ` `   ./`
          `'{_            )
              ^^\..___,.--`

**********************************
    ''')
else:
    print('invalid text. Please type "left" or "right" in the next time.')