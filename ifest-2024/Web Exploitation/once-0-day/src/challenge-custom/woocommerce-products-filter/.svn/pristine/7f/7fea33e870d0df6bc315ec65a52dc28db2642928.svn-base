<?php
if (!defined('ABSPATH'))
    die('No direct access allowed');

include_once 'classes/additional.php';
include_once 'classes/options.php';
include_once 'classes/options-layout.php';
include_once 'classes/options-sections.php';
include_once 'classes/options-sections-layout.php';
include_once 'classes/viewtypes.php';

//16-07-2023
final class WOOF_FRONT_BUILDER extends WOOF_EXT {

    public $type = 'application';
    public $folder_name = 'front_builder';
    public $html_type_dynamic_recount_behavior = 'none';
    public static $filter_id = 0; //for ajax, because WOOF_REQUEST doesn work
    private $db = null;
    private $table = null;
    private $demo = null;
    public $additional = null;
    public $options = null;
    public $options_sections = null;
    public $options_sections_layout = null;
    public $options_layout = null;
    public $viewtypes = null;

    public function __construct() {
        parent::__construct();
        global $wpdb;
        $this->db = $wpdb;
        $this->table = $this->db->prefix . 'woof_front_builder';
        $this->demo = get_option('woof_front_builder_demo', 0); //not for production
        if ($this->demo) {
            $this->table .= '_demo';
        }

		//add global  option woof_print_option_advanced
		add_action('woof_print_option_advanced', array($this, 'global_options'));
		
        $this->init_request();

        add_filter('woof_modify_settings_before_action', [$this, 'woof_modify_settings_before_action'], 10, 2);
        add_filter('woof_get_request_data', [$this, 'woof_get_request_data']);
        add_filter('woof_get_meta_query', [$this, 'woof_get_meta_query'], 1);
        add_filter('woof_regulate_by_only_show', [$this, 'woof_regulate_by_only_show'], 10, 2);

        //for filter-sections customizations
        add_filter('woof_generate_container_css_classes', function ($section_key) {
            return " woof_fs_{$section_key} ";
        });

        add_action('init', function () {
            $this->additional = new WOOF_FRONT_BUILDER_ADDITIONAL($this->db, $this->table, $this->get_ext_path(), $this->demo, $this->is_admin());
            $this->options = new WOOF_FRONT_BUILDER_OPTIONS($this->db, $this->table, $this->get_ext_path(), $this->demo, $this->is_admin());
            if (!isset($this->options_sections)) {
                $this->options_sections = new WOOF_FRONT_BUILDER_OPTIONS_SECTIONS($this->db, $this->table, $this->get_ext_path(), $this->demo, $this->is_admin());
            }
            $this->options_sections_layout = new WOOF_FRONT_BUILDER_OPTIONS_SECTIONS_LAYOUT($this->db, $this->table, $this->get_ext_path(), $this->demo, $this->is_admin());
            if (!isset($this->options_layout)) {
                $this->options_layout = new WOOF_FRONT_BUILDER_OPTIONS_LAYOUT($this->db, $this->table, $this->get_ext_path(), $this->demo, $this->is_admin());
            }
            $this->viewtypes = new WOOF_FRONT_BUILDER_VIEWTYPES($this->db, $this->table, $this->get_ext_path(), $this->demo, $this->is_admin());

            add_action('wp_ajax_woof_form_builder_get_items', array($this, 'get_items'));
            add_action('wp_ajax_woof_front_builder_save', array($this, 'save_items'));
            add_action('wp_ajax_woof_form_builder_set_sd', array($this, 'set_sd'));

            //+++

            $this->options->init($this->demo);

            if ($this->demo) {
                add_action('wp_ajax_nopriv_woof_form_builder_get_items', array($this, 'get_items'));
                add_action('wp_ajax_nopriv_woof_front_builder_save', array($this, 'save_items'));
            }
        });

        $this->init();
    }

