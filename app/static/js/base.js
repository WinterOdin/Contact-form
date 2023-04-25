function redirect(url) {
    window.location.href = url
}

function createJson(form_data){
    const data = new FormData(form_data);
    const formJSON = Object.fromEntries(data.entries());
    return formJSON
}

function postData(url){

    const form = document.getElementById("contact_form")
    const data = createJson(form)

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": data["csrfmiddlewaretoken"],
        },
        body: JSON.stringify(data)
    }).then(response => {
            if (!response.ok) {
                return Promise.reject(response);
            }
            return response.json();
        })
        .then(data => {
            showPopUp("Success", "Thank you for your message we will contact you soon.", "fas fa-solid fa-check check")
            form.reset();
        })
        .catch(error => {
            if (typeof error.json === "function") {
                error.json().then(jsonError => {

                    for (const [key, value] of Object.entries(jsonError)) {
                        let str = '';
                    
                        if (Array.isArray(value)) {
                            str += value.join(', ');
                        } else {
                            str += value;
                        }
                        showPopUp(key, str, "fas fa-solid fa-solid fa-xmark error_mark", "red")
                    }
                    
                }).catch(genericError => {
                    showPopUp("Server error", JSON.stringify(error.statusText), "fas fa-solid fa-solid fa-xmark error_mark", "red")
                });
            }
        });
}