<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

return [
    [
        'title' => esc_html__('Text search conditional', 'woocommerce-products-filter'),
        'description' => esc_html__('LIKE or Exact match', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'text_conditional',
        'value' => [
            'value' => 'LIKE',
            'options' => [
                '=' => esc_html__('Exact match', 'woocommerce-products-filter'),
                'LIKE' => esc_html__('LIKE', 'woocommerce-products-filter')
            ],
        ]
    ],
];

