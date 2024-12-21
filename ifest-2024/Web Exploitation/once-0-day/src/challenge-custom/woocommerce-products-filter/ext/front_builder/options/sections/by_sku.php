<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

return [
    [
        'title' => esc_html__('Placeholder text', 'woocommerce-products-filter'),
        'description' => esc_html__('SKU textinput placeholder. Set "none" if you want leave it empty on the front.', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'placeholder',
        'value' => ''
    ],
    [
        'title' => esc_html__('Conditions logic', 'woocommerce-products-filter'),
        'description' => esc_html__('LIKE or Exact match', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'logic',
        'value' => [
            'value' => 'LIKE',
            'options' => [
                '=' => esc_html__('Exact match', 'woocommerce-products-filter'),
                'LIKE' => esc_html__('LIKE', 'woocommerce-products-filter')
            ],
        ]
    ],
    [
        'title' => esc_html__('Autocomplete', 'woocommerce-products-filter'),
        'description' => esc_html__('Autocomplete relevant variants in SKU textinput', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'autocomplete',
        'value' => 1
    ],
    [
        'title' => esc_html__('Behavior of reset button', 'woocommerce-products-filter'),
        'description' => esc_html__('Make filtering after clearing the SKU field or just clear the text input.', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'reset_behavior',
        'value' => [
            'value' => 1,
            'options' => [
                0 => esc_html__('Clear text input', 'woocommerce-products-filter'),
                1 => esc_html__('Make filtering', 'woocommerce-products-filter')
            ],
        ]
    ],
    [
        'title' => esc_html__('Autocomplete products count', 'woocommerce-products-filter'),
        'description' => esc_html__('How many show products in the autocomplete list', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'autocomplete_items',
        'value' => 10
    ],
    [
        'title' => esc_html__('Search in variable produts', 'woocommerce-products-filter'),
        'description' => esc_html__('Will the plugin look in each variable of variable products. Request for variables products creates more mysql queries in database ...', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'use_for',
        'value' => [
            'value' => 'simple',
            'options' => [
                'simple' => esc_html__('Simple products only', 'woocommerce-products-filter'),
                'both' => esc_html__('Search in products and their variations', 'woocommerce-products-filter')
            ],
        ]
    ],
    [
        'title' => esc_html__('Notes for customer', 'woocommerce-products-filter'),
        'description' => esc_html__('Any notes for customer. Example: use comma for searching by more than 1 SKU!', 'woocommerce-products-filter'),
        'element' => 'textarea',
        'field' => 'notes_for_customer',
        'value' => ''
    ],
    [
        'title' => esc_html__('Image', 'woocommerce-products-filter'),
        'description' => esc_html__('Image for sku search button which appears near input when users typing there any symbols. Better use png. Size is: 20x20 px.', 'woocommerce-products-filter') . ' ' . sprintf(esc_html__('Example %s', 'woocommerce-products-filter'), WOOF_LINK . 'img/eye-icon1.png'),
        'element' => 'textarea',
        'field' => 'image',
        'value' => ''
    ],
];

