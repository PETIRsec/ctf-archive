'use strict';
import Helper from './helper.js';
//16-07-2023
export default class Selector {
    constructor(builder) {
        this.builder = builder;
    }

    draw() {
        this.select = Helper.create_element('select');
        this.select.className = 'woof-front-builder-selector';

        this.add('', woof_lang_front_builder_select, 0);

        let titles_arr = [];
        let titles_obj = {};
        for (const [key, value] of Object.entries(this.builder.data)) {
            if (this.builder.selected.includes(key)) {
                continue;
            }

            //we do it for next sorting
            titles_arr.push(value.title);
            titles_obj[value.title] = key;
        }

        //sort
        if (titles_arr.length > 0) {
            titles_arr.sort(function (a, b) {
                return a.localeCompare(b);
            })

            let counter = 1;
            titles_arr.forEach(title => {
                this.add(titles_obj[title], title, counter);
                counter++;
            })
        }

        this.builder.appendChild(this.select);

        this.select.addEventListener('change', e => {

            let max_count = (typeof woof_front_builder_is_demo !== 'undefined') ? 10 : 1000;

            if (this.builder.list.list.childElementCount >= max_count) {
                alert('In demo mode there is limit to 10 filter sections');
                return false;
            }

            if (this.select.value.length > 0) {
                this.builder.append_to_list(this.select.value);
                [...this.select.options].find(option => option.selected).remove();
            }
        });

        this.builder.append_content_to_popup(this.select);
    }

    add(key, value, counter = 0) {
        let option = Helper.create_element('option', {
            value: key
        }, value);

        if (counter === 0) {
            option.setAttribute('hidden', '');
        }

        this.select.appendChild(option);
    }
}