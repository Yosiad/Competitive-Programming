/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function(nums, target) {
   nums.sort((a, b) => a - b); // Sort the array in ascending order
let closestSum = Infinity;

for (let i = 0; i < nums.length - 2; i++) {
    let left = i + 1;
    let right = nums.length - 1;

    while (left < right) {
        const currentSum = nums[i] + nums[left] + nums[right];

        if (Math.abs(currentSum - target) < Math.abs(closestSum - target)) {
            closestSum = currentSum;
        }

        if (currentSum < target) {
            left++;
        } else if (currentSum > target) {
            right--;
        } else {
            return currentSum; // If exact match is found
        }
    }
}

return closestSum;
};