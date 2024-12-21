<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

final class WOOF_EXT_STOCK_QUANTITY extends WOOF_EXT {

    public $type = 'by_html_type';
    public $html_type = 'stock_quantity'; //your custom key here
    public $index = 'stock_quantity';
    public $html_type_dynamic_recount_behavior = 'none';

    public function __construct() {
        parent::__construct();
        $this->init();
    }

    public function get_ext_path() {
        return plugin_dir_path(__FILE__);
    }

    public function get_ext_override_path() {
        return get_stylesheet_directory() . DIRECTORY_SEPARATOR . "woof" . DIRECTORY_SEPARATOR . "ext" . DIRECTORY_SEPARATOR . $this->html_type . DIRECTORY_SEPARATOR;
    }

    public function get_ext_link() {
        return plugin_dir_url(__FILE__);
    }

    public function woof_add_items_keys($keys) {
        $keys[] = $this->html_type;
        return $keys;
    }

    public function init() {
        add_filter('woof_add_items_keys', array($this, 'woof_add_items_keys'));
        add_action('woof_print_html_type_options_' . $this->html_type, array($this, 'woof_print_html_type_options'), 10, 1);
        add_action('woof_print_html_type_' . $this->html_type, array($this, 'print_html_type'), 10, 1);
        add_filter('woof_get_all_filter_titles', array($this, 'add_titles'));

        self::$includes['js']['woof_' . $this->html_type . '_html_items'] = $this->get_ext_link() . 'js/' . $this->html_type . '.js';
        // self::$includes['css']['woof_' . $this->html_type . '_html_items'] = $this->get_ext_link() . 'css/' . $this->html_type . '.css';
        self::$includes['js_init_functions'][$this->html_type] = 'woof_init_stock_quantity';
        // self::$includes['js_lang_custom'][$this->index] = esc_html__('Stock quantity', 'woocommerce-products-filter');
    }

    //settings page hook
    public function woof_print_html_type_options() {

        woof()->render_html_e($this->get_ext_path() . 'views' . DIRECTORY_SEPARATOR . 'options.php', array(
            'key' => $this->html_type,
            "woof_settings" => get_option('woof_settings', array())
                )
        );
    }

    public function add_titles($titles) {
        if (isset($titles['stock_quantity'])) {
            $title = apply_filters('woof_ext_custom_title_stock_quantity', esc_html__('Stock quantity slider', 'woocommerce-products-filter'));
            $titles['stock_quantity'] = WOOF_HELPER::wpml_translate(null, $title);
        }
        return $titles;
    }

    public function assemble_query_params(&$meta_query, $wp_query = NULL) {

        $use_for = isset(woof()->settings['stock_quantity']['use_for']) ? woof()->settings['stock_quantity']['use_for'] : 'simple';

        if ($use_for == 'both') {
            add_filter('posts_where', array($this, 'posts_where'), 9999, 2);
        } else {

            $request = woof()->get_request_data();
            if (isset($request['stock_quantity'])) {
                $from_to = explode('^', $request['stock_quantity']);
                if (count($from_to) == 2) {
                    $meta_query[] = array(
                        'key' => '_stock',
                        'value' => $from_to,
                        'type' => 'numeric',
                        'compare' => 'BETWEEN'
                    );
                }
            }
        }

        //***

        return $meta_query;
    }

    public function posts_where($where = '', $query = null) {

        global $WOOF, $wpdb;
        $request = woof()->get_request_data();
        if (!is_array($request)) {
            $request = array();
        }
        static $where_instock = "";

        //cache on the fly
        if (!empty($where_instock)) {
            return $where . $where_instock;
        }

        //+++
        if (WOOF_REQUEST::isset('woof_current_recount')) {
            $dynamic_request = WOOF_REQUEST::get('woof_current_recount');
            if (isset($dynamic_request["slug"]) AND isset($dynamic_request["taxonomy"])) {
                if (isset($request[$dynamic_request["taxonomy"]])) {
                    $request[$dynamic_request["taxonomy"]] = $request[$dynamic_request["taxonomy"]] . "," . $dynamic_request["slug"];
                } else {

                    $request[$dynamic_request["taxonomy"]] = $dynamic_request["slug"];
                }
            }
        }

        if (isset($request['stock_quantity'])) {

            $from_to = explode('^', $request['stock_quantity']);
            if (count($from_to) == 2) {

                $stock_quantity_from = intval($from_to[0]);
                $stock_quantity_to = intval($from_to[1]);

                if ($stock_quantity_from == $stock_quantity_to && $stock_quantity_from) {

                    $addtn_query = '';

                    $product_variations = $wpdb->get_results("
									SELECT posts.ID
									FROM $wpdb->posts AS posts
									LEFT JOIN $wpdb->postmeta AS postmeta ON ( posts.ID = postmeta.post_id )
									WHERE posts.post_type IN ('product','product_variation')
									AND postmeta.meta_key = '_stock'
									AND postmeta.meta_value = $stock_quantity_from" . $addtn_query, ARRAY_N);
                } else {

                    $product_variations = $wpdb->get_results("
									SELECT posts.ID
									FROM $wpdb->posts AS posts
									LEFT JOIN $wpdb->postmeta AS postmeta ON ( posts.ID = postmeta.post_id )
									WHERE posts.post_type IN ('product','product_variation')
									AND postmeta.meta_key = '_stock'
									AND postmeta.meta_value >= $stock_quantity_from AND  postmeta.meta_value < $stock_quantity_to", ARRAY_N);
                }


                $product_variations_ids = array();
                $product_ids = array();
                if (!empty($product_variations)) {
                    foreach ($product_variations as $v) {
                        $product_variations_ids[] = $v[0];
                    }

                    //+++
                    $product_variations_ids_string = implode(',', $product_variations_ids);

                    $products = $wpdb->get_results("
									SELECT posts.post_parent
									FROM $wpdb->posts AS posts
									WHERE posts.ID IN ($product_variations_ids_string) AND posts.post_parent > 0", ARRAY_N);
                    //+++


                    if (!empty($products)) {
                        foreach ($products as $v) {
                            $product_ids[] = $v[0];
                        }
                    }
                    $product_ids = array_unique($product_ids);
                }
                $product_ids = implode(',', array_merge($product_ids, $product_variations_ids));
                $product_ids = !empty($product_ids) ? $product_ids : '-1';
                $where_instock = " AND ( $wpdb->posts.ID IN($product_ids) )";
                $where .= " AND ( $wpdb->posts.ID IN($product_ids) )";
            }
        }

        return $where;
    }

}

WOOF_EXT::$includes['html_type_objects']['stock_quantity'] = new WOOF_EXT_STOCK_QUANTITY();
