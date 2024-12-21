<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

//13-07-2023
final class WOOF_FRONT_BUILDER_ADDITIONAL {

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
        add_action('wp_ajax_woof_front_builder_update_additional', array($this, 'update'));

        if ($this->demo) {
            add_action('wp_ajax_nopriv_woof_front_builder_update_additional', array($this, 'update'));
        }
    }

    public function update() {

        if (!$this->is_admin) {
            return false;
        }

        $name = esc_html($_REQUEST['name']);
        $options = $this->get($name);

        $accepted_keys = ['popup_width', 'popup_height'];
        foreach ($accepted_keys as $key) {
            if (isset($_REQUEST[$key])) {
                $options[$key] = esc_html($_REQUEST[$key]);
            }
        }

        $this->db->update($this->table, array('additional' => json_encode($options)), array('name' => $name));
    }

    public function get($name) {

        static $cache = [];

        if (!isset($cache[$name])) {
            $cache[$name] = $this->db->get_row("SELECT additional FROM {$this->table} WHERE name='{$name}'")->additional;
            if (!$cache[$name]) {
                $cache[$name] = '{}';
            }
        }

        return json_decode($cache[$name], true);
    }

}
