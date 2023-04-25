let timer1, timer2;
const wrapper = document.getElementById('wrapper')
let counter = 0;


function updateToastPosition(distance) {
    let allToasts = document.querySelectorAll(".toast");
    allToasts.forEach(element => {
        let pos = parseInt(element.style.top.split("px")[0]);
        element.style.top = (pos - distance) + "px";
    });
}

function showPopUp(title, body, mark, color) {
    const popup_data =
        `<div id="toast_${counter}"class="toast active">
            <div class="toast-content">
                <i class="${mark}"></i>
                <div class="message">
                    <span id="text_title" class="text text-1">${title}</span>
                    <span id="text_body" class="text text-2">${body}</span>
                </div>
            </div>
            <div class="progress active ${color}"></div>
        </div>`

    wrapper.insertAdjacentHTML('beforeend', popup_data);
    const toastElement = document.getElementById("toast_" + counter);
    let height = toastElement.offsetHeight + 5

    let allToasts = document.querySelectorAll(".toast.active");
    toastElement.style.top = 25 + (allToasts.length - 1) * height + "px";

    const progress = document.querySelector(`#toast_${counter} > .progress`);
    toastElement.classList.add("active");
    progress.classList.add("active");

    timer1 = setTimeout(() => {
        toastElement.classList.remove("active");
        updateToastPosition(height);
    }, 5000);

    timer2 = setTimeout(() => {
        progress.classList.remove("active");
        toastElement.remove()
    }, 5300);

    counter++;
}


