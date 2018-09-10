console.log("Boop")

forms = document.getElementsByClassName("affirmation_submit")
edit_button = document.getElementsByClassName("edit_button")

Array.from(forms).forEach(function(form) {
    form.parentNode.style.display = 'none';
})

Array.from(edit_button).forEach(function(edit) {
    edit.parentElement.style.display = '';
    edit.addEventListener("click", function(){
        parent = edit.parentElement.parentElement;
        edit.parentElement.style.display = 'none';
        form = parent.children[1]
        form.style.display = '';
    })
})