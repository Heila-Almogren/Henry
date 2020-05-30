# Initial Knowledge
attributes = \
    {'mammal': set(['dog', 'cat', 'horse', 'Lion', 'Cheetah']),
     'fast': set(['dog', 'horse', 'Cheetah']),
     'reptile': set(['frog', 'turtle', 'dinosaur']),
     'cute': set(['dog', 'cat']),
     'scary': set(['dinosaur', 'Lion'])}

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
    global reboot
    global n_round

    print('Henry: let\'s start')

    reboot = False
    n_round += 1

    search(attributes)


def search(dic):

    print(dic)
    global reboot, excluded_animals, n_round, possible_output

    if len(dic) == 0:
        give_up('')

    # first case: one attribute is remaining
    iterator = iter(dic)
    current = next(iterator)

    if len(possible_output) == 1 or len(dic) == 1:
        print('is it', next(iter(possible_output)),'?')
        return

    while current in common_attributes and not len(common_attributes) == len(dic):
        current = next(iterator)

    print('is it', current, '?')
    ans = input()

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
            print('reached out')
        else:
            print('sent', dic_rec)
            print('possible_output:', possible_output)
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
        search(dic_rec)


def give_up(wrong_answer):


    print('Henry: hmm.. What\'s the correct answer then?!')
    correct = input().lower()

    if not wrong_answer == '':
        print('Henry: Really :\\ and What\'s the difference between ', correct, ' and ', wrong_answer, '?!')
    else:
        print('Henry: Hmm, what\'s special about ', correct, '?')

    print('(write a single property like: fast)')
    new_property = input().lower()
    print('Henry: wait, which one is ', new_property, '? ', correct, ' or ', wrong_answer, '?')
    property_owner = input().lower()
    common_attributes.add(new_property)
    for k in common_attributes:
        if k in attributes:
            attributes[k].add(property_owner)
        else:
            attributes[k] = set([property_owner])



    print('common attributes updated: ', common_attributes)
    print('attributes updated: ', attributes)
    print('Henry: Ok! Let\'s play again :D')
    print('----------- ROUND ', n_round, ' -----------')
    ans = input.lower()



if __name__ == "__main__":
    main()