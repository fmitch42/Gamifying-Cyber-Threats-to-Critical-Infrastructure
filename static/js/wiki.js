// Expand/Collapse Sections
// document.addEventListener("DOMContentLoaded", function () {
//     const collapsibles = document.querySelectorAll(".collapsible");

//     collapsibles.forEach(button => {
//         button.addEventListener("click", function () {
//             const content = this.nextElementSibling;
//             if (content.style.display === "block") {
//                 content.style.display = "none";
//             } else {
//                 content.style.display = "block";
//             }
//         });
//     });
// });


document.addEventListener("DOMContentLoaded", function () {
    const collapsibles = document.querySelectorAll(".collapsible");

    collapsibles.forEach(button => {
        button.addEventListener("click", function () {
            const content = this.nextElementSibling;
            content.classList.toggle("active");
        });
    });
});

// Search Function
function searchWiki() {
    let input = document.getElementById("searchBar").value.toLowerCase();
    let items = document.getElementsByClassName("wiki-item");

    for (let i = 0; i < items.length; i++) {
        let btn = items[i].getElementsByClassName("collapsible")[0];
        if (btn.innerText.toLowerCase().includes(input)) {
            items[i].style.display = "";
        } else {
            items[i].style.display = "none";
        }
    }
}
