<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

$skins = woof()->get_icheck_skins();
unset($skins['none']);
$formated_skins = [];
foreach ($skins as $key => $ss) {
    foreach ($ss as $skey) {
        $formated_skins[$skey] = $skey;
    }
}

return [
    [
        'title' => esc_html__('Filter max width', 'woocommerce-products-filter'),
        'description' => esc_html__('filter form width, example: 200px, 100%', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'width',
        'default_measure' => '%',
        'value' => '100%'//default
    ],
    [
        'title' => esc_html__('Filter max height', 'woocommerce-products-filter'),
        'description' => esc_html__('filter form max height, example: 300px', 'woocommerce-products-filter'),
        'element' => 'hidden',
        'field' => 'max-height',
        'default_measure' => 'px',
        'value' => '100%'
    ],
    [
        'title' => esc_html__('Default filter section width', 'woocommerce-products-filter'),
        'description' => esc_html__('default filter section width. Allows to place filter sections as columns on a page. Example: 150px, 33%, 49%, 50%. For each filter-section you can set its width in its own options!', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => '--woof-fb-section-width',
        'default_measure' => '%',
        'value' => '100%'
    ],
    [
        'title' => esc_html__('Filter section max height', 'woocommerce-products-filter'),
        'description' => esc_html__('each filter section max height. Example: 200px, auto', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => '--woof-fb-section-height',
        'default_measure' => 'px',
        'value' => 'auto'
    ],
    [
        'title' => esc_html__('Margint top', 'woocommerce-products-filter'),
        'description' => esc_html__('filter form top margin, example: 10px, 10%', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'margin-top',
        'default_measure' => 'px',
        'value' => 0,
        'is_not_free' => 0
    ],
    [
        'title' => esc_html__('Margint bottom', 'woocommerce-products-filter'),
        'description' => esc_html__('filter form bottom margin, example: 10px, 10%', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'margin-bottom',
        'default_measure' => 'px',
        'value' => 0,
        'is_not_free' => 0
    ],
    [
        'title' => esc_html__('Margint left', 'woocommerce-products-filter'),
        'description' => esc_html__('filter form left margin, example: 10px, 10%', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'margin-left',
        'default_measure' => 'px',
        'value' => 0,
        'is_not_free' => 0
    ],
    [
        'title' => esc_html__('Margint right', 'woocommerce-products-filter'),
        'description' => esc_html__('filter form right margin, example: 10px, 10%', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'margin-right',
        'default_measure' => 'px',
        'value' => 0,
        'is_not_free' => 0
    ],
    [
        'title' => esc_html__('Float', 'woocommerce-products-filter'),
        'description' => esc_html__('float of the filter form in the text content', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'float',
        'default_measure' => '',
        'value' => [
            'value' => 'none',
            'options' => [
                'none' => esc_html__('none', 'woocommerce-products-filter'),
                'left' => esc_html__('left', 'woocommerce-products-filter'),
                'right' => esc_html__('right', 'woocommerce-products-filter'),
            ],
        ],
        'is_not_free' => 0
    ],
    [
        'title' => esc_html__('Radio and Checkbox skin', 'woocommerce-products-filter'),
        'description' => esc_html__('skins for radio and checkbox items. Has no sense for Smart designer filter items', 'woocommerce-products-filter'),
        'element' => 'select',
        'field' => 'icheck_skin',
        'default_measure' => '',
        'value' => [
            'value' => woof()->settings['icheck_skin'],
            'options' => $formated_skins,
        ],
        'is_not_free' => 0
    ],
];