    public function get_ext_path() {
        return plugin_dir_path(__FILE__);
    }

    public function get_ext_override_path() {
        return get_stylesheet_directory() . DIRECTORY_SEPARATOR . "woof" . DIRECTORY_SEPARATOR . "ext" . DIRECTORY_SEPARATOR . $this->folder_name . DIRECTORY_SEPARATOR;
    }

    public function get_ext_link() {
        return plugin_dir_url(__FILE__);
    }

    public function woof_modify_settings_before_action($settings, $atts) {
        if (isset($atts['name']) AND !empty($atts['name'])) {
            $filter_id = 0;
            $name = $atts['name'];
			
            if (isset($atts['filter_id']) AND !empty(intval($atts['filter_id']))) {
                if (wp_doing_ajax()) {
                    //in non-ajax mode this interfere into query to below shortcode [woof_products]
                    self::$filter_id = intval($atts['filter_id']);
                }

                $filter_id = intval($atts['filter_id']);
            }

            //we need this trick for meta search query trought hook woof_get_meta_query in this file
            if ($filter_id && !isset($atts['by_only']) && !isset($atts['tax_only'])) {
                $atts['by_only'] = $atts['tax_only'] = $this->get_selected_by_id($filter_id);
            }

            //fix: if $this->options_sections not else created
            if (!isset($this->options_sections)) {
                $this->options_sections = new WOOF_FRONT_BUILDER_OPTIONS_SECTIONS($this->db, $this->table, $this->get_ext_path(), $this->demo, $this->is_admin());
            }

            if (!isset($this->options_layout)) {
                $this->options_layout = new WOOF_FRONT_BUILDER_OPTIONS_LAYOUT($this->db, $this->table, $this->get_ext_path(), $this->demo, $this->is_admin());
            }

            //+++

            $section_options = $this->options_sections->get_options_key_value($name, $this->extract_sections_keys($atts));

            //https://share.pluginus.net/image/i20230614172809.png
            if (!empty($section_options) AND is_array($section_options)) {
                foreach ($section_options as $section_key => $section_options) {
                    if (taxonomy_exists($section_key)) {
                        //taxonomies
                        if (!empty($section_options) AND is_array($section_options)) {
                            foreach ($section_options as $key => $value) {
                                $settings[$key][$section_key] = $value;
                            }
                        }
                    } else {
                        //not taxonomies
                        if (!empty($section_options) AND is_array($section_options)) {
                            foreach ($section_options as $key => $value) {
                                $settings[$section_key][$key] = $value;
                            }
                        }
                    }
                }
            }
        }

        //+++
        //fix: we use it also for some another options
        if (isset($name)) {
            $layout_options = $this->options_layout->get_options_key_value($name);

            $settings['icheck_skin'] = $layout_options['icheck_skin']; //fix for icheck
            //fix for tax block heights
            $section_options['tax_block_height'] = [];
            if (isset($settings['tax_type']) && isset($layout_options['--woof-fb-section-height'])) {
                foreach (array_keys($settings['tax_type']) as $key) {
                    $settings['tax_block_height'][$key] = $layout_options['--woof-fb-section-height'];
                }
            }

            //fix for taxonomies just added to the system, but if not cliked save button on the HUSKY dashboard
            if (isset($settings['tax']) && !empty($settings['tax'])) {
                foreach ($settings['tax'] as $tax => $enabled) {
                    if (intval($enabled) && !empty($tax) && !isset($settings['tax_type'][$tax])) {
                        $view_type = 'radio';
                        if ($this->viewtypes) {
                            $viewtypes = $this->viewtypes->get($name);
                            if (isset($viewtypes[$tax])) {
                                $view_type = $viewtypes[$tax];
                            }
                        }

                        $settings['tax_type'][$tax] = $view_type;
                    }
                }
            }
        }

        return $settings;
    }

