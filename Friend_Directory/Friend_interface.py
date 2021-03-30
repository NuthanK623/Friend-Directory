import Friend_Directory as fd
import pickle

def main():
    run = True
    directory = pickle.load( open( "dir.pickle", "rb" ) )
    while run:
        choices = {
            1: "Display all Friends",
            2: "Search for a Friend",
            3: "Modify a Friend",
            4: "Add a Friend",
            5: "Delete a Friend",
            6: "File Dump",
            7: "Quit the Program"
        }

        characteristics = {
            1: "First Name",
            2: "Last Name",
            3: "Primary Phone Number",
            4: "Secondary Phone Number",
            5: "Age"
        }

        print("Welcome to the Friend Directory!" + '\n' + str(choices))
        user = int(input("What would you like to do?" + '\n'))

        if user == 1:
            if len(directory.friends) == 0:
                print("Your directory is empty!" + '\n')
            else:
                for i in directory.friends:
                    print(directory.toString(i))

        elif user == 2:
            if len(directory.friends) == 0:
                print("There is no one in your directory!" + '\n')
            else:
                name = input("Who are you searching for?")
                count = 0
                for i in directory.friends:
                    if i.FName == name:
                        print(directory.toString(i))
                        count +=1
                if count == 0:
                    print('Sorry, you have no friend with that name' + '\n')
        
        elif user == 3:
            if len(directory.friends) == 0:
                print("There is no one in your directory!" + '\n')
            else:
                first = input('What is the first name of the person you would like to modify?')
                last = input('And their last name? \n')
                count = 0
                for i in directory.friends:

                    if i.FName == first and i.LName == last:
                        count +=1
                        print(directory.toString(i))
                        answer = input('Is this the person you would like to modify?')
                        if answer == 'yes':
                            print(str(characteristics))
                            a = True
                            while a:
                                option = int(input('What characteristic would you like to modify?'))
                                if option == 1:
                                    name = input('What is their new first name?')
                                    i.set_first_name(name)
                                    a = False
                                    print('All Set!'+ '\n')
                                elif option == 2:
                                    name = input('What is their new last name?')
                                    i.set_last_name(name)
                                    a = False
                                    print('All Set!'+ '\n')
                                elif option == 3:
                                    num = input("What is their new Primary Phone Number?")
                                    i.set_phone1(num)
                                    a = False
                                    print('All Set!'+ '\n')
                                elif option == 4:
                                    num = input("What is their new Secondary Phone Number?")
                                    i.set_phone2(num)
                                    a = False
                                    print('All Set!'+ '\n')
                                elif option == 5:
                                    num = input("What is their new age?")
                                    i.set_age(num)
                                    a = False
                                    print('All Set!'+ '\n')
                                else:
                                    print('Please select from choices given')
                        else:
                            continue
                if count == 0:
                    print('Friend not found. Try again')

        elif user == 4:
            first = input("What is your friend's first name?")
            last = input("What is your friend's last name?")
            age = input("What is your friend's age?")
            friend = fd.Friend(first, last, age=age)
            directory.add_friend(friend)
            print("Friend added!")
        
        elif user == 5:
            if len(directory.friends) == 0:
                print("There is no one to delete!")
            else:
                first = input("What is the first name of the friend you want to delete?")
                last = input("What is the last name of the friend you want to delete?")
                print(directory.delete_friend(first,last))
        
        elif user == 6:
            for i in directory.friends:
                directory.delete_friend(i.FName, i.LName)
            print("New Directory!")

        elif user == 7:
            pickle.dump(directory, open( "dir.pickle", "wb" ))
            print("Bye!")
            run = False
        
        else:
            print("Please pick your option between choices 1 through 7 \n ")

if __name__ == "__main__":
    main()

    



    
