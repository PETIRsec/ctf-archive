const merge = (obj1, obj2) => {
    for (let key in obj2) {
        if (typeof obj1[key] !== "undefined" && typeof obj2[key] === "object") {
            obj1[key] = merge(obj1[key], obj2[key]);
        } else {
            obj1[key] = obj2[key];
        }
    }
    return obj1;
}

module.exports = { merge

}