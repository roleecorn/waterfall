function initImg(path = '/search_img/',shop='eddiebauer') {
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
                tag.src = v.src;
                var word = document.createElement('div');
                word.style = 'white-space: pre-line;'
                word.innerHTML = '品名: ' + v.name + '<br>';
                word.innerHTML += '金額: ' + v.price + '<br>';
                gender = 'Other';
                if (v.gender === 0) {
                    gender = 'Female';
                }
                if (v.gender === 1) {
                    gender = 'Male';
                }
                word.innerHTML += '性別: ' + gender  + '<br>';
                $('#container').children().eq(eqv).append(tag).append(word);
            });
        })
        .catch(error => console.error(error));
}