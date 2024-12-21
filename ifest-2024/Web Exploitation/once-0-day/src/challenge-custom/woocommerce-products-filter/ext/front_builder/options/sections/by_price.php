<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

$price_filter_types = woof()->get_price_filter_types();
unset($price_filter_types[0]);
//unset($price_filter_types[1]);

return [
    [
        'title' => esc_html__('How to show', 'woocommerce-products-filter'),
        'description' => esc_html__('Different views of price filter', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'show',
        'value' => [
            'value' => 3, //default
            'options' => $price_filter_types
        ]
    ],
    [
        'title' => esc_html__('Drop-down OR radio ranges', 'woocommerce-products-filter'),
        'description' => esc_html__('Drop-down OR radio price filter ranges. Ranges for price filter. Example: 0-50,51-100,101-i. Where "i" is infinity.', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'ranges',
        'value' => '0-50,51-100,101-i'
    ],
    [
        'title' => esc_html__('Title text', 'woocommerce-products-filter'),
        'description' => esc_html__('Text before the price filter range slider. Leave it empty if you not need it!', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'title_text',
        'value' => ''
    ],
    [
        'title' => esc_html__('Tooltip', 'woocommerce-products-filter'),
        'description' => esc_html__('Show tooltip in title label. Enter any text.', 'woocommerce-products-filter'),
        'element' => 'textarea',
        'field' => 'tooltip_text',
        'value' => ''
    ],
    [
        'title' => esc_html__('Show button for woo range-slider', 'woocommerce-products-filter'),
        'description' => esc_html__('Show button for woocommerce filter by price inside woof search form when it is dispayed as woo range-slider', 'woocommerce-products-filter'),
        'element' => 'hidden',
        'field' => 'show_button',
        'value' => 1
    ],
    [
        'title' => esc_html__('Show toggle button for radio', 'woocommerce-products-filter'),
        'description' => esc_html__('Show toggle button near the title on the front above the block of html-items if price filter displayed as radio buttons', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'show_toggle_button',
        'value' => [
            'value' => 0,
            'options' => [
                0 => esc_html__('No', 'woocommerce-products-filter'),
                1 => esc_html__('Yes, show as closed', 'woocommerce-products-filter'),
                2 => esc_html__('Yes, show as opened', 'woocommerce-products-filter'),
            ],
        ]
    ],
    [
        'title' => esc_html__('Drop-down price filter text', 'woocommerce-products-filter'),
        'description' => esc_html__('Drop-down price filter first option text', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'first_option_text',
        'value' => ''
    ],
    [
        'title' => esc_html__('Ion Range slider step', 'woocommerce-products-filter'),
        'description' => esc_html__('predifined step', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'ion_slider_step',
        'value' => 1
    ],
    [
        'title' => esc_html__('Ion Range slider text inputs', 'woocommerce-products-filter'),
        'description' => esc_html__('This works with ionSlider only', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'show_text_input',
        'value' => 1
    ],
    [
        'title' => esc_html__('Ion Range slider Taxes', 'woocommerce-products-filter'),
        'description' => esc_html__('It will be counted in the filter (only for ion-slider)', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'price_tax',
        'value' => ''
    ],
    [
        'title' => esc_html__('Ion Range slider skin', 'woocommerce-products-filter'),
        'description' => esc_html__('Skins only works for ion slider', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'price_slider_skin',
        'value' => [
            'value' => 0,
            'options' => [
                0 => esc_html__('Default', 'woocommerce-products-filter'),
                'round' => 'Round',
                'flat' => 'skinFlat',
                'big' => 'skinHTML5',
                'modern' => 'skinModern',
                'sharp' => 'Sharp',
                'square' => 'Square'
            ],
        ]
    ],
];
