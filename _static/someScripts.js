function getPart(r) {
    if (r == 1) {return 'Part I'}
    else {return 'Part II'}
}

function getRound(r, stage) {
    if (r == 1) {return ''}
    else {return 'Round ' + (r-1).toString() + ': ' + stage + ' Stage'}
}

function setPartAndRound(r, stage) {
    document.getElementById('part').innerHTML = getPart(r);
    document.getElementById('round').innerHTML = getRound(r, stage);
}

function setLowBound(send_min, send_selfish, mode) {
    if (mode == 'selfish') {return send_selfish}
    else {return send_min}
}

function setUpperBound(send_max, send_fair, mode) {
    if (mode == 'fair') {return send_fair}
    else {return send_max}
}
