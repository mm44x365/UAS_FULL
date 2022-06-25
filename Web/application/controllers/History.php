<?php

class History extends CI_Controller
{
    public function __construct()
    {
        parent::__construct();
        $this->load->model('history_model');
        $this->load->helper(array('form', 'url'));
        // load helper
        $this->load->helper(array('form', 'url', 'timezone_helper'));
        $this->load->library(array('session', 'form_validation'));
        if (!$this->session->userdata('is_logged_in')) {
            redirect("home");
        } 
    }

    public function index()
    {
        $data['title'] = 'Data History';
        $data['subtitle'] = 'List Data History';

        $this->load->view('templates/admin-header', $data);
        $this->load->view('templates/admin-topbar', $data);
        $this->load->view('history/list', $data);
        $this->load->view('templates/admin-footer');
        $this->load->view('history/script', $data);
    }

    public function ajax_list()
    {
        $list = $this->history_model->get_datatables();
        $data = array();
        $no = $_POST['start'];
        foreach ($list as $history) {
            $no++;
            $row = array();
            $row[] = $no;

            $row[] = $history->data;
            $row[] = tgl_indo($history->waktu);
            $data[] = $row;
        }
        $output = array(
            "draw" => $_POST['draw'],
            "recordsTotal" => $this->history_model->count_all(),
            "recordsFiltered" => $this->history_model->count_filtered(),
            "data" => $data,
        );
        //output to json format
        echo json_encode($output);
    }

    public function sensor(){
		if (isset($_GET['data'])) {
			$panjang = $this->input->get('data');
			$datasensor = array('data' => $panjang, 'waktu' => time());

			if($this->history_model->savesensor($datasensor)){
				echo "BERHASIL";
			}else{
				echo "ERROR";
			}
		}else{
			echo "Variabel data tidak terdefinisi";
		}
	}
}