    private function extract_sections_keys($atts) {
        $sections = [];
        if (isset($atts['tax_only']) && !empty($atts['tax_only'])) {
            $sections = explode(',', $atts['tax_only']);
        }

        if (isset($atts['by_only']) && !empty($atts['by_only'])) {
            $sections = array_merge($sections, explode(',', $atts['by_only']));
        }

        return $sections;
    }

    private function get_name_by_id($filter_id) {
        static $cache = [];

        if (!$filter_id) {
            return '';
        }

        if (!isset($cache[$filter_id])) {
            $cache[$filter_id] = $this->db->get_row("SELECT name FROM {$this->table} WHERE id={$filter_id}")->name;
        }

        return $cache[$filter_id];
    }

    private function get_selected_by_id($filter_id) {
        static $cache = [];

        if (!isset($cache[$filter_id])) {
            $cache[$filter_id] = $this->db->get_row("SELECT selected FROM {$this->table} WHERE id={$filter_id}")->selected;
        }

        return $cache[$filter_id];
    }

    private function get_selected_by_name($name) {
        static $cache = [];

        if (!isset($cache[$name])) {
            $cache[$name] = $this->db->get_row("SELECT selected FROM {$this->table} WHERE name='{$name}'")->selected;
        }

        return $cache[$name];
    }

    private function decompose_search_slug($slug) {
        $filter_id = preg_replace('/[^0-9]/', '', $slug);
        $slug_string = preg_replace('/[^a-zA-Z]/', '', $slug);
        return ['filter_id' => $filter_id, 'slug' => $slug_string];
    }

    private function init_request() {
        $plugin_options = get_option('woof_settings', []);
        $slug = 'swoof'; //default slug
        if (isset($plugin_options['swoof_search_slug']) AND !empty(trim($plugin_options['swoof_search_slug']))) {
            $slug = trim($plugin_options['swoof_search_slug']);
        }

        $parts = [];

        if (isset($plugin_options['woof_url_request']) AND intval($plugin_options['woof_url_request']['enable'])) {
            //ext woof_url_request is enabled
            $request_string = WOOF_HELPER::get_server_var('REQUEST_URI');
            $parts = explode('/', $request_string);
            //$search_slug = woof()->get_swoof_search_slug();//NULL
            //hook for SEO ext to make it possible filter items when they are has conditional logic 'NOT IN'
            add_filter('woof_url_parser_all_data', function ($data) {
                if (isset($data['filters']) && !empty($data['filters']) && is_array($data['filters'])) {
                    foreach ($data['filters'] as $key => $value) {
                        if (taxonomy_exists($key)) {
                            //just collect the data to make it possible filtration, no interference directly with the logic
                            $data['filters']['rev_' . $key] = $value;
                        }
                    }
                }

                return $data;
            });
        } else {
            if (!empty($_GET)) {
                $parts = array_keys($_GET);
            }
        }

        //lets get $filter_id
        if (wp_doing_ajax()) {
            if (isset($_REQUEST['woof_shortcode'])) {
                $atts = shortcode_parse_atts($_REQUEST['woof_shortcode']);
                if (isset($atts['filter_id'])) {
                    $filter_id = self::$filter_id = intval($atts['filter_id']);
                    add_filter('woof_filter_search_slug', function ($slug)use ($filter_id) {
                        WOOF_REQUEST::set('woof_form_builder_filter_id', $filter_id);
                        return $this->get_alias_by_id($filter_id);
                    });
                }
            }
        } else {
            if (!empty($parts)) {
				
                foreach ($parts as $value) {
					

					$value = $this->get_slug_by_alias($value);

					
					
                    if (substr($value, 0, strlen($slug)) === $slug) {
                        $d = $this->decompose_search_slug($value);
                        $filter_id = intval($d['filter_id']);

                        if ($filter_id > 0 AND $this->db->get_row("SELECT id FROM {$this->table} WHERE id={$filter_id}", ARRAY_A)) {
                            add_filter('woof_filter_search_slug', function ($slug)use ($filter_id) {
                                WOOF_REQUEST::set('woof_form_builder_filter_id', $filter_id);

                                return $this->get_alias_by_id($filter_id);
                            });
                        }

                        break;
                    }
                }
            }
        }
    }

