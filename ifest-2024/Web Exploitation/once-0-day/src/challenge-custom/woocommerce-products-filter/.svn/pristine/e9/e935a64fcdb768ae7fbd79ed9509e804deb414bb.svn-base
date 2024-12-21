'use strict';
import Helper from './helper.js';
import Popup from './popup-23.js';
import Selector from './selector.js';
import List from './list.js';
import Options from './options.js';
//13-07-2023
export default class Builder {
    constructor(button) {
        this.button = button;
        this.name = button.dataset.name;
        this.husky = button.querySelectorAll('img')[1];
        //this.exclude_from_options = ['xxxx', 'yyyy'];//some filter sections not has options
        this.exclude_from_options = [];//but has layout, so button should be shown

        this.container = this.look_for_container();
        this.popup = new Popup({
            id: 'p' + button.id,
            title: this.name,
            title_logo: this.husky.src,
            title_top_info: typeof woof_front_builder_is_demo !== 'undefined' ? woof_lang_front_builder_title_top_info_demo : woof_lang_front_builder_title_top_info,
            hide_backdrop: true,
            mousemove: true,
            /*
             top: '25%',
             bottom: '25%',
             left: '25%',
             right: '25%',
             */
            top: '25%',
            left: '25%',
            width: button.dataset.popupWidth,
            height: button.dataset.popupHeight,
            close_word: woof_lang_front_builder_close,
            start_content: woof_lang_loading,
            left_button_link: 'https://pluginus.net/support/forum/woof-woocommerce-products-filter/',
            left_button_word: woof_lang_front_builder_suggest
        });

        this.button.style.display = 'none';
        document.addEventListener('popup23-close', e => {
            if (e.detail.popup.id === this.popup.id) {
                this.button.style.display = 'inline-block';
            }
        });

        document.addEventListener('popup23-window-size', e => {
            if (e.detail.popup.id === this.popup.id) {
                if (this.popup.is_resized) {

                    if (!e.detail.width || !e.detail.height) {
                        return;
                    }

                    button.dataset.popupWidth = e.detail.width + 'px';
                    button.dataset.popupHeight = e.detail.height + 'px';

                    if (this.fetch_timer_flag) {
                        clearInterval(this.fetch_timer_flag);
                    }

                    if (this.fetch_controller) {
                        this.fetch_controller.abort();
                    }

                    this.fetch_controller = new AbortController();

                    this.fetch_timer_flag = setTimeout(() => {
                        Helper.ajax('woof_front_builder_update_additional', {
                            name: this.name,
                            popup_width: e.detail.width,
                            popup_height: e.detail.height
                        }, content => {
                            //+++
                        }, true, null, this.fetch_controller.signal);
                    }, 777);
                }

                this.popup.is_resized = true;//just flag
            }
        });

        this.fill_popup();
    }

    fill_popup() {
        if (!this.data) {
            Helper.ajax('woof_form_builder_get_items', {
                name: this.name
            }, data => {
                this.data = data;
                this._init(true);
            });
        } else {
            this._init();
        }
    }

    _init(first_init = false) {
        this.popup.generate_tabs();
        this.popup.clear_content();

        if (this.button.dataset.selected.length > 0) {
            this.selected = this.button.dataset.selected.split(',');
        } else {
            this.selected = [];
        }

        if (first_init) {
            setTimeout(e => this.popup.set_title_info(this.get_options_btn()), 777);//lets options data properly be loaded
            this.selector = new Selector(this);
            this.selector.draw();
            this.list = new List(this);
            this.list.create();
            this.options = new Options(this);
        } else {
            this.popup.set_title_info(this.get_options_btn());
            this.selector.draw();
            this.list.create();
    }
    }

