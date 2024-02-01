/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProfit=0;
    let buy=prices[0];
    for(let i=1; i<prices.length; i++){
        if (buy>prices[i]){
            buy=prices[i];
        }
        else if(maxProfit<prices[i]-buy){
            maxProfit=prices[i]-buy;
        }
    }
    return maxProfit;
};