function initImg() {
    $.ajax({
        url: '/data/',
        // url: {{{}}},
        type: 'GET',
        data: { nid: NID },
        dataType: 'JSON',
        success: function (arg) {

            var img_list = JSON.parse(arg).data;
            console.log(img_list);
            var c=0;
            $.each(img_list, function (index, v) {
                // {#    index, v，index是指的索引，v是指的内容        # }
                var eqv = c % 4;
                c=c+1;
                var tag = document.createElement('img');
                tag.src = "http://localhost:8000/" + v.src;
                var word = document.createElement('div');
                word.textContent = v.title + "," + v.id;
                
                $('#container').children().eq(eqv).append(tag).append(word);
            })

        }

    })
}