'use strict';

var woof_front_builder = null;//current builder

addEventListener('DOMContentLoaded', function (e) {
    let buttons = document.getElementsByClassName('woof-form-builder-btn');
    Array.from(buttons).forEach(btn => {
        btn.addEventListener('click', e => {
            if (!document.getElementById('p' + btn.id)) {
                document.dispatchEvent(new CustomEvent('woof_front_builder_start', {detail: {button: btn}}));
            }
        });
    });

    window.addEventListener('message', message => {
        let allowed = ['woof_sd_update_option', 'woof_sd_get_options', 'woof_sd_change_template',
            'woof_sd_change_term_color', 'woof_sd_change_term_color_image'];

        if (allowed.includes(message.data.action)) {
            woof_front_builder.redraw_filter();
        }
    });
});

