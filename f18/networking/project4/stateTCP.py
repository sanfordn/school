#############################
##  Nick Sanford
##  stateTCP.py
##  11/15/2018
#############################


#function that changes state of program
def changeState(state,choice):
    if state == "CLOSED":
        if choice == "passive open":
	        #closed -> listen
            return ("<nothing>","LISTEN")
        elif choice == "active open":
	        #CLOSED -> SYN_SENT
            return ("SYN","SYN_SENT")
        else:
            return ("INVALID","CLOSED")
    elif state == "LISTEN":
        if choice == "SYN":
	        #LISTEN -> SYN_RCVD
            return ("SYN,ACK","SYN_RCVD")
        else:
            return ("INVALID","LISTEN")
    elif state == "SYN_RCVD":
        if choice == "ACK":
	        #SYN_RCVD -> ESTABLISHED
            return ("<nothing>","ESTABLISHED")
        elif choice == "close":
	        #SYN_RCVD -> FIN_WAIT_1
            return ("FIN","FIN_WAIT_1")
        else:
            return ("INVALID","SYN_RCVD")
    elif state == "SYN_SENT":
        if choice == "SYN,ACK":
	        #SYN_SENT -> ESTABLISHED
            return ("ACK","ESTABLISHED")
        elif choice == "SYN":
	        #SYN_SENT -> SYN_RCVD
            return ("SYN,ACK","SYN_RCVD")
        elif choice == "close":
	        #SYN_SENT -> CLOSED
            return ("close","CLOSED")
        else:
            return ("INVALID","SYN_SENT")
    elif state == "ESTABLISHED":
        if choice == "close":
	        #ESTABLISHED -> FIN_WAIT_1
            return ("FIN","FIN_WAIT_1")
        elif choice == "FIN":
            #ESTABLISHED -> CLOSE_WAIT
            return ("ACK","CLOSE_WAIT")
        else:
            return ("INVALID","ESTABLISHED")
    elif state == "FIN_WAIT_1":
        if choice == "FIN":
            #FIN_WAIT_1 -> CLOSING
            return ("ACK","CLOSING")
        elif choice == "FIN,ACK":
            #FIN_WAIT_1 -> TIME_WAIT
            return ("ACK","TIME_WAIT")
        elif choice == "ACK":
            #FIN_WAIT_1 -> FIN_WAIT_2
            return ("<nothing>","FIN_WAIT_2")
        else:
            return ("INVALID","FIN_WAIT_1")
    elif state == "CLOSING":
        if choice == "ACK":
            #CLOSING -> TIME_WAIT
            return ("<nothing>","TIME_WAIT")
        else:
            return ("INVALID","CLOSING")
    elif state == "CLOSE_WAIT":
        if choice == "close":
            #CLOSE_WAIT -> LAST_ACK
            return ("FIN","LAST_ACK")
        else:
            return ("INVALID","CLOSE_WAIT")
    elif state == "FIN_WAIT_2":
        if choice == "FIN":
            #FIN_WAIT_2 -> TIME_WAIT
            return ("ACK","TIME_WAIT")
        else:
            return ("INVALID","FIN_WAIT_2")
    elif state == "LAST_ACK":
        if choice == "ACK":
            #LAST_ACK -> CLOSED
            return("<nothing>","CLOSED")
        else:
            return ("INVALID","LAST_ACK")
    else:
        #JUST IN CASE TEST
        print("Reached an invalid state")

state = "CLOSED"
choice = ""

while choice != "quit":
    print("Current State is: {}\n".format(state))
    choice = input("Choice:")
    send,state = changeState(state,choice)
    if send == "INVALID":
        print(send)
    elif state == "TIME_WAIT":
	#print current state and change to close because
	#time_wait doesn't do anything beside switch to close
        print("Current State is: {}".format(state))
        state = "CLOSED"
    else:
        print("\nrecv: {}".format(choice))
        print("send: {}".format(send))
#broken out of while loop and quitting
print("Quitting!")
