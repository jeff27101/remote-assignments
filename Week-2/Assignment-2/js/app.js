const mywelcome = document.getElementById('mywelcome');
const button1 = document.querySelector('.button1');
const hidden = document.querySelector('.container-hidde');

mywelcome.addEventListener('click',() => {
    mywelcome.textContent = "Have a Good Time!";
})

button1.addEventListener('click', () => {
    if (hidden.style.display == 'none'){
        hidden.style.display = 'block';
        button1.textContent = 'Show Hidden';
    } else {
        hidden.style.display = 'none';
        button1.textContent = 'Call to Action';
    }
})