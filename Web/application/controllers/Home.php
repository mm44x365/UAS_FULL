<?php

class Home extends CI_Controller
{

    public function __construct()
    {
        parent::__construct();
        $this->load->model('user_model');
        $this->load->model('history_model');
        $this->load->helper(array('form', 'url'));
        $this->load->library(array('session', 'form_validation'));
    }

    public function index()
    {
        $data['title'] = 'Beranda';
        $data['subtitle'] = 'Rangkuman Data';
        $data['user'] = $this->user_model->getRows();
        $data['history'] = $this->history_model->getRowsAll();

        $this->load->view('templates/admin-header', $data);
        $this->load->view('templates/admin-topbar', $data);
        $this->load->view('home', $data);
        $this->load->view('templates/admin-footer');
        $this->load->view('script');
    }
}
