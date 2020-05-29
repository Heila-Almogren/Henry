# Initial Knowledge
attributes = \
        {'mammal': set(['dog', 'cat', 'horse', 'Lion', 'Cheetah']),
         'fast': set(['dog','horse', 'Cheetah']),
         'reptile': set(['frog', 'turtle', 'dinosaur']),
         'cute': set(['dog', 'cat']),
         'scary': set(['dinosaur', 'Lion'])}

# Temporary sets to store specified attributes to be used later
common_attributes = set([])
excluded_attributes = set([])
excluded_animals = set([])
# to reboot game
reboot = False

# to count rounds
n_round = 0


def main():
    global reboot
    global n_round
    global common_attributes
    global excluded_attributes
    global excluded_animals

    print('Henry: let\'s start')
    while True:
        reboot = False
        n_round += 1
        common_attributes = set([])
        excluded_attributes = set([])
        excluded_animals = set([])
        if search(attributes):
            print("New Game")


def search(dic):

    if dic == {}:
        return False

    # reboot used to restore the definition when new knowledge is acquired
    global reboot, excluded_animals
    global n_round

    print('Henry: so, it can be ', dic.keys())

    # Iterate through all keys
    for key in dic.keys():

        # ask if the key is correct
        print('Henry: is it', key, '?')
        ans = input()

        # case: Wrong attribute
        if ans == 'N':
            print('Henry: hmm, OK THEN..')
            excluded_attributes.add(key)
            print(excluded_attributes, ' added to excluded attributes')

            if(excluded_animals != set([])):
                print('not empty, union')
                excluded_animals = excluded_animals.union(dic[key])
            else:
                print('empty, copy')
                excluded_animals = dic[key].copy()

            # First case: If there is only one attribute left --> take one possible output and ask the user
            if len(dic) == 1:
                print('Henry: OK, I give up.. what is it? ', dic[key], '?')
                property_owner = input()
                for k in common_attributes:
                    attributes[k].add(property_owner)

                print('common attributes updated: ', common_attributes)

                print('Henry: Ok! Let\'s play again :D')
                print('----------- ROUND ', n_round, ' -----------')
                reboot = True
            # Second case: If there are other attributes
            else:
                # Copy of dic used in inner loops
                dic_copy = dic.copy()
                dic_rec = {}
                del dic_copy[key]
                for keyCopy in dic_copy.keys():
                    print('finding differences.. ')
                    diff = dic_copy[keyCopy].difference(excluded_animals)
                    if diff != {}:
                        print('found differences')
                        dic_rec[keyCopy] = diff

                print('result of difference: ', dic_rec)


                print('Result Dictionary: ', dic_rec, 'Recursion:')
                print()
                if search(dic_rec): return False
                # if reboot is required, skip and return
                if reboot:
                    return True

        # case: Correct attribute
        if ans == 'Y':
            print(type(common_attributes))
            # Record as a global common attribute
            common_attributes.add(key)
            print(common_attributes, ' added to common attributes')

            # First case: If there is only one attribute left --> take one possible output and ask the user
            if len(dic) == 1:
                print('Henry: hmm, is it ', dic[key], '?   (Y/N)')
                ans = input()

                # If it's correct, celebrate :P
                if ans == 'Y':
                    print('Henry: I WIN!!')
                    print('Henry: Do you want to play another Round?  (Y/N)')
                    repeat = True
                    while(repeat):
                        another_round = input()
                        if another_round == 'Y':
                            repeat = False
                            print('----------- ROUND ', n_round, ' -----------')
                            reboot = True
                        else:
                            if another_round == 'N':
                                repeat = False
                                print('Henry: Bye! Nice play BTW ;D ')
                                exit(0)
                            else:
                                print('Henry: That\'s not a Y or N! DO YOU WANT ANOTHER ROUND OR NOT??  (Y/N)')

                # If it's incorrect, ask the user for a way to differentiate
                if ans == 'N':
                    print('Henry: hmm.. What\'s the correct answer then?!')
                    correct = input()
                    print('Henry: Really :\\ and What\'s the difference between ', correct, ' and ', dic[key], '?!')
                    print('(write a single property like: fast)')
                    new_property = input()
                    print('Henry: wait, which one is ', new_property, '? ' , correct , ' or ', dic[key], '?')
                    property_owner = input()
                    common_attributes.add(new_property)
                    for k in common_attributes:
                        if k in attributes:
                            attributes[k].add(property_owner)
                        else: attributes[k] = ([property_owner])

                    print('common attributes updated: ', common_attributes)
                    print('attributes updated: ', attributes)
                    print('Henry: Ok! Let\'s play again :D')
                    print('----------- ROUND ', n_round, ' -----------')
                    reboot = True

            # Second case: If there are other attributes
            else:
                possible_output = set(dic[key])
                print('possible output: ', possible_output)
                # Copy of dic used in inner loops
                dic_copy = dic.copy()
                dic_rec = {}
                del dic_copy[key]
                for keyCopy in dic_copy.keys():
                    print('finding intersections.. ')
                    if not possible_output.isdisjoint(dic_copy[keyCopy]):
                        dic_rec[keyCopy] = possible_output.intersection(dic_copy[keyCopy])
                if dic_rec != {}:
                    print('NOT EMPTY')
                    print('Result Dictionary: ', dic_rec, 'Recursion:')
                    print()
                    if search(dic_rec): return False
                else:
                    print('idk')
                # if reboot is required, skip and return
                if reboot:
                    return True


if __name__ == "__main__":
    main()