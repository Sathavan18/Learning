A list is a data structure able to store values at certain indexes. They hold strucutre. Elements can be moved throughout the list through methods like sort etc but unless acted upon, they remain as they were constructed. List lookup would be O(n) time complexity, as in the worst case scenario, the value wanteed is last in the list.

A set is an unordered list, containing no duplicates. Choose this if only existence of a value is required. Set lookup would be O(1) time complexity, as Python uses hashing to check quickly.

A dictionary is a data structure containing pairs of key and value. Choose this if you need the context of a value such as frequency. Dictionary lookup would be O(1) time complexity, as Python uses hashing to check quickly.

Frequency count pattern is when you want to see of much of an element is in a provided string,list etc. For this use dictionaries to keep count of the frequency. 

Complement lookup is the pattern where there are pairs within a provided string or list that you may require. For this pattern, check what the complement of your current value is and check if you have added it to the dictionary.

Two Sum Optimal:
def twoSum(nums,target):
    complement_dict = dict()
    for i in range (len(nums)):
        if target - nums[i] in complement_dict:
            return [complement_dict[target-nums[i]], i]
        else:
            complement_dict[nums[i]] = i

Ransom Note:
def canConstruct(ransomNote, magazine):
    mag_letters = dict()
    for characters in magazine:
        if characters in mag_letters:
            mag_letters[characters] += 1
        else:
            mag_letters[characters] = 1
    for characters in ransomNote:
        if characters in mag_letters:
            mag_letters[characters] -= 1
            if mag_letters[characters] < 0:
                return False
        else:
            return False 
    return True