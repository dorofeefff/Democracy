function getRound(r) {
    if (r == 1) {return ''}
    else {return 'Round ' + (r-1).toString()}
}

function getPart(r) {
    if (r == 1) {return 'Part I'}
    else {return 'Part II'}
}

function getPartRound(r) {return getPart(r) + ': ' + getRound(r)}

function getStage(r, stage) {return stage + ' Stage'}

function setPartAndRound(r, stage) {
    let docPart = document.getElementById('part');
    let docStage = document.getElementById('stage');
    if (r == 1) {
        docPart.innerHTML = getPart(r);
    } else {
        docPart.innerHTML = getPartRound(r);
        docStage.innerHTML = stage;
    }
}