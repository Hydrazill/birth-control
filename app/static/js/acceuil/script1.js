
// window.addEventListener('click', (event) => {
//     console.log(event.target)
// })

window.addEventListener("load", () => {
    if(document.querySelector(".role").textContent === "parent") {
        document.getElementById('declaration').style.display= 'block' // declarer.classList.toggle("reveal")
    }else {
        document.getElementById('admin').style.display= 'block' // admin.classList.add("reveal")
    }
})

document.querySelector(".middle").addEventListener('click', () => {
    document.getElementById('form').style.display = 'flex'
    document.getElementById('list').style.display = 'none'
})
document.addEventListener('click', (event) => {
    if (!document.querySelector('.middle').contains(event.target) && !document.querySelector('.form').contains(event.target)) {
        document.getElementById('form').style.display = 'none'
        document.getElementById('list').style.display = 'flex'
    }
})