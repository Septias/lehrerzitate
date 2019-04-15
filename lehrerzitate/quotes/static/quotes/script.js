"use strict"

function formatItalic(elemsClass) {
    const regex = /\*[^\*]+\*/gm;

    let elems = document.getElementsByClassName(elemsClass);
    for (let elem of elems) {
        elem.innerHTML = elem.innerHTML.replace(regex, '<i> $& </i>');
    }
}

function hovered(elem) {
    elem.children[0].innerHTML = "+1";
    elem.children[2].style.display = "inline-block";
}

function _hovered(elem) {
    elem.children[2].style.display = "inline-block";
}

function not_hovered(elem) {
    elem.children[0].innerHTML = (likes[elem.id] == 0 ? '' : likes[elem.id]);
    elem.children[2].style.display = "none";
}

function like(id) {
    $.ajax({
        url: '/ajax/like/' + id,
        dataType: 'json',
        success: function (data) {
            let n = document.getElementById(data.id);
            n.children[0].innerHTML = data.likes;
            n.children[0].onclick = '';
            n.onmouseover = function () {
                _hovered(this)
            };
            likes[data.id] = data.likes;
        }
    });
}