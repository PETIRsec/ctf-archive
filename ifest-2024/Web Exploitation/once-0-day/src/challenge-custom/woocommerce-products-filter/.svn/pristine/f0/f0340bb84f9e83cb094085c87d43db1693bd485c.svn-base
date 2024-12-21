/**
 * @summary     Popup23
 * @description pure javascript popup window
 * @version     1.0.9
 * @file        popup-23
 * @author      realmag777
 * @contact     https://pluginus.net/contact-us/
 * @github      https://github.com/realmag777/popup-23
 * @copyright   Copyright 2020 - 2023 PluginUs.NET
 *
 * This source file is free software, available under the following license: MIT license - https://en.wikipedia.org/wiki/MIT_License
 */

'use strict';
//13-07-2023
//1 object is 1 popup
export default class Popup23 {
    constructor(data = {}) {
        if (typeof Popup23.z_index === 'undefined') {
            Popup23.z_index = 15001;
        } else {
            ++Popup23.z_index;
        }

        this.create(data);
    }

    create(data = {}) {
        this.data = data;
        this.data.close_word = data.close_word ?? 'Close';
        this.data.left_button_word = data.left_button_word ?? '';
        this.data.left_button_link = data.left_button_link ?? '#';
        this.data.start_content = data.start_content ?? 'Loading ...';

        this.node = document.createElement('div');

        if (typeof data.id === 'undefined') {
            data.id = this.create_id();
        }
        this.node.setAttribute('id', data.id);

        this.node.className = 'popup23-wrapper';
        this.node.innerHTML = this.get_template();

        document.querySelector('body').appendChild(this.node);

        this.generate_tabs();
        this.node.querySelector('.popup23').style.zIndex = Popup23.z_index;

        if (!this.data.hide_backdrop) {
            this.node.querySelector('.popup23-backdrop').style.zIndex = Popup23.z_index - 1;
        } else {
            this.node.querySelector('.popup23-backdrop').remove();
        }

        this.node.querySelectorAll('.popup23-close, .popup23-footer-button-close').forEach(item => {
            item.addEventListener('click', e => {
                e.preventDefault();
                e.stopPropagation();
                this.close();
                return false;
            });
        });

        this.init_left_button();

        //***

        this.set_title(data.title);

        if (typeof data.help_info !== 'undefined') {
            this.set_title_info(data.help_info);
        }

        if (typeof data.title_top_info !== 'undefined') {
            this.set_title_top_info(data.title_top_info);
        }
        /*
         if (typeof data.width !== 'undefined') {
         this.node.querySelector('.popup23').style.maxWidth = data.width;
         this.node.querySelector('.popup23').style.minWidth = data.width;
         }
         
         if (typeof data.height !== 'undefined') {
         this.node.querySelector('.popup23').style.maxHeight = data.height;
         this.node.querySelector('.popup23').style.minHeight = data.height;
         }
         */

        if (typeof data.width !== 'undefined') {
            this.node.querySelector('.popup23').style.width = data.width;
        }

        if (typeof data.height !== 'undefined') {
            this.node.querySelector('.popup23').style.height = data.height;
        }


        if (typeof data.left !== 'undefined') {
            this.node.querySelector('.popup23').style.left = data.left;
        }

        if (typeof data.right !== 'undefined') {
            this.node.querySelector('.popup23').style.right = data.right;
        }

        if (typeof data.top !== 'undefined') {
            this.node.querySelector('.popup23').style.top = data.top;
        }

        if (typeof data.bottom !== 'undefined') {
            this.node.querySelector('.popup23').style.bottom = data.bottom;
        }


        if (typeof data.action !== 'undefined' && data.action.length > 0) {
            document.dispatchEvent(new CustomEvent(data.action, {detail: {...data, ... {popup: this}}}));
        }

        this.node.querySelector('.popup23-content-wrapper').addEventListener('scroll', (e) => {
            document.dispatchEvent(new CustomEvent('popup23-scrolling', {
                detail: {
                    top: e.srcElement.scrollTop,
                    self: this
                }
            }));
        });

        //***
        if (typeof data.mousemove !== 'undefined') {

            let can_move = false;
            let header = this.node.querySelector('.popup23-header');
            header.onmouseover = () => header.style.cursor = 'move';

            let prev_screenX = -1;
            let prev_screenY = -1;

            header.addEventListener('mousedown', e => {
                can_move = true;
            });

            document.addEventListener('mouseup', e => {
                can_move = false;
                prev_screenX = -1;
                prev_screenY = -1;
            });


            let position = localStorage.getItem(data.title) ? JSON.parse(localStorage.getItem(data.title)) : {};
            
            if (position.left) {
                this.node.querySelector('.popup23').style.setProperty('left', position.left);
            }

            if (position.top) {
                this.node.querySelector('.popup23').style.setProperty('top', position.top);
            }

            let timer = null;

            //+++

            document.addEventListener('mousemove', e => {

                if (can_move) {

                    if (prev_screenX !== -1 && e.which === 1 && e.clientX > 0) {
                        let left = this.node.querySelector('.popup23').style.left;
                        let diff = parseInt(e.screenX) - parseInt(prev_screenX);
                        position.left = `calc(${left} + ${diff}px)`;
                        this.node.querySelector('.popup23').style.setProperty('left', position.left);
                    }

                    if (prev_screenY !== -1 && e.which === 1 && e.clientY > 0) {
                        let top = this.node.querySelector('.popup23').style.top;
                        let diff = parseInt(e.screenY) - prev_screenY;
                        position.top = `calc(${top} + ${diff}px)`;
                        this.node.querySelector('.popup23').style.setProperty('top', position.top);
                    }

                    prev_screenX = parseInt(e.screenX);
                    prev_screenY = parseInt(e.screenY);
                    if (timer) {
                        clearInterval(timer);
                    }
                    
                    timer = setTimeout(() => localStorage.setItem(data.title, JSON.stringify(position)), 777);
                }

            });
        }
        //***

        (new ResizeObserver(function (mutations) {
            document.dispatchEvent(new CustomEvent('popup23-window-size', {detail: {
                    popup: this,
                    width: parseInt(mutations[0].borderBoxSize[0].inlineSize),
                    height: parseInt(mutations[0].borderBoxSize[0].blockSize)
                }}));
        })).observe(this.node.querySelector('.popup23'));

        return this.node;
    }

