<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

return [
    [
        'title' => esc_html__('Autosubmit', 'woocommerce-products-filter'),
        'description' => esc_html__('allows auto-submiting of the search form even if its disabled in the plugin options page', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'autosubmit',
        'value' => 1//default
    ],
    [
        'title' => esc_html__('Autohide', 'woocommerce-products-filter'),
        'description' => esc_html__('is search form for should be hidden or shown after page loaded', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'autohide',
        'value' => 0
    ],
    [
        'title' => esc_html__('Is AJAX', 'woocommerce-products-filter'),
        'description' => esc_html__('is generated searching form should works with AJAX. Should be activated option in tab Options [Try to ajaxify the shop]. Also for using with shortcode [woof_products] use there required attribute is_ajax=1: [woof_products is_ajax=1]', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'is_ajax',
        'value' => 0
    ],
    [
        'title' => esc_html__('AJAX redraw', 'woocommerce-products-filter'),
        'description' => esc_html__('redraws search form without submiting of the search data. Doesn work in AJAX mode', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'ajax_redraw',
        'value' => 0
    ],
    [
        'title' => esc_html__('Redirect', 'woocommerce-products-filter'),
        'description' => esc_html__('allows to show results on any another page of the site', 'woocommerce-products-filter'),
        'element' => 'textarea',
        'field' => 'redirect',
        'value' => ''
    ],
    [
        'title' => esc_html__('Buttons position', 'woocommerce-products-filter'),
        'description' => esc_html__('allows to set Filter and Reset button on bottom – b, top – t, top and bottom – tb. Default is bottom', 'woocommerce-products-filter'),
        'element' => 'text',
        'field' => 'btn_position',
        'value' => 'tb',
        'is_not_free' => intval(woof()->show_notes)
    ],
    [
        'title' => esc_html__('As button', 'woocommerce-products-filter'),
        'description' => esc_html__('is generated searching form should be hidden. In the case of the hidden form you will see simple button where after clicking on search form will be appeared', 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'start_filtering_btn',
        'value' => 0
    ],
    /*
      [
      'title' => esc_html__('Dynamic recount', 'woocommerce-products-filter'),
      'description' => esc_html__('enables dynamic recount personally for current products search form. Default is option in tab Options', 'woocommerce-products-filter'),
      'element' => 'switcher',
      'field' => 'dynamic_recount',
      'value' => 1,
      'is_not_free' => 0
      ],
      [
      'title' => esc_html__('Hide terms count text', 'woocommerce-products-filter'),
      'description' => esc_html__('hide text with count of variants', 'woocommerce-products-filter'),
      'element' => 'switcher',
      'field' => 'hide_terms_count',
      'value' => 0,
      'is_not_free' => intval(woof()->show_notes)
      ],
      [
      'title' => esc_html__('Conditionals', 'woocommerce-products-filter'),
      'description' => esc_html__("special attribute for extension 'Conditionals' which allows to define the conditions for displaying filter elements depending of the current filtering request, something like predefined steps. Example: product_cat>by_price,pa_size,by_instock>pa_color+pa_size->by_price", 'woocommerce-products-filter'),
      'element' => 'textarea',
      'field' => 'conditionals',
      'value' => ''
      ],
     * 
     */
    [
        'title' => esc_html__('Mobile mode', 'woocommerce-products-filter'),
        'description' => esc_html__("hide the HUSKY filter form on a mobile device and a button appears to show the filter. To display the button in a specific place use the shortcode [woof_mobile] – this shortcode adds a container to which the button is inserted.", 'woocommerce-products-filter'),
        'element' => 'switcher',
        'field' => 'mobile_mode',
        'value' => 0
    ],
    [
        'title' => 'sid',
        'description' => esc_html__("shortcode-identificator – uses for generating unique CSS class in main container of generated search form making unique design. Defined and basic sid in the plugin is 'auto_shorcode'. Customers and developers can create any sids and apply theirs own CSS styles. If you not understand - do not touch.", 'woocommerce-products-filter'),
        'element' => 'hidden',
        'field' => 'sid',
        'value' => 'flat_white woof_auto_1_columns woof_sid_front_builder'
    ],
    [
        'title' => esc_html__('Slug alias', 'woocommerce-products-filter'),
        'description' => esc_html__("To change the slug alias for this shortcode, please navigate to the plugin settings, select the 'Advanced' tab, and then proceed to 'Slug aliases for front builder forms'", 'woocommerce-products-filter'),
        'element' => 'xxx',
        'field' => 'xxx',
        'value' => 0
    ],
];

