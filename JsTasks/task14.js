
// const books= [
//         {
//     title: 'Dream Come True',
//     description: 'Fiction',
//     numberOfPages: 240,
//     author: 'Richard Price',
//     reading: false,

//         },
//         {
//     title: 'My First JavaScript',
//     description: 'Engineering',
//     numberOfPages: 15,
//     author: 'Chioma Ikerionwu',
//     reading: true,

//         },
//         {
//     title: 'Flowers',
//     description: 'True Live Story',
//     numberOfPages: 80,
//     author: 'Adeola',
//     reading: true,

//         }
// ]


// for (let i=0; i<books.length; i++) {
//     if (books[i].reading === true) {
//         console.log (books[i]);
//     }

// }

// for(let i=0; i<books.length; i++){
//     if(books[i].reading===true){
//         console.log(books[i]);
//     }
// }





//Use a for-loop to loop through the books array and log all books 
// where the reading status is true to the console

const books = [
    {
        title: 'My JavaScript',
        description: 'Enginnering',
        numberOfPages: 25,
        author: 'Chioma',
        reading: false,

},

    {
    title: 'Dream Come True',
    description: 'True Live Story',
    numberOfPages: 55,
    author: 'Chioma Ik',
    reading: true,

},
    {   
    title: 'Unveiling',
    description: 'Fiction',
    numberOfPages: 30,
    author: 'Chioma Ikerionwu',
    reading: false,

},

]
for (let i=0; i<books.length; i++){
    if(books[i].reading===true){
        console.log(books[i]);
    }
}