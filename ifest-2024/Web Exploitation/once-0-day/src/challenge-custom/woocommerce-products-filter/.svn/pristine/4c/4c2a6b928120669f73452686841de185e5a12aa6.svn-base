<?php
if (!defined('ABSPATH'))
    die('No direct access allowed');


$woof_ext_featured_label = apply_filters('woof_ext_custom_title_by_featured', __('Featured products', 'woocommerce-products-filter'));
if (isset(woof()->settings['by_featured']) AND woof()->settings['by_featured']['show']) {
    ?>
    <div data-css-class="woof_checkbox_featured_container" class="woof_checkbox_featured_container woof_container woof_container_product_visibility <?php echo WOOF_HELPER::generate_container_css_classes('by_featured') ?>">
        <div class="woof_container_overlay_item"></div>
        <div class="woof_container_inner">

            <?php
            if (isset(woof()->settings['by_featured']['view']) && woof()->settings['by_featured']['view'] === 'switcher') {
                $unique_id = uniqid('woof_checkbox_by_featured-');
                ?>
                <div class="switcher23-container">

                    <input type="checkbox" class="woof_checkbox_featured_as_switcher switcher23" id="<?php echo $unique_id ?>" name="product_visibility" value="0" <?php checked('featured', woof()->is_isset_in_request_data('product_visibility') ? 'featured' : '', true) ?> />

                    <label for="<?php echo $unique_id ?>" class="switcher23-toggle">
                        <div class="switcher23-title2"><?php esc_html_e($woof_ext_featured_label) ?></div>
                        <span></span>                    
                    </label>
                </div>
                <?php
            } else {
                ?>
                <input type="checkbox" class="woof_checkbox_featured" id="woof_checkbox_featured" name="product_visibility" value="0" <?php checked('featured', woof()->is_isset_in_request_data('product_visibility') ? 'featured' : '', true) ?> />&nbsp;&nbsp;<label for="woof_checkbox_featured"><?php esc_html_e($woof_ext_featured_label) ?></label><br />
                <?php
            }
            ?>
        </div>
    </div>
    <?php
}


