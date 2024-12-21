"use strict";
function woof_init_acf_true_false() {
    if (icheck_skin != 'none') {

        let icheck_selector = '.woof_acf_checkbox';
        let skin = jQuery(icheck_selector).parents('.woof_redraw_zone').eq(0).data('icheck-skin');
        if (skin) {
            skin = skin.split('_');
            jQuery(icheck_selector).iCheck({
                checkboxClass: 'icheckbox_' + skin[0] + '-' + skin[1]
            });
        } else {
            jQuery(icheck_selector).iCheck({
                checkboxClass: 'icheckbox_' + icheck_skin.skin + '-' + icheck_skin.color
            });
        }

        jQuery('.woof_acf_checkbox').on('ifChecked', function (event) {
            jQuery(this).attr("checked", true);
            woof_current_values[jQuery(this).attr("name")] = 1;
            woof_ajax_page_num = 1;
            if (woof_autosubmit) {
                woof_submit_link(woof_get_submit_link());
            }
        });

        jQuery('.woof_acf_checkbox').on('ifUnchecked', function (event) {
            jQuery(this).attr("checked", false);
            delete woof_current_values[jQuery(this).attr("name")];
            woof_ajax_page_num = 1;
            if (woof_autosubmit) {
                woof_submit_link(woof_get_submit_link());
            }
        });

    } else {
        jQuery('.woof_acf_checkbox').on('change', function (event) {
            if (jQuery(this).is(':checked')) {
                jQuery(this).attr("checked", true);
                woof_current_values[jQuery(this).attr("name")] = 1;
                woof_ajax_page_num = 1;
                if (woof_autosubmit) {
                    woof_submit_link(woof_get_submit_link());
                }
            } else {
                jQuery(this).attr("checked", false);
                delete woof_current_values[jQuery(this).attr("name")];
                woof_ajax_page_num = 1;
                if (woof_autosubmit) {
                    woof_submit_link(woof_get_submit_link());
                }
            }
        });
    }
}