    redraw_filter() {
        let ordered_items = this.selected.join(',');
        let tax_only = [];
        let by_only = [];

        if (this.selected.length > 0) {
            this.selected.forEach(key => {
                if (parseInt(this.data[key].is_taxonomy)) {
                    tax_only.push(key);
                } else {
                    by_only.push(key);
                }
            });
        }

        tax_only = tax_only.join(',');
        by_only = by_only.join(',');

        if (by_only.length === 0) {
            by_only = 'none';
        }

        if (tax_only.length === 0) {
            tax_only = 'none';
        }

        //refresh attributes
        let attributes = '';
        if (this.options.unformatted_data) {

            if (!this.options.get_option_value('sid')) {
                this.options.set_option_value('sid', 'flat_white woof_auto_1_columns woof_sid_front_builder');
            }

            this.options.unformatted_data.forEach(att => {
                attributes += `${att.field}='${att.value}' `;
            });

        }

        let viewtypes = '';
        Object.keys(this.data).forEach(item_key => {
            if (this.data[item_key].is_taxonomy) {
                viewtypes += `${item_key}:${this.data[item_key].viewtype},`;
            }
        });

        let shortcode = `woof id='xxx' name='${this.name}' swoof_slug='${this.button.dataset.slug}' filter_id='${this.button.dataset.filterId}' ${attributes} viewtypes='${viewtypes}' items_order='${ordered_items}' tax_only='${tax_only}' by_only='${by_only}'`;

        let data = {
            page: 1,
            shortcode: 'woof_nothing', //we do not need get any products, search form data only
            woof_shortcode: shortcode,
            woof_form_builder: 1
        };

        this.popup.set_flash_title(`${woof_lang_front_builder_filter_redrawing} ...`);

        //+++

        if (this.fetch_timer_flag) {
            clearInterval(this.fetch_timer_flag);
        }

        if (this.fetch_controller) {
            //cancel ajax request if user go through too quick
            this.fetch_controller.abort();
        }

        this.fetch_controller = new AbortController();

        this.fetch_timer_flag = setTimeout(() => {

            //new HTML for the filter
            Helper.ajax('woof_draw_products', data, content => {
                this.container.innerHTML = content.form;
                woof_autosubmit = parseInt(this.options.get_option_value('autosubmit'));
                woof_ajax_redraw = parseInt(this.options.get_option_value('ajax_redraw'));
                woof_is_ajax = parseInt(this.options.get_option_value('is_ajax'));

                woof_shop_page = woof_current_page_link = woof_redirect = this.options.get_option_value('redirect');
                /*
                 if (!woof_is_ajax) {
                 woof_shop_page = woof_current_page_link = woof_redirect = this.options.get_option_value('redirect');
                 } else {
                 woof_shop_page = woof_current_page_link = woof_redirect = '';
                 }
                 */
                woof_mass_reinit();
                woof_init_tooltip();
                woof_init_show_auto_form();
                woof_init_hide_auto_form();
                this.popup.reset_flash_title(woof_lang_front_builder_filter_redrawn);
            }, true, null, this.fetch_controller.signal);

            //+++

            //save selected fields into DB
            Helper.ajax('woof_front_builder_save', {
                name: this.name,
                fields: ordered_items
            }, null, true, null, this.fetch_controller.signal);

        }, 777);

    }

    update_button_data() {
        this.button.dataset.selected = this.selected.join(',');
    }

    add_to_selector(key) {
        this.selector.add(key, this.data[key].title, 1);
    }

    redraw_list() {
        this.list.draw();
    }

    append_to_list(key) {
        this.selected.push(key);
        this.update_button_data();
        this.redraw_list();
        this.redraw_filter();
    }

    appendChild(item) {
        this.container.appendChild(item);
    }

    append_content_to_popup(item) {
        this.popup.append_content(item);
    }

    //wordpress sometimes wrapping button into <p>
    look_for_container() {
        let container = this.button.nextElementSibling;
        if (!container) {
            container = this.button.parentNode.nextElementSibling;
        }

        return container;
    }

    get_options_btn() {
        return Helper.create_element('a', {
            href: '#',
            class: 'woof-front-builder-btn-options',
        }, Helper.create_element('img', {
            src: woof_link + 'ext/front_builder/img/options.gif'
        }), {
            name: 'click',
            callback: e => {
                e.preventDefault();
                this.options.draw();
                return false;
            }
        });
    }

    draw_back_btn() {
        this.popup.set_title_info(Helper.create_element('a', {
            href: '#',
            class: 'woof-front-builder-btn-back',
        }, Helper.create_element('img', {
            src: woof_link + 'ext/front_builder/img/back.svg'
        }), {
            name: 'click',
            callback: e => {
                e.preventDefault();
                this.popup.set_title(this.name);
                this.popup.set_title_info(this.get_options_btn());
                this.popup.set_content(woof_lang_loading);
                this.fill_popup();
                return false;
            }
        }));
    }
}

