const sum = (...nums: Array<number | BigInt>): number => {
    return nums.map((num) => {
        return typeof num === "number" ? num : Number(num);
    }).reduce((total, num) => {
        return total + num;
    }, 0);
};

type Chainable = {
    add: (...nums: Array<number | BigInt>) => Chainable;
    subtract: (...nums: Array<number | BigInt>) => Chainable;
    negate: () => Chainable;
    value: () => number;
};

const chainable = (...nums: Array<number | BigInt>): Chainable => {
    const add = (...newNums: Array<number | BigInt>): Chainable => chainable(...nums, ...newNums);
    const subtract = (...newNums: Array<number | BigInt>): Chainable => chainable(...nums, ...newNums.map((num) => -num));
    const negate = (): Chainable => chainable(...nums.map((num) => -num));
    const value = (): number => sum(...nums);

    return {
        add,
        subtract,
        negate,
        value,
    };
};