    init_left_button() {
        if (!this.data.left_button_word) {
            this.node.querySelector('.popup23-footer-button-left').remove();
        }
    }

    get_template() {
        return `
        <div class="popup23">
               <div class="popup23-inner">
                   <div class="popup23-header">
                       <h3 class="popup23-title">&nbsp;</h3>
                       <div class="popup23-title-top-info"></div>
                       <div class="popup23-title-info">&nbsp;</div>
                       <a href="javascript: void(0);" class="popup23-close"></a>
                   </div>
                   <div class="popup23-content-wrapper">
                       <div class="popup23-content">${this.data.start_content}</div>
                   </div>
                   <div class="popup23-footer">
                       <a href="${this.data.left_button_link}" target="_blank" class="button popup23-footer-button-left">${this.data.left_button_word}</a>
                       <a href="javascript: void(0);" class="button popup23-footer-button-right popup23-close">${this.data.close_word}</a>
                   </div>
               </div>
           </div>

        <div class="popup23-backdrop"></div>
    `;
    }

    generate_tabs(tabs_data = null) {

        if (!tabs_data) {
            tabs_data = [
                {
                    title: '',
                    content: this.data.start_content
                }
            ];
        }

        this.data.tabs = tabs_data;

        //+++

        let container = document.createElement('div');
        container.className = 'popup23-tabset';

        //create tabs
        this.data.tabs.forEach((tab, index) => {
            let tab_radio = document.createElement('input');
            tab_radio.setAttribute('type', 'radio');
            tab_radio.setAttribute('name', 'popup23-tabset');
            tab_radio.setAttribute('id', `popup23-tab${index}`);
            tab_radio.setAttribute('aria-controls', `popup23-tab-section-${index}`);

            if (index === 0) {
                tab_radio.setAttribute('checked', true);
            }

            let tab_label = document.createElement('label');
            tab_label.setAttribute('for', `popup23-tab${index}`);
            tab_label.innerText = tab.title

            container.appendChild(tab_radio);
            if (this.data.tabs.length > 1) {
                container.appendChild(tab_label);
            }
        });


        let content_container = document.createElement('div');
        content_container.className = 'popup23-tab-panels';
        container.appendChild(content_container);

        this.data.tabs.forEach((tab, index) => {
            let section = document.createElement('section');
            section.setAttribute('id', `popup23-tab-section-${index}`);
            section.className = 'popup23-tab-panel';

            section.innerHTML = tab.content;
            content_container.appendChild(section);

            this.data.tabs[index].container = section;
        });

        this.node.querySelector('.popup23-content').innerHTML = '';
        this.node.querySelector('.popup23-content').appendChild(container);
    }

    close() {
        this.node.remove();
        document.dispatchEvent(new CustomEvent('popup23-close', {detail: {popup: this}}));
    }

    create_id(prefix = 'popup23-') {
        return prefix + Math.random().toString(36).substring(7);
    }

    set_title(title = '', flash_string = '') {
        this.title = title;

        this.node.querySelector('.popup23-title').innerHTML = title = title + (flash_string ? ` <span class="popup23-flash-title-add">[${flash_string}]</span>` : '');

        if (this.data.title_logo) {
            this.node.querySelector('.popup23-title').innerHTML = `<span><img src="${this.data.title_logo}" alt=""></span>` + title;
        } else {
            this.node.querySelector('.popup23-title').innerHTML = title;
    }
    }

    //for flash information, for examle: 'redrawing ...'
    set_flash_title(string) {
        this.set_title(this.title, string);
    }

    reset_flash_title(string = '') {
        if (string) {
            this.set_flash_title(string);
            setTimeout(() => {
                this.reset_flash_title();
            }, 999);
        } else {
            let flash = this.node.querySelector('.popup23-title').querySelector('.popup23-flash-title-add');
            if (flash) {
                flash.remove();
            }
    }
    }

    set_title_info(info) {
        let container = this.node.querySelector('.popup23-title-info');
        container.innerHTML = '';
        if (typeof info === 'object') {
            container.appendChild(info);
        } else {
            container.innerHTML = info;
        }
    }

    set_title_top_info(info) {
        let container = this.node.querySelector('.popup23-title-top-info');
        container.innerHTML = '';
        if (typeof info === 'object') {
            container.appendChild(info);
        } else {
            container.innerHTML = info;
        }
    }

    set_content(content, tab_num = 0) {
        this.get_container(tab_num).innerHTML = content;
        document.dispatchEvent(new CustomEvent('popup23-set-content', {detail: {popup: this, content: content}}));
    }

    clear_content(tab_num = 0) {
        this.get_container(tab_num).innerHTML = '';
        document.dispatchEvent(new CustomEvent('popup23-clear-content', {detail: {popup: this, content: ''}}));
    }

    append_content(node, tab_num = 0) {
        this.get_container(tab_num).appendChild(node);
    }

    get_container(tab_num = 0) {
        //return this.node.querySelector('.popup23-content');
        if (!this.data.tabs) {
            this.data.tabs = [
                {
                    title: '',
                    content: this.data.start_content
                }
            ];
        }
        return this.data.tabs[tab_num].container;
    }
}
