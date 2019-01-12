/*
Given n non-negative integers a1, a2, ..., an , 
where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints 
of line i is at (i, ai) and (i, 0). Find two lines, 
which together with x-axis forms a container, 
such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
*/
var min = (...args) => {
  return args.reduce((acc, val) => {
    return (acc > val)? val:acc;
  }, args[0]);
}

var checkAllPositive = arr => {
  return arr.reduce((acc, val) => {
    return val > -1 && acc;
  }, true);
}

var maxArea = function(height) {
  if(height.length === 0 || !checkAllPositive(height)){
    return -1;
  }

  let maxAmount = 0;  
  let length = height.length - 1;
  let [headCur, tailCur] = [0, length];

  while(headCur != tailCur){
    var currentAmount = min(height[headCur], height[tailCur]) * length;  
    
    if(currentAmount > maxAmount){
      maxAmount = currentAmount;
    }
    
    if(height[headCur] > height[tailCur]){
      tailCur -= 1;
    }else{
      headCur += 1;
    }
    
    length -= 1;
  }

  return maxAmount;
};

/*
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
*/
var arraifyNum = num => {
  num = num.toString();
  
  while(num.length != 4){
    num = "0" + num;
  }

  return num.split("").map(val => parseInt(val));
}

var numRules = (num, small_unit, middle_unit, top_unit) => {
  if(num === 0){
    return "";
  }else if(num < 4){
    return Array(num).fill(small_unit).join("");
  }else if(num === 4){
    return small_unit + middle_unit;
  }else if(num === 5){
    return middle_unit;
  }else if(num < 9){
    return middle_unit + Array(num-5).fill(small_unit).join("");
  }else{
    return small_unit + top_unit;
  }
}

var intToRoman = function(num) {
  if(num < 0 || num > 4000){
    return "Error: Out Of Range Number";
  }  

  return arraifyNum(num).map((val, index) => {
    switch(index){
      case 0: return numRules(val, 'M', '', '');
      case 1: return numRules(val, 'C', 'D', 'M');
      case 2: return numRules(val, 'X', 'L', 'C');
      case 3: return numRules(val, 'I', 'V', 'X');
    }
  }).join("");
};

var romanChar = {'I': 1, 'V':5, 'X':10, 'L':50,'C':100, 'D':500, 'M':1000}
var romanToInt = function(s) {
    var value = 0;
    for(var i=0; i<s.length; i++){
      if(i < s.length-1){
        if(romanChar[s[i]] < romanChar[s[i+1]]){
          value = value + romanChar[s[i+1]] - romanChar[s[i++]]
          continue;
        }
      }
      value += romanChar[s[i]];
    }
    return value;
};


/*
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
*/
var longestCommonPrefix = function(strs) {
  if(strs.length === 0) return "";

  let shortesStrLen = strs.reduce((acc, val) => {
    return acc > val.length? val.length:acc;
  }, 99999);

  while(shortesStrLen > 0){
    strs = strs.map(val => {
      return val.substring(0, shortesStrLen);
    });

    let allPrefixMatched = strs.map(val => {
      return val === strs[0]
    }).reduce((acc, val) => acc && val, true);

    if(allPrefixMatched){
      return strs[0];
    }else{
      shortesStrLen -= 1;
    }
  }

  return "";
};

/*
Given an array nums of n integers, are there elements a, b, c in nums 
such that a + b + c = 0? Find all unique triplets in the array 
which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.
*/
var threeSum = function(nums) {
  let save = [];
  nums.sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 2; i++) {
    if (nums[i] > 0) break;

    if (i > 0 && nums[i] === nums[i - 1]) continue;

    let l = i + 1, r = nums.length - 1;
    while (l < r) {
      if (l - i > 1 && nums[l] === nums[l - 1]){
        l++; continue;
      }

      let sum = nums[i] + nums[l] + nums[r];

      if (sum === 0) {
        save.push([nums[i], nums[l], nums[r]]);
      }

      if (sum > 0) r--;
      else l++;
    }
  }

  return save;
}