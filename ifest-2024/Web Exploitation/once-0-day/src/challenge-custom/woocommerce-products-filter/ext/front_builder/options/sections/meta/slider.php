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
        'title' => esc_html__('Step', 'woocommerce-products-filter'),
        'description' => esc_html__('Range step', 'woocommerce-products-filter'),
        'element' => 'number',
        'field' => 'step',
        'value' => 1
    ],
    [
        'title' => esc_html__('Range', 'woocommerce-products-filter'),
        'description' => esc_html__('Example: 1^100', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'range',
        'value' => '1^100'
    ],
    [
        'title' => esc_html__('Prefix', 'woocommerce-products-filter'),
        'description' => esc_html__('Prefix for slider slides', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'prefix',
        'value' => ''
    ],
    [
        'title' => esc_html__('Postfix', 'woocommerce-products-filter'),
        'description' => esc_html__('Postfix for slider slides', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'postfix',
        'value' => ''
    ],
    [
        'title' => esc_html__('Show inputs', 'woocommerce-products-filter'),
        'description' => esc_html__('Show two number inputs: from minimum value to maximum value of the search range', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'show_inputs',
        'value' => 1
    ],
    [
        'title' => esc_html__('Use prettify', 'woocommerce-products-filter'),
        'description' => esc_html__('The number will have a thousands separator', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'use_prettify',
        'value' => 1
    ],
    [
        'title' => esc_html__('Slider skin', 'woocommerce-products-filter'),
        'description' => esc_html__('It is possible to select a unique slider design for each meta field', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'meta_slider_skin',
        'value' => [
            'value' => 0,
            'options' => [
                0 => esc_html__('Default', 'woocommerce-products-filter'),
                'round' => 'Round',
                'flat' => 'skinFlat',
                'big' => 'skinHTML5',
                'modern' => 'skinModern',
                'sharp' => 'Sharp',
                'square' => 'Square',
            ],
        ]
    ],
];

