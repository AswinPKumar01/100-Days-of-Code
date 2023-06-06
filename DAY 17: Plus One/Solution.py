class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        arr_str =  ""
        for i in digits:
            arr_str += str(i)

        num = str(int(arr_str) +1)

        return [int(num[i]) for i in range(len(num))]
