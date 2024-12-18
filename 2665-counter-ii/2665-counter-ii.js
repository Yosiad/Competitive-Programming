/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let counter= init;
    function print(){
    }
    print.increment=()=>{
        return ++counter;
    }
    print.decrement=()=>{
        return --counter;
    }
    print.reset=()=>{
        counter=init;
        return counter;
    }
    return print
    
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */