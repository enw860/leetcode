/*
  leetCode #1

  Two Sum

  Description:
  Given an array of integers, return indices of the two numbers such that they add up to a specific target.
  You may assume that each input would have exactly one solution, and you may not use the same element twice.
  
  Example:
  Given nums = [2, 7, 11, 15], target = 9,
  Because nums[0] + nums[1] = 2 + 7 = 9,
  return [0, 1].
*/
function twoSum(nums, target) {
  for (let i = 0; i < nums.length; i++) {
    let rest = target - nums[i];
    let index = nums.slice(i + 1).indexOf(rest);
    if (index > -1) return [i, i + index + 1]
  }
};

/*
  leetCode #2

  Add Two Numbers

  Description:
  You are given two non-empty linked lists representing two non-negative integers. 
  The digits are stored in reverse order and each of their nodes contain a single digit. 
  Add the two numbers and return it as a linked list.
  You may assume the two numbers do not contain any leading zero, except the number 0 itself.
  
  Example:
  Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
  Output: 7 -> 0 -> 8
  Explanation: 342 + 465 = 807.
*/
function ListNode(val) {
  this.val = val;
  this.next = null;
}

function printListNode(node) {
  let walker = node;
  while (walker != null) {
    console.log(walker.val)
    walker = walker.next;
  }
}

function createList(arr, head = null) {
  if (arr.length === 0) return head;
  let [first, ...rest] = arr;
  if (head == null) {
    return createList(rest, new ListNode(first));
  } else {
    let temp = new ListNode(first);
    temp.next = head;
    return createList(rest, temp);
  }

}

function add(val1, val2, carry) {
  console.log(val1, val2, carry)
  let temp = val1 + val2 + carry;
  return [Math.floor(temp / 10), temp % 10];
}

let addTwoNumbers = function (l1, l2) {
  let walker1 = l1, walker2 = l2;
  let retArr = [], carry = 0, sum = 0;
  while (walker1 !== null || walker2 !== null) {
    let val1, val2;
    val1 = (walker1 === null) ? 0 : walker1.val;
    val2 = (walker2 === null) ? 0 : walker2.val;
    [carry, sum] = add(val1, val2, carry);
    retArr.push(sum);
    walker1 = walker1 ? walker1.next : walker1;
    walker2 = walker2 ? walker2.next : walker2;
  }
  if (carry > 0) retArr.push(carry)
  return createList(retArr.reverse());
};

/*
  leetCode #3

  Length Of Longest Substring

  Description:
  Given a string, find the length of the longest substring without repeating characters
  
  Example:
  Given "abcabcbb", the answer is "abc", which the length is 3.
  Given "bbbbb", the answer is "b", with the length of 1.
  Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
*/
function isValidString(str) {
  let tempStr = '';
  for (let i = 0; i < str.length; i++) {
    let index = tempStr.indexOf(str[i]);
    if (index > -1) {
      return tempStr;
    } else {
      tempStr += str[i];
    }
  }
  return str;
}

let lengthOfLongestSubstring = function (s) {
  let retStr = '';
  for (let i = 0; i < s.length; i++) {
    let subString = s.slice(i);
    let temp = isValidString(subString);
    if (temp.length > retStr.length) retStr = temp;
  }
  return retStr;
}

/*
  leetCode #4

  Median of Two Sorted Arrays

  Description:
  There are two sorted arrays nums1 and nums2 of size m and n respectively.
  Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
  You may assume nums1 and nums2 cannot be both empty.
  
  Example:
  nums1 = [1, 3]; nums2 = [2] => The median is 2.0
  nums1 = [1, 2]; nums2 = [3, 4] => The median is (2 + 3)/2 = 2.5
*/

function findKth(nums1, nums2, kth) {
  let [n, m] = [nums1.length, nums2.length];
  if (m < n) {
    return findKth(nums2, nums1, kth);
  } else if (n === 0) {
    return nums2[kth - 1];
  } else if (kth === 1) {
    return (nums1[0] < nums2[0]) ? nums1[0] : nums2[0];
  } else if (kth === n + m) {
    return (nums1[n - 1] < nums2[m - 1]) ? nums2[m - 1] : nums1[n - 1];
  }

  let mid1 = (Math.floor(kth / 2) < n) ? Math.floor(kth / 2) : n;
  let mid2 = kth - mid1;

  if (nums1[mid1 - 1] < nums2[mid2 - 1]) {
    return findKth(nums1.slice(mid1), nums2, kth - mid1);
  } else if (nums1[mid1 - 1] > nums2[mid2 - 1]) {
    return findKth(nums1, nums2.slice(mid2), kth - mid2);
  } else {
    return nums1[mid1 - 1];
  }
};

function findMedianSortedArrays(nums1, nums2) {
  let kValue = nums1.length + nums2.length;
  if (kValue % 2 === 1) return findKth(nums1, nums2, Math.floor(kValue / 2) + 1);
  return (findKth(nums1, nums2, Math.floor(kValue / 2)) + findKth(nums1, nums2, Math.floor(kValue / 2) + 1)) / 2;
};

/*
  leetCode #5

  Longest Palindromic Substring

  Description:
  Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
  
  Example:
  Input: "babad" => Output: "bab" //Note: "aba" is also a valid answer.
  Input: "cbbd" => Output: "bb"
  Input: "babaddtattarbrattatddetartrateedredividerb" => Output: "ddtattarbrattatdd"
*/

function getMaxCentroidPalindromicCount(str, position) {
  if (position === 0 || position === str.lenght - 1) return 1;

  let maxLength = 1;
  for (let i = 1; i < position + 1; i++) {
    if (str[position - i] !== str[position + i]) return maxLength;
    maxLength += 1;
  }

  return maxLength;
}

function replaceAll(s, target, replacement) {
  let str = s.slice();
  while (str.indexOf(target) > -1) {
    str = str.replace(target, replacement);
  }
  return str;
}

function maxInArray(arr) {
  return arr.reduce((acc, val) => {
    return (acc < val) ? val : acc;
  }, 0);
}

function longestPalindrome(s) {
  if (s.length === 1) return s;

  let temp = '$';
  for (let i = 0; i < s.length; i++) {
    temp = temp + s[i] + '$';
  }

  let records = [];
  for (let i = 0; i < temp.length; i++) {
    records.push(getMaxCentroidPalindromicCount(temp, i));
  }

  let maxCount = maxInArray(records);
  let index = records.indexOf(maxCount);
  let str = temp.slice(index - maxCount + 1, index + maxCount);

  return replaceAll(str, '$', '');
}