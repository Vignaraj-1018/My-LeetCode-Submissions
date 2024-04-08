/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    res = {}
    this.forEach((item)=>{
        cur = fn(item);
        if( res.hasOwnProperty(cur)){
            res[cur].push(item);
        }
        else{
            res[cur] = [item];
        }
    });
    return res;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */