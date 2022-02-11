function getPart(r) {
    if (r == 1) {return 'Part I'}
    else {return 'Part II'}
}

function getRound(r, stage) {
    if (r == 1) {return ''}
    else {
        r = r - 1;
        if (stage == 'decision') {
            return 'Round ' + r.toString() + ': Decision Stage'
        }
    }
}

function setPartAndRound(r, stage) {
    document.getElementById('part').innerHTML = getPart(r);
    document.getElementById('round').innerHTML = getRound(r, stage);
}
