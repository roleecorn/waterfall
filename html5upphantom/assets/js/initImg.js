function initImg(path = '/ttttest/') {
    fetch(path, {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }

    })
        .then(response => response.json())
        .then(response => {
            var img_list = response.data;
            var c = 0;
            Object.values(img_list).forEach(v => {
                var eqv = c % 4;
                c = c + 1;
                var tag = document.createElement('img');
                tag.src = "../" + v.src;
                var word = document.createElement('div');
                word.textContent = v.title + "," + v.id;
                $('#container').children().eq(eqv).append(tag).append(word);
            });
        })
        .catch(error => console.error(error));
}