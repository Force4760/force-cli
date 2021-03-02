var at = document.getElementsByTagName("a")
var img = document.getElementById("card-view")

console.log(at)

for (const i of at) {
    i.addEventListener("mouseenter", ()=>changeImg(i.getAttribute("href")))
    i.addEventListener("mouseleave", ()=>changeImg("#"))
}

function changeImg(h){
    img.setAttribute("style", "background: url("+ h +") center / cover no-repeat;")
}