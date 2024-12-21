'use strict';
import Helper from './helper.js';
import Table from './table/table.js';
//13-07-2023
export default class SectionOptions {
    constructor(builder, section_key) {
        this.builder = builder;
        this.section_key = section_key;
        this.call_id = Helper.generate_key('op-');//to get events for current object only
        this.draw();

        //+++

        //tab 1
        document.addEventListener('woof_front_builder_save_section_option', e => {
            if (e.detail.call_id === this.call_id) {
                Helper.ajax('woof_front_builder_save_section_option', {
                    name: this.builder.name,
                    section_key: this.section_key,
                    field: e.detail.field,
                    value: e.detail.value
                }, data => this.builder.redraw_filter());
            }
        });

        //tab 2
        document.addEventListener('woof_front_builder_save_section_layout_option', e => {
            if (e.detail.call_id === this.call_id) {
                let value = e.detail.value;
                let field = e.detail.field;
                let styles = document.getElementById(`${this.builder.button.id}-styles`);

                if (!value.includes('px') && !value.includes('%') && value !== 'auto' && value !== 'inherit') {
                    value = value + this.layout_data.find(el => el.field === field).default_measure;
                }

                //this.builder.container.querySelector(`.woof_fs_${this.section_key}`).style[field] = value;
                //if no rules for the section lets create it
                let rules_txt = styles.innerHTML;
                if (rules_txt.search(`.woof_fs_${this.section_key}`) === -1) {
                    rules_txt += ` #woof-front-builder-${this.builder.button.id} .woof_fs_${this.section_key}{width: ${value}; } `;
                    styles.innerHTML = rules_txt;
                }

                //!!important because css is in tag <style>
                if (styles.sheet.cssRules.length > 0) {
                    Array.from(styles.sheet.cssRules).forEach((rule, index) => {
                        if (rule.selectorText.indexOf(this.section_key) !== -1) {
                            styles.sheet.cssRules[index].style[field] = value;
                            return;
                        }
                    });
                }

                Helper.ajax('woof_front_builder_save_section_layout_option', {
                    name: this.builder.name,
                    section_key: this.section_key,
                    field: field,
                    value: value
                }, data => this.builder.redraw_filter());

            }
        });
    }

    draw() {

        this.builder.popup.generate_tabs([
            {
                title: woof_lang_front_builder_filter_section,
                content: this.builder.popup.start_content
            },
            {
                title: woof_lang_front_builder_layout,
                content: ''
            }
        ]);

        this.builder.popup.set_content(woof_lang_loading);
        this.builder.popup.set_title(this.builder.name + ': ' + woof_lang_front_builder_section_options + ' [' + this.section_key + ']');
        this.builder.draw_back_btn();
        this.draw_tab_options();
        this.draw_tab_layout_options();
    }

    //tab 1
    draw_tab_options() {
        Helper.ajax('woof_form_builder_get_section_options', {
            name: this.builder.name,
            section_key: this.section_key
        }, data => {
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

            data.forEach(option => {

                if (option.element === 'hidden') {
                    return;
                }

                formated_data.rows[counter] = {
                    element: {
                        "value": {
                            element: `${option.element}`,
                            value: option.value,
                            action: 'woof_front_builder_save_section_option'
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

            this.table = new Table(formated_data, this.builder.popup.get_container(0));
        });
    }

    //tab 2
    draw_tab_layout_options() {
        Helper.ajax('woof_form_builder_get_section_layout_options', {
            name: this.builder.name,
            section_key: this.section_key
        }, data => {
            this.layout_data = data;
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

            this.builder.popup.clear_content(1);
            let counter = 1;

            this.layout_data.forEach(option => {

                if (option.element === 'hidden') {
                    return;
                }

                formated_data.rows[counter] = {
                    element: {
                        "value": {
                            element: `${option.element}`,
                            value: option.value,
                            action: 'woof_front_builder_save_section_layout_option'
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

        });
    }

}

