/**
 * @param {number} num
 * @return {number[]}
 */
var closestDivisors = function(num) {
    let nums=[1, num]
    for(let s=Math.floor(Math.sqrt((num+3)));s>=1; s--){
        if(Number.isInteger((num+1)/s)){
            if(Math.abs(nums[1]-nums[0])>((num+1)/s-s)){
                nums=[s,(num+1)/s];
                break;
            }
        }
        if(Number.isInteger((num+2)/s)){
            if(Math.abs(nums[1]-nums[0])>((num+2)/s-s)){
                nums=[s,(num+2)/s];
                break;
            }
        }
    }
    return nums;
    
};