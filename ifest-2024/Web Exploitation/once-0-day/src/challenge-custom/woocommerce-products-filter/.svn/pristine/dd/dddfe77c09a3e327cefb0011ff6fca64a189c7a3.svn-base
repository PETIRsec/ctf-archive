<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

return [
    [
        'title' => esc_html__('Search option', 'woocommerce-products-filter'),
        'description' => esc_html__('Search by exact value OR if meta key exists', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'search_option',
        'value' => [
            'value' => 1,
            'options' => [
                0 => esc_html__('Exact value', 'woocommerce-products-filter'),
                1 => esc_html__('Value exists', 'woocommerce-products-filter')
            ],
        ]
    ],
    [
        'title' => esc_html__('Search value (for not numeric)', 'woocommerce-products-filter'),
        'description' => esc_html__('TRUE value, all another are FALSE. Example: yes or true or 1. By default if this textinput empty 1 is true and 0 is false', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'search_value',
        'value' => ''
    ],
];

