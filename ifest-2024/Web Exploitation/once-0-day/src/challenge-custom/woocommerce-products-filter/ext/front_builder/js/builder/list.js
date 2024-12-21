'use strict';
import Helper from './helper.js';
import SectionOptions from './section-options.js';//1
//16-07-2023
export default class List {
    constructor(builder) {
        this.builder = builder;
    }

    create() {
        this.list = Helper.create_element('ul');
        this.list.className = 'woof-front-builder-list';
        this.builder.append_content_to_popup(this.list);
        this.draw();
    }

    draw() {
        this.list.innerHTML = '';
        this.builder.selected.forEach(key => this.add(key, this.builder.data[key]));
        this.check_sd_buttons();
    }

    add(key, value) {
        if (!key) {
            return;
        }

        let li = Helper.create_element('li', {}, Helper.create_element('span', {}, '[<strong>' + value.title + '</strong>]'));

        let del = Helper.create_element('a', {
            href: '#',
            class: 'woof-front-builder-list-li-del'
        }, Helper.create_element('img', {
            src: woof_link + 'ext/front_builder/img/cross.svg'
        }), {
            name: 'click',
            callback: e => {
                e.preventDefault();
                if (confirm(woof_lang_front_builder_del)) {
                    let key = li.dataset.key;
                    this.builder.selected = this.builder.selected.filter(v => v !== key);//!!
                    this.builder.add_to_selector(key);
                    this.refresh();
                }
                return false;
            }
        });

        li.appendChild(del);
        li.dataset['key'] = key;

        this.add_type_selector(li, key);
        if (!this.builder.exclude_from_options.includes(key)) {
            this.add_section_options(li, key);
        }
        this.add_buttons(li);

        this.list.appendChild(li);
    }

    add_section_options(li, key) {
        let btn = Helper.create_element('a', {
            href: '#',
            class: 'woof-front-builder-type-section-options'
        }, Helper.create_element('img', {
            src: woof_link + 'ext/front_builder/img/cog2.svg',
            width: '25px'
        }));

        li.appendChild(btn);

        btn.addEventListener('click', e => {
            e.preventDefault();
            new SectionOptions(this.builder, key);
            return true;
        });
    }

    add_type_selector(li, tax_key) {

        if (!this.builder.data[tax_key].is_taxonomy) {
            return;
        }

        let select = Helper.create_element('select');
        select.className = 'woof-front-builder-type-selector';
        this.viewtypes = JSON.parse(this.builder.container.dataset.viewtypes);

        let selected = this.builder.data[tax_key].viewtype;

        Object.keys(this.viewtypes).forEach(key => {
            let option = Helper.create_element('option');
            option.setAttribute('value', key);
            option.innerText = this.viewtypes[key];

            if (selected === key) {
                option.setAttribute('selected', '');
                li.dataset.viewtype = key;
            }

            if (woof_front_sd_is_a && woof_front_show_notes) {
                if (key.indexOf('woof_sd_') !== -1) {
                    this.list_has_sd = true;
                }
            }

            select.appendChild(option);
        });

        li.appendChild(select);

        select.addEventListener('change', e => {
            e.stopPropagation();
            Helper.ajax('woof_form_builder_update_viewtype', {
                key: tax_key,
                value: select.value,
                name: this.builder.name
            }, data => {
                this.builder.data[tax_key].viewtype = select.value;
                li.dataset.viewtype = select.value;
                this.update_sd_btn(li);
                this.builder.redraw_filter();
            });

            return true;
        });
    }