    //we need it to overide woof settings related to logic 'OR' 'AND' 'NOT IN' in comparison_logic, NO INFLUENT on request data
    public function woof_get_request_data($data) {

        if (wp_doing_ajax()) {
            $filter_id = self::$filter_id;
        } else {
            $filter_id = intval(WOOF_REQUEST::get('woof_form_builder_filter_id'));
        }

        if ($filter_id > 0) {
            woof()->settings = $this->woof_modify_settings_before_action(woof()->settings, ['name' => $this->get_name_by_id($filter_id), 'filter_id' => $filter_id]);
        }

        return $data;
    }

    //we need it to overide woof settings related to logic 'OR' 'AND' 'NOT IN' in comparison_logic, NO INFLUENT on request data
    public function woof_get_meta_query($meta_query) {

        if (wp_doing_ajax()) {
            $filter_id = self::$filter_id;
        } else {
            $filter_id = intval(WOOF_REQUEST::get('woof_form_builder_filter_id'));
        }

        if ($filter_id > 0) {
            woof()->settings = $this->woof_modify_settings_before_action(woof()->settings, ['name' => $this->get_name_by_id($filter_id), 'filter_id' => $filter_id]);
        }

        return $meta_query;
    }

    //hook woof_regulate_by_only_show is need here only for price filter because its view depends of this value: 1,2,3,4,5 ...
    public function woof_regulate_by_only_show($value, $key) {
        if ($key === 'by_price') {
            $value = intval(woof()->settings[$key]['show']);
        }

        return $value;
    }

