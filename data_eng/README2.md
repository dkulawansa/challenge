<h2>CredSimple Digala's Solution</h2>
#### Part 1
**Description:**
Code has been written in python 3.6.2 but it is also compatible with python 2.7. The following NPI Numbers listed in the README.md file was copied to a text file called npi to be used with this the program. It is required to have this file in the same folder to run the code. Once code is pulled from the github repo, to run the code please type 'python check_luhn.py' (without quotes) on the command line. One test was added to test the function that does the luhn check. The test can be run by typing 'python tests.py' (without quotes)

Resources:
+ NPI Numbers:<br>
1356320139<br>
1285849489<br>
1265795159<br>
1922087766<br>
1932224400<br>
1467538918<br>
1861414096<br>
1528142197<br>
1306070885<br>
141799038<br>
1144258609<br>
1467446575<br>
1285652024<br>
1104084334<br>
144750284<br>
1356585673<br>
1740232941<br>
1992776843<br>
1215965934<br>
1154348176

Sample Output
CredSimple\challenge\data_eng>python check_luhn.py

NPI Number   Valid?
==========   ======
1356320139   True
1285849489   True
1265795159   False
1922087766   True
1932224400   False
1467538918   True
.........    ...

#### Part 2
**Instructions:**
Code has been written in python 3.6.2 environment. Once all the files are pulled from the github location it should be ready to run without installing any additional software libraries. To find help please type 'python providers.py --help' (without quotes). It will display information on how to use appropriate command line arguments to get desired sorting.

Here is the program signature:

python providers.py --help
usage: providers.py [-h] [--ptype_lname] [--dob] [--lastname]

Displays a list of providers sorted by the following command line arguments.
If no argument is provided it will be defaulted to 'ptype_lname' sort order

optional arguments:
  -h, --help     show this help message and exit
  --ptype_lname  sorted by provider type then by last name ascending.
  --dob          sorted by birth date, ascending.
  --lastname     sorted by last name, descending.

Here are some sample runs of the program

Sorted by provider type then by last name ascending.<br>
CredSimple\challenge\data_eng>python providers.py --ptype_lname

Last Name First name         Gender  DoB     Provider Type
========= ==========         ======  ===     ==============

Agredo, Sandra                 F  01/22/1964  CSW
Beecher, Andrew                M  07/04/1947  CSW
Chase, Carola                  F  01/21/1949  CSW
Emerton, Mary                  F  08/07/1962  CSW
Faunt, Nancy                   F  01/31/1959  CSW
Feist, Sandra                  F  05/30/1968  CSW
Guido, Marietta                F  01/05/1963  CSW
Kossuth, Jeannette             F  10/01/1953  CSW
Lee, Donna                     F  07/20/1977  CSW
Sekulic, Deirdre               F  03/01/1972  CSW
Huang, Yeli                    F  07/29/1976  DO
Hausman, Lionel                M  08/14/1963  DPM
Jin, Tsen-Tsen                 F  04/24/1963  M
Handler, Bradley               M  09/29/1966  MD
Henner, Jaryn                  F  10/14/1978  MD
Herschorn, Brian               M  12/13/1951  MD

sorted by birth date, ascending.<br>
CredSimple\challenge\data_eng>python providers.py --dob

Last Name First name         Gender  DoB     Provider Type
========= ==========         ======  ===     ==============

Kaufman, Stephen               M  05/30/1939  MD
O'Dowd, Mary                   F  01/19/1942  MD
Mallard, Henry                 M  08/15/1945  MD
Beecher, Andrew                M  07/04/1947  CSW
Iqbal, Muhammad                M  02/17/1948  MD
Chase, Carola                  F  01/21/1949  CSW
Kaufman, Allen                 M  06/06/1949  MD
Koci, Piro                     M  10/02/1949  MD
Herschorn, Brian               M  12/13/1951  MD
Cullen-Kortleven, Kathleen     F  09/10/1952  NP
Kossuth, Jeannette             F  10/01/1953  CSW

sorted by last name, descending.<br>
CredSimple\challenge\data_eng>python providers.py --lastname

Last Name First name         Gender  DoB     Provider Type
========= ==========         ======  ===     ==============

Tepedino, Jenna                F  06/10/1990  SLP
Syrkin, Grigory                M  07/16/1981  MD
SwÃŸan, Matthew                M  12/01/1980  MD
Sullivan, Daniel               M  12/06/1984  PSYD
Shariff, Saadat                F  07/16/1979  MD
Sekulic, Deirdre               F  03/01/1972  CSW
Reddy, Divya                   F  12/03/1982  MD
Polycarpe, Myreille            F  04/08/1958  MD
Pilika, Asti                   M  02/13/1976  MD
Perez, Joanna                  F  12/19/1990  SLP
Patel, Nihal                   M  03/18/1984  MD
Patel, Archita                 F  10/18/1986  PA
O'Dowd, Mary                   F  01/19/1942  MD

