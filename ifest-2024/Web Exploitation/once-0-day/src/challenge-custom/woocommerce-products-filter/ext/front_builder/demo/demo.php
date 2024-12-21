<?php

if (!defined('ABSPATH'))
    die('No direct access allowed');

//09-06-2023
final class WOOF_FRONT_BUILDER_DEMO {

    public function __construct($ext_path) {
        $this->ext_path = $ext_path;
    }

    public function install() {
        if (!is_file($this->get_data_file_path())) {
            file_put_contents($this->get_data_file_path(), '');
        }

        return '';
    }

    private function get_data_file_path() {
        $file_name = md5(filter_var(WOOF_HELPER::get_server_var('REMOTE_ADDR'), FILTER_VALIDATE_IP)) . '.txt';
        return $this->ext_path . 'demo' . DIRECTORY_SEPARATOR . 'data' . DIRECTORY_SEPARATOR . $file_name;
    }

    private function get_options_file_path() {
        $file_name = md5(filter_var(WOOF_HELPER::get_server_var('REMOTE_ADDR'), FILTER_VALIDATE_IP)) . '_options.txt';
        return $this->ext_path . 'demo' . DIRECTORY_SEPARATOR . 'data' . DIRECTORY_SEPARATOR . $file_name;
    }

    private function get_options_layout_file_path() {
        $file_name = md5(filter_var(WOOF_HELPER::get_server_var('REMOTE_ADDR'), FILTER_VALIDATE_IP)) . '_options_layout.txt';
        return $this->ext_path . 'demo' . DIRECTORY_SEPARATOR . 'data' . DIRECTORY_SEPARATOR . $file_name;
    }

    private function get_viewtypes_layout_file_path() {
        $file_name = md5(filter_var(WOOF_HELPER::get_server_var('REMOTE_ADDR'), FILTER_VALIDATE_IP)) . '_viewtypes.txt';
        return $this->ext_path . 'demo' . DIRECTORY_SEPARATOR . 'data' . DIRECTORY_SEPARATOR . $file_name;
    }

    public function get_data() {

        if (!file_exists($this->get_data_file_path())) {
            file_put_contents($this->get_data_file_path(), '');
        }

        $data_string = file_get_contents($this->get_data_file_path());

        if (empty($data_string)) {
            $data = [
                'selected' => [],
                'options' => []
            ];
        } else {
            $data = [
                'selected' => explode(',', $data_string),
                'options' => []
            ];
        }

        $data['name'] = 'My test with filter';

        $data['selected_taxonomies'] = [];
        $data['selected_nontaxonomies'] = [];

        if (empty($data['selected'])) {
            $data['selected'] = []; //NULL
        } else {
            foreach ($data['selected'] as $key) {
                if (taxonomy_exists($key)) {
                    $data['selected_taxonomies'][] = $key;
                } else {
                    $data['selected_nontaxonomies'][] = $key;
                }
            }
        }

        return $data;
    }

    public function save_items() {
        file_put_contents($this->get_data_file_path(), esc_html($_REQUEST['fields']));
    }

    public function save_options() {
        $name = esc_html($_REQUEST['name']);
        $field = esc_html($_REQUEST['field']);
        $value = esc_html($_REQUEST['value']);

        $options = $this->get_options_db($name);
        $options[$field] = $value;

        file_put_contents($this->get_options_file_path(), json_encode($options));
    }

    public function get_options_db() {

        if (!file_exists($this->get_options_file_path())) {
            file_put_contents($this->get_options_file_path(), '');
        }

        $options = file_get_contents($this->get_options_file_path());

        if (!$options) {
            $options = '{}';
        }

        return json_decode($options, true);
    }

    public function save_options_layout() {
        $name = esc_html($_REQUEST['name']);
        $field = esc_html($_REQUEST['field']);
        $value = esc_html($_REQUEST['value']);

        $options = $this->get_options_layout_db($name);
        $options[$field] = $value;

        file_put_contents($this->get_options_layout_file_path(), json_encode($options));
    }

    public function get_options_layout_db() {

        if (!file_exists($this->get_options_layout_file_path())) {
            file_put_contents($this->get_options_layout_file_path(), '');
        }

        $options = file_get_contents($this->get_options_layout_file_path());

        if (!$options) {
            $options = '{}';
        }

        return json_decode($options, true);
    }

    //+++

    public function update_viewtypes() {
        $name = esc_html($_REQUEST['name']);
        $key = esc_html($_REQUEST['key']);
        $value = esc_html($_REQUEST['value']);

        $viewtypes = $this->get_viewtypes($name);
        $viewtypes[$key] = $value;

        file_put_contents($this->get_viewtypes_layout_file_path(), json_encode($viewtypes));
    }

    public function get_viewtypes() {

        if (!file_exists($this->get_viewtypes_layout_file_path())) {
            file_put_contents($this->get_viewtypes_layout_file_path(), '');
        }

        $viewtypes = file_get_contents($this->get_viewtypes_layout_file_path());

        if (!$viewtypes) {
            $viewtypes = '{}';
        }

        return json_decode($viewtypes, true);
    }

}
