# pin: Proccess Identification Number
# pid: Proccess ID or Proccess Identification
# pn: Process Name (proccess name only without the extension)
# pcn: Proccess Complete Name (complete name of the proccess)
# apsn: All Programs Same Name (all programs with one/same name)
# cm: complete name (Complete Name mode)

import os, sys, platform

def parameters():
    arguments = len(sys.argv)
    argument = sys.argv
    if arguments == 1:
        pass # run the program in default mode
    
    elif arguments == 2:
        program_help = f"""Windows Proccess Managment Tool Version 2.1 02/10/2022\nParameters Usage:\n   -cm: stands for COMPLETE MODE\n   complete_mode: COMPLETE MODE\n   -h or --help: shows this message\n\nProgram identificators:\n   pin: Proccess Identification Number\n   pid: Proccess ID or Proccess Identification\n   pn: Process Name (proccess name only without the extension)\n   pcn: Proccess Complete Name (complete name of the proccess)\n   apsn: All Programs Same Name (all programs with one/same name)\n   cm: complete mode usage (complete mode feature)\n\nExamples:\n    python3 {sys.argv[0]} : default usage\n    python3 {sys.argv[0]} -cm : complete mode option\n    python3 {sys.argv[0]} complete_mode : complete mode option\n"""
        if argument[1] == "--help" or argument[1] == "-h":
            sys.exit(program_help)

        elif argument[1] == "-cm" or argument[1] == "complete_mode":
            # just the pin and kill all proccess with the same nome of the pin, do it with pcn, pn
            return "COMPLETE_MODE"

        else:
            sys.exit(f"parameter error: try python3 {sys.argv[0]} --help")
    else:
        sys.exit(f"error error")


def onename(option,name,pids,names,cm):
    def pidstr_to_integer(pid_string):
        pid = pid_string.strip()
        try:
            return int(pid)
        except:
            pass

    pids, names = pids[1:], names[1:]
    if option == 4 and cm == None or option == 4 and cm == "COMPLETE_MODE":
        name += (25 - len(name)) * ' '
        names, pids = names[1:], pids[1:] # names and pids list
        names_number = names.count(name) # number of names (number of all names)
        lenght = len(names) == len(pids), len(names)
        kill_list = [] # list of pid's to kill
        i=0
        pid = None

        if names_number > 0: # if choiced option is 5 and there's at least one proccess name found at all proccess names
            for name_ in names: # for each proccess name in proccess names list
                pid = pids[i] # each pid in pids
                i+=1
            
                if name_ == name: # if found a proccess name that corresponds to requested proccess name, add to killing list
                    pid_to_kill = pidstr_to_integer(pid) # converts pid long string to pids short integer
                    kill_list.append(pid_to_kill) # adding the proccess name pid that attends/corresponds to requested proccess name 

            return 4, kill_list # option and pids to kill
        else:
            sys.exit(f"apsn name error: invalid proccess name")

    elif option == 1 and cm == "COMPLETE_MODE":
        kill_list = []
        i=0

        for name_ in names:
                pid = pids[i]
                i+=1
                searched_name = name_ # required name

                if i == name:
                    i = 0

                    for _name_ in names:
                        pid = pids[i]
                        i+=1

                        if _name_ == searched_name: # if found a proccess name that corresponds to requested proccess name, add to killing list
                            pid_to_kill = pidstr_to_integer(pid) # converts pid long string to pids short integer
                            kill_list.append(pid_to_kill) # adding the proccess name pid that attends/corresponds to requested proccess name 

                    return 4, kill_list #return kill_list # option updated with value 5 and pids to kill
                else:
                    # still not found
                    pass

        sys.exit(f"pin error: maybe the proccess id number is wrong!")


    elif option == 2 and cm == "COMPLETE_MODE":
        kill_list = []
        i=0

        for name_ in names:
                pid = pids[i]
                pid = pidstr_to_integer(pid)
                i+=1
                searched_name = name_ # required name

                if pid == name:
                    i = 0

                    for name_ in names: # for each proccess name in proccess names list
                        pid = pids[i] # each pid in pids
                        i+=1
            
                        if name_ == searched_name: # if found a proccess name that corresponds to requested proccess name, add to killing list
                            pid_to_kill = pidstr_to_integer(pid) # converts pid long string to pids short integer
                            kill_list.append(pid_to_kill) # adding the proccess name pid that attends/corresponds to requested proccess name 
                        else:
                            pass

                    return 4, kill_list # option updated with value 5 and pids to kill
                else:
                    pass # pid not equal to name
        sys.exit("pid error: maybe the proccess id is wrong! ")
 
    
    elif option == 3 and cm == "COMPLETE_MODE":
        if len(value) > 4:
            # check if the lasts four characters are '.exe'
            exe_check = name[-4] + name[-3] + name[-2] + name[-1]
            if exe_check != '.exe':
                # if the lasts four characters are not '.exe'
                name = name + ".exe" # appends '.exe' extension th the (value/name/proccess name given)

            else: 
                # if the lasts four characters are '.exe'
                pass
        else:
            # if the given value is not greatter than four, if it's less than four
            pass

        i = 0
        name = name + (" "*(25-len(name))) # (proccess name buffer is 25 bytes)
        kill_list = []
        for name_ in names:
            pid = pids[i]
            i+=1

            if name_ == name: # if found a proccess name that corresponds to requested proccess name, add to killing list
                pid_to_kill = pidstr_to_integer(pid) # converts pid long string to pids short integer
                kill_list.append(pid_to_kill) # adding the proccess name pid that attends/corresponds to requested proccess name 
            else:
                # name not same to required name
                pass

        if len(kill_list) == 0 : sys.exit("pn error: maybe the proccess name is wrong!")
        else: return (4, kill_list) # option updated with value 5 and pids to kill

    else:
        return option, []


