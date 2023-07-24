  def DFS(self,end_len,path,recoder):
      if len(path) == end_len:
          self.res.append(path)
      else:
          for key in recoder:
              if recoder[key] > 0:
                  recoder[key] -= 1
                  self.DFS(end_len,path+[key],recoder)
                  recoder[key] += 1


  def permute(self, nums: List[int]) -> List[List[int]]:
  # def permuteUnique(self, nums: List[int]) -> List[List[int]]:
      import collections
      recoder = collections.Counter(nums)
      self.res = []
      self.DFS(len(nums),[],recoder)
      return self.res