    public function init() {
        add_action('wp_footer', array($this, 'wp_footer'), 10);
        add_action('admin_footer', array($this, "admin_footer"));
        add_shortcode("woof_front_builder", array($this, "woof_front_builder"));

        add_action('woof_wp_load_js', function ($str) {

            if ($this->demo) {
                $str .= ';var woof_front_builder_is_demo=1;';
            }

            $str .= ';var woof_front_sd_is_a=' . intval(isset(WOOF_EXT::$includes['applications']['sd'])) . ';';
            $str .= 'var woof_front_show_notes=' . intval(woof()->show_notes) . ';';
            $str .= 'var woof_lang_front_builder_del="' . esc_html__('Are you sure you want to delete this filter-section?', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_options="' . esc_html__('Options', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_option="' . esc_html__('Option', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_section_options="' . esc_html__('Section Options', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_description="' . esc_html__('Description', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_close="' . esc_html__('Close', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_suggest="' . esc_html__('Suggest the feature', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_good_to_use="' . esc_html__('good to use in content areas', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_confirm_sd="' . esc_html__('Smart Designer item will be created and attached to this filter section and will cancel current type, proceed?', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_creating="' . esc_html__('Creating', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_shortcode="' . esc_html__('Shortcode', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_layout="' . esc_html__('Layout', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_filter_section="' . esc_html__('Section options', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_filter_redrawing="' . esc_html__('filter redrawing', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_filter_redrawn="' . esc_html__('redrawn', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_filter_redrawn="' . esc_html__('redrawn', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_title_top_info="' . esc_html__('this functionality is only visible for the site administrator', 'woocommerce-products-filter') . '";';
            $str .= 'var woof_lang_front_builder_title_top_info_demo="' . esc_html__('demo mode is activated, and results are visible only to you', 'woocommerce-products-filter') . '";';

            return $str . ';var woof_lang_front_builder_select="+ ' . esc_html__('Add filter section', 'woocommerce-products-filter') . '";';
        });
    }

    private function is_admin() {
        $can = true;

        if (!current_user_can('administrator')) {
            $can = false;
        }

        if ($this->demo) {
            $can = true;
        }

        return $can;
    }

    public function wp_footer() {

        wp_enqueue_style('woof-front-builder-css', $this->get_ext_link() . 'css/front-builder.css', [], WOOF_VERSION);

        if (!$this->is_admin()) {
            return false;
        }

        wp_enqueue_style('woof-front-builder-popup-23', $this->get_ext_link() . 'css/popup-23.css', [], WOOF_VERSION);

        wp_enqueue_style('woof-front-builder-table', $this->get_ext_link() . 'css/table.css', [], WOOF_VERSION);

        wp_enqueue_script('woof-front-builder-boot', $this->get_ext_link() . 'js/boot.js', [], WOOF_VERSION);
        wp_enqueue_script('woof-front-builder', $this->get_ext_link() . 'js/front-builder.js', [], WOOF_VERSION);

        $this->script_loader_tag(); //!!
    }

    public function admin_footer() {
        if (isset($_GET['woof-action']) AND $_GET['woof-action'] === 'form-builder') {
            //for Smart Designer iframe
            ?>
            <style type="text/css">
                #wpbody-content,
                #wpcontent,
                #wpbody
                {
                    background: #fff;
                    margin-top: 0 !important;
                }

                #mainform > .nav-tab-wrapper.woo-nav-tab-wrapper,
                #wpadminbar,
                .woocommerce-layout__header,
                #screen-meta-links,
                .woof-header,
                .screen-reader-text,
                .woocommerce-layout,
                #tabs > nav,
                .woof__alert.woof__alert-success,
                p.submit
                {
                    display: none;
                }

                .html.wp-toolbar,
                .woocommerce-embed-page .woocommerce-layout__notice-list-hide+.wrap,
                .wp-toolbar,
                .woocommerce-embed-page .wrap,
                .woocommerce-embed-page.wrap,
                .content-wrap section,
                .woof-control-section
                {
                    padding: 0 !important;
                }

                #tabs-sd > .woof-tabs > .content-wrap > section > .woof-section-title,
                #tabs-sd > .woof-tabs > .content-wrap > section > .woof-notice,
                #tabs-sd > .woof-tabs > .content-wrap > section > .woof__alert.woof__alert-info2.woof_tomato,
                .woof_fix19,
                #sd-visor,
                #sd-scene data-table data-table-row:first-child,
                .woof-sd-btn-back,
                .notice,
                .notice.notice-info,
                .woof-sd-create-element{
                    display: none !important;
                }

                #sd-scene{
                    width: 100% !important;
                }

                #sd-scene data-table data-table-row:nth-child(2){
                    border-top: solid 1px #d9d9d9;
                }

                #sd-scene > div{
                    max-height: calc(<?php echo intval($_GET['max_height']) ?>px - 30px) !important;
                }

                .woof-sd-select-type{
                    min-width: 125px !important;
                }

                #adminmenumain{
                    display: none;
                }

                #wpcontent{
                    margin-left: 0;
                }

                #sd-panel > div:nth-child(1){
                    margin-right: 0;
                }

            </style>

            <script>
                window.addEventListener('load', function () {
                    let hash = window.location.hash.trim();
                    if (hash) {
                        woof_tab_click(document.querySelector(`#tabs li a[href = "${hash}"]`), hash);
                        let id =<?php echo intval($_GET['sd_id']) ?>;

                        //call SD interface
                        let timer = setInterval(() => {
                            //call SD interface
                            let btn = document.querySelector(`data-table > data-table-row[data-id='${id}']`)?.querySelector('.woof-sd-edit-row > a');
                            if (btn) {
                                btn.click();
                                clearInterval(timer);
                            }
                        }, 111);

                    }
                });
            </script>
            <?php
        }
    }

