//Sort an array of numbers in descending order

const age =[17, 20, 15, 70, 55, 82, 18, 77]


age.sort(function(a,b){
    if (a > b){
        return -1
    }else if (b > a){
        return 1
    } else {
        return 0
    }
})
console.log(age)