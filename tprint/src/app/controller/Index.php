<?php
namespace app\controller;

use app\BaseController;
use think\facade\View;
use think\facade\Request;


class Index extends BaseController
{
    public function index()
    {
        $msg = Request::get('msg','Get in Touch');
        if(Request::has('message','post')){
            redirect('/index.php?msg=发送成功');
        }

        View::assign('msg',$msg);
        return View::fetch();
    }
    public function show(){
        $pic = Request::get('pic','01.jpg');
        View::assign('pic',$pic);
        return View::fetch();
    }
}
