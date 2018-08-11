/*
  leetCode #6

  ZigZag Conversion

  Description:
  The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
  (you may want to display this pattern in a fixed font for better legibility)
  P   A   H   N
  A P L S I I G
  Y   I   R
  And then read line by line: "PAHNAPLSIIGYIR"
  
  Example:
  Input: s = "PAYPALISHIRING", numRows = 3 => Output: "PAHNAPLSIIGYIR"
  Input: s = "PAYPALISHIRING", numRows = 4 => Output: "PINALSIGYAHRPI"
*/
var convert = function(s, numRows) {
  if (numRows === 0) return "";
  else if (numRows === 1) return s;

  var pointer = 0;
  var forward = true;
  var rows = Array(numRows).fill("");
  for (var i = 0; i < s.length; i++) {
    rows[pointer] += s[i];

    if (forward) {
      pointer += 1;
      if (pointer === numRows - 1) {
        forward = !forward;
      }
    } else {
      pointer -= 1;
      if (pointer === 0) {
        forward = !forward;
      }
    }
  }
  return rows.reduce((acc, val) => acc + val, "");
};

/*
  leetCode #7

  Reverse Integer

  Description:
  Given a 32-bit signed integer, reverse digits of an integer.
  
  Note:
  Assume we are dealing with an environment which could only store integers within the 32-bit signed integer 
  range: [−231,  231 − 1]. For the purpose of this problem, 
  assume that your function returns 0 when the reversed integer overflows.
  
  Example:
  Input: -123 => Output: -321
*/
const MAX_VALUE = Math.pow(2, 31) - 1;
const MIN_VALUE = -1 * Math.pow(2, 31);

var reverse = function(x) {
  if (x < MIN_VALUE || x > MAX_VALUE) return 0;
  var str = x.toString();
  var mid = str.length % 2 == 0 ? "" : str[Math.floor(str.length / 2)];
  var firstHalf = "";
  var restHalf = "";
  for (var i = 0; i < Math.floor(str.length / 2); i++) {
    firstHalf = firstHalf + str[str.length - 1 - i];
    restHalf = str[i] + restHalf;
  }
  str = parseInt(firstHalf + mid + restHalf);

  if (str < MIN_VALUE || str > MAX_VALUE) return 0;
  return x < 0 ? -1 * str : str;
};

/*
  leetCode #8

  String to Integer (atoi)

  Description:
  Implement atoi which converts a string to an integer.

  The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. 
  Then, starting from this character, 
  takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
  The string can contain additional characters after those that form the integral number, 
  which are ignored and have no effect on the behavior of this function.
  If the first sequence of non-whitespace characters in str is not a valid integral number, 
  or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
  If no valid conversion could be performed, a zero value is returned.

  Note:
  Only the space character ' ' is considered as whitespace character.
  Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
  If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
  
  Example:
  Input: '42' => Output: 42
*/

var myAtoi = function(str) {
  let val = parseInt(str);
  if (val) {
    if (val < MIN_VALUE) return MIN_VALUE;
    else if (val > MAX_VALUE) return MAX_VALUE;
    else return val;
  } else {
    return 0;
  }
};

/*
  leetCode #9

  Palindrome Number

  Description:
  Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
  
  Example:
  Input: -123 => Output: false
*/

var isPalindrome = function(x) {
  if (x < 0) return false;
  else if (x < 10) return true;
  var revert = reverse(x);
  return x - revert === 0;
};

/*
  leetCode #10

  Regular Expression Matching

  Description:
  Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
  '.' Matches any single character.
  '*' Matches zero or more of the preceding element.
  
  Example:
  Input: s = "aa" p = "a" => Output: false
  Input: s = "aa" p = "a*" => Output: true
*/
var isMatch = function(s, p) {};