    private function script_loader_tag() {
        add_filter('script_loader_tag', function ($tag, $handle, $src) {

            if ('woof-front-builder-boot' === $handle) {
                $tag = '<script type="module" src="' . esc_url($src) . '"></script>';
            }

            return $tag;
        }, 10, 3);
    }

    public function woof_front_builder($atts, $content = '') {

        if (!isset($atts['name'])) {
            return esc_html__('Unique name should be set for shortcode [woof_front_builder]', 'woocommerce-products-filter');
        }

        $name = esc_html($atts['name']);
        if ($this->demo) {
            $name .= ' ' . str_replace(':', '', str_replace('.', '', filter_var(WOOF_HELPER::get_server_var('REMOTE_ADDR'), FILTER_VALIDATE_IP)));
        }

        $is_admin = $this->is_admin();

        if ($is_admin) {
            $answer = $this->install();
            if ($answer) {
                return $answer;
            }
        }

        $data = $this->get_data($name);
        $data['is_admin'] = $is_admin;

        //+++

        if (isset($atts['popup_width'])) {
            $data['popup_width'] = intval($atts['popup_width']) . 'px';
        } else {
            $data['popup_width'] = isset($this->additional->get($name)['popup_width']) ? $this->additional->get($name)['popup_width'] . 'px' : '800px';
        }

        if (isset($atts['popup_height'])) {
            $data['popup_height'] = intval($atts['popup_height']) . 'px';
        } else {
            $data['popup_height'] = isset($this->additional->get($name)['popup_height']) ? $this->additional->get($name)['popup_height'] . 'px' : '600px';
        }

        //+++

        $data['options'] = $this->options->get_options_key_value($name);
        $data['layout_options'] = $this->options_layout->get_options_key_value($name);
        $data['sections_layout_options'] = $this->options_sections_layout->get_options_db($name);

        $data['ext_link'] = $this->get_ext_link();
        $viewtypes = array_merge(woof()->settings['tax_type'], $this->viewtypes->get($name));
        $data['viewtypes'] = '';
        if (!empty($viewtypes)) {
            foreach ($viewtypes as $key => $value) {
                $data['viewtypes'] .= $key . ':' . $value . ',';
            }
            $data['viewtypes'] = trim($data['viewtypes'], ',');
        }

        //fix for redirect + ajax mode filter-sections order
        $data['options']['items_order'] = $this->get_selected_by_name($name);

        if ($this->demo) {
            $data['options']['dynamic_recount'] = 0;
            $data['options']['hide_terms_count'] = 1;
        }

		$data['swoof_slug'] = $this->get_alias_by_id($data['id']);
		
        return woof()->render_html($this->get_ext_path() . 'views' . DIRECTORY_SEPARATOR . 'shortcodes' . DIRECTORY_SEPARATOR . 'woof_front_builder.php', $data);
    }

    private function get_data($name) {
        $data = $this->db->get_row("SELECT * FROM {$this->table} WHERE name='{$name}'", ARRAY_A);
        if (empty($data)) {
            //create if not exists
            $data = $this->create($name);
        }

        $data['selected_taxonomies'] = [];
        $data['selected_nontaxonomies'] = [];

        if (empty($data['selected'])) {
            $data['selected'] = []; //NULL
        } else {
            $data['selected'] = $selected = explode(',', $data['selected']);
            foreach ($selected as $key) {
                if (taxonomy_exists($key)) {
                    $data['selected_taxonomies'][] = $key;
                } else {
                    $data['selected_nontaxonomies'][] = $key;
                }
            }
        }

        return $data;
    }

    private function create($name) {
        $data = [
            'name' => esc_html($name),
            'selected' => 'by_text,by_instock,by_onsales,by_price',
            'sections_options' => '{"by_price":{"show_text_input":"0"}}',
            'sections_layout_options' => '{"by_text":{"width":"100%"},"by_price":{"width":"100%"}}'
        ];

        $this->db->insert($this->table, $data);
        $data['id'] = $this->db->insert_id;
        $data['options'] = [];
        return $data;
    }

