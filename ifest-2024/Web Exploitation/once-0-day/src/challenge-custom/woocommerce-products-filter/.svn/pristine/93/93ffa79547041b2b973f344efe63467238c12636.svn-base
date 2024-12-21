<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

return [
    [
        'title' => esc_html__('Placeholder text', 'woocommerce-products-filter'),
        'description' => esc_html__('Leave it empty if you not need it.', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'placeholder',
        'value' => ''
    ],
    [
        'title' => esc_html__('Behavior', 'woocommerce-products-filter'),
        'description' => esc_html__('Behavior of the text searching', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'behavior',
        'value' => [
            'value' => 'title',
            'options' => [
                'title' => esc_html__("Search by title", 'woocommerce-products-filter'),
                'content' => esc_html__("Search by content", 'woocommerce-products-filter'),
                'excerpt' => esc_html__("Search by excerpt", 'woocommerce-products-filter'),
                'content_or_excerpt' => esc_html__("Search by content OR excerpt", 'woocommerce-products-filter'),
                'title_or_content_or_excerpt' => esc_html__("Search by title OR content OR excerpt", 'woocommerce-products-filter'),
                'title_or_content' => esc_html__("Search by title OR content", 'woocommerce-products-filter'),
            //'title_and_content' => esc_html__("Search by title AND content", 'woocommerce-products-filter')
            ],
        ]
    ],
    [
        'title' => esc_html__('Search by full word only', 'woocommerce-products-filter'),
        'description' => esc_html__('The result is only with the full coincidence of words', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'search_by_full_word',
        'value' => 0
    ],
    [
        'title' => esc_html__('Autocomplete', 'woocommerce-products-filter'),
        'description' => esc_html__('Show found variants in drop-down list', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'autocomplete',
        'value' => 1
    ],
    [
        'title' => esc_html__('How to open links with posts in suggestion', 'woocommerce-products-filter'),
        'description' => esc_html__('In the same window (_self) or in the new one (_blank)', 'woocommerce-products-filter'),
        'element' => 'hidden',
        'field' => 'how_to_open_links',
        'value' => 1
    ],
    [
        'title' => esc_html__('+Taxonomies', 'woocommerce-products-filter'),
        'description' => esc_html__('Text search also works with taxonomies (attributes, categories, tags)', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'taxonomy_compatibility',
        'value' => 0
    ],
    [
        'title' => esc_html__('+SKU', 'woocommerce-products-filter'),
        'description' => esc_html__('Activates the ability to search by SKU in the same text-input', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'sku_compatibility',
        'value' => 0
    ],
    [
        'title' => esc_html__('Custom fields', 'woocommerce-products-filter'),
        'description' => esc_html__('Type meta keys separated by comma. An example:_seo_description,seo_title', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'custom_fields',
        'value' => ''
    ],
    [
        'title' => esc_html__('Search by description in product variations', 'woocommerce-products-filter'),
        'description' => esc_html__('Ability to search by the description of the any variation of the variable product', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'search_desc_variant',
        'value' => 0
    ],
    [
        'title' => esc_html__('Use cache', 'woocommerce-products-filter'),
        'description' => esc_html__('Works for text search and make its faster', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'use_cache',
        'value' => 0
    ],
    [
        'title' => esc_html__('Text length', 'woocommerce-products-filter'),
        'description' => esc_html__('Number of words in the description', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'view_text_length',
        'value' => 10
    ],
    [
        'title' => esc_html__('Min symbols', 'woocommerce-products-filter'),
        'description' => esc_html__('Minimum number of symbols to start searching. By default 3 symbols', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'min_symbols',
        'value' => 3
    ],
    [
        'title' => esc_html__('Per page', 'woocommerce-products-filter'),
        'description' => esc_html__('Number of products per one block on the search drop-down', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'max_posts',
        'value' => 10
    ],
    [
        'title' => esc_html__('Max drop-down height', 'woocommerce-products-filter'),
        'description' => esc_html__('The maximum height of the drop-down with the results in px.', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'max_open_height',
        'value' => 300
    ],
    [
        'title' => esc_html__('Template', 'woocommerce-products-filter'),
        'description' => esc_html__('Insert the name of your custom template. The template must be located at:', 'woocommerce-products-filter') . ' ' . esc_html(get_stylesheet_directory() . DIRECTORY_SEPARATOR . "woof" . DIRECTORY_SEPARATOR . "ext" .
                DIRECTORY_SEPARATOR . 'by_text' . DIRECTORY_SEPARATOR . "views" . DIRECTORY_SEPARATOR . "templates" . DIRECTORY_SEPARATOR),
        'element' => 'text',
        'field' => 'template',
        'value' => ''
    ],
    [
        'title' => esc_html__('Notes for customer', 'woocommerce-products-filter'),
        'description' => esc_html__('Text notes for customer if you need it.', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'notes_for_customer',
        'value' => ''
    ],
];

