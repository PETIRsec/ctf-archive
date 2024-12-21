'use strict';
import Helper from './helper.js';
import Table from './table/table.js';
//12-07-2023
export default class Options {
    constructor(builder) {
        this.builder = builder;
        this.unformatted_data = null;
        this.call_id = Helper.generate_key('op-');//to get events for current object only

        //load current shortcode options
        Helper.ajax('woof_form_builder_get_options', {
            name: this.builder.name
        }, data => this.unformatted_data = data);

        Helper.ajax('woof_form_builder_get_layout_options', {
            name: this.builder.name
        }, data => this.unformatted_layout_data = data);

        //+++

        document.addEventListener('woof_front_builder_save_option', e => {
            if (e.detail.call_id === this.call_id) {
                this.unformatted_data.forEach((v, k) => {
                    if (e.detail.field === v.field) {
                        this.unformatted_data[k].value = e.detail.value;
                    }
                });

                Helper.ajax('woof_form_builder_save_options', {
                    name: this.builder.name,
                    field: e.detail.field,
                    value: e.detail.value
                }, data => this.builder.redraw_filter());
            }
        });

        //+++

        document.addEventListener('woof_front_builder_save_layout_option', e => {
            if (e.detail.call_id === this.call_id) {
                this.unformatted_layout_data.forEach((v, k) => {
                    if (e.detail.field === v.field) {
                        this.unformatted_layout_data[k].value = this.format_layout_val(e.detail.value, v.field);
                    }
                });

                let style = '';
                if (this.unformatted_layout_data && this.unformatted_layout_data.length > 0) {
                    this.unformatted_layout_data.forEach(option => {
                        style += option.field + ': ' + option.value + '; ';
                    });
                }
                this.builder.container.setAttribute('style', style);

                Helper.ajax('woof_form_builder_save_layout_options', {
                    name: this.builder.name,
                    field: e.detail.field,
                    value: this.format_layout_val(e.detail.value, e.detail.field)
                }, data => {
                    //fix for icheck
                    if (e.detail.field === 'icheck_skin' || e.detail.field === '--woof-fb-section-height') {
                        this.builder.redraw_filter();
                    }
                });
            }
        });
    }

    //avoid user data error about option value measure
    format_layout_val(value, key) {
        value = value.toLowerCase();

        if (!value.includes('px') && !value.includes('%') && value !== 'auto') {
            value = value + this.unformatted_layout_data.find(el => el.field === key).default_measure;
        }

        return value;
    }

    get_option_value(field) {
        return this.unformatted_data.find(el => el.field === field)?.value;
    }

    set_option_value(field, value) {
        return this.unformatted_data.map(el => {
            if (el.field === field) {
                el.value = value;
            }
        }).value;
    }

    draw() {
        this.builder.popup.generate_tabs([
            {
                title: woof_lang_front_builder_shortcode,
                content: this.builder.popup.start_content
            },
            {
                title: woof_lang_front_builder_layout,
                content: ''
            }
        ]);

        this.builder.popup.set_content(woof_lang_loading);
        this.builder.popup.set_title(this.builder.name + ': ' + woof_lang_front_builder_options);
        this.builder.draw_back_btn();

        this.draw_shortcode_options();
        this.draw_layout_options();
    }

    draw_layout_options() {
        //tab 2
        let formated_data = {
            header: [
                {
                    "value": woof_lang_front_builder_option,
                    "width": "30%",
                    "key": "element",
                    "role": "cell"
                },
                {
                    "value": woof_lang_front_builder_description/* + ' [<em>' + woof_lang_front_builder_good_to_use + '</em>]'*/,
                    "width": "70%",
                    "key": "description",
                    "role": "cell"
                }
            ],
            rows: {}
        };


        //+++

        this.builder.popup.clear_content(1);
        let counter = 1;

        this.unformatted_layout_data.forEach(option => {

            if (option.element === 'hidden') {
                return;
            }

            formated_data.rows[counter] = {
                element: {
                    "value": {
                        element: `${option.element}`,
                        value: option.value,
                        action: 'woof_front_builder_save_layout_option'
                    },
                    cast_fields: {
                        field: option.field,
                        name: this.builder.name,
                        call_id: this.call_id,
                    },
                    "role": "cell",
                    "width": "30%",
                    "key": "element"
                },
                description: {
                    "value": `<strong>${option.title}</strong>:<br>${option.description}`,
                    "role": "cell",
                    "width": "70%",
                    "key": "description"
                },
            };

            counter++;
        });

        this.table = new Table(formated_data, this.builder.popup.get_container(1));
    }

    draw_shortcode_options() {

        let formated_data = {
            header: [
                {
                    "value": woof_lang_front_builder_option,
                    "width": "30%",
                    "key": "element",
                    "role": "cell"
                },
                {
                    "value": woof_lang_front_builder_description,
                    "width": "70%",
                    "key": "description",
                    "role": "cell"
                }
            ],
            rows: {}
        };


        //+++

        this.builder.popup.clear_content();
        let counter = 1;

        this.unformatted_data.forEach(option => {

            if (option.element === 'hidden') {
                return;
            }

            formated_data.rows[counter] = {
                element: {
                    "value": {
                        element: `${option.element}`,
                        value: option.value,
                        action: 'woof_front_builder_save_option'
                    },
                    cast_fields: {
                        field: option.field,
                        name: this.builder.name,
                        call_id: this.call_id,
                    },
                    "role": "cell",
                    "width": "30%",
                    "key": "element"
                },
                description: {
                    "value": `<strong>${option.title}</strong>:<br>${option.description}`,
                    "role": "cell",
                    "width": "70%",
                    "key": "description"
                },
            };

            counter++;
        });

        this.table = new Table(formated_data, this.builder.popup.get_container());
    }

}