def os_checking():
    try:
        system = 'Windows'
        os = [list(platform.uname())[0],platform.platform()]
        os = os[1][:7],os[0]
        boolean = os[0] == os[1]
        guess = os[0] == system or os[1] == system
        o_s = os[0] == system and os[1] == system
        if boolean is True and o_s is True:
            pass # operating system checked successfully

        elif guess == True:
            print('problem checking OS, this program may run incorrectlly')

        else:
            sys.exit('operating system must be windows')

    except Exception as err:
        sys.exit(err)

# converts number in string type to integer type
def int_convert(value,code):
    if len(str(value)) > 0:
        pass
    else:
        sys.exit(f"empty value error: no value received")
 
    try:
        try:
            if code != 3 and code != 4:
            # excepting 3, 4 and 5, because of these are non number options or strings characters options
                return int(value) # return converted string to integer
            else:
                # if it's not a number, it's letters(string chars), returns the letters(string chars) itself
                return value

        except:
            pass

    except Exception as err:
        pass

def kill_proccess(option,signterm,value,numbers,names,pids,names_pids):

    try:
        if signterm == 15:
            signterm = "" # this option terminates the program but wihtout forcing it 
        elif signterm == 9:
            signterm = " /f " # this option forces the program to stop 
        else:
            sys.exit(f"signterm error: wrong signterm code")

        if option == 1:
        # option one, PIN option (proccess identification number)
            pid = int_convert(numbers[value],1)
            command = f"taskkill{signterm}/pid {pid}"
            os.system(command)

        elif option == 2:
        # option two, PID option (proccess identification)
            command = f"taskkill{signterm}/pid {value}"
            os.system(command)

        elif option == 3:

        # option three, PN option (program name)
            # if given value is greatter than four characters
            if len(value) > 4:
            # check if the lasts four characters are '.exe'
                exe_check = value[-4] + value[-3] + value[-2] + value[-1]
                if exe_check != '.exe':
                # if the lasts four characters are not '.exe'
                    value = value + ".exe"
                    value = value+(" "*(25-len(value))) # (proccess name buffer is 25 bytes)
                    pid = names_pids[value]
                    pid = int_convert(pid,0)
                    command = f"taskkill{signterm}/pid {pid}"
                    os.system(command)

                else:
                # if the lasts four characters are '.exe'
                    value = value+(" "*(25-len(value))) # (proccess name buffer is 25 bytes)
                    pid = names_pids[value]
                    pid = int_convert(pid,0)
                    command = f"taskkill{signterm}/pid {pid}"
                    os.system(command)

            else:
            # if the given value is not greatter than four, if it's less than four
                value = value+(" "*(25-len(value))) # (proccess name buffer is 25 bytes) 
                pid = names_pids[value]
                pid = int_convert(pid,0)
                command = f"taskkill{signterm}/pid {pid}"
                os.system(command)


        elif option == 4:
            input(f"there's {len(pids)} pids that the PINs are: {pids}")
            for pid in pids:
                pid = int_convert(pid,0)
                command = f"taskkill{signterm}/pid {pid}"
                os.system(command)

        else:
            sys.exit(f"error: wrong option code {option}")

    except Exception as error:
        sys.exit(error)

