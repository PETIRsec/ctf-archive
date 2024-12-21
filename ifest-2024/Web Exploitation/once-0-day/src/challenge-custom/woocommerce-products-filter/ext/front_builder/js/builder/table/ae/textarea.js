'use strict';
import Helper from '../../helper.js';
import Element from './element.js';
//05-06-2023
export default class Textarea extends Element {
    constructor(key, value, wrapper, params) {
        super(key, value, wrapper, params);
    }

    draw() {
        this.input = Helper.create_element('textarea', {
            form: 'fakeForm',
        }, this.value);

        this.wrapper.appendChild(this.input);
        this.input.focus();
        return this.input;
    }
}
