//My Personal Library 2

// Add a toggleReadingStatus method to your books objects. 

// The method should update the value of the reading property of the book object.

// Remember to log the reading property to the console to confirm the current status.



// const books= {
//     reading: false,
//     numberOfPages: 150,
//     publisher: 'longman',
//     toggleReadingStatus: function(){
//         if (books.reading===true){
//             books.reading=false
//         }else {
//             books.reading=true
//         }
//     }
// }

// books.toggleReadingStatus()
// console.log(books.reading)



// const books = {

//     reading: true,
//     numberOfPages: 150,
//     publisher: 'longman',
//     toggleReadingStatus: function (){
//         if (books.reading===false){
//             books.reading=true
//         }else {
//             books.reading = false
//         }
//     }
// }
// books.toggleReadingStatus()
// console.log(books.reading)



const books ={
    name: 'Dream come True',
    reading: true,
    numberOfPages: 240,
    publisher: 'longman',
    bookfans: ['chioma', 'kene', 'ife'],
    addBookFans: function (name){
        books.bookfans.push(name)
    }
    // toggleReadingStatus: function (){
    //     if (this.reading === true){
    //         books.reading = false
    //     }else {
    //         books.reading = true
    //     }
    // }

}
// books.toggleReadingStatus()
books.addBookFans('Eunice')
console.log(books)