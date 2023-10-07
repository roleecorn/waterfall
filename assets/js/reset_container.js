function reset_container(){
    for (let i = 0; i < 4; i++) {
        $('#container').children().eq(0).remove();
    }
    for (let i = 0; i < 4; i++) {
        var tag = document.createElement("div");
        tag.className = "item";
        // tag.innerHTML = "第一行";
        $('#container').append(tag);
    }
}