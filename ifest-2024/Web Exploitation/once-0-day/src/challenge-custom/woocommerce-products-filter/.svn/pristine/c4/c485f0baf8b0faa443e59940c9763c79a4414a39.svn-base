"use strict";
function woof_init_onbackorder() {
    if (icheck_skin != 'none') {

        jQuery('.woof_checkbox_onbackorder').iCheck('destroy');

        let icheck_selector = '.woof_checkbox_onbackorder';
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

        jQuery('.woof_checkbox_onbackorder').on('ifChecked', function (event) {
            jQuery(this).attr("checked", true);
            woof_current_values.backorder = 'onbackorder';
            woof_ajax_page_num = 1;
            if (woof_autosubmit) {
                woof_submit_link(woof_get_submit_link());
            }
        });

        jQuery('.woof_checkbox_onbackorder').on('ifUnchecked', function (event) {
            jQuery(this).attr("onbackorder", false);
            delete woof_current_values.backorder;
            woof_ajax_page_num = 1;
            if (woof_autosubmit) {
                woof_submit_link(woof_get_submit_link());
            }
        });

    } else {
        jQuery('.woof_checkbox_onbackorder').on('change', function (event) {
            if (jQuery(this).is(':checked')) {
                jQuery(this).attr("checked", true);
                woof_current_values.backorder = 'onbackorder';
                woof_ajax_page_num = 1;
                if (woof_autosubmit) {
                    woof_submit_link(woof_get_submit_link());
                }
            } else {
                jQuery(this).attr("checked", false);
                delete woof_current_values.backorder;
                woof_ajax_page_num = 1;
                if (woof_autosubmit) {
                    woof_submit_link(woof_get_submit_link());
                }
            }
        });
    }

    //+++

    jQuery('.woof_checkbox_onbackorder_as_switcher').on('change', function (event) {
        if (jQuery(this).is(':checked')) {
            jQuery(this).attr("checked", true);
            woof_current_values.backorder = 'onbackorder';
            woof_ajax_page_num = 1;
            if (woof_autosubmit) {
                woof_submit_link(woof_get_submit_link());
            }
        } else {
            jQuery(this).attr("checked", false);
            delete woof_current_values.backorder;
            woof_ajax_page_num = 1;
            if (woof_autosubmit) {
                woof_submit_link(woof_get_submit_link());
            }
        }
    });
}
