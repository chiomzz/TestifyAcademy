//Return the number of vowels in a string

const vowels = ['a', 'e', 'i', 'o', 'u']

    // Initialize count
function countVowel(text){
    
    let count = 0


   // Loop through string to test if each character is a vowel

        for (let letter of text.toLowerCase()){
            if (vowels.includes(letter)) {
                count = count + 1
            }
        }
  // Return number of vowels
        return count
}





// const vowels = ["a", "e", "i", "o", "u"]


// function countVowels(text) {
// // Initialize counter
// let count = 0;


// // Loop through text to test if each character is a vowel
// for (let letter of text.toLowerCase()){
//     if (vowels.includes(letter)) {
//        count++
//     }
// }


// // Log formatted response to console
// console.log(`The text contains ${count} vowels`)


// // Return number of vowels
// return count
// }



// countVowels('Return the number of vowels in a string')

