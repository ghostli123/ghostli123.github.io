def all_possible_sfc_break_helper(target_sfc, servers, start, max_sfc_length, DP):
    """"Returns all possible sfc instances."""
    if start == len(target_sfc):
        return [""]

    if start in DP:
        return DP[start]

    sfcs = []
    for i in range(start, start + max_sfc_length):
        if i < len(target_sfc):
            new_sfc = target_sfc[start: i + 1]
            if new_sfc not in servers:
                continue
            sub_sfcs = all_possible_sfc_break_helper(target_sfc, servers, i + 1, max_sfc_length, DP)
            for sfc in sub_sfcs:
                extra_space = "" if len(sfc) == 0 else " "
                sfcs.append(new_sfc + extra_space + sfc)

    DP[start] = sfcs
    return sfcs


def all_possible_sfc_instances_helper(target_sfc, servers):
    DP = dict()
    max_sfc_length = len(max(servers, key=len))
    return all_possible_sfc_break_helper(target_sfc, servers, 0, max_sfc_length, DP)

def subsets(self, nums):
        #nums.sort()
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result

def longest_common_substring(s1, s2):
   m = [[0] * (1 + len(s2)) for i in xrange(1 + len(s1))]
   longest, x_longest = 0, 0
   for x in xrange(1, 1 + len(s1)):
       for y in xrange(1, 1 + len(s2)):
           if s1[x - 1] == s2[y - 1]:
               m[x][y] = m[x - 1][y - 1] + 1
               if m[x][y] > longest:
                   longest = m[x][y]
                   x_longest = x
           else:
               m[x][y] = 0
   return s1[x_longest - longest: x_longest]

if __name__ == '__main__':
    servers = {"ab", "bcd", "cde"}
    #preprocessing with subsets and lcs
    target_sfc = "abcde"
    print all_possible_sfc_instances_helper(target_sfc, servers)
