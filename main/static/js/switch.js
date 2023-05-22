let body = document.querySelectorAll('body')
let david = document.querySelectorAll('.david')
let icon = document.querySelectorAll('.bi-full-moon')

david.addEventListener('click', ()=>{
    body.classList.toggle('dark')
    if(body.classList.contains('dark')){
        icon.classList.replace('bi-moon-fill', 'bi-sun-fill')
    }
    else{
        icon.classList.replace('bi-moon-fill', 'bi-sun-fill')
    }
})
