<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

//30-06-2023
final class WOOF_FRONT_BUILDER_VIEWTYPES {
    
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
        add_action('wp_ajax_woof_form_builder_update_viewtype', array($this, 'update'));

        if ($this->demo) {
            add_action('wp_ajax_nopriv_woof_form_builder_update_viewtype', array($this, 'update'));
        }
    }

    public function update() {

        if (!$this->is_admin) {
            return false;
        }

        $name = esc_html($_REQUEST['name']);
        $key = esc_html($_REQUEST['key']);
        $value = esc_html($_REQUEST['value']);

        $viewtypes = $this->get($name);
        $viewtypes[$key] = $value;

        $this->db->update($this->table, array('viewtypes' => json_encode($viewtypes)), array('name' => $name));
    }

    public function get($name) {
        static $cache = [];

        if (!isset($cache[$name])) {
            $cache[$name] = $this->db->get_row("SELECT viewtypes FROM {$this->table} WHERE name='{$name}'")->viewtypes;
            if (!$cache[$name]) {
                $cache[$name] = '{}';
            }
        }

        return json_decode($cache[$name], true);
    }

}