    add_buttons(li) {

        let key = li.dataset.key;

        let wrapper = Helper.create_element('div');
        wrapper.className = 'woof-front-builder-list-li-move';

        let up = Helper.create_element('a', {
            href: '#',
            class: 'woof-front-builder-list-li-up'
        }, Helper.create_element('img', {
            src: woof_link + 'ext/front_builder/img/arrow.svg'
        }), {
            name: 'click',
            callback: e => {
                e.preventDefault();

                let index = this.builder.selected.indexOf(key);
                let key_above = this.builder.selected[index - 1];
                this.builder.selected[index - 1] = key;
                this.builder.selected[index] = key_above;

                this.refresh();
                highlight(key, this.list);

                return false;
            }
        });

        //+++

        let down = Helper.create_element('a', {
            href: '#',
            class: 'woof-front-builder-list-li-down'
        }, Helper.create_element('img', {
            src: woof_link + 'ext/front_builder/img/arrow.svg'
        }), {
            name: 'click',
            callback: e => {
                e.preventDefault();

                let index = this.builder.selected.indexOf(key);
                let key_below = this.builder.selected[index + 1];
                this.builder.selected[index + 1] = key;
                this.builder.selected[index] = key_below;

                this.refresh();
                highlight(key, this.list);

                return false;
            }
        });


        if (this.builder.selected.indexOf(key) > 0 && this.builder.selected.length >= 1) {
            wrapper.appendChild(up);
        }

        if (this.builder.selected.indexOf(key) < this.builder.selected.length - 1) {
            wrapper.appendChild(down);
        }

        //+++

        if (this.builder.data[key].is_taxonomy) {
            let sd = null;

            if (typeof woof_front_builder_is_demo !== 'undefined') {
                sd = Helper.create_element('a', {
                    href: 'https://products-filter.com/extencion/smart-designer',
                    class: '',
                    target: '_blank'
                }, Helper.create_element('img', {
                    src: woof_link + 'ext/front_builder/img/sd.svg'
                }));
                console.log('demo');
                wrapper.appendChild(sd);
            } else {
                if (woof_front_sd_is_a) {
                    sd = Helper.create_element('a', {
                        href: '#',
                        class: 'woof-front-builder-sd-btn',
                        "data-sd-state": this.is_sd(li)
                    }, Helper.create_element('img', {
                        src: woof_link + `ext/front_builder/img/sd${this.is_sd(li) ? '' : '-no'}.svg`,
                        class: ''
                    }), {
                        name: 'click',
                        callback: e => {
                            e.preventDefault();

                            if (this.is_sd(li)) {
                                this.init_sd_iframe(key, li);
                            } else {
                                if (confirm(woof_lang_front_builder_confirm_sd)) {

                                    if (woof_front_sd_is_a && woof_front_show_notes) {
                                        if (this.list_has_sd) {

                                            if (confirm('Hi! In the free version of HUSKY you can operate with 1 element! If you want to create more elements you can make upgrade to the premium version of the plugin. Would you like to visit the plugin page on Codecanyon?')) {
                                                window.location.href = 'https://products-filter.com/a/buy';
                                            }

                                            return false;
                                        }
                                    }

                                    this.builder.popup.set_title(woof_lang_front_builder_creating + ' ...');
                                    Helper.ajax('woof_form_builder_set_sd', {
                                        key: key,
                                        name: this.builder.name
                                    }, responce => {
                                        this.viewtypes[`woof_sd_${responce.sd_id}`] = responce.title;
                                        this.builder.container.dataset.viewtypes = JSON.stringify(this.viewtypes);
                                        this.builder.data[key].viewtype = li.dataset.viewtype = `woof_sd_${responce.sd_id}`;
                                        this.init_sd_iframe(key, li);
                                    });
                                }
                            }

                            return false;
                        }
                    });

                    wrapper.appendChild(sd);
                }
            }

        }


        li.appendChild(wrapper);


        //+++

        function highlight(key, list) {
            let li_actioned = list.querySelector(`li[data-key='${key}']`);
            li_actioned.classList.add('woof-front-builder-list-li-selected');
            setTimeout(() => li_actioned.classList.remove('woof-front-builder-list-li-selected'), 777)
        }
    }

    init_sd_iframe(key, li) {
        this.builder.popup.clear_content();
        this.builder.popup.set_title(this.builder.data[key].title);

        let back = Helper.create_element('a', {
            href: '#',
            class: 'woof-front-builder-btn-back',
        }, Helper.create_element('img', {
            src: woof_link + 'ext/front_builder/img/back.svg'
        }), {
            name: 'click',
            callback: e => {
                e.preventDefault();
                back.remove();
                this.builder.popup.set_title(this.builder.name);
                this.builder.popup.set_content(woof_lang_loading);
                this.builder.fill_popup();
                return false;
            }
        });

        this.builder.popup.set_title_info(back);

        //+++

        let sd_id = parseInt(this.is_sd(li));

        let ifrm = document.createElement('iframe');
        let ifrm_max_height = parseInt(parseInt(this.builder.popup.data.height) * 0.75);
        ifrm.setAttribute('src', woof_ajaxurl.replace('admin-ajax.php', `admin.php?page=wc-settings&tab=woof&woof-action=form-builder&max_height=${ifrm_max_height}&sd_id=${sd_id}#tabs-sd`));
        ifrm.width = '100%';
        ifrm.height = '99%';
        ifrm.seamless = 'seamless';
        ifrm.scrolling = 'no';
        ifrm.style.border = 0;

        ifrm.addEventListener('load', e => {
            let doc = ifrm.contentDocument;
            let style = doc.createElement('style');
            style.textContent = ``;
            doc.head.append(style);
        });

        this.builder.append_content_to_popup(ifrm);
    }

    is_sd(li) {
        let res = 0;

        if (li.dataset.viewtype && li.dataset.viewtype.indexOf('woof_sd_') !== -1) {
            res = parseInt(li.dataset.viewtype.replace('woof_sd_', ''));
        }

        return res;
    }

    update_sd_btn(li) {
        if (woof_front_sd_is_a) {
            if (li && li.querySelector('.woof-front-builder-sd-btn img')) {
                li.querySelector('.woof-front-builder-sd-btn img').setAttribute('src', woof_link + `ext/front_builder/img/sd${(this.is_sd(li) ? '' : '-no')}.svg`);
            }

            this.check_sd_buttons();
        }
    }

    //to avoid confusing lets hide SD buttons if one is selected or SD created
    check_sd_buttons() {
        if (woof_front_sd_is_a && woof_front_show_notes) {
            let images = this.list.querySelectorAll('.woof-front-builder-sd-btn img');
            let hide = false;

            if (images.length) {
                images.forEach((img, k) => {
                    if (img.src && img.src.indexOf('sd.svg') !== -1) {
                        hide = true;
                        return;
                    }
                });

                images.forEach((img, k) => {
                    if (img.src && img.src.indexOf('sd-no.svg') !== -1) {
                        if (hide) {
                            img.style.display = 'none';
                        } else {
                            img.style.display = 'block';
                        }
                    }
                });

            }
        }
    }

    refresh() {
        this.draw();
        this.builder.redraw_filter();
        this.builder.update_button_data();
    }

}

