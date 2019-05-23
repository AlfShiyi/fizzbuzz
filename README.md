# Inwk6312-openBookFinal-2019
# Basic instructions 

  - Ensure that you are the only person logged into github.com and classroom.github.com
  - Use the Ubuntu VM to write the progrm.
  - Use git add, commit and push to send the code back. 
  - Don't forget to add user name and email on git. 
  - You are allowed to use any form of searching and documentation reading and book reading is promoted
  - Read the API
  - You cannot talk to your other people or ask for help!
 
# Task 0 - Fizz Buzz

### Objectives
- Create your own empty repository in your github account called fizzbuzz (Public)
- Create a local repository on your computer called fizzbuzz-yourname and set the github repository as remote 
- Write a python program to solve the problem given below
- Add, Commit and Push the code
- In your openbook final repository(the one you cloned) create a file called task0.link and paste the https link to clone your fizzbuzz github repo.  

### Problem 
 "Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”."
 
 
# Task 1 - File copy 

### Objectives

Write the solution in task1.py
You are to create a program that does text file copying. But with a twist!

    - You get a target file name and (optionally a target folder) 
    - Copy specific pages of text to a new file (Assume 25 lines to be a page of a text)
    - Copy with l33t code on (Write a function for this!)
    - Create a menu to provide these options and get all the input from the users
    
Also, when done copying display a report indicating success and the count of pages, line and words copied and the count of alphabetic characters and also a count of numeric characters written. 

Please ensure that the code handles errors in user input or system faluts. [Handle exceptions]


### l33t code rules

    - Replace o or O with 0(number) and a or A with 4
    - Replace e or E with 3 and i or I with 1
    - Words ending with (suffix) "-er" ends with "-xor" or "-zor" [ hacker -> h4x0r) 


# Task 2 - Directory Details

### Objectives

Write the solution in task2.py

1. Traverse through a target directory collecting all the directories and sub-directories and files in them. For each directory you find create a dictonary that contains the folders as keys and files as values. (Write a function for this and call it)
2. Write the files names in the target directory and it's subfolders to a file called file.list in the following format 
    - FileName - Extension - Character Count 
3. Write the sub-folder names in the target directory and it's subfolders to a file called folder.list, apply l33t code. [import from task1.py]
4. How can you check if this works correctly? Write test Cases.

# Task 3 - Book Play?

Write the solution in task3.py
The books are Book1.txt, Book2.txt, Book3.txt and they are found in your repo.
You also have a file called 20k.txt that contains a list of common english words. Using this you can find the characters and nouns in the books. 

### Objectives

    1. Find words in Books that are non present in 20k.txt [Do it for each book]
    2. Find words in the 20k.txt that are non present in any Books
    3. Write the result of part (1) to bookXuniqu.list [X is the book number]
    4. Write the result of part (2) to rarewords.list
  



# Task 4 - APIC-EM API

You are given a code to talk to the APIC-EM sandbox controller in the files, create-ticket.py and get-network-hosts.py through RESI. 
The API-DOCS can be found at https://developer.cisco.com/site/apic-em/docs/api.gsp

### Objectives
[Create a newfile called task4.py and import create-ticket.py to achive this]

1. Modify get-network-host.py to get-interface and display / return a dict that contains the interfaces with their deviceId and macAddress tuple as keys and portName as values. [This should be done on the same file and you have to change the api call]

2. Write a new function called gethostcount that gets the count of hosts. (The API can be found under Inventory -> network-device -> count)


Use the controller at: https://sandboxapic.cisco.com/

### Max time: 3 hours!
