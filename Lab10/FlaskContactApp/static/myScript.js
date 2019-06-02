function submit_form() {

    var inputs = document.getElementById("creation_form").elements;

    var is_valid = true;
    for (var i = 0; i < inputs.length; i++) {
        var currentInput = inputs[i].value;
        if (currentInput.indexOf(";") != -1){
            is_valid = false;
        }
    }

    if (is_valid){
        return true;
    }
    else{
        alert("Invalid format!");
        return false;
    }
}

function alertUser(msg) {
    alert(msg);
}