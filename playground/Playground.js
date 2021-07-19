function flatten(init_list) {
    let global_list = [];
    for (element of init_list) {
        if (typeof element == "array") {
            global_list = [...global_list, ...flatten(element)];
        } else {
            global_list = [...global_list, element];
        }
    }
    return global_list;
}

function flatten(init_list) {
    if (typeof init_list !== 'array') {
        return [init_list];
    } else {
        return flatten(init_list);
    }
}


flatten([
    1,
    [2,3],
    [4,5,6],
    [7,8,9]]
)
