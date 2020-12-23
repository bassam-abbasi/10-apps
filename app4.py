import journal

def print_app_header():
    print('-------------------------')
    print('     Journal App')
    print('-------------------------')


def run_event_loop():
    cmd = 'pff'
    journal_list =[]
    while cmd!='x':
        cmd = input(' Enter your choice, [L]ist , [A]dd or E[X]it :')
        cmd = cmd.lower().strip()

        if cmd == 'l':
            journal.save(journal_list, 'default')
            journal_list = journal.load('default')
            list_journal(journal_list)
        elif cmd == 'a':
            add_journal(journal_list)
        elif cmd == 'x':
            journal.save(journal_list,'default')
            print ('Existing...')
        else:
            print("Sorry, Didn't understand {}".format(cmd))


def list_journal(journal):
    reverse_journal = reversed(journal)
    for indx, entry in enumerate(reverse_journal):
        print ("* [{}], {}".format(indx, entry))


def add_journal(journal_data):
    data = input("Enter your text, <enter> to return:  ")
    journal.add_entry(data, journal_data)


def main():
    print_app_header()
    run_event_loop()



if __name__ == '__main__':
    main()