<?php
if (!defined('ABSPATH'))
    die('No direct access allowed');
?>

<li data-key="<?php echo esc_attr($key) ?>" class="woof_options_li">

    <?php
    $show = 0;
    if (isset($woof_settings[$key]['show'])) {
        $show = (int) $woof_settings[$key]['show'];
    }
    ?>

    <span class="icon-arrow-combo help_tip woof_drag_and_drope" data-tip="<?php esc_html_e("drag and drop", 'woocommerce-products-filter'); ?>"></span>

    <strong class="woof_fix1"><?php esc_html_e("Stock Quantity", 'woocommerce-products-filter'); ?>:</strong>

    <span class="icon-question help_tip" data-tip="<?php esc_html_e('Show In stock only checkbox inside woof search form', 'woocommerce-products-filter') ?>"></span>
 
    <div class="select-wrap">
        <select name="woof_settings[<?php echo esc_attr($key) ?>][show]" class="woof_setting_select">
            <option value="0" <?php selected($show, 0) ?>><?php esc_html_e('No', 'woocommerce-products-filter') ?></option>
            <option value="1" <?php selected($show, 1) ?>><?php esc_html_e('Yes', 'woocommerce-products-filter') ?></option>
        </select>
    </div>


    <a href="#" data-key="<?php echo esc_attr($key) ?>" data-name="<?php esc_html_e("Search by InStock", 'woocommerce-products-filter'); ?>" class="woof-button js_woof_options js_woof_options_<?php echo esc_attr($key) ?> help_tip" data-tip="<?php esc_html_e('additional options', 'woocommerce-products-filter') ?>"><span class="icon-cog-outline"></span></a>


    <?php
    if (!isset($woof_settings[$key]['range'])) {
        $woof_settings[$key]['range'] = '0^100';
    }
    if (!isset($woof_settings[$key]['step'])) {
        $woof_settings[$key]['step'] = 1;
    }
    if (!isset($woof_settings[$key]['show_inputs'])) {
        $woof_settings[$key]['show_inputs'] = 0;
    }
	if (!isset($woof_settings[$key]['prefix'])) {
        $woof_settings[$key]['prefix'] = '';
    }
	if (!isset($woof_settings[$key]['postfix'])) {
        $woof_settings[$key]['postfix'] = '';
    }
	if (!isset($woof_settings[$key]['slider_skin'])) {
        $woof_settings[$key]['slider_skin'] = 'round';
    }
	if (!isset($woof_settings[$key]['use_prettify'])) {
        $woof_settings[$key]['use_prettify'] = 1;
    }
	if (!isset($woof_settings[$key]['show_title_label'])) {
        $woof_settings[$key]['show_title_label'] = 1;
    }
	if (!isset($woof_settings[$key]['show_toggle_button'])) {
        $woof_settings[$key]['show_toggle_button'] = 0;
    }
	if (!isset($woof_settings[$key]['tooltip_text'])) {
        $woof_settings[$key]['tooltip_text'] = '';
    }	
	if (!isset($woof_settings[$key]['use_for'])) {
        $woof_settings[$key]['use_for'] = 'simple';
    }		
    ?>

   
    <input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][range]" value="<?php echo esc_html($woof_settings[$key]['range']) ?>" />
    <input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][step]" value="<?php echo esc_html($woof_settings[$key]['step']) ?>" />
    <input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][show_inputs]" value="<?php echo esc_html($woof_settings[$key]['show_inputs']) ?>" />
    <input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][prefix]" value="<?php echo esc_html($woof_settings[$key]['prefix']) ?>" />
    <input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][postfix]" value="<?php echo esc_html($woof_settings[$key]['postfix']) ?>" />
    <input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][slider_skin]" value="<?php echo esc_html($woof_settings[$key]['slider_skin']) ?>" />
	<input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][use_prettify]" value="<?php echo esc_html($woof_settings[$key]['use_prettify']) ?>" />
    <input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][show_title_label]" value="<?php echo esc_html($woof_settings[$key]['show_title_label']) ?>" />
    <input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][show_toggle_button]" value="<?php echo esc_html($woof_settings[$key]['show_toggle_button']) ?>" />
	<input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][use_for]" value="<?php echo esc_html($woof_settings[$key]['use_for']) ?>" />
    <input type="hidden" name="woof_settings[<?php echo esc_attr($key) ?>][tooltip_text]" value="<?php echo esc_html($woof_settings[$key]['tooltip_text']) ?>" />
    <div id="woof-modal-content-<?php echo esc_attr($key) ?>" style="display: none;">

        <div class="woof-form-element-container">

            <div class="woof-name-description">
                <strong><?php esc_html_e('Search in variable produts', 'woocommerce-products-filter') ?></strong>
                <span><?php esc_html_e('Will the plugin look in each variable of variable products. Request for variables products creates more mysql queries in database ...', 'woocommerce-products-filter') ?></span>
            </div>

            <div class="woof-form-element">
                <?php
                $use_for = array(
                    'simple' => esc_html__('Simple products only', 'woocommerce-products-filter'),
                    'both' => esc_html__('Search in products and their variations', 'woocommerce-products-filter')
                );
                ?>
                <div class="select-wrap">
                    <select class="woof_popup_option" data-option="use_for">
                        <?php foreach ($use_for as $key => $value) : ?>
                            <option value="<?php echo esc_attr($key) ?>"><?php esc_html_e($value) ?></option>
                        <?php endforeach; ?>
                    </select>
                </div>

            </div>

        </div>
    <div class="woof-form-element-container">
        <div class="woof-name-description">
            <strong><?php esc_html_e('Show title label', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('Show/Hide meta block title on the front', 'woocommerce-products-filter') ?></span>
        </div>

        <div class="woof-form-element">
            <?php
            $show_title = array(
                0 => esc_html__('No', 'woocommerce-products-filter'),
                1 => esc_html__('Yes', 'woocommerce-products-filter')
            );
            ?>

            <div class="select-wrap">
                <select class="woof_popup_option" data-option="show_title_label">
                    <?php foreach ($show_title as $id => $value) : ?>
                        <option value="<?php echo esc_attr($id) ?>"><?php echo esc_html($value) ?></option>
                    <?php endforeach; ?>
                </select>
            </div>

        </div>

    </div>
    <div class="woof-form-element-container">
        <div class="woof-name-description">
            <strong><?php esc_html_e('Show toggle button', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('Show toggle button near the title on the front above the block of html-items', 'woocommerce-products-filter') ?></span>
        </div>

        <div class="woof-form-element">
            <?php
            $show_toogle = array(
                0 => esc_html__('No', 'woocommerce-products-filter'),
                1 => esc_html__('Yes, show as closed', 'woocommerce-products-filter'),
                2 => esc_html__('Yes, show as opened', 'woocommerce-products-filter')
            );
            ?>

            <div class="select-wrap">
                <select class="woof_popup_option" data-option="show_toggle_button">
                    <?php foreach ($show_toogle as $id => $value) : ?>
                        <option value="<?php echo esc_attr($id) ?>"><?php echo esc_html($value) ?></option>
                    <?php endforeach; ?>
                </select>
            </div>

        </div>

    </div>
    <div class="woof-form-element-container">

        <div class="woof-name-description">
            <strong><?php esc_html_e('Tooltip', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('Tooltip text if necessary', 'woocommerce-products-filter') ?></span>
        </div>

        <div class="woof-form-element">

            <div class="select-wrap">
                <textarea class="woof_popup_option" data-option="tooltip_text" ></textarea>
            </div>

        </div>

    </div>
    <div class="woof-form-element-container">

        <div class="woof-name-description">
            <strong><?php esc_html_e('Step', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('Range step', 'woocommerce-products-filter') ?></span>
        </div>

        <div class="woof-form-element">
            <input type="text" class="woof_popup_option" data-option="step" placeholder="" value="" />
        </div>
    </div>
    <div class="woof-form-element-container">
        <div class="woof-name-description">
            <strong><?php esc_html_e('Range', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('Example: 1^100', 'woocommerce-products-filter') ?></span>
        </div>

        <div class="woof-form-element">
            <input type="text" class="woof_popup_option" data-option="range" placeholder="" value="" />
        </div>
    </div>
    <div class="woof-form-element-container">

        <div class="woof-name-description">
            <strong><?php esc_html_e('Prefix', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('Prefix for slider slides', 'woocommerce-products-filter') ?></span>
        </div>

        <div class="woof-form-element">
            <input type="text" class="woof_popup_option" data-option="prefix" placeholder="" value="" />
        </div>

    </div>
    <div class="woof-form-element-container">

        <div class="woof-name-description">
            <strong><?php esc_html_e('Postfix', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('Postfix for slider slides', 'woocommerce-products-filter') ?></span>
        </div>

        <div class="woof-form-element">
            <input type="text" class="woof_popup_option" data-option="postfix" placeholder="" value="" />
        </div>
    </div>
    <div class="woof-form-element-container">
        <div class="woof-name-description">
            <strong><?php esc_html_e('Show inputs', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('Show two number inputs: from minimum value to maximum value of the search range', 'woocommerce-products-filter') ?></span>
        </div>

        <div class="woof-form-element">
            <?php
            $show_inputs = array(
                0 => esc_html__('No', 'woocommerce-products-filter'),
                1 => esc_html__('Yes', 'woocommerce-products-filter'),
            );
            ?>

            <div class="select-wrap">
                <select class="woof_popup_option" data-option="show_inputs">
                    <?php foreach ($show_inputs as $id => $value) : ?>
                        <option value="<?php echo esc_attr($id) ?>"><?php echo esc_html($value) ?></option>
                    <?php endforeach; ?>
                </select>
            </div>

        </div>

    </div>
    <div class="woof-form-element-container">
        <div class="woof-name-description">
            <strong><?php esc_html_e('Use prettify', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('The number will have a thousands separator', 'woocommerce-products-filter') ?></span>
        </div>

        <div class="woof-form-element">
            <?php
            $use_prettify = array(
                0 => esc_html__('No', 'woocommerce-products-filter'),
                1 => esc_html__('Yes', 'woocommerce-products-filter'),
            );
            ?>

            <div class="select-wrap">
                <select class="woof_popup_option" data-option="use_prettify">
                    <?php foreach ($use_prettify as $id => $value) : ?>
                        <option value="<?php echo esc_attr($id) ?>"><?php echo esc_html($value) ?></option>
                    <?php endforeach; ?>
                </select>
            </div>

        </div>

    </div>	
    <div class="woof-form-element-container">

        <div class="woof-name-description">
            <strong><?php esc_html_e('Slider skin', 'woocommerce-products-filter') ?></strong>
            <span><?php esc_html_e('It is possible to select a unique slider design for each meta field', 'woocommerce-products-filter') ?></span>
        </div>
        <?php
        $skins = array(
            0 => esc_html__('Default', 'woocommerce-products-filter'),
            'round' => 'Round',
            'flat' => 'skinFlat',
            'big' => 'skinHTML5',
            'modern' => 'skinModern',
            'sharp' => 'Sharp',
            'square' => 'Square',
        );
        ?>
        <div class="woof-form-element">
            <div class="select-wrap">
                <select class="woof_popup_option" data-option="slider_skin">
                    <?php foreach ($skins as $key => $value) : ?>
                        <option value="<?php echo esc_attr($key) ?>"><?php echo esc_html($value) ?></option>
                    <?php endforeach; ?>
                </select>
            </div>

        </div>

    </div>


    </div>


</li>
