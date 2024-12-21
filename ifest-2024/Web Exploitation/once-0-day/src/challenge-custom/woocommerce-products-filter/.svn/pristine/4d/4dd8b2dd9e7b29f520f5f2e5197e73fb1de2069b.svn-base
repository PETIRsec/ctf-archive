<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

return [
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
        'title' => esc_html__('View', 'woocommerce-products-filter'),
        'description' => esc_html__('How to show: checkbox or switcher', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'view',
        'value' => [
            'value' => 'switcher',
            'options' => [
                'checkbox' => esc_html__('Checkbox', 'woocommerce-products-filter'),
                'switcher' => esc_html__('Switcher', 'woocommerce-products-filter')
            ],
        ]
    ],
    [
        'title' => esc_html__('Use new DB.', 'woocommerce-products-filter'),
        'description' => esc_html__('This can speed up in stock searches for variable products.', 'woocommerce-products-filter'),
        'element' => 'hidden',
        'field' => 'new_db',
        'value' => 1
    ],
];

