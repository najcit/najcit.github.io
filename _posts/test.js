
function countFun(numsArr, size, lower, upper) {
    let result = 0;
    if(size > 0){
        let sum = [];
        for (let i = 0; i < size; i++) {
            sum.push(0);
            for(let j = 0; j < sum.length; j++){
                sum[j] = numsArr[i] + sum[j];
                if(sum[j] >= lower && sum[j] <= upper){
                    result++;
                }
            }
            
        }
    }
    return result;  
}