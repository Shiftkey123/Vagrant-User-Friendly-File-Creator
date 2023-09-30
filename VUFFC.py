#Vagrant User Friendly File Creator
#Created by: Austin Schuller, 2023
#Version: 1.0.0
#Last Update: 9/29/23

#os module for opening and running the Vagrantfile
import os
import time


#Simple file creator: Can name box, and download box || See Advanced file creator for more options
def vagrant_simple():
    print("<<Selected Type: Simple>>")
    time.sleep(0.5)
    #Name of the virtual machine within Virtualbox
    operating_system_name = input("Name of Operating System: ").lower()
    #Name of the box || GET FROM VAGRANT CLOUD
    vagrant_box = input("Input name of the preferred box: ")


    #Simple file code
    code_line1 = "Vagrant.configure('2') do |config|"
    code_line2 = (f"  config.vm.define '{operating_system_name}' do |{operating_system_name}|")
    code_line3 = (f"    {operating_system_name}.vm.box = '{vagrant_box}'")
    code_line4 = (f"    {operating_system_name}.vm.provider 'virtualbox' do |vb|")
    code_line5 = (f"      vb.name = '{operating_system_name}-vagrant'")
    code_line6 = "    end"
    code_line7 = "  end"
    code_line8 = "end"

    #Writes lines to Vagrantfile after it's created
    WRITE = [code_line1, "\n", code_line2, "\n", code_line3, "\n", code_line4, "\n", code_line5, "\n", code_line6, "\n", code_line7, "\n", code_line8]

    #Creates and opens the Vagrantfile then writes the lines to it
    file = open("Vagrantfile", "x")
    file.writelines(WRITE)
    #Closes and saves the Vagrantfile
    file.close()

    #Runs the Vagrantfile and begins the install/opening of the virtual machine
    os.system("vagrant up")


#start of the program
def main():
    print("Welcome to: Vagrant User Friendly File Creator(VUFFC)")
    print("Please select the type of Vagrantfile you would like to create...")
    #Choose which type of Vagrantfile you want to make
    vagrant_type = input("Simple/Advanced/Custom: ").lower()
    #makes simple Vagrantfile with user input
    if vagrant_type == "simple":
        vagrant_simple()
    #WIP
    if vagrant_type == "advanced":
        pass
    #WIP
    if vagrant_type == "custom":
        pass

#Redundancies
if __name__ == "__main__":
    main()