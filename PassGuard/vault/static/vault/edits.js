function generatePassword(div) {
    length = 12
    const uppercaseChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const lowercaseChars = "abcdefghijklmnopqrstuvwxyz";
    const specialChars = "!@#$%^&*_-+=";
    const numberChars = "0123456789";

    const allChars = uppercaseChars + lowercaseChars + numberChars + specialChars;
    let password = "";

    for (let i = 0; i < length; i++) {
        const randomIndex = Math.floor(Math.random() * allChars.length);
        password += allChars.charAt(randomIndex);
    }

    div.parentElement.querySelector(".form-control").value = password;
}

function copy(div){
    const text = div.parentElement.querySelector(".card-password");
    //text.select();
    //text.setSelectionRange(0, 99999);
    navigator.clipboard.writeText(text.innerHTML);
    div.parentElement.querySelector(".card-body").style.display = "block";
    div.parentElement.querySelector(".card-password").style.display = "none";
    div.style.display = "none";
}


function revealdata(div, id ,master_key){
        function gettoken(name) {
            const value = `;${document.cookie}`;
            const parts = value.split(`;${name}=`);
            if (parts.length == 2) return parts.pop().split(';').shift();
        }

    fetch(`/reveal/${id}`,{
        method: "POST",
        headers: {"Content-type":"application/json", "X-CSRFToken":gettoken("csrftoken")},
        body: JSON.stringify({
            masterkey: master_key
        })
    }).then(response => response.json())
        .then(result => {
            const password = result["password"]
            div.parentElement.parentElement.querySelector(".card-password").innerHTML = `${password}`;
            div.parentElement.parentElement.querySelector(".card-password").style.display="block";
            div.parentElement.parentElement.querySelector(".card-body").style.display="none";
            div.parentElement.parentElement.querySelector(".cool-button").style.display="block";
        })

}


function reveal(div){
    // to make sure masterkey is inserted
    if (document.querySelector(".form-control").value === `` ){
        alert("Fill in you Master-key please:");
    }
    else{
        const id = div.parentElement.querySelector(".id").innerHTML;
        //const person_id = div.parentElement.querySelector(".person-id").innerHTML;
        const master_key = document.querySelector(".form-control").value;
        revealdata(div, id,master_key)
    }
}