# HQAM constellations
We will briefly explain the code that generates regular and irregular HQAM and
the corresponding received symbols in the presence of additive white gaussian noise
(AWGN).
All classes are called from the main class, which takes input from the user and generates the
appropriate constellation. Each class contains code for generating some constellations such as
regular and irregular 4-ary HQAM,8-ary HQAM and 16-ary HQAM. In each class we calculate
the symbols close to the origin and from there we expand the symbols according to the
constellation.In addition there are functions to add noise to the constellation by adding more
symbols randomly distributed around each existing symbol.
Lastly, when we run the program the user is prompted to enter the number of symbols he or
she wants the constellation to have (possible answers:4,8,16) ,then if the constellation is regular
or irregular (possible answers "regular","r" or "irregular","i") and finally if the constellation is
in the presence of additive white gaussian noise (possible answers:"true","yes","y" or "false"
,"n","no"). After the constellation plot pops up ,user can continue seeing other constellations
till he or she types -1 where the program stops.
6
