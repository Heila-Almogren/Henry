# Initial Knowledge
attributes = \
    {'mammal': {'dog', 'cat', 'horse', 'Lion', 'Cheetah'},
     'fast': {'dog', 'horse', 'Cheetah'},
     'reptile': {'frog', 'turtle', 'dinosaur'},
     'cute': {'dog', 'cat'},
     'scary': {'dinosaur', 'Lion'}}

# Temporary sets to store specified attributes to be used later
common_attributes = set([])
excluded_attributes = set([])
excluded_animals = set([])
possible_output = set([])
# to reboot game
reboot = False

# to count rounds
n_round = 0


def main():
    global reboot, n_round, common_attributes, excluded_attributes, excluded_animals, possible_output
    global n_round
    reboot = True

    while reboot:
        print('Henry: let\'s start')
        common_attributes = set([])
        excluded_attributes = set([])
        excluded_animals = set([])
        possible_output = set([])
        n_round += 1
        reboot = False
        search(attributes)


def search(dic):

    # print(dic)
    global reboot, excluded_animals, n_round, possible_output

    if len(dic) == 0:
        give_up('')
        return

    # first case: one attribute is remaining
    iterator = iter(dic)
    current = next(iterator)

    if len(possible_output) == 1 or len(dic) == 1 or len(common_attributes) == len(dic):
        possible_outcome = possible_output.pop()
        print('Henry: is it', possible_outcome, '?')
        possible_output.add(possible_outcome)

        repeater = True
        ans = input().upper()

        while repeater:

            if ans != 'Y' and ans != 'N':
                print('Henry: That\'s not neither Y or N! ', 'is it', possible_outcome, ' or not?')
                ans = input().upper()
                repeater = True
            else:
                repeater = False

        if ans == 'Y':
            print('Henry: HURRAAAY!! ')
            print('Henry:Nice game, friend! Would like to play again?')

            repeat = input().upper()

            repeater = True
            while repeater:

                if repeat != 'Y' and ans != 'N':
                    print('Henry: That\'s not neither Y or N! ', 'is it', possible_outcome, ' or not?')
                    repeat = input().upper()
                    repeater = True
                else:
                    repeater = False

            if repeat == 'Y':
                main()
            if repeat == 'N':
                print('Henry: Bye then, see you later!')
                exit(0)

        if ans == 'N':
            give_up(possible_outcome)
        return

    while current in common_attributes:
        current = next(iterator)

    print('is it', current, '?')
    ans = input().upper()

    repeater = True

    while repeater:

        if ans != 'Y' and ans != 'N':
            print('Henry: That\'s not neither Y or N! ', 'is it', current, ' or not?')
            ans = input().upper()
            repeater = True
        else:
            repeater = False

    if ans == 'Y':
        # Record as a global common attribute
        common_attributes.add(current)
        possible_output = set(dic[current])
        dic_rec = {}
        for key in dic.keys():
            if not possible_output.isdisjoint(dic[key]):
                dic_rec[key] = possible_output.intersection(dic[key])
                possible_output.union(dic_rec[key])
        if dic_rec == {}:
            # print('reached out')
            give_up('')
        else:
            # print('sent', dic_rec)
            # print('possible_output:', possible_output)
            search(dic_rec)

    if ans == 'N':
        if excluded_animals != set([]):
            excluded_animals = excluded_animals.union(dic[current])
        else:
            excluded_animals = dic[current].copy()
        dic_rec = {}
        for key in dic.keys():
            diff = dic[key].difference(excluded_animals)
            if diff != set([]):
                dic_rec[key] = diff
        possible_output.difference_update(excluded_animals)
        search(dic_rec)


def give_up(wrong_answer):

    global reboot

    print('Henry: hmm.. What\'s the correct answer then?!')
    correct = input().lower()

    repeater = True

    while repeater:

        if correct == '':
            print('Henry: Seriously.. WHAT IS THE CORRECT ANSWER!?')
            correct = input().lower()
            repeater = True
        else:
            repeater = False

    if wrong_answer == '':
        print('Henry: Hmm, what\'s special about ', correct, '?')

    else:
        print('Henry: Really :\\ and What\'s the difference between ', correct, ' and ', wrong_answer, '?!')

    print('(write a single property like: fast)')
    new_property = input().lower()

    repeater = True

    while repeater:

        if new_property == '':
            print('Henry: HEY!? I WANT TO KNOW WHAT\'S SPECIAL ABOUT', correct.upper(), '!')
            new_property = input().lower()
            repeater = True
        else:
            repeater = False

    if not wrong_answer == '':
        print('Henry: wait, which one is ', new_property, '? ', correct, ' or ', wrong_answer, '?')
        property_owner = input().lower()

        repeater = True

        while repeater:

            if property_owner == '':
                print('Henry: You heard my question right? WHICH ONE!?')
                property_owner = input().lower()
                repeater = True
            else:
                repeater = False

    else:
        property_owner = correct

    common_attributes.add(new_property)
    for k in common_attributes:
        if k in attributes:
            attributes[k].add(property_owner)
        else:
            attributes[k] = {property_owner}

    # print('common attributes updated: ', common_attributes)
    # print('attributes updated: ', attributes)
    print('Henry: Ok! Let\'s play again :D')
    print('----------- ROUND ', n_round, ' -----------')
    reboot = True


if __name__ == "__main__":
    main()
