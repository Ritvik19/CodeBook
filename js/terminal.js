$('#command').keyup(function(e) {
    if (e.keyCode === 13) {
        command = this.value
        console.log(command)
    }
});