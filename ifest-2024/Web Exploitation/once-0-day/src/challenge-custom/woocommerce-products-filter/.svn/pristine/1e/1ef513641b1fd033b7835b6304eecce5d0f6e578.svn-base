<?php
if (!defined('ABSPATH'))
    die('No direct access allowed');


$woof_ext_instock_label = apply_filters('woof_ext_custom_title_by_instock', __('In stock', 'woocommerce-products-filter'));
if (isset(woof()->settings['by_instock']) AND woof()->settings['by_instock']['show']) {
    if (isset(woof()->settings['by_instock']['view']) && woof()->settings['by_instock']['view'] === 'switcher') {
        $unique_id = uniqid('woof_checkbox_instock-');
        ?>
        <div data-css-class="woof_checkbox_instock_container" class="woof_checkbox_instock_container woof_container woof_container_stock <?php echo WOOF_HELPER::generate_container_css_classes('by_instock') ?>">
            <div class="woof_container_overlay_item"></div>
            <div class="woof_container_inner">

                <div class="switcher23-container">

                    <input type="checkbox" class="woof_checkbox_instock_as_switcher switcher23" id="<?php echo $unique_id ?>" name="stock" value="0" <?php checked('instock', woof()->is_isset_in_request_data('stock') ? 'instock' : '', true) ?> />

                    <label for="<?php echo $unique_id ?>" class="switcher23-toggle">
                        <div class="switcher23-title2"><?php esc_html_e($woof_ext_instock_label) ?></div>
                        <span></span>                    
                    </label>
                </div>

            </div>
        </div>
        <?php
    } else {
        ?>
        <div data-css-class="woof_checkbox_instock_container" class="woof_checkbox_instock_container woof_container woof_container_stock <?php echo WOOF_HELPER::generate_container_css_classes('by_instock') ?>">
            <div class="woof_container_overlay_item"></div>
            <div class="woof_container_inner">
                <input type="checkbox" class="woof_checkbox_instock" id="woof_checkbox_instock" name="stock" value="0" <?php checked('instock', woof()->is_isset_in_request_data('stock') ? 'instock' : '', true) ?> />&nbsp;&nbsp;<label for="woof_checkbox_instock"><?php esc_html_e($woof_ext_instock_label) ?></label><br />
            </div>
        </div>
        <?php
    }
}


