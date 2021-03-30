
class Directory():
    def __init__(self):
        self.number_of_friends = 0
        self.friends = []
    
    def add_friend(self, friend):
        self.number_of_friends +=1
        self.friends.append(friend)

    def delete_friend(self, fname, lname):
        for friend in self.friends:
            if friend.FName == fname and friend.LName == lname:
                self.friends.remove(friend)
                self.number_of_friends -=1
                return friend.FName + ' ' + friend.LName + ' removed from directory \n'
        return "friend not found \n"
    
    def modify(self):
        name = input("Who is the person you would like to modify")
        if self.friends.count(FName == name) == 1:
            mod = input("Would you like to modify their first name, last name, age, primary phone number, or secondary phone number?")
        elif self.friends.count(FName == name) == 0:
            return "Sorry no such person was found"
        elif self.friends.count(FName == name) > 1:
            name2 = input("What is their last name?")
    
    def toString(self, friend):
        print("First Name: "+str(friend.FName)+' , '+'Last Name: '+str(friend.LName)+' , '+'Primary Number: '+str(friend.phone1)+' , '+'Secondary Number: '+
        str(friend.phone2)+' , '+'Age: '+str(friend.age)+ '\n')




class Friend():
    def __init__(self, FName, LName, phone1 = None, phone2 = None, age = None):
        self.FName = FName
        self.LName = LName
        self.phone1 = phone1
        self.phone2 = phone2
        self.age = age
    
    def get_first_name(self):
        return self.FName
    
    def get_last_name(self):
        return self.LName
    
    def get_phone1(self):
        return self.phone1
    
    def get_phone2(self):
        return self.phone2
    
    def get_age(self):
        return self.age
    
    def set_first_name(self, name):
        self.FName = name
    
    def set_last_name(self, name):
        self.LName = name
    
    def set_phone1(self, num):
        self.phone1 = num
    
    def set_phone2(self, num):
        self.phone2 = num
    
    def set_age(self, num):
        self.age = num


    



    
    

