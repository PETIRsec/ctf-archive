<?php
$woof_settings = woof()->settings;
?>

<div class="woof-control-section">

    <h5><?php esc_html_e('Slug aliases for front builder forms', 'woocommerce-products-filter') ?></h5>

    <div class="woof-control-container">
        <div class="woof-control">
            <ul>
                <?php
                if (!isset($woof_settings['slug_alias']) || !is_array($woof_settings['slug_alias'])) {
                    $woof_settings['slug_alias'] = array();
                }
                foreach ($ids as $id) {
                    ?>
                    <li>
                        <label><?php echo esc_html($slug . $id['id']) ?></label>
                        <input type="text"
                               name="woof_settings[slug_alias][<?php echo esc_attr($id['id']) ?>]" 
                               value="<?php echo esc_html(isset($woof_settings['slug_alias'][$id['id']]) ? $woof_settings['slug_alias'][$id['id']] : '') ?>"  />
                    </li>
                    <?php
                }
                ?>
            </ul>

        </div>
        <div class="woof-description">
            <p class="description"><?php esc_html_e("Here, you can set slug aliases for front builder forms. Ensure that the default slug is not already integrated into the shop logic. If it is, you should also update it wherever it is used. It's important to understand the implications of these changes!", 'woocommerce-products-filter') ?></p>
        </div>
    </div>

</div><!--/ .woof-control-section-->

