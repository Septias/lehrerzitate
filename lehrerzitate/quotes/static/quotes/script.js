function formatItalic(elemsClass) {
    const regex = /\*[^\*]+\*/gm;

    let elems = document.getElementsByClassName(elemsClass);
    for (let elem of elems) {
        elem.innerHTML = elem.innerHTML.replace(regex, '<i> $& </i>');
    }
}