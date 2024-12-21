<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

//03-07-2023
final class WOOF_FRONT_BUILDER_OPTIONS {

    private $db = null;
    private $table = null;
    private $demo = null;
    private $ext_path = null;
    private $is_admin = null;

    public function __construct($db, $table, $ext_path, $demo, $is_admin) {
        $this->db = $db;
        $this->table = $table;
        $this->ext_path = $ext_path;
        $this->demo = $demo;
        $this->is_admin = $is_admin;
        $this->init();
    }

    public function init() {
        add_action('wp_ajax_woof_form_builder_get_options', function () {
            die(json_encode($this->get_options(esc_html($_REQUEST['name']))));
        });
        add_action('wp_ajax_woof_form_builder_save_options', array($this, 'save_options'));

        if ($this->demo) {
            add_action('wp_ajax_nopriv_woof_form_builder_get_options', function () {
                die(json_encode($this->get_options(esc_html($_REQUEST['name']))));
            });
            add_action('wp_ajax_nopriv_woof_form_builder_save_options', array($this, 'save_options'));
        }
    }

    public function save_options() {

        if (!$this->is_admin) {
            return false;
        }

        $name = esc_html($_REQUEST['name']);
        $field = esc_html($_REQUEST['field']);
        $value = esc_html($_REQUEST['value']);

        $options = $this->get_options_db($name);
        $options[$field] = $value;
        $options = apply_filters('woof_front_builder_options_after_update', $options);

        $this->db->update($this->table, array('options' => json_encode($options)), array('name' => $name));
    }

    public function get_options_db($name) {
        static $cache = [];

        if (!isset($cache[$name])) {
            $cache[$name] = $this->db->get_row("SELECT options FROM {$this->table} WHERE name='{$name}'")->options;
            if (!$cache[$name]) {
                $cache[$name] = '{}';
            }
        }

        return json_decode($cache[$name], true);
    }

    public function get_options($name) {
        $options = require $this->ext_path . 'options/options.php';
        $options_data = $this->get_options_db($name);

        if (!empty($options_data)) {
            foreach ($options as $k => $option) {
                if (array_key_exists($option['field'], $options_data)) {
                    $options[$k]['value'] = array_key_exists($option['field'], $options_data) ? $options_data[$option['field']] : $options['value'];
                    $options[$k]['value'] = apply_filters('woof_front_builder_option', $options[$k]['value'], $option['field']);
                    if (woof()->show_notes && isset($options[$k]['is_not_free'])) {
                        $options[$k]['description'] .= '. <span class="woof-front-builder-premium">' . esc_html__('Not has effect in free version!', 'woocommerce-products-filter') . '</span>';
                    }
                }
            }
        }

        return $options;
    }

    public function get_options_key_value($name) {
        $res = [];
        $options = $this->get_options($name);

        if (!empty($options)) {
            foreach ($options as $opt) {
                if (is_array($opt['value'])) {
                    $res[$opt['field']] = $opt['value']['value'];
                } else {
                    $res[$opt['field']] = $opt['value'];
                }
            }
        }

        return $res;
    }

}
