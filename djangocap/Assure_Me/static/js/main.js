forms = document.getElementsByClassName("edit_form")
edit_button = document.getElementsByClassName("edit_button")

Array.from(edit_button).forEach(function(edit) {
    edit.addEventListener("click", function(){
        parent = edit.parentElement.parentElement.parentElement;
        Array.from(edit_button).forEach(function(edit) {
            edit.parentElement.classList.remove("is_hidden");
            edit.parentElement.parentElement.classList.remove("is_hidden");
        })
        edit.parentElement.classList.add("is_hidden");
        edit.parentElement.parentElement.classList.add("is_hidden");
        Array.from(forms).forEach(function(form){
            form.classList.add("is_hidden");
        })
        form = parent.children[0];
        form.classList.remove("is_hidden");
    })
})