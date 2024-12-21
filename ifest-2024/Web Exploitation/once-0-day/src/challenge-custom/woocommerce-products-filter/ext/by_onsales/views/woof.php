<?php
if (!defined('ABSPATH'))
    die('No direct access allowed');


$woof_ext_onsales_label = apply_filters('woof_ext_custom_title_by_onsales', esc_html__('On sale', 'woocommerce-products-filter'));
if (isset(woof()->settings['by_onsales']) AND woof()->settings['by_onsales']['show']) {
    if (!isset($additional_taxes)) {
        $additional_taxes = "";
    }

    WOOF_REQUEST::set('additional_taxes', $additional_taxes);
    $show_count = get_option('woof_show_count', 0);
    $show_count_dynamic = get_option('woof_show_count_dynamic', 0);
    $hide_dynamic_empty_pos = get_option('woof_hide_dynamic_empty_pos', 0);
    WOOF_REQUEST::set('hide_terms_count_txt', isset(woof()->settings['hide_terms_count_txt']) ? woof()->settings['hide_terms_count_txt'] : 0);
    $count_string = "";
    $count = 0;
    $current_request = woof()->get_request_data();

    if (!isset($current_request['onsales'])) {
        if ($show_count) {

            if ($show_count_dynamic) {

                $count = woof()->dynamic_count(array(), 'multi', WOOF_REQUEST::get('additional_taxes'), array(), "onsale");
            } else {
                $all_ids = wc_get_product_ids_on_sale();
                $count = count($all_ids);
            }
			$count_format = apply_filters('woof_term_count_format', '(%d)',  'by_onsales');		
            $count_string = '<span>' . sprintf($count_format, $count). '</span>';
        }
        //+++
        if ($hide_dynamic_empty_pos AND $count == 0) {
            return "";
        }
    }

    if (WOOF_REQUEST::isset('hide_terms_count_txt') AND WOOF_REQUEST::get('hide_terms_count_txt')) {
        $count_string = "";
    }
    ?>
    <div data-css-class="woof_checkbox_sales_container" class="woof_checkbox_sales_container woof_container woof_container_onsales <?php echo WOOF_HELPER::generate_container_css_classes('by_onsales') ?>">
        <div class="woof_container_overlay_item"></div>
        <div class="woof_container_inner">


            <?php
            if (isset(woof()->settings['by_onsales']['view']) && woof()->settings['by_onsales']['view'] === 'switcher') {
                $unique_id = uniqid('woof_checkbox_by_onsales-');
                ?>
                <div class="switcher23-container">

                    <input type="checkbox" class="woof_checkbox_sales_as_switcher switcher23" id="<?php echo $unique_id ?>" name="sales" value="0" <?php checked('salesonly', woof()->is_isset_in_request_data('onsales') ? 'salesonly' : '', true) ?> />

                    <label for="<?php echo $unique_id ?>" class="switcher23-toggle">
                        <div class="switcher23-title2"><?php echo esc_html__($woof_ext_onsales_label) . ' ' . $count_string ?></div>
                        <span></span>                    
                    </label>
                </div>
                <?php
            } else {
                ?>
                <input type="checkbox" class="woof_checkbox_sales" id="woof_checkbox_sales" name="sales" value="0" <?php checked('salesonly', woof()->is_isset_in_request_data('onsales') ? 'salesonly' : '', true) ?> />&nbsp;&nbsp;<label for="woof_checkbox_sales"><?php
                    esc_html_e($woof_ext_onsales_label);
                    echo wp_kses_post(wp_unslash($count_string))
                    ?></label>
                <?php
            }
            ?>
        </div>
    </div>
    <?php
}