// Set the current year in the 'date' element

let date=document.getElementById('date')
const d =new Date()
let year =d.getFullYear()
console.log(d.getFullYear());
date.innerHTML=year


// Set a timeout function to automatically close the Bootstrap alert after 2500 milliseconds (2.s seconds)

setTimeout(function () {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 2500);

