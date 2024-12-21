<?php
if (!defined('ABSPATH'))
    die('No direct access allowed');

$selected_list = esc_html__(implode(',', $selected));
$tax_only = esc_html__(implode(',', $selected_taxonomies));
$by_only = esc_html__(implode(',', $selected_nontaxonomies));


if (empty($by_only)) {
    $by_only = 'none';
}

if (empty($tax_only)) {
    $tax_only = 'none';
}

$shortcode_id = uniqid('b-');
$attributes_string = '';

//+++

if (!empty($options)) {
    if (!isset($options['sid']) OR empty($options['sid'])) {
        $options['sid'] = 'flat_white woof_auto_1_columns woof_sid_front_builder';
    }

    foreach ($options as $key => $value) {
        $attributes_string .= "{$key}='{$value}' ";
    }
}

$style = '';
if (!empty($layout_options)) {
    foreach ($layout_options as $key => $value) {
        $style .= "{$key}:{$value}; ";
    }
}

//$swoof_slug = woof()->get_swoof_search_slug_opt() . $id;

$name = stripslashes(esc_sql($name)); //!!
$container_id = 'woof-front-builder-' . $shortcode_id;
?>

<div><!-- avoid wpautop for button -->
    <?php if ($is_admin): ?>
        <a href="javascript: void(0);" id="<?php echo esc_html__($shortcode_id) ?>" data-selected="<?php echo esc_html__($selected_list) ?>" data-slug="<?php echo $swoof_slug ?>" data-filter-id="<?php echo $id ?>" data-name="<?php echo esc_html__($name) ?>" data-popup-width="<?php echo esc_html__($popup_width) ?>" data-popup-height="<?php echo esc_html__($popup_height) ?>" class="woof-form-builder-btn">
            <img src="<?php echo $ext_link . 'img/cog.svg' ?>" style="opacity: 0;" alt="<?php echo esc_html__($name) ?>">
            <img src="<?php echo $ext_link . 'img/husky.svg' ?>" alt="<?php echo esc_html__($name) ?>">
        </a>
    <?php endif; ?>

    <div id="<?php echo $container_id ?>" class="woof-front-builder-container woof_section_scrolled woof_use_beauty_scroll" style="<?php echo $style ?>" data-name="<?php echo esc_html__($name) ?>" data-viewtypes='<?php echo json_encode(woof()->html_types) ?>'>
        <?php
        if (!empty($selected)) {
            echo do_shortcode("[woof id='{$shortcode_id}' filter_id={$id} name='{$name}' swoof_slug='{$swoof_slug}' {$attributes_string} viewtypes='{$viewtypes}' tax_only='{$tax_only}' by_only='{$by_only}']");
        }
        ?>   
    </div>
    <style type="text/css" id="<?php echo $shortcode_id ?>-styles">
        /* styles for the current HUSKY products filter form */
        <?php
        if (!empty($sections_layout_options)) {
            foreach ($sections_layout_options as $section_key => $values) {
                if (!empty($values)) {
                    echo '#' . $container_id . ' .woof_fs_' . $section_key . '{';
                    foreach ($values as $k => $v) {
                        echo $k . ': ' . $v . '; ';
                    }
                    echo '}' . PHP_EOL . PHP_EOL;
                }
            }
        }
        ?>
    </style>
</div>
