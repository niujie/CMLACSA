voting_data = list(open("voting_record_dump109.txt"))

## Task 1

def create_voting_dict():
    """
    Input: None (use voting_data above)
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting
            record.
    Example: 
        >>> create_voting_dict()['Clinton']
        [-1, 1, 1, 1, 0, 0, -1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
         -1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]

    This procedure should return a dictionary that maps the last name
    of a senator to a list of numbers representing that senator's
    voting record, using the list of strings from the dump file (strlist). You
    will need to use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    You can use the split() procedure to split each line of the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.
    A "1" represents a 'yea' vote, a "-1" a 'nay', and a "0" an abstention.

    The lists for each senator should preserve the order listed in voting data. 
    """
    mydict = {}
    for line in voting_data:
        mylist = line.split()
        mydict[mylist[0]] = list(map(int, mylist[3::]))
    return mydict    

## Task 2

def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    """
    return sum([voting_dict[sen_a][i] * voting_dict[sen_b][i] for i in range(len(voting_dict[sen_a]))])


## Task 3

def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    output = ''
    minimum = -1e6
    for key in voting_dict:
        if key != sen:
            dot_product = policy_compare(sen, key, voting_dict)
            if dot_product > minimum:
                minimum = dot_product
                output = key
    return output
    

## Task 4

def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> least_similar('Klein', vd)
        'Ravella'
    """
    output = ''
    maximum = policy_compare(sen, sen, voting_dict)
    for key in voting_dict:
        if key != sen:
            dot_product = policy_compare(sen, key, voting_dict)
            if dot_product < maximum:
                maximum = dot_product
                output = key
    return output
    
    

## Task 5

most_like_chafee    = 'Jeffords'
least_like_santorum = 'Feingold' 



# Task 6

def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    dot_products = []
    for d in sen_set:
        if d != sen:
            dot_products.append(policy_compare(sen, d, voting_dict))
    return float(sum(dot_products))/len(dot_products)

most_average_Democrat = 'Biden' # give the last name (or code that computes the last name)


# Task 7

def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
    """
    output = []
    for key in sen_set:
        if output == []: output = [0] * len(voting_dict[key])
        output = [output[i] + float(voting_dict[key][i])/len(sen_set) for i in range(len(voting_dict[key]))]
    return output

average_Democrat_record = [-0.16279069767441862,
 -0.2325581395348837,
 1.0000000000000007,
 0.8372093023255818,
 0.9767441860465123,
 -0.13953488372093026,
 -0.9534883720930238,
 0.8139534883720934,
 0.9767441860465123,
 0.9767441860465123,
 0.906976744186047,
 0.7674418604651165,
 0.6744186046511629,
 0.9767441860465123,
 -0.511627906976744,
 0.9302325581395354,
 0.9534883720930238,
 0.9767441860465123,
 -0.3953488372093022,
 0.9767441860465123,
 1.0000000000000007,
 1.0000000000000007,
 1.0000000000000007,
 0.9534883720930238,
 -0.4883720930232556,
 1.0000000000000007,
 -0.3255813953488371,
 -0.06976744186046514,
 0.9767441860465123,
 0.8604651162790702,
 0.9767441860465123,
 0.9767441860465123,
 1.0000000000000007,
 1.0000000000000007,
 0.9767441860465123,
 -0.3488372093023255,
 0.9767441860465123,
 -0.4883720930232556,
 0.2325581395348837,
 0.8837209302325586,
 0.4418604651162789,
 0.906976744186047,
 -0.906976744186047,
 1.0000000000000007,
 0.906976744186047,
 -0.30232558139534876] # (give the vector)


# Task 8

def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> bitter_rivals(voting_dict)
        ('Fox-Epstein', 'Ravella')
    """
    output = ()
    maximum = []
    for key1 in voting_dict:
        for key2 in voting_dict:
            if maximum == []: maximum = policy_compare(key1, key2, voting_dict)
            if key1 != key2:
                dot_product = policy_compare(key1, key2, voting_dict)
                if dot_product < maximum:
                    maximum = dot_product
                    output = (key1, key2)
    return output