    //ajax
    public function get_items() {

        if (!$this->is_admin()) {
            return false;
        }

        //+++

        $woof_settings = woof()->settings;
        $items_order = [];
        $taxonomies = woof()->get_taxonomies();
        $taxonomies_keys = array_keys($taxonomies);
        if (isset($woof_settings['items_order']) AND !empty($woof_settings['items_order'])) {
            $items_order = explode(',', $woof_settings['items_order']);
        } else {
            $items_order = array_merge(woof()->items_keys, $taxonomies_keys);
        }

        //*** lets check if we have new taxonomies added in woocommerce or new item
        foreach (array_merge(woof()->items_keys, $taxonomies_keys) as $key) {
            if (!in_array($key, $items_order)) {
                $items_order[] = $key;
            }
        }

        $res = [];
        $labels = woof()->get_all_filter_titles();
        $viewtypes = array_merge(woof()->settings['tax_type'], $this->viewtypes->get(esc_html($_REQUEST['name'])));
        foreach ($items_order as $key) {
            if (isset($taxonomies[$key])) {
                $res[$key] = [
                    'title' => $labels[$key] ?? $taxonomies[$key]->label,
                    'is_taxonomy' => 1,
                    //'is_sd' => $this->is_sd($key),
                    'viewtype' => isset($viewtypes[$key]) ? $viewtypes[$key] : 'radio'
                ];
            } else {
                $titles = array(
                    'by_price' => esc_html__("Price", 'woocommerce-products-filter'),
                    'by_rating' => esc_html__("Rating", 'woocommerce-products-filter'),
                    'by_sku' => esc_html__("SKU", 'woocommerce-products-filter') . (woof()->show_notes ? ' [premium]' : ''),
                    'by_text' => esc_html__("Text", 'woocommerce-products-filter'),
                    'by_author' => esc_html__("Author", 'woocommerce-products-filter'),
                    'by_backorder' => esc_html__("Exclude products on backorder", 'woocommerce-products-filter') . (woof()->show_notes ? ' [premium]' : ''),
                    'by_featured' => esc_html__("Featured", 'woocommerce-products-filter'),
                    'by_instock' => esc_html__("In stock", 'woocommerce-products-filter'),
                    'by_onsales' => esc_html__("On sale", 'woocommerce-products-filter'),
                    'products_messenger' => esc_html__("Products Messenger", 'woocommerce-products-filter'),
                    'query_save' => esc_html__("Save search query", 'woocommerce-products-filter'),
                );

                if (isset($this->woof_settings['meta_filter']) && !empty($this->woof_settings['meta_filter']) && is_array($this->woof_settings['meta_filter'])) {
                    foreach ($this->woof_settings['meta_filter'] as $k => $m) {
                        $titles[$k] = $m['title'];
                    }
                }

                $res[$key] = [
                    'title' => isset($titles[$key]) ? $titles[$key] : $key,
                    'is_taxonomy' => 0
                ];
            }
        }


        die(json_encode($res));
    }

    //is for filter element applied SD options
    //viewtype is taken fromattributes, do not use
    private function is_sd($key) {
        $id = 0;

        if (WOOF_EXT::is_ext_a('smart_designer')) {
            $types_attached = woof()->settings['tax_type'];

            if ($types_attached[$key]) {
                if (strpos($types_attached[$key], 'woof_sd_') !== false) {
                    $id = intval(str_replace('woof_sd_', '', $types_attached[$key]));
                }
            }
        }

        return $id;
    }

