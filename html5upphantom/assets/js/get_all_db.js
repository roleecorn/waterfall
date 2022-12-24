function dbs() {
    fetch('/dbs')
        .then(response => response.json())
        .then(data => {
            var cite_list = data.data;
            $.each(cite_list, function (index, v) {
                // {#    index, v，index是指的索引，v是指的内容        # }
                var tag = document.createElement('option');
                tag.text=v.name;
                tag.value=v.src;
                console.log(v.name);
                $('#input-select').append(tag);
            })
        });
}