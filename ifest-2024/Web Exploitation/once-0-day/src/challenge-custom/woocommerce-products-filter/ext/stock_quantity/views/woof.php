<?php
if (!defined('ABSPATH'))
    die('No direct access allowed');


if (isset(woof()->settings['stock_quantity']) AND woof()->settings['stock_quantity']['show']) {

$skin = 'round';
if (isset(woof()->settings['ion_slider_skin'])) {
    $skin = woof()->settings['ion_slider_skin'];
}
$skin = WOOF_HELPER::check_new_ion_skin($skin);
if (isset(woof()->settings['stock_quantity']['slider_skin']) && woof()->settings['stock_quantity']['slider_skin']) {
    $skin = woof()->settings['stock_quantity']['slider_skin'];
}
$use_prettify = 'false';
if (isset(woof()->settings['stock_quantity']['use_prettify']) && woof()->settings['stock_quantity']['use_prettify']) {
    $use_prettify = 'true';
}

$request = woof()->get_request_data();
$current_request_txt = "";
if (woof()->is_isset_in_request_data("stock_quantity")) {
    $current_request_txt = $request["stock_quantity"];
    $current_request = explode('^', urldecode($current_request_txt));
} else {
    $current_request = array();
}

//***
$range = '0^100';
if (isset(woof()->settings['stock_quantity']['range']) && woof()->settings['stock_quantity']['range']) {
    $range = woof()->settings['stock_quantity']['range'];
}


$min = 0;
$max = 100;
$min_max = explode("^", $range, 2);
if (count($min_max) > 1) {
    $min = floatval($min_max[0]);
    $max = floatval($min_max[1]);
}

$min_value = $min;
$max_value = $max;
if (!empty($current_request)) {
    $min_value = floatval($current_request[0]);
    $max_value = floatval($current_request[1]);
    if ($min_value < $min) {
        $min_value = $min;
    }
    if ($max_value > $max) {
        $max_value = $max;
    }
}
//Check if slider has  products in current request
$count = 0;
$show = true;
$hide_dynamic_empty_pos = get_option('woof_hide_dynamic_empty_pos', 0);
if (empty($current_request)) {
    if ($hide_dynamic_empty_pos) {
        $meta_field = array(
            'key' => '_stock',
            'value' => array($min, $max),
        );
        $count_data = array();
        $count = woof()->dynamic_count(array(), 'slider', (WOOF_REQUEST::isset('additional_taxes')) ? WOOF_REQUEST::get('additional_taxes') : "", $meta_field);
    }
    //+++
    if ($hide_dynamic_empty_pos AND $count == 0) {
        $show = false;
    }
}

$show_title_label = (isset(woof()->settings['stock_quantity']['show_title_label'])) ? woof()->settings['stock_quantity']['show_title_label'] : 1;
$css_classes = "woof_block_html_items";
$show_toggle = 0;
if (isset(woof()->settings['stock_quantity']['show_toggle_button'])) {
    $show_toggle = (int) woof()->settings['stock_quantity']['show_toggle_button'];
}
//***
$block_is_closed = true;
if (!empty($current_request)) {
    $block_is_closed = false;
}
if ($show_toggle === 1 AND empty($current_request)) {
    $css_classes .= " woof_closed_block";
}

if ($show_toggle === 2 AND empty($current_request)) {
    $block_is_closed = false;
}
$tooltip_text = "";
if (isset(woof()->settings['stock_quantity']['tooltip_text'])) {
    $tooltip_text = woof()->settings['stock_quantity']['tooltip_text'];
}
if (in_array($show_toggle, array(1, 2))) {
    $block_is_closed = apply_filters('woof_block_toggle_state', $block_is_closed);
    if ($block_is_closed) {
        $css_classes .= " woof_closed_block";
    } else {
        $css_classes = str_replace('woof_closed_block', '', $css_classes);
    }
}
$woof_ext_stock_quantity_label = apply_filters('woof_ext_custom_title_stock_quantity', __('Stock Quantity', 'woocommerce-products-filter'));

if ($show){
    $top_panel_txt = "";
    //$top_panel_txt = WOOF_HELPER::wpml_translate(null, $woof_ext_stock_quantity_label);
    $top_panel_txt .= sprintf(":%s %s %s", (isset(woof()->settings['stock_quantity']['prefix']) ? woof()->settings['stock_quantity']['prefix'] : ''), str_replace("^", "-", $current_request_txt), (isset(woof()->settings['stock_quantity']['postfix']) ? woof()->settings['stock_quantity']['postfix'] : ''));
    $slider_id = "woof_stock_quantity_slider";
    ?>
    <div data-css-class="woof_stock_quantity_slider_container" class="woof_meta_slider_container woof_container woof_container_stock_quantity">
        <div class="woof_container_inner">
            <div class="woof_container_inner woof_container_inner_stock_quantity_slider">
                <?php if ($show_title_label) {
                    ?>
                    <<?php echo esc_html(apply_filters('woof_title_tag', 'h4')); ?>>
                    <?php echo esc_html(WOOF_HELPER::wpml_translate(null, $woof_ext_stock_quantity_label)) ?>
                    <?php WOOF_HELPER::draw_tooltipe(WOOF_HELPER::wpml_translate(null, $woof_ext_stock_quantity_label), $tooltip_text) ?>
                    <?php WOOF_HELPER::draw_title_toggle($show_toggle, $block_is_closed); ?>
                    </<?php echo esc_html(apply_filters('woof_title_tag', 'h4')); ?>>
                <?php }
                ?>
                <div class="<?php echo esc_attr($css_classes) ?>">
                    <?php
                    if (isset(woof()->settings['stock_quantity']['show_inputs']) AND woof()->settings['stock_quantity']['show_inputs']) {
                        ?>
                        <div class="woof_stock_quantity_slider_inputs">
                            <label class="woof_wcga_label_hide"  for="<?php echo esc_attr($slider_id) ?>_from"><?php esc_html_e('From', 'woocommerce-products-filter') ?></label>
                            <input id="<?php echo esc_attr($slider_id) ?>_from" type="number" data-name="stock_quantity" class="woof_metarange_slider_input_stock_quantity woof_stock_quantity_slider_from" placeholder="<?php echo esc_html($min) ?>" min="<?php echo esc_html($min) ?>" max="<?php echo esc_html($max) ?>"  value="<?php echo esc_html($min_value) ?>" />&nbsp;
                            <label class="woof_wcga_label_hide"  for="<?php echo esc_attr($slider_id) ?>_to"><?php esc_html_e('To', 'woocommerce-products-filter') ?></label>
                            <input id="<?php echo esc_attr($slider_id) ?>_to" type="number" data-name="stock_quantity" class="woof_metarange_slider_input_stock_quantity woof_stock_quantity_slider_to" placeholder="<?php echo esc_html($max) ?>" min="<?php echo esc_html($min) ?>" max="<?php echo esc_html($max) ?>"  value="<?php echo esc_html($max_value) ?>" />
                            <div class="woof_float_none"></div>
                        </div>
                    <?php } ?>

                    <label class="woof_wcga_label_hide"  for="<?php echo esc_attr($slider_id) ?>"><?php echo esc_html(WOOF_HELPER::wpml_translate(null, $woof_ext_stock_quantity_label)) ?></label>
                    <input id="<?php echo esc_attr($slider_id) ?>" 
						   class="woof_stock_quantity_slider" 
						   name="stock_quantity" 
						   data-skin="<?php echo esc_attr($skin) ?>" 
						   data-min="<?php echo esc_html($min) ?>" 
						   data-max="<?php echo esc_html($max) ?>" 
						   data-min-now="<?php echo esc_html($min_value) ?>" 
						   data-max-now="<?php echo esc_html($max_value) ?>" 
						   data-step="<?php echo esc_html(woof()->settings['stock_quantity']['step']) ?>" 
						   data-slider-prefix="<?php echo esc_html((isset(woof()->settings['stock_quantity']['prefix']) ? woof()->settings['stock_quantity']['prefix'] : '')) ?>" 
						   data-slider-postfix="<?php echo esc_html(woof()->settings['stock_quantity']['postfix']) ?>"  
						   data-prettify="<?php echo esc_html($use_prettify); ?>" 
						   value="" />
                </div>
                <input type="hidden" 
					   value="<?php echo esc_html($top_panel_txt) ?>" 
					   data-anchor="woof_n_stock_quantity_<?php echo esc_attr($current_request_txt) ?>" />
            </div>
        </div>
    </div>
<?php }
	
}