    //ajax
    public function set_sd() {
        $key = esc_html($_REQUEST['key']);
        $sd = WOOF_EXT::$includes['applications']['sd'];
        $title = sprintf(esc_html__('by Front Builder for: %s', 'woocommerce-products-filter'), $key);
        $sd_responce = $sd->create_element($title);
        $sd_id = intval($sd_responce['id']);
        $sd->change_title($sd_id, $title . ' #' . $sd_id);

        WOOF_REQUEST::set('value', 'woof_sd_' . $sd_id);
        $this->viewtypes->update();

        //do not change global settings, viewtype is shortcode attribute!
        //woof()->settings['tax_type'][$key] = 'woof_sd_' . $sd_id;
        //update_option('woof_settings', woof()->settings);

        echo json_encode([
            'sd_id' => $sd_id,
            'title' => 'SD: ' . $title . ' #' . $sd_id
        ]);
        exit;
    }

    public function save_items() {

        if (!$this->is_admin()) {
            return false;
        }

        $name = esc_html($_REQUEST['name']);
        $fields = esc_html($_REQUEST['fields']);

        $this->db->update($this->table, array('selected' => $fields), array('name' => $name));
    }
	public function get_alias_by_id($id) {
        $woof_settings = get_option('woof_settings', []);
        $slug = 'swoof'; //default slug
        if (isset($woof_settings['swoof_search_slug']) AND !empty(trim($woof_settings['swoof_search_slug']))) {
            $slug = trim($woof_settings['swoof_search_slug']);
        }
		$slug .= $id;
		if (isset($woof_settings['slug_alias']) && isset($woof_settings['slug_alias'][$id]) && !empty(trim($woof_settings['slug_alias'][$id])) ) {
			$slug = trim($woof_settings['slug_alias'][$id]);
		}
		return $slug;
	}
	
	public function get_slug_by_alias($alias) {
		if (empty($alias)) {
			return $alias;
		}
        $woof_settings = get_option('woof_settings', []);
        $slug = $alias; //default slug
		if (!isset($woof_settings['slug_alias']) || !is_array($woof_settings['slug_alias'])) {
			$woof_settings['slug_alias'] = array();
		}
		if (array_search($alias, $woof_settings['slug_alias']) !== false) {
			$slug = 'swoof'; //default slug
			if (isset($woof_settings['swoof_search_slug']) AND !empty(trim($woof_settings['swoof_search_slug']))) {
				$slug = trim($woof_settings['swoof_search_slug']);
			}			
			$slug .= array_search($alias, $woof_settings['slug_alias']);
		}

		return $slug;
	}	
	
	public function global_options(){
		$data['ids'] = $this->db->get_results("SELECT id FROM {$this->table}", ARRAY_A);
		$data['slug'] = woof()->get_swoof_search_slug();
		
		woof()->render_html_e($this->get_ext_path() . 'views' . DIRECTORY_SEPARATOR . 'global_options.php', $data);
	}

    private function install() {
        $charset_collate = '';

        if (method_exists($this->db, 'has_cap') AND $this->db->has_cap('collation')) {
            if (!empty($this->db->charset)) {
                $charset_collate = "DEFAULT CHARACTER SET {$this->db->charset}";
            }

            if (!empty($this->db->collate)) {
                $charset_collate .= " COLLATE {$this->db->collate}";
            }
        }

        //+++

        $sql = "CREATE TABLE IF NOT EXISTS `{$this->table}` (
                `id` int(11) NOT NULL AUTO_INCREMENT,
                `name` varchar(64) DEFAULT NULL,
                `selected` text,
                `options` text,
                `layout_options` text,
                `sections_options` text,
                `sections_layout_options` text,
                `viewtypes` text,
                `additional` text,
                PRIMARY KEY (`id`),
                KEY (`name`)
              ) {$charset_collate};";

        $answer = '';
        if ($this->db->query($sql) === false) {
            $answer = esc_html__("HUSKY cannot create database table for front builder! Make sure that your MySQL user has the CREATE privilege! Do it manually using your host panel and phpmyadmin!", 'woocommerce-products-filter');
            //$answer = $this->db->last_error;
        }

        return $answer;
    }

}

WOOF_EXT::$includes['applications']['front_builder'] = new WOOF_FRONT_BUILDER();

