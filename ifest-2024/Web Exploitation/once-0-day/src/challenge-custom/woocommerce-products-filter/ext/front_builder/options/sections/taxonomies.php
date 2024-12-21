<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

return [
    [
        'title' => esc_html__('Show title label', 'woocommerce-products-filter'),
        'description' => esc_html__('Visibility of block title', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'show_title_label',
        'value' => 1//default
    ],
    [
        'title' => esc_html__('Show toggle button', 'woocommerce-products-filter'),
        'description' => esc_html__('Show toggle button near the title on the front above the block of html-items. If title label is disabled leave here [No].', 'woocommerce-products-filter'),
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
        'title' => esc_html__('Tooltip', 'woocommerce-products-filter'),
        'description' => esc_html__('Show tooltip in title label. Enter any text.', 'woocommerce-products-filter'),
        'element' => 'textarea',
        'field' => 'tooltip_text',
        'value' => ''
    ],
    [
        'title' => esc_html__('Not toggled terms count', 'woocommerce-products-filter'),
        'description' => esc_html__('Enter count of terms which should be visible to make all other collapsible. "Show more" button will be appeared. This feature is works with: radio, checkboxes, labels, colors, smart designer items.', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'not_toggled_terms_count',
        'value' => '0'
    ],
    [
        'title' => esc_html__('Taxonomy custom label', 'woocommerce-products-filter'),
        'description' => esc_html__('For example you want to show title of Product Categories as "My Products". Just for your convenience.', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'custom_tax_label',
        'value' => ''
    ],
    [
        'title' => esc_html__('Display items in a row', 'woocommerce-products-filter'),
        'description' => esc_html__('Works for radio and checkboxes only. Allows show radio/checkboxes in 1 row!', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'dispay_in_row',
        'value' => 0
    ],
    [
        'title' => esc_html__('Sort terms', 'woocommerce-products-filter'),
        'description' => esc_html__('How to sort terms inside of filter block', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'orderby',
        'value' => [
            'value' => -1,
            'options' => [
                '-1' => esc_html__('Default', 'woocommerce-products-filter'),
                'id' => 'ID',
                'name' => esc_html__('Title', 'woocommerce-products-filter'),
                'numeric' => esc_html__('Numeric', 'woocommerce-products-filter')
            ],
        ]
    ],
    [
        'title' => esc_html__('Sort terms direction', 'woocommerce-products-filter'),
        'description' => esc_html__('Direction of terms sorted inside of filter block', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'order',
        'value' => [
            'value' => 'ASC',
            'options' => [
                'ASC' => 'ASC',
                'DESC' => 'DESC'
            ],
        ]
    ],
    [
        'title' => esc_html__('Logic of filtering', 'woocommerce-products-filter'),
        'description' => esc_html__('AND or OR: if to select AND and on the site front select 2 terms - will be found products which contains both terms on the same time. If to select NOT IN will be found items which not has selected terms!! Means vice versa to the the concept of including: excluding. AND works for that filter sections which allows to select more than one filter item (checkbox, color)', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'comparison_logic',
        'value' => [
            'value' => 'OR',
            'options' => [
                'OR' => 'OR',
                'AND' => 'AND',
                'NOT IN' => 'NOT IN'
            ],
        ]
    ],
];
