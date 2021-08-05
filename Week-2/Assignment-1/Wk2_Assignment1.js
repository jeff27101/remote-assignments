function max(array) {
    var val = array[0];

    for (var i = 1; i < array.length; i++) {
        if (array[i] > val) {val = array[i];}
    }

    return val;
}

function findPosition(numbers,target) {
    var findit = false;
    for (var i = 0; i < numbers.length; i++) {
        if (numbers[i] == target) {
            findit = true;
            return i;}
    }
    if (findit == false) {
        return -1;
    }

}
