<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

return [
    [
        'title' => esc_html__('Show title label', 'woocommerce-products-filter'),
        'description' => esc_html__('Show/Hide meta block title on the front', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'show_title_label',
        'value' => 1//default
    ],
    [
        'title' => esc_html__('Show toggle button', 'woocommerce-products-filter'),
        'description' => esc_html__('Show toggle button near the title on the front above the block of html-items', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'show_toggle_button',
        'value' => [
            'value' => 0,
            'options' => [
                0 => esc_html__('No', 'woocommerce-products-filter'),
                1 => esc_html__('Yes, show as closed', 'woocommerce-products-filter'),
                2 => esc_html__('Yes, show as opened', 'woocommerce-products-filter')
            ],
        ]
    ],
    [
        'title' => esc_html__('Tooltip', 'woocommerce-products-filter'),
        'description' => esc_html__('Tooltip text if necessary', 'woocommerce-products-filter'),
        'element' => 'textarea',
        'field' => 'tooltip_text',
        'value' => ''
    ],
    [
        'title' => esc_html__('Calendar date format', 'woocommerce-products-filter'),
        'description' => '',
        'element' => 'select',
        'field' => 'format',
        'value' => [
            'value' => 'mm/dd/yy',
            'options' => [
                'mm/dd/yy' => esc_html__("Default - mm/dd/yy", 'woocommerce-products-filter'),
                'dd-mm-yy' => esc_html__("Europe - dd-mm-yy", 'woocommerce-products-filter'),
                'yy-mm-dd' => esc_html__("ISO 8601 - yy-mm-dd", 'woocommerce-products-filter'),
                'd M, y' => esc_html__("Short - d M, y", 'woocommerce-products-filter'),
                'd MM, y' => esc_html__("Medium - d MM, y", 'woocommerce-products-filter'),
                'D, d M, yy' => esc_html__("Full - DD, d MM, yy", 'woocommerce-products-filter')
            ],
        ]
    ],
];

