from collections import defaultdict


def groupAnagram(strs: list[str]) -> list[list[str]]:

    sols = defaultdict(list)

    for i in range(0, len(strs)):
        key = "".join(sorted(strs[i]))
        sols[key].append(strs[i])

    return list(sols.values())


print(groupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"]))