# gets and manages the proccess's
def proccess():
    try:
        nn=0
        pin_pid = {} # this dict stores 'pin' as key and 'pid' as value (all pin's and pid's)
        max = 34
        min = 26
        pids = [] # proccess id's list
        number = 0
        names_pid = {}
        proccess_names = []
        data = os.popen("tasklist").read()
        line, lines = '',[]
        n = -3 # pin counter to work after 'number' var stops (this -3 stands for the first three lines in 'tasklist' command output, these first 3 lines are not necessary so we jump it and go directly to the proccess's)
        for character in data:

            if character == "ÿ": character = " "
            line += character
            if character == '\n':
                lines.append(line)
                number += 1
                n +=1 # keep incrementing like 'number' var, also/so/cause it comes to help the 'number' var
                proccess_pid = line[min:max]
                proccess_name = line[:25]
                if number == 3:
                # if counter variable is equal to one
                    pids = []
                    names_pid = {}
                    pin_pid = {}
                    lines = []
                    proccess_names = []

                proccess_names.append(proccess_name)
                pids.append(proccess_pid)
                names_pid[proccess_name] = proccess_pid
                pin_pid[n] = proccess_pid
                line = ""
                nn+=1

            else:
            # if character is not equal to break line '\n' just keep adding/appending character to 'line' variable
                pass

        n=0 # pin auxiliary var (variable that represents pin)
        print("PIN ==== ====== PCN ==================  PID=Session Name ======= Session == Mem Usage",end="\n\n")
        for each_line in lines:
            n+=1
            str_n = str(n)
            buffer_n = (8-len(str_n)) * " " # 8 is the number of PIN buffer, (bytes reserved to store PIN number)
            buffer_n = str_n + buffer_n
            print(f"{buffer_n} {each_line}",end="") # prints pin, and the complete line of proccess
        
        return pin_pid, pids, lines, proccess_names, names_pid

    except Exception as error:
        sys.exit(error)

    except:
        sys.exit()

def user_input():

    print('1.PIN, 2.PID, 3.PN, 4.APSN; and signterm: 9. force kill, 15. terminates/kill')
    try:
        user_option = input("option: ").strip()
        signterm = input("signterm: ").strip()

        if user_option == '1':
            proccess_number = input("proccess id number: ")
            return 1, signterm, proccess_number

        elif user_option == '2':
            proccess_id = input("proccess id: ")
            return 2, signterm, proccess_id

        elif user_option == '3':
            proccess_name = input("proccess name: ")
            return 3, signterm, proccess_name

        elif user_option == '4':
            one_name = input("the proccess name: ")
            return 4, signterm, one_name

        elif signterm != '9' and signterm != '15':
            sys.exit(f"signterm code must be 9 or 15!")

        else:
            sys.exit("allowed options are: 1, 2, 3 and 4.")

    except Exception as error:
        sys.exit(error)

# checks if operating system is windows
os_checking()

cm = parameters() 

pin_pid, pids, proccess_lines, proccess_names, names_pids = proccess()

# user data inputs
option, signterm, value = user_input()

# if is string number converts it to a integer number
value = int_convert(value,option)

# converts signalterm string number to a integer type
signterm = int_convert(signterm,0)

option, pids_list = onename(option, value,pids, proccess_names, cm)

# kills the proccess
kill_proccess(option,signterm,value,pin_pid,pids,pids_list,names_pids)
