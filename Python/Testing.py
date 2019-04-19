class Range(object):
    def __init__(self):
        self.lower_bound = -1
        self.upper_bound = -1

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "[" + str(self.lower_bound) + "," + str(self.upper_bound) + "]"


def find_range(input_list,input_number):
    ans = Range()
    first = True
    for i in range(0,len(input_list)):
        if input_list[i] == input_number:
            if i < ans.lower_bound:
                if first is True:
                    ans.lower_bound = i
                    first = False
            if i > ans.upper_bound:
                ans.upper_bound = i
    return ans


print(find_range([1,2,5,5,8,8,10],8))